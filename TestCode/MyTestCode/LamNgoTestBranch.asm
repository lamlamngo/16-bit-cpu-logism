# Lam Ngo, Test beq.
# Using a simple if else statement
#True if  registers 0-4 are 0, and first branch not taken and second branch
#taken.

addi $1 $0 1 # x = 1
addi $2 $0 2 #y = 2
addi $3 $0 3 # a = 3

beq $1 $2 3  # this branch should not be taken
add $5 $1 $0
add $1 $2 $0
add $2 $5 $0

add $4 $1 $2 # b = x + y
beq $4 $3 4 # else if b == a, this branch should be taken.
addi $1 $0 1  #
addi $2 $0 2  #
addi $3 $0 3  # skip these line if correct
addi $4 $0 4
addi $1 $0 0
addi $2 $0 0
addi $3 $0 0
addi $4 $0 0
