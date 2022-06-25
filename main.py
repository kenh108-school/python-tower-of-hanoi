import time
import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    num_disks = int(sys.argv[1])
else :
    num_disks = 10

num_moves = 0

def tower_of_hanoi(disk_num, source, spare, dest):
    global num_moves

    if disk_num == 0:
        return
    
    num_moves += 1
    tower_of_hanoi(disk_num - 1, source, dest, spare)
    print("Move disk " + str(disk_num) + " from pole " + source + " to pole " + dest + " using pole " + spare + ".")
    tower_of_hanoi(disk_num - 1, spare, source, dest)


start_time = time.time()
tower_of_hanoi(num_disks, 'A', 'B', 'C')
end_time = time.time()

elapsed_time = end_time - start_time
print("Number of disks = " + str(num_disks))
print("Execution time = " + str(elapsed_time) + "s")
print("Number of moves = " + str(num_moves) + "m")

time_per_move = elapsed_time / num_moves
print("Time per move = " + str(time_per_move) + "s/m")
