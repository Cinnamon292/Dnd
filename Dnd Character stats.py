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
        self.spellcastAbility = 8 + self.mod('cha')
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
        self.spells= {'FRIENDS': ['Concentration, i have advantage on all cha checks on creature of my choice. creature realizes when spell ends and becomes hostile towards me' 'cantrip'],
		'LIGHT':['touch range, object sheds light in a 20ft radius. if on creature, must make a dex save throw' 'cantrip'],
		'VICIOUS MOCKERY': ['instant spell range 60ft, insult a creature, if it fails a wis save throw it takes 2D4 psychic damage and takes disadvange on next attak roll before the end of the next turn.' 'cantrip'],
		'CURE WOUNDS': ['instant touch, creature i touch gets hit points equal to 1D8 plus spell casting mod, increases by 1D8 per slot level.' '1st level'],
		'TASHAS HIDEOUS LAUGHTER': ['conentration 1 min, 30 ft range, a creature of choice percieves anything hilariously funn and falls, mus succeed on a wisdom save or fall prone, does not effect if has 4 or less intelligence,' '1st level'],
		'THUNDER WAVE': ['instant spell self(15ft cube), all creatures in cube make a con save throw, takes 2D8 and is pushed 10ft, save takes half and is not pushed. increase 1D8 for each level above 1st,' '1st level,'],
		'PHANTASMAL FORCE': ['concentration 1 min range 60ft, a creature in range sees an illusion, must make int check, target can use action to investigate against spell dc. if target is is within 5ft of illusion, spell deals 1D6 psychic damage,' '2nd level'],
		'SHATTER': ['instant spell range 60ft, 10ft raidus sphere centere on point within range, each creature makes con save throw, if failed takes 3D8 thunder damage, half on succes save, inorganic creatures take disadvange on throw,' '2nd level'],
		'SUGGESTION': ['concentration up to 8 hours, range 30ft up to 2 sentences suggest a course of activity, if the creature hurts itself it ends the spell,' '2nd level'],
		'BESTOW COURSE': ['concentration up to 1 min on touch, touched creature takes wis save throw or becom cursed for duration of the spell, check page 218 for all posibilities,' '3rd level'],
		'STINKING CLOUD':['concentration up to 1 min range 90ft, creates a 20ft sphere of yellow nauseating gas centered on a point in range. spreads around corners. each creature if in cloud makes a con save against poison if failed takes turn retching and reeling,' '3rd level'] 
		}


    def mod(self, a: object) -> object: #function that uses the values from the class and creates the ability modifier
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
exit = False
while exit != True:
    command = input('Enter a Command')
    if command == "exit":
        print('Closing Loop')
        exit = True
    if command ==('Skills'):
        for k in (DanDLion.SD):
            s = DanDLion.SD[k]
            x = DanDLion.mod(s[0])
            if DanDLion.SD[k][1]:
                x += DanDLion.prof
            print(k, x)
    if command ==('Spells'):
        for k in (DanDLion.spells):
            s = DanDLion.spells[k]
            x = s[0]
            print(k, x, DanDLion.spellcastAbility + DanDLion.prof)

#this for statement takes the skill dictionary prints out the skills and the modifier for each skill


#this statement looks at the spell dictionary prints out the spells, the level of the spell and the spells ability.

