## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary
from arrays import creature_kinds as name_list
summon_realm = ["Nether", "Hell", "Crypt", "Void", "Golem"]
import random
## Cards class
class Summon():
	#creature_kinds=["a","b","c"];
	realm = "";
	name = "";
	symbol = "#";
	power = 1;
	life = 1;
	cost = 0;
	rarity = random.randint(1,3);
	tapped = False;
	
	def __init__(self):
		self.cost = random.randint(0,rarity*3)
		self.power = random.randint(0,rarity)
		self.life = random.randint(0,rarity)
		self.realm = creature_kinds[random.randint(0,len(summon_realm)-1)]; # Human, Dinosaur Avatar, Vampire...
		self.name = name_list[random.randint(0,len(name_list)-1)] + " of the " + name_list[random.randint(0,len(name_list)-1)]	

	def summon(self,player):

				
		# 0- count untap land on the land_zone
		# 1- check for the card cost
		# 2- tap land
		# 3- remove it self from the hand array
		# 4- add it self to the field


# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	Mana = []; # lands are divided by color in this 2d array. so you can easily know how meny of each color their is with len(lands_zone[index])
	summon_zone = [];
	graveyard = [];
	deck=[];
	cursor_x = 0;
	cursor_y = 2;
	
	def __init__(self, name, health):
		self.name = "Bob Smith",
		self.health = health,
		
	def shuffle_deck():
		random.shuffle(self.deck)
		
	def draw(self,amounth):
		for x in range(amounth):
			draw = self.deck[-1]
			self.deck.pop()
			self.hand.append(draw)
		
	def gen_deck(self):
		# This is just a temporary solution.
		land_count = 30;
		creature_count = 30;
		
		for x in range(land_count):
			self.deck.append(Land())
		for x in range(creature_count):
			self.deck.append(Creature())
		random.shuffle(self.deck)


class AI:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	mana_zone = [];
	creatures_zone = [];
	permanents_zone = []; # for artefacts, enchantments, plainwalkers?, non-creature.
	graveyard = [];
	deck=[];
	cursor_x = 0;
	cursor_y = 2;
	card_back="?"
	
	def __init__(self, name, health):
		self.name = "BOT",
		self.health = health,
		
	def shuffle_deck():
		random.shuffle(self.deck)
		
	def draw(self,amounth):
		for x in range(amounth):
			draw = self.deck[-1]
			self.deck.pop()
			self.hand.append(draw)
		
	def gen_deck(self):
		# This is just a temporary solution.
		land_count = 30;
		creature_count = 30;
		
		for x in range(land_count):
			self.deck.append(Land())
		for x in range(creature_count):
			self.deck.append(Creature())
		random.shuffle(self.deck)
