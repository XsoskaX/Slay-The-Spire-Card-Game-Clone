class Cards:
    def __init__(self,type ,cost , damage , block):
        self.type=type
        self.cost=cost
        self.damage=damage
        self.block=block

    def Show_card_info(self):


        return f"Type {self.type}",f"cost {self.cost}",f"damge {self.damage}"

car = Cards("hassan",1,2,3)
car.Show_card_info()