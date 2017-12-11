#Lam Ngo Test Jump to a label far away.
#it should jump past all these instructions, and only do the last two.
# correct if $1 contains 4.

j done
subi $1 $0 -1
subi $2 $0 -2
subi $3 $0 -3
add  $4 $2 $2
subi $5 $0 -5
subi $6 $0 -6
subi $7 $0 -7
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
done: addi $1 $8 1
      sll $1 $1 2
