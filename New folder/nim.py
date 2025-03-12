def pb(heap):
    print(f"current heap{'|'*heap}")

def user(heap):
    while True:
        try:
            sticks_to_remove=int(input(f"enter no of sticks to remove (minimum 1, maximum {min(heap,heap //2 )}):"))
            if 1<=sticks_to_remove<=min(heap,heap//2):
                break
            else:
                print("invalid input,try again")
        except ValueError:
            print("invalid input,try again")
    return sticks_to_remove

def computer(heap):
    xor_sum=heap
    for i in range(heap):
        xor_sum^=i

    if xor_sum==0:
        max_sticks=min(heap,heap//2)
        sticks_to_remove=random.randint(1,max_sticks)
    else:
        max_sticks=min(heap // 2,heap)
        sticks_to_remove=max(1,min(max_sticks,heap-xor_sum))
    
    return sticks_to_remove

def nim():
    heap=16
    player=1

    while heap>1:
        pb(heap)

        if player == 1:
            player_name="player 1"
            sticks_to_remove=user(heap)
        else:
            player_name="computer"
            sticks_to_remove=computer(heap)

        
        heap-=sticks_to_remove
        print(f"{player_name} removed {sticks_to_remove} sticks")

        player=3-player
    
    pb(heap)
    winner="player 1" if player ==2 else "computer"
    print(f"Player {player} picks last stick")
    print(f"\n{winner} wins")

if __name__=="__main__":
    import random
    nim()
