#this should store values 0..5 into
# registers 0..5
# then recursively add them together
# storing the result in address 1.

addi $1 $0 1
addi $2 $0 2
addi $3 $0 3
add $4 $2 $2
add $5 $4 $1
sw $1 1($0)
sw $2 2($0)
sw $3 3($0)
sw $4 0($4)
sw $5 0($5)
add $a0 $0 $0  #a0 = 0
add $a1 $5 $2  #a1 = 7
jal recursadd
sw $v0 1($0)
beq $0 $0 -1 #infinite loop here when done

#recursadd
#expects $a0 to contain a pointer to an array
# and $a1 to contain the address of the end of the array
# (after last item)
# and returns the sum in $v0
#and could be much better
recursadd: beq $a0 $a1 base #if we are at end of array

        addi $sp $sp -2
        sw $ra 0($sp)
        sw $a0 1($sp)

        addi $a0 $a0 1 #else get sum of rest of array
        jal recursadd #v0 contains the sum of the rest of the array
        lw $a0 1($sp) #oops, restore the a0 we clobbered
        lw $1 0($a0)   #then add this item
        add $v0 $v0 $1 #and return that.

        lw $ra 0($sp)
        addi $sp $sp 2
        jr $ra
base:   addi $v0 $0 0  #return 0
        jr $ra
