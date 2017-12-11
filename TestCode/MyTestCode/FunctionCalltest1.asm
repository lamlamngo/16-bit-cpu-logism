# written by Lam Ngo
#Test jal and jr
#Should jump to min subroutine and jump back.
#check to see if $a0 is less than $a1 (testing slt also)
#result: if correct, should print at address1.
addi $1 $1 1
addi $2 $2 2
add $a0 $1 $0
add $a1 $2 $0
jal min
sw $v0 0($1)
beq $0 $0 -1 #infinite loop here when done

min: slt $3 $a0 $a1
     beq $3 $0 2
     addi $v0 $0 1
     jr $ra
     addi $v0 $0 0
     jr $ra
