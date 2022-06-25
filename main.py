import time
import sys

# Check for system arg
if len(sys.argv) == 2 and sys.argv[1].isdigit():
    num_disks = int(sys.argv[1])
else :
    num_disks = 10

num_moves = 0

def tower_of_hanoi(disk_num, source, spare, dest):
    # Use global variable
    global num_moves

    if disk_num == 0:
        return
    
    
    num_moves += 1 # Move will be made
    
    # Move n-1 disks from source to spare
    tower_of_hanoi(disk_num - 1, source, dest, spare)
    # Move n disk from source to dest
    print("Move disk " + str(disk_num) + " from pole " + source + " to pole " + dest + " using pole " + spare + ".")
    # Move n-1 disks from spare to dest
    tower_of_hanoi(disk_num - 1, spare, source, dest)

# Measure execution time
start_time = time.time()
tower_of_hanoi(num_disks, 'A', 'B', 'C')
end_time = time.time()
elapsed_time = end_time - start_time
time_per_move = elapsed_time / num_moves

# Stats
print("Number of disks = " + str(num_disks))
print("Execution time = " + str(elapsed_time) + "s")
print("Number of moves = " + str(num_moves) + "m")
print("Time per move = " + str(time_per_move) + "s/m")
