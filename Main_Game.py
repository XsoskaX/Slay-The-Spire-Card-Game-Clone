from Player import Player
from Cards import Cards
from Enemy import Enemies
import random
playerOne= Player("hassan",150,0,0,True)
enemy_one = Enemies("punisher",20,3,False)
attack_card1 = Cards("attack1",1,6,0)
attack_card2 = Cards("attack2",1,9,0)
block_card1 = Cards("block1",1,5,0)
block_card2 = Cards("block2",1,8,0)
cardss= [attack_card1,attack_card2,block_card1,block_card2]
eny = {
  "slash"  : attack_card1,
  "bash"   : attack_card2,
  "protect": block_card1,
  "guard"  : block_card2
}
# def attack (a,b):
#
#     playerOne.damage=a
#     e = b - playerOne.damage
#     if(playerOne.turn):
#         print(playerOne.damage)
#         print(b)
#         print(e)
#
# attack(attack_card1.damage,enemy_one.health)



def rand_num():
    return random.randint(0, 3)


def pick_cards():
    card_picked =[]
    for x in range(4):
        card_picked.append(cardss[rand_num()])
        # print(card_picked[x])
    return card_picked

# print(pick_cards())




def player_choise():
    a = pick_cards()
    print("Please Choose a card _________________")
    b = 1
    for x  in a :
        print(b,x.Show_card_info())
        b+=1
    return a



def player_picking(cards_choosen):
    p1_choose =input("please enter a card number ")
    if(p1_choose=="1"):
        print(cards_choosen[0].Show_card_info())
        

player_picking(player_choise())