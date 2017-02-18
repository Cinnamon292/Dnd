class characterStats: #specify's dandilions abilty scores and creates values for them.
    def __init__(self, name, str = 13, dex = 14, con = 13, int = 14, wis = 13, cha = 14,):
        self.name = name
        self.strength = str
        self.dexterity = dex
        self.constitution = con
        self.intelligence = int
        self.wisdom = wis
        self.charisma = cha
        self.prof = 3
	self.spellcastAbility = 8 + cha 
        self.SD = {'Acrobatics':['dex', False], #Dictionary for  functions to pull up skills and if Dandlion is trained
            'Animal Handling': ['wis', False],  # in them or not
             'Arcana': ['int', False],
            'Athletics': ['str', False],
            'Deception': ['cha', True],
             'History': ['int', False],
             'Insight': ['wis', False],
             'Intimidation': ['cha', False],
             'Medicine': ['wis', False],
             'Nature': ['int', False],
             'Perception': ['wis', False],
              'Performance': ['cha', True],
              'Persuasion': ['cha', False],
              'Religion': ['int', False],
             'Sleight of Hand': ['dex', False],
             'Stealth': ['dex', True],
              'Survival': ['wis', False]
            }
	#Dicionary for spell. tells the spell its level and its abilty
	self.Spells= {'cure wounds':['Instantaneous spell at touch range. "a creature i touch regains a number of hit points = to 1D8 + my spell casting ability modifier. Increase by 1D8 for each slot level above 1st"', '1st level spell'], 
	'Shatter': ['Instantaneous spell with range of 60ft.', 'A sudden loud ringing noise erupts from a point of my choice within range. each creature in a 10ft radius shpere centered at point must make a constitution saving throw. takes 3D8 thunder damage or half on a succesfull throw']
	    }


    def mod(self, a): #function that uses the values from the class and creates the ability modifier
        if a == 'str':
            return((self.strength -10)//2)
        if a == 'dex':
            return((self.dexterity -10)//2)
        if a == 'con':
            return((self.constitution -10)//2)
        if a == 'int':
            return((self.intelligence -10)//2)
        if a == 'wis':
            return((self.wisdom -10)//2)
        if a == 'cha':
            return((self.charisma -10)//2)





    def attack(self, a):

        if a == 'spell':
            return 7
        if a == 'melee':
            return self.mod('str') + self.prof
        if a =='weapon':
            return self.mod('dex') + self.prof

        a = "+"
        b = self.strength + self.prof

        a += str(b)
        return a


DanDLion = characterStats("Dandlion")
Char = characterStats("char", str = 14, dex = 13 )

#print(DanDLion.strength, Char.strength)
#
for each in [Char, DanDLion]:
    print(each.name)
    print(each.attack('melee'))
    print(each.attack('spell'))
    print(each.attack('weapon'), '\n')


#this for statement takes the skill dictionary prints out the skills and the modifier for each skill
for k in (DanDLion.SD):
    s = DanDLion.SD[k]
    x = DanDLion.mod(s[0])
    if DanDLion.SD[k][1]:
        x += DanDLion.prof
    print(k, x)

#this statement looks at the spell dictionary prints out the spells, the level of the spell and the spells ability.
for k in (DandDLion.spells):
	s = DandDLion.spells[k]
	x = DandDLion.mod(s[0])
	print(k,x, DanDLion.spellcastingAbility + DanDLion.prof


