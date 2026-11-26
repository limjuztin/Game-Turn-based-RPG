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
def recovermana_from_basic(mana,maxmana,amount):# function that recovers mana from basic attack
    return min(mana+amount,maxmana)
class combatant(ABC):# the real blank model that can be uses by anyone like character ,boss or miniboss and such else
    def __init__(self,hp,atk,mana,defense,speed):
        self._hp=hp
        self._maxhp=hp
        self._mana=mana
        self._maxmana=mana
        self._atk=atk
        self._defense=defense
        self._speed=speed
        self._effect=None
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
        old_hp=self._hp
        efective_defense=self._defense #this initiate defense that ready to be added by def+ amount
        if isinstance(self._effect,(defplus)):#if player uses def+ 
            efective_defense+=self._effect.amount #defence added by effect amount
            self._effect=None
        full_dmg=dmg * 100 / (100 + efective_defense)#calculate full dmg with defense stat from the character
        self._hp = max(0, self._hp - full_dmg)# character takes damage and their hp will not be negative
        actual_dmg=old_hp-self._hp #this calculate the real dmg in case the character's hp if below 0
        print(f"{self.__class__.__name__} has taken {actual_dmg:g} dmg") #display how much dmg taken to the player
        print(f"HP: {self._hp:g}/{self._maxhp}") #display the remaining Hp
    def is_alive (self):
        if self._hp>0:
            return True
        return False

class character(combatant):# standard model for many game class like  barbarian, archer, mage , assassin and it can be more with this inheritance
    def __init__(self, hp=10000, atk=300, defense=200, mana=100, speed=125):
        super().__init__(
            hp=hp,
            atk=atk,
            mana=mana,
            defense=defense,
            speed=speed,
        )
        self._effect=None
    @abstractmethod
    def basic_attack(self,target):#why this is an abstract method?because every game classes have their own combo and personality
        pass
    @abstractmethod
    def skill(self,target):#why this is an abstract method?because every game classes have their own combo and personality
        pass
    
    def take_heal(self,heal):
        if not isinstance(heal,(int,float)):
            raise TypeError("heal must be a number")
        if heal<0:
            raise ValueError("heal must not a negative")
        old_hp=self._hp
        self._hp=min(self._maxhp , self._hp + heal)#heal the character according to the heal and make sure if the hp won't exceed the max hp
        actual_heal=self._hp-old_hp
        print(f"{self.__class__.__name__} has obtain {actual_heal:g} hp")#display how much heal obtained to the player
        print(f"HP: {self._hp:g}/{self._maxhp}") #display the remaining Hp
    def take_effect(self,effect):
        if self._effect is not None:
            return False
        self._effect=effect
        return True
    def check_status(self):#display the hp, mana and effect to the player
        print(f"{self.__class__.__name__} status:")
        print(f"    HP      : {self._hp:g}/{self._maxhp}")
        print(f"    Mana    : {self._mana:g}/{self._maxmana}")
        print(f"    effect  : {self._effect}")

class barbarian(character):# the man who counquer many monsters, no need to ask why he is tanky and has decent atk
    def __init__(self):
        super().__init__(hp=17500, atk=350, speed=100,defense=350)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("barbarian uses axe slam")
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=(effective_atk+(effective_atk*0.1))#barbarian gets another 10% of his atk
        dmg=critical(3,base_dmg)#calculate if the dmg will be crit
        target.take_dmg(dmg)#give damage to the target
        self._mana=recovermana_from_basic(self._mana,self._maxmana,15)
    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<25:
            print("barbarian's mana is not enough to use his skill")
            return False
        print("barbarian uses axe dial")
        
        self._mana-=25
        total_dmg=0
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=effective_atk+(effective_atk*0.2)
        for _ in range(3):# barbarian swing the axe 3 times
            dmg=critical(3,base_dmg)
            total_dmg+=dmg
            print(f"{dmg}")
        print("Dmg given:",total_dmg)
        target.take_dmg(total_dmg)
       
        
class archer(character):#the hunter that mastered archery,why you ask if she has a big atk and decent crit rate? we wonder why
    def __init__(self):
        super().__init__(atk=400, mana=75,defense=225)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("archer uses arrow shooting")
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=effective_atk+(effective_atk*0.2)#archer get another 20% of her atk
        dmg=critical(4,base_dmg)#calculate if the dmg will be crit
        print("Dmg given:",dmg)
        target.take_dmg(dmg)#give damage to the target
        self._mana=recovermana_from_basic(self._mana,self._maxmana,15)
    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<35:
            print("archer's mana is not enough to use her skill")
            return False
        print("archer uses big arrow")
        self._mana-=35
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=effective_atk+(effective_atk*1.2)
        dmg=critical(4,base_dmg)
        print("Dmg Given:",dmg)
        target.take_dmg(dmg)
        

class assassin(character):#a bounty hunter who like sneaky attack,focusing onto weakspots,so dont ask me if he is really like crit chance so much
    def __init__(self):
        super().__init__(hp=8500, atk=350, speed=130,defense=175)
    def basic_attack(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("assassin uses dagger slash")
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=effective_atk+(effective_atk*0.2)#assassin get another 20% of his atk
        dmg=critical(5,base_dmg)#calculate if the dmg will be crit
        target.take_dmg(dmg)#give damage to the target
        self._mana=recovermana_from_basic(self._mana,self._maxmana,15)
    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<25:
            print("assassin's mana is not enough to use his skill")
            return False
        print("assassin uses shadows cut")
        self._mana-=25
        total_dmg=0
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=effective_atk+(effective_atk*0.1)
        for _ in range(5):#assassin will cut the target 5 times
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
        effective_atk=self._atk
        if isinstance(self._effect,atkplus):
            effective_atk+=self._effect.amount
            self._effect=None
        base_dmg=effective_atk+(effective_atk*0.15)#mage get another 15% of her atk
        dmg=critical(2,base_dmg)#calculate if the dmg will be crit
        print("Dmg given:",dmg)
        target.take_dmg(dmg)#give damage to the target
        self._mana=recovermana_from_basic(self._mana,self._maxmana,15)
    def skill(self,target):
        if not isinstance(target,(character)):
            raise ValueError("target must be a character ")
        if self._mana<35:
            print("mage's mana is not enough to use her skill")
            return False
        print("mage uses heal prayer")
        self._mana-=35
        healing=(self._maxhp*0.3)
        target.take_heal(healing)

      
class boss(combatant):# it is a strong fire dragon you know? the classical movie ?
    def __init__(self, hp=100000, atk=500, defense=100, mana=100, speed=125):
        super().__init__(
        hp=hp,
        atk=atk,
        mana=mana,
        defense=defense,
        speed=speed,
        )
    def basic_attack(self, target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        print("Dragon uses claw slash")
        effective_atk=self._atk
        base_dmg=effective_atk+(effective_atk*0.1)#mage get another 15% of her atk
        dmg=critical(2,base_dmg)#calculate if the dmg will be crit
        print("Dmg given:",dmg)
        target.take_dmg(dmg)
        self._mana=recovermana_from_basic(self._mana,self._maxmana,15)
    def skill(self,target):
        if not isinstance(target,(character,boss)):
            raise ValueError("target must be a character or a boss")
        if self._mana<35:
            print("Dragons mana isn't enough to use its skill")
            return False
        print("Dragon uses fire ball")
        self._mana-=35
        effective_atk=self._atk
        base_dmg=effective_atk+(effective_atk*0.5)
        dmg=critical(2,base_dmg)
        print("Dmg Given:",dmg)
        target.take_dmg(dmg)
#not implemented yet 
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
    def __init__(self,amount):
        self.amount=amount
        self.status="ATK+"
    def apply(self, target):
        target.take_effect(self)
class defplus(effect):
    def __init__(self,amount):
        self.amount=amount
        self.status="DEF+"
    def apply(self,target):
        target.take_effect(self)
        