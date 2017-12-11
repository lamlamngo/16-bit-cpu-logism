#Lam Ngo
#This test basic load word and store word
#Adapt from Lab 4 and John's test.
#load 1 to 7 into reg 1 to 7 and load into memory. Then reverse the order
#of the array in memory.
#reg 1 to 7 should contain 7 to 1
#memory 1 to 7 should also contain 7 to 1

addi $1 $0 1
addi $2 $0 2
add  $3 $2 $1
add  $4 $2 $2
addi $5 $0 5
add  $6 $2 $4
addi $7 $0 7
sw   $1 1($0)
sw   $2 2($0)
sw   $3 3($0)
sw   $4 3($1)
sw   $5 2($3)
sw   $6 0($6)
sw   $7 7($0)
lw   $0 0($7)
lw   $1 -1($7)
lw   $2 -2($7)
lw   $3 -3($7)
lw   $4 -4($7)
lw   $5 -5($7)
lw   $6 -6($7)
lw   $7 -7($0)
sw $0 1($8)
sw $1 2($8)
sw $2 3($8)
sw $3 4($8)
sw $4 5($8)
sw $5 6($8)
sw $6 7($8)
sw $7 1($0)
