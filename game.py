def navigate(map,direction,current_position):
    if map[current_position][direction] != 0:
        next_position = map[current_position][direction]
    else:
        next_position = current_position
    return next_position

def main():
    print("Start")
    
    map = {1:{'n':2,'s':3,'e':0,'w':0,'room':'Hall'},2:{'n':0,'s':1,'e':3,'w':0,'room':'Kitchen'},3:{'n':1,'s':0,'e':0,'w':2,'room':'Garden'}}
    
    d = ""
    current_position = 1
    while d != "exit"  :
        d = input(">>>>> ")
        next_position = navigate(map,d,current_position)
        
        if current_position == next_position:
            print("Take another way")
            continue
        
        print("You are in {}".format(map[next_position]['room']))
        current_position = next_position

main()
