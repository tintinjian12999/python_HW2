import random 
index_used = []
index_used_this_round = 0
pick_times = int(input("please enter an integer:"))
for i in range(pick_times-1):
    color_pick_index = random.randint(1,4)
    number_pick_index = random.randint(1,13)
    index_used_this_round = str(color_pick_index) + str(number_pick_index)
    while(index_used_this_round in index_used):
            color_pick_index = random.randint(1,4)
            number_pick_index = random.randint(1,13)
            index_used_this_round = str(color_pick_index) + str(number_pick_index)
    
    match color_pick_index:
        case 1:
            color_picked = "黑桃"
        case 2:
            color_picked = "梅花"
        case 3:
            color_picked = "紅心"
        case 4:
            color_picked = "方塊"
    match number_pick_index:
        case 1:
            number_picked = "A"
        case 11:
            number_picked = "J"
        case 12:
            number_picked = "Q"
        case 13:
            number_picked = "K"  
        case _:
            number_picked = str(number_pick_index)

    index_used.append(index_used_this_round)
    print("你拿到:")
    print(color_picked+' '+number_picked)
