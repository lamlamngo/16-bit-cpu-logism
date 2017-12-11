# Lam Ngo
# test using function calls: jal and jr with the stack.
# first calls a subroutine, then jumps back and jump to another subroutine,
# which call another subrotine, a stack is required at this point.

#result: should store 18 at address 1.

addi $1 $1 1
addi $2 $2 2
add $a0 $1 $0
add $a1 $2 $0
jal Add
add $a0 $0 $v0
jal DoubleThenTriple
sw $v0 1($0)
beq $0 $0 -1 #infinite loop here when done

Add: add $v0 $a0 $a1
     jr $ra
DoubleThenTriple: add $a0 $a0 $a0
        addi $sp $sp -1
        sw $ra 0($sp)
        jal Triple
        lw $ra 0($sp)
        addi $sp $sp 1
        jr $ra
Triple: add $a0 $a0 $a0
        add $v0 $a0 $a0
        jr $ra
