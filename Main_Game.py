from Player import Player
from Cards import Cards
from Enemy import Enemies
import random
playerOne= Player("hassan",150,0,0,True)


#enemies beta type 
enemy_one = Enemies("Dawnsoul",15,8,False)
enemy_two = Enemies("slayer",25,5,False)
enemy_three = Enemies("Mage",10,10,False)
enemy_four = Enemies("The Icy Hag",30,2,False)
enemies_array = [enemy_one,enemy_two,enemy_three,enemy_four]
enemies_dictionary={
    "Dawnsoul":enemies_array[0],
    "Slayer":enemies_array[1],
    "Mage":enemies_array[2],
    "The Icy Hag":enemies_array[3]
}


#card choices
attack_card1 = Cards("Melting Kiss",1,6,0)
attack_card2 = Cards("Wild Nova",1,9,0)
block_card1 = Cards("Dragon Flash",1,0,5)
block_card2 = Cards("ice Sheild",1,0,8)
cardss= [attack_card1,attack_card2,block_card1,block_card2]
eny = {
  "Melting Kiss": cardss[0],
  "Wild Nova"   : cardss[1],
  "Dragon Flash": cardss[2],
  "ice Sheild"  : cardss[3]
}

#pick random enemie
def rand_enemy():
    return random.randint(0, 3)
    
# Random number for picking Hand cards
def rand_num():
    return random.randint(0, 3)

# picking the card return array with cards 
def pick_cards():
    card_picked =[]    #This_array_contain_random_cards
    for x in range(4):
        card_picked.append(cardss[rand_num()])
    return card_picked
# it gets the card name from to use with dictionary
def get_cards_names(card_array):
    card_array_name=[]
    for x in card_array:
        card_array_name.append(x.type)
    return card_array_name

# it show the player the card chosen
def show_player_cards(cards_selected):
    y = 1
    for x in cards_selected:
        print(y,"\n")
        x.Show_card_info()
        print("******************************\n")
        y+=1

show_player_cards(pick_cards())

# nyn = get_cards_names(pick_cards())
# print(nyn)

#prompt the hand card info to the player
# def player_picking():
#     choise = input()


