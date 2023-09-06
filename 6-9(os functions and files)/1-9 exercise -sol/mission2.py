def elevator_manage(left, right, call):
    right_distance = abs(right - call)
    left_distance = abs(left - call)
    if right_distance <= left_distance:
        print('right')
    elif right_distance > left_distance:
        print('left')


elevator_manage(0, 2, 1)
elevator_manage(0, 1, 2)
elevator_manage(0, 1, 0)
