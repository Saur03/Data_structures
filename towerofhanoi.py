# Tower of hanoi
# It is a mathematical puzzle that involves peg and discs. There are three pegs and n(let n=3) discs of different sizes
# Puzzle begin with the state that one peg has all the discs stacked one above the other in descendng order from the below.
# The game is about solving the puzzle such that all the discs are arranged in differenet peg in different order
# The rules to be followed are:-
# 1. Oly one discs can be moved at a time
# 2. largers dics are NOT allowed  to be on top of smaller size
def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from peg {} to peg {}.'. format(source, target))
        return
    hanoi(disks - 1, source, target, auxiliary)
    print('Move disk 1 from peg {} to peg {}.'. format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)
disks = int(input(' Enter number of disks: '))
hanoi(disks, 'X', 'Y', 'Z')        
