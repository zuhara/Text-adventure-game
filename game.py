import sys
import ast

def navigate(map,direction,current_position):
    if map[current_position][direction] != 0:
        next_position = map[current_position][direction]
    else:
        next_position = current_position
    return next_position

def main():
    print("Start")
    print("Type 'n' for NORTH")
    print("Type 's' for SOUTH")
    print("Type 'w' for WEST")
    print("Type 'e' for EAST")
    print()
    print("You are in the hall now")
    print()
    
    sys.argv.pop(0)
    
    with open(sys.argv[0]) as f:
        map = ast.literal_eval(f.read())
    
    d = ""
    current_position = 1
    while True  :
        d = input(">>>>> ")
        if d == 'exit':
            break
        next_position = navigate(map,d,current_position)
        
        if current_position == next_position:
            print("Take another way")
            continue
        
        print("You are in {}".format(map[next_position]['room']))
        current_position = next_position
    
main()
