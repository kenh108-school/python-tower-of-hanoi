def tower_of_hanoi(disk_num, source, spare, dest):
    if disk_num == 0:
        return
    
    tower_of_hanoi(disk_num - 1, source, dest, spare)
    print("Move disk " + str(disk_num) + " from pole " + source + " to pole " + dest + " using pole " + spare + ".")
    tower_of_hanoi(disk_num - 1, spare, source, dest)


num_disks = 10
tower_of_hanoi(num_disks, 'A', 'B', 'C')
