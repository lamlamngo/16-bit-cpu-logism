# Written By Lam Ngo and John Rieffel
#Assembler for Chiron CPU

import sys
import re

from helperfunctions import *

opcodeDict = {'add':'010000000','sub':'010000011','and':'010000001','or':'010000010', 'addi':'110000000','subi':'110000011',
              'j':'000001000','jal':'010001000','jr':'100001000','beq':'000010011','lw':'111000000','sw':'100100000','slt':'010000110'
              ,'andi':'110000001','ori':'110000010','sll':'110000100','srl':'110000101','sgt':'0', 'blt':'0','bgt':'0'}
oprandDict = {'$0':'0000','$1':'0001','$2':'0010','$3':'0011','$4':'0100','$5':'0101','$6':'0110','$7':'0111','$8':'1000','$v1':'1001','$v0':'1010','$a1':'1011','$a0':'1100','$at':'1101','$ra':'1110','$sp':'1111'}
label = {}
count = 3

def ConvertAssemblyToMachineCode(inline, lineCount):
	'''given a string corresponding to a line of assembly,
	strip out all the comments, parse it, and convert it into
	a string of binary values'''
	global count
	global label
	outstring = ''
	if inline.find('#') == 0:
                inline = '' # if line starts with #, get rid of it
	if inline.find('#') != -1:
		inline = inline[0:inline.find('#')] #get rid of anything after a comment
	inline = inline.lstrip() # get rid of any white space
	if inline != '':
		words = inline.split() #assuming syntax words are separated by space, not comma
		operation = words[0]
		operands = words[1:]
                if opcodeDict.has_key(operation) == False: # handle invalid opcode or label
                        operation = operation[0:len(operation)-1]
                        if len(words) < 2:
                                return ''
                        else:
                                operation = words[1]
                                operands = words[2:]
                                
                if operation == 'sgt':          # handle pseudo instruction sgt
                        outstring += opcodeDict['slt']
                        outstring += oprandDict[operands[1]]
                        outstring += oprandDict[operands[0]]
                elif operation == 'bgt':        #handle pseudo instruction bgt
                        outstring += opcodeDict['slt']
                        outstring += oprandDict['$at']
                        outstring += oprandDict[operands[1]]
                        outstring += oprandDict[operands[0]]
                        outstring += opcodeDict['beq']
                        outstring += oprandDict['$at']
                        outstring += oprandDict['$1']
                        if label.has_key(operands[2]) == True:
                                offset = label[operands[2]] - lineCount
                                if offset > 7 or offset < -8:           # if label is too far away
                                        outstring += int2bs(1,4)
                                        outstring += opcodeDict['j'] + int2bs(lineCount+3,12)
                                        outstring += opcodeDict['j'] + int2bs(label[oprand],12)
                                else:
                                        outstring += int2bs(offset,4)
                        else:
                                outstring += int2bs(operands[2],4)
                elif operation == 'blt':                #handle pseudo instruction blt
                        outstring += opcodeDict['slt']
                        outstring += oprandDict['$at']
                        outstring += oprandDict[operands[0]]
                        outstring += oprandDict[operands[1]]
                        outstring += opcodeDict['beq']
                        outstring += oprandDict['$at']
                        outstring += oprandDict['$1']
                        if label.has_key(operands[2]) == True:
                                offset = label[operands[2]] - lineCount
                                if offset > 7 or offset < -8:
                                        outstring += int2bs(1,4)
                                        outstring += opcodeDict['j'] + int2bs(lineCount+3,12)
                                        outstring += opcodeDict['j'] + int2bs(label[oprand],12)
                                else:
                                        outstring += int2bs(offset,4)
                        else:
                                outstring += int2bs(operands[2],4)
                else:
                        outstring += opcodeDict[operation]
		if operation == 'j' or operation == 'jal':                      #special cases for jump instruction
                        if label.has_key(operands[0]) == True:
                                outstring += int2bs(label[operands[0]],12)
                        else:
                                offset = 3 + int(operands[0])
                                outstring += int2bs(offset,12)
                elif operation == 'jr':
                        outstring += int2bs(0,4)
                        outstring += int2bs(14,4)
                        outstring += int2bs(0,4)
                elif operation == 'sgt':
                        outstring += int2bs(operands[0],4)
                        outstring += int2bs(operands[2],4)
                        outstring += int2bs(operands[1],4)
                else:                                                           # for normal instructions go in here
                        for oprand in operands:
                                if label.has_key(oprand) == True:
                                        offset = label[oprand] - lineCount
                                        if offset > 7 or offset < -8:           # if label is too far away for beq
                                                outstring += int2bs(1,4)
                                                outstring += opcodeDict['j'] + int2bs(lineCount+3,12)
                                                outstring += opcodeDict['j'] + int2bs(label[oprand],12)
                                        else:
                                                outstring += int2bs(offset,4)
                                else:  
                                        if oprand.find('(') != -1:              # handle lw and sw
                                                offset = oprand[0:oprand.find('(')]
                                                base = oprand[oprand.find('(')+1:oprand.find(')')]
                                                outstring += oprandDict[base]
                                                outstring += int2bs(offset,4)
                                        else:
                                                if oprand[0] == '$':            # convert register to binary
                                                        outstring += oprandDict[oprand]
                                                else:                           # convert intermediate values to binary
                                                        outstring += int2bs(oprand,4)
	return outstring	
        
def getlabel(inline):
        # go through the entire code and record labels and their corresponding lines.
        global count
	global label
	outstring = ''
	if inline.find('#') == 0:
                inline = ''
	if inline.find('#') != -1:
		inline = inline[0:inline.find('#')] #get rid of anything after a comment
	inline = inline.lstrip()
	if inline != '':
		words = inline.split() #assuming syntax words are separated by space, not comma
		operation = words[0]
		operands = words[1:]
                if opcodeDict.has_key(operation) == False:
                        operation = operation[0:len(operation)-1]
                        label[operation] = count
                inline = 'ye'
        return inline

def AssemblyToHex(infilename,outfilename):
	'''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
	then save that machinecode to an outputfile'''
	outlines = []
	global count
	with open(infilename) as f:
		lines = [line.rstrip() for line in f.readlines()]  
		for curline in lines:
                        outstring = getlabel(curline)
                        if outstring != '':
                                count = count + 1
                count = 3 # count start at three because 3 lines of code are used for initializing the stack.
		for curline in lines:
			outstring = ConvertAssemblyToMachineCode(curline,count)
			if outstring != '':
                                count = count + len(outstring)/21
                                if (len(outstring) > 21):  #incase there are any pseudoinstruction
                                        i = 0
                                        aString = ''
                                        while i < len(outstring)/21:
                                                if i == 0:
                                                        aString = outstring[i:21]
                                                        aString = bs2hex(aString)
                                                        outlines.append(aString)
                                                else:
                                                        aString = outstring[21*i:21*i+21]
                                                        aString = bs2hex(aString)
                                                        outlines.append(aString)
                                                i = i + 1
                                else:                   
                                        outstring = bs2hex(outstring)
                                        outlines.append(outstring)

	f.close()

	with open(outfilename,'w') as of:
                of.write('v2.0 raw' + "\n")
                of.write('180f07' + "\n")
                of.write('184ff4'  + "\n")
                of.write('184ff4'  + "\n")
		for outline in outlines:
			of.write(outline)
			of.write("\n")
	of.close()		
			

if __name__ == "__main__":
	#in order to run this with command-line arguments
	# we need this if __name__ clause
	# and then we need to read in the subsequent arguments in a list.
	
	#### These two lines show you how to iterate through arguments ###
	#### You can remove them when writing your own assembler
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)

	## This is error checking to make sure the correct number of arguments were used
	## you'll have to change this if your assembler takes more or fewer args	
	if (len(sys.argv) != 3):
		print('usage: python skeleton-assembler.py inputfile.asm outputfile.hex')
		exit(0)
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	AssemblyToHex(inputfile,outputfile)
