from microbit import *
import random

dice1 = Image('00000:' 
              '03530:' 
              '05950:' 
              '03530:' 
              '00000:')

dice2 = Image('35300:' 
              '59500:' 
              '35353:' 
              '00595:' 
              '00353:')

dice3 = Image('95000:' 
              '53530:' 
              '05950:' 
              '03535:' 
              '00059:')

dice4 = Image('35353:' 
              '59595:' 
              '35353:' 
              '59595:' 
              '35353:')

dice5 = Image('35353:' 
              '59595:' 
              '35953:' 
              '59595:' 
              '35353:')

dice6 = Image('59595:' 
              '35353:' 
              '59595:' 
              '35353:' 
              '59595:')

list_of_all_results = []
list_of_player_results = []
number_of_players = int(input("Podaj ilosc graczy:" ))
number_of_rounds = int(input("Podaj ilosc rund: " ))

for i in range(number_of_players):
    for j in range(number_of_rounds):
        
        while not accelerometer.was_gesture('shake'):
            pass
        
        dice_result = random.randint(1, 6)

        if dice_result == 1:
            display.show(dice1)
        elif dice_result == 2:
            display.show(dice2)
        elif dice_result == 3:
            display.show(dice3)
        elif dice_result == 4:
            display.show(dice4)
        elif dice_result == 5:
            display.show(dice5)
        elif dice_result == 6:
            display.show(dice6)
            
        print(dice_result)
            
        list_of_player_results.append(dice_result)
    
    list_of_all_results.append(list_of_player_results)
    list_of_player_results = []
    
dice_result = 0

sums = [[sum(sublist)] for sublist in list_of_all_results]
print(list_of_all_results)
print(sums)