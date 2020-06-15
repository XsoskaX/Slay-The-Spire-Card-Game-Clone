class Cards:
    def __init__(self,type ,cost , damage , block):
        self.type=type
        self.cost=cost
        self.damage=damage
        self.block=block

    def Show_card_info(self):
        if(self.damage!=0):
            print(f" {self.type}",f"cost {self.cost}",f"damge {self.damage}") 
        else:
            print(f" {self.type}",f"cost {self.cost}",f"block {self.block}") 

        

