# 16-bit-cpu-logism
Designed and implemented an 16-bit CPU architecture in Logism.

Assembler file: lamassembler.py
Logism circuit file: LamNgoFinalProject.circ 

I. Directions for translating assembly code into hexadecimal machine code:

To do so, users can choose between writing their own assemblers for my CPU, or they can use my assembler.

First, users will need to write Assembly code and save them as .asm files. 

I recommend using Atom to do this, as it is fast, light and supports color-coded writing.

My assembler requires Python 2.7 or above, which comes with macOS, but Windows users will have to download it from Python 
website. After doing that, they can choose to move python.exe to my assembler folder, or add python.exe to their PATH 
environment variable. This can be done easily following instructions on the internet. Using command line is preferable. 

To translate any assembly files into their corresponding hex files, type this inside the terminal (provided that you have cd 
inside the assembler folder):
    python lamassembler.py inputfile.asm outputfile.hex
    
If it is translated successfully, this line will appear:
    Number of arguments: 3 arguments.
    Arguments list: ...
    
If there is any error, it will be displayed in the terminal console.
The outputfile can be used to load into Logisim immediately.

II. Coding conventions:

Since this is my first time making an assembler, there is still a lot of things to be done. 
Thus, to have a enjoyable and error-free experience with my CPU, this guideline should be followed closely:

When using labels, be sure to include a “:” after the label and write your code immediately on the same line. 
That is, you should not enter a new line after declaring a label.

Registers 0, register 15 ($sp), register 14 ($ra), register 13 ($at) must not be touched.

Registers 12 ($a0) and registers 11 ($a1) can be used to pass arguments for a subroutine.

Registers 10 ($v0) and 9 ($v1) can be used to return values.

Registers from 1 to 8 can be used freely by you.

To use the stack, do addi $sp $sp -1 instead of -4, and push and pop are the same with MIPs assembly.

Also, you can branch freely to any labels, but if you use offset, please use from -8 to 7.
