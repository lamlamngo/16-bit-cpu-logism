#Lam Ngo
#This code tests basic Rtype instructions
#After the code finishes, $1 should contain: 1
# $2 should contain: 5
# $3 should contain: 3
# $4 should contain: 7
# $5 should contain: 2

subi $1 $0 1
addi $2 $0 5
addi $3 $0 3
and $1 $1 $0
addi $1 $1 1
or $4 $2 $3
sub $5 $3 $1
