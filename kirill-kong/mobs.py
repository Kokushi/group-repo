#item stats are in this order HEALTH,ATTACK,DEFENSE
from items import *
mob_zero = { 
     "id": "0", 
     "name": "Ghost", 
     "stats": [12, 1, 2], 
     "description": "2sP0okY4m3", 
     "loot": [item_rusty_sword, item_leather_shield, item_leather_helmet, item_leather_chestplate] 
 } 

mob_one = { 
 	"id": "1", 
 	"name": "Zombie", 
 	"stats": [12, 2, 1], 
 	"description": "The Undead, peices of flesh hang loose", 
 	"loot": [item_rusty_sword, item_leather_shield, item_leather_helmet, item_leather_chestplate] 
 } 
 
 
mob_two = { 
 	"id": "2", 
 	"name": "Skeleton", 
 	"stats": [12, 2, 1], 
 	"description": "Its bones rattle as it moves", 
 	"loot": [item_rusty_sword, item_leather_shield, item_leather_helmet, item_leather_chestplate] 
 } 
mob_three = { 
 	"id": "3", 
 	"name": "Slime", 
 	"stats": [12, 2, 2], 
 	"description": "Squishy and slightly adorable", 
 	"loot": [item_rusty_sword, item_leather_shield, item_leather_helmet, item_leather_chestplate] 
 } 
mob_four = { 
 	"id": "4", 
 	"name": "Spider", 
 	"stats": [19, 3, 3], 
 	"description": "Too many legs to be friendly", 
 	"loot": [item_iron_sword, item_copper_shield, item_iron_helmet, item_iron_chestplate] 
 } 
mob_five = { 
 	"id": "5", 
 	"name": "Gorilla Minion", 
 	"stats": [15, 3, 4], 
 	"description": "This ape doesnt monkey around, a loyal servant of Kirill-Kong", 
 	"loot": [item_copper_sword, item_wooden_shield, item_copper_helmet, item_copper_chestplate] 
 } 
mob_six = { 
 	"id": "6", 
 	"name": "Phantom", 
 	"stats": [17, 4, 2], 
 	"description": "Strikes fear in even the bravest of warriors", 
 	"loot": [item_platinum_sword, item_platinum_shield, item_platinum_helmet, item_platinum_chestplate] 
 } 
mob_seven = { 
 	"id": "7", 
 	"name": "Dragon", 
 	"stats": [25, 8, 8], 
 	"description": "Slightly smaller than expected, but dangerous nonetheless", 
 	"loot": [item_platinum_sword, item_platinum_shield, item_platinum_helmet, item_platinum_chestplate] 
 } 
mob_eight = { 
 	"id": "8", 
 	"name": "Balrog", 
 	"stats": [25, 8, 8], 
 	"description": "A horned demon from the depths of hell", 
 	"loot": [item_platinum_sword, item_platinum_shield, item_platinum_helmet, item_platinum_chestplate] 
 } 
mob_nine = { 
 	"id": "9", 
 	"name": "Orangutan Warrior", 
 	"stats": [15, 3, 2], 
 	"description": "A loyal follower of Kirill-Kong, its long arms give it a vicious swing", 
 	"loot": [item_copper_sword, item_wooden_shield, item_copper_helmet, item_copper_chestplate] 
 } 
mob_ten = { 
 	"id": "10", 
 	"name": "Chimp Scout", 
 	"stats": [15, 2, 3], 
 	"description": "Fast and agile, it will be tough to defend from this follower", 
 	"loot": [item_copper_sword, item_wooden_shield, item_copper_helmet, item_copper_chestplate] 
 } 

mob_eleven = { 
 	"id": "11", 
 	"name": "Reaper", 
 	"stats": [21, 6, 6], 
 	"description": "A hooded ghoul, beware it's deathly touch", 
 	"loot": [item_steel_sword, item_iron_shield, item_steel_helmet, item_steel_chestplate] 
 } 
mob_twelve = { 
 	"id": "12", 
 	"name": "Wraith", 
 	"stats": [21, 6, 6], 
 	"description": "A lost soul wrought with revenge", 
 	"loot": [item_steel_sword, item_iron_shield, item_steel_helmet, item_steel_chestplate] 
 } 
mob_thirteen = { 
 	"id": "13", 
 	"name": "Gremlin", 
 	"stats": [19, 3, 5], 
 	"description": "An ugly little creature with claws that could do some serious damage", 
 	"loot": [item_iron_sword, item_copper_shield, item_iron_helmet, item_iron_chestplate] 
 } 
mob_fourteen = { 
 	"id": "14", 
 	"name": "Mimic", 
 	"stats": [19, 5, 3], 
 	"description": "This nasty being tricks travellers by imitating a chest or door", 
 	"loot": [item_iron_sword, item_copper_shield, item_iron_helmet, item_iron_chestplate] 
 } 
mob_fifteen = { 
 	"id": "15", 
 	"name": "Kirill-Kong", 
 	"stats": [30, 12, 12], 
 	"description": "Kirill-Kong himself, a cunning but brutish fiend it will take all your strength to bring him down", 
 	"loot": [] 
 } 

 
all_mobs = {
     "0": mob_zero, 
     "1": mob_one, 
     "2": mob_two,
     "3": mob_three,
     "4": mob_four,
     "5": mob_five,
     "6": mob_six,
     "7": mob_seven,
     "8": mob_eight,
     "9": mob_nine,
     "10": mob_ten,
     "11": mob_eleven,
     "12": mob_twelve,
     "13": mob_thirteen,
     "14": mob_fourteen,
     "15": mob_fifteen,
} 
