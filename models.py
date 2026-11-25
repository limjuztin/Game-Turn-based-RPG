from abc import ABC ,abstractmethod # so we can make a real blueprint for a character and effect or maybe more.
import random # so we can make a RNG in this game,such as crit rate/chance
def critical(chance,atk):#function that make dmg Critical
    #chance is a number that state how often the dmg will be critical (just make chance * 10 so it will be percentage),example: 6=60%, 5=50%
    #then why i use interger for chance??? because i dont know yet how to make random randint can choose a float .
    if not isinstance(chance,int) :
        raise TypeError("chance must be a interger")
    if chance<0 or chance>10:
        raise ValueError("chance must between 0 to 10")
    if not isinstance(atk,(int,float)):
        raise TypeError("atk must be a number")
    if atk <0:
        raise ValueError("atk can't be negative")
    if random.randint(1,10)<=chance:
        print("CRIT DMG!!!")
        return atk*2
    else:return atk
class character(ABC):# standard model for many game class like barbarian, archer, mage , assassin and it can be more with this inheritance
    def __init__(self, hp=10000, atk=300, defense=200, mana=100, speed=125):
        self._hp=hp
        self._maxhp=hp
        self._atk=atk
        self._defense=defense
        self._mana=mana
        self._maxmana=mana
        self._speed=speed
        self.__effect=None
    @abstractmethod
    def basic_attack(self,target):#why this is an abstract method?because every game classes have their own combo and personality
        pass
    @abstractmethod
    def skill(self,target):#why this is an abstract method?because every game classes have their own combo and personality
        pass
    def take_dmg(self,dmg):
        if not isinstance(dmg,(int,float)):
            raise TypeError("Dmg taken must be number")
        if dmg<0:
            raise ValueError("Dmg can't be negative")
        self._hp = max(0, self._hp - dmg)# character takes damage and their hp will not be negative
    #not implemented yet
    def take_heal(self,heal):
        pass
    def take_effect(self,effect):
        pass
    def cek_status(self):
        pass
    def is_alive(self):
        pass

class barbarian(character):# the man who counquer many monsters, no need to ask why he is tanky and has decent atk
    def __init__(self):
        super().__init__(hp=17500, atk=350, speed=100)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("barbarian uses axe slam")
        base_dmg=(self._atk+(self._atk*0.1))#barbarian gets another 10% of his atk
        dmg=critical(3,base_dmg)#calculate if the dmg will be crit
        target.take_dmg(dmg)#give damage to the target

    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<25:
            print("barbarian's mana is not enough to use his skill")
            return False
        print("barbarian uses axe dial")
        self._mana-=25
        total_dmg=0
        base_dmg=self._atk+(self._atk*0.2)
        for rotation in range(3):# barbarian swing the axe 3 times
            dmg=critical(3,base_dmg)
            total_dmg+=dmg
            print(f"{dmg}")
        print("Dmg given:",total_dmg)
        target.take_dmg(total_dmg)
        
class archer(character):#the hunter that mastered archery,why you ask if she has a big atk and decent crit rate? we wonder why
    def __init__(self):
        super().__init__(atk=400, mana=75)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("archer uses arrow shooting")
        base_dmg=self._atk+(self._atk*0.2)#archer get another 20% of her atk
        dmg=critical(4,base_dmg)#calculate if the dmg will be crit
        print("Dmg given:",dmg)
        target.take_dmg(dmg)#give damage to the target

    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<35:
            print("archer's mana is not enough to use her skill")
            return False
        print("archer uses big arrow")
        self._mana-=25
        base_dmg=self._atk+(self._atk*1.2)
        dmg=critical(4,base_dmg)
        print("Dmg Given:",dmg)
        target.take_dmg(dmg)

class assassin(character):#a bounty hunter who like sneaky attack,focusing onto weakspots,so dont ask me if he is really like crit chance so much
    def __init__(self):
        super().__init__(hp=8500, atk=350, speed=130)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("assassin uses dagger slash")
        base_dmg=self._atk+(self._atk*0.2)#assassin get another 20% of his atk
        dmg=critical(5,base_dmg)#calculate if the dmg will be crit
        target.take_dmg(dmg)#give damage to the target
    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<25:
            print("assassin's mana is not enough to use his skill")
            return False
        print("assassin uses shadows cut")
        self._mana-=25
        total_dmg=0
        base_dmg=self._atk+(self._atk*0.1)
        for cut in range(5):#assassin will cut the target 5 times
            dmg=critical(5,base_dmg)
            total_dmg+=dmg
            print(dmg)
        print("Dmg Given:",total_dmg)
        target.take_dmg(total_dmg)
           
class mage(character):#she is the lovely girl who want to 'heal the world',you get it? no? so thats why her atk,crit is so low and her skill is healing
    def __init__(self):
        super().__init__(atk=250, mana=150, speed=105)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("mage uses water ball")
        base_dmg=self._atk+(self._atk*0.15)#mage get another 15% of her atk
        dmg=critical(2,base_dmg)#calculate if the dmg will be crit
        print("Dmg given:",dmg)
        target.take_dmg(dmg)#give damage to the target
    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<35:
            print("mage's mana is not enough to use her skill")
            return False
        print("mage uses heal prayer")
        self._mana-=25
        healing=(self._maxhp*0.3)
        target.take_heal(healing)

#not implemented yet        
class boss():
    pass

class inventory:
    def __init__(self):
        self.items=[]
    def input_item(self,data):
        pass
    def use_item(self):
        pass

class barang():
    def __init__(self,name,effect):
        self.itemname=name
        self.effect=effect
    def use(self,target):
        self.effect.apply(target)

class effect(ABC):
    @abstractmethod
    def apply(self,target):
        pass

class heal(effect):
    def __init__(self,amount):
        self.amount=amount
    def apply(self, target):
        target.take_heal(self.amount)

class atkplus(effect):
    def __init__(self,amount,status="ATK+"):
        self.amount=amount
        self.status=status
    def apply(self, target):
        target.take_effect(self.status)