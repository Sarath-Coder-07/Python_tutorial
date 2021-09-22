import random


def roll_dice():
    return random.randint(1, 6)

def play():
    val= int(input("Which dice you choose\n Type 1 for Crooked dice (only even number on dice)\n Type 2 for Normal dice\n"))
    if val == 2:
        snake_at_pos = [14, 30, 28, 22, 45, 50, 99]
        cur_pos = 1
        print("Game Starting current pos: " + str(cur_pos))
        while True:
            n = roll_dice()
            print("Number on dice :" + str(n))
            cur_pos = n + cur_pos
            print("cur_pos " + str(cur_pos))
            if cur_pos >= 100:
                print("Winner Winner chicken diner!!!")
                break
            if cur_pos in snake_at_pos:
                print("Ohhno Snake attacked, Start again!!")
                cur_pos = 1
            else:
                continue
    elif val == 1:
        snake_at_pos = [14, 30, 28, 22, 45, 50, 99]
        cur_pos = 1
        print("Game Starting with crooked dice, current pos: " + str(cur_pos))
        while True:
            n = roll_dice()
            if n % 2 == 0:
                print("Number on dice :" + str(n))
                cur_pos = n + cur_pos
                print("cur_pos " + str(cur_pos))
                if cur_pos >= 100:
                    print("Winner Winner chicken diner!!!")
                    break
                if cur_pos in snake_at_pos:
                    print("Ohhno Snake attacked, Start again!!")
                    cur_pos = 1
                else:
                    continue
            else:
                continue
    else:
        print("Invalid input")





play()

