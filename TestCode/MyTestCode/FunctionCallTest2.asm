#Test Jal and JR test2
#jump to one subroutine, jump back and jump to another subroutine and jump
#back.
#result: should display 6 at memory address 1.
#Written by Lam Ngo
addi $1 $1 1
addi $2 $2 2
add $a0 $1 $0
add $a1 $2 $0
jal Add
add $a0 $0 $v0
jal Double
sw $v0 1($0)
beq $0 $0 -1 #infinite loop here when done

Add: add $v0 $a0 $a1
     jr $ra
Double: add $v0 $a0 $a0
        jr $ra
