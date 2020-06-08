class Player:
    def __init__(self,name ,health,damge,block,turn ):
        self.name = name
        self.health = health
        self.damage=damge
        self.block = block
        self.turn = turn

    def player_turn(self,turn):
        if turn:
            self.turn==True
        else:
            self.turn=False

    def card_player(self, card):
        if (card =="block" and self.turn==True):
            self.block+=5
        else :
            self.block = 0
        if (card == "attacl" and self.turn==True):
            return 5


