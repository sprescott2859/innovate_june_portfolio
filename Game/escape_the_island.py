# inventory = []
# sc_inventory = ["Amulet Of Relflection", "Potion Of Healing", "Crystal Shard", "Woodcutter's Axe", "Scythe"]
# gt_inventory = ["Enchanted Blade", "Enchatnted Shield", "Enchanted Scroll", "Goblet Of Fire", "Enchanted Ring"]
# # These globals will enable inventory list's to be added to the main inventory global
# sc_explored = False
# gt_explored = False
# # These globals will identify which area the player has explored and what items have been recoved throughout the game
# def island_introduction():
#     print("You are a part of an envoy of ships at sail, of which is decimated by a gigantic 8 headed hydra of which emerges out of the ocean. You are thrown into the sea when it smashes through the ship of which you are on, you manage to get onto a piece of driftwood but loose consciousness shortly thereafter…")
#     print("When you awaken, you find yourself in a large campsite surrounded by tall stockade fences. This campsite you notice, is filled with soldiers (mostly humans and minotaur’s). A Feline woman approaches you and identifies herself as Kyolie, “You’re fortunate, most that washed up were already dead, now that you seem rested, I expect that you will be leaving our camp today.” After she explains that this is a campsite for a rebellion against a tyrant, you leave the camp and walk along a winding path until you reach a crossroad, one path takes you to a Forest, and the other leads into the Mountains.")
#     print("Would you like to go through the forest or the mountains?")
#     print("Select 1 for the forest or 2 for the mountains.")
#     answer1 = input(">> ")
#     if answer1 == ("1"):
#         forest()
#     elif answer1 == ("2"):
#         mountains()
#     else:
#         island_introduction()
# # This should print the intro and provide first IfElse Staement Selection (Player Input)
# def forest():
#     print("You enter the forest, you notice a largely overgrown path through the forest, you also notice a ritual being performed through some trees away from the overgrown path.")
#     print("Select 1 to go down the overgrown path, or 2 to interrupt the ritual.")
#     answer2 = input(">> ")
#     if answer2 == ("1"):
#         secluded_cabin()
#     elif answer2 == ("2"):
#         ritual()
#     else:
#         island_introduction()
# # This is the same to intro code.
# def mountains():
#     print("You come to the mountains, you notice a small overhang a small stream and a winding path up to what you notice to be a Grand temple in the mountains. You also notice a reptilian searching through around half a dozen corpses.")
#     print("Select 1 to continue along the path to the Grand Temple, or 2 to attempt to loot one of the corpses.")
#     answer3 = input(">> ")
#     if answer3 == ("1"):
#         grand_temple()
#     elif answer3 == ("2"):
#         reptillian_encounter()
#     else:
#         mountains()
# # This is the same to intro code.
# def secluded_cabin():
#     global sc_explored
#     print("You enter the Secluded cabin, and immediately notice that the house is mostly ransacked (It doesn’t look like anyone has lived here in a while. You search the cabin thoroughly and find a small list of items : Amulet of Reflection, Potion of Healing, Crystal Shard, Woodcutters axe, and a Scythe. You spend the night in one of the more secure room of the cabin. The next day you move on to the Bonestrewn Canyon.")
#     inventory.extend(sc_inventory)
#     inventory.sort()
#     sc_explored = True
# # This should update the inventory with the sc inventory and set the True/False Global function to True
#     print("Your Inventory now contains:", inventory)
#     Encounter()
# def ritual():
#     print("You attempt to interrupt the ritual being performed, and are quickly murdered by the coven.")
#     print("Game Over")
#     game_over()
# def game_over():
#     print("Press 0 to restart the game.")
#     answer_r = input(">> ")
#     if answer_r == ("0"):
#         island_introduction()
#     else:
#         game_over()
# def grand_temple():
#     global gt_explored
#     print("You enter the Grand Temple, of which you notice to be remarkable empty, aside from one High priestess, she immediately notices and identifies herself as Kynessa, “I have seen your coming to this temple, and believe these items will be of use to you” she hands you a pack of items of which contains :  A Enchanted blade, An Enchanted Shield, An Enchanted Scroll, A Goblet of fire, and an Enchanted Ring. After spending the night at the temple you move Bonestrewn Canyon.")
#     inventory.extend(gt_inventory)
#     inventory.sort()
# # Forgot to input this .sort into initial code, remember to mention
#     gt_explored = True
#     print("Your inventory now contains:", inventory)
#     Encounter()
# def reptillian_encounter():
#     print("You attempt to loot one of the corpses, the reptillian quickly approaches and murders you before you have any chance to respond.")
#     print("Game Over")
#     game_over()
# def Encounter():
#     print("You enter the Bonestrewn Canyon where there are the remains of skeletons from battles from all time. You are aware that you are not alone as people rise from bedding of all descriptions. The bones are used to make coverings with tarpaulins; horse carcasses used to cover two or three people at a time. Human leg bones and arms to burn for fires. Skulls stacked as walls to shelter behind.You encounter 3 people who may be able to help you escape the canyon")
#     print("You need to find your way out of the canyon. The canyon has high walls that cannot be climbed, you need to converse with those who have been left here in the canyon.Not all speak your language so you must be careful to make the correct contacts to escape the Bonestrewn Canyon")
#     contact()
# def contact():
#     print("Select 1, select 2, or select 3 ")
#     answer1 = input(">> ")
#     if answer1 == ("1"):
#         ignorant()
#     elif answer1 == ("2"):
#         friendly()
#     elif answer1 == ("3"):
#         thief()
#     else:
#         contact()
# def ignorant():
#     print("Ignores You!")
#     contact()
# def friendly():
#     print("Hello, Can I help you?")
#     answer2 =  input("1 for Yes! or 2 for No! >> ")
#     if answer2 == ("1"):
#         print("If you are a good reader; you can find your way to a Hidden Camp; However, On refection, I can advise you that there could be an Unmarked Cave nearby! ")
#         next_day()
#     elif answer2 == ("2"):
#         print("No!...ok then you will be sorry!")
#         next_day()
#     else:
#         game_over()
# def thief():
#     print("Is sleeping")
#     contact()
# def next_day():
#     global sc_explored
#     global gt_explored
#     if sc_explored == True and gt_explored == False:
#         print("You wake up the next day alone after resting in the canyon. Only when you wake do you realise you have been robbed! You have lost: Wood cutters axe and Scythe ")
#         inventory.remove("Woodcutter's Axe")
#         inventory.remove("Scythe")
#         print(inventory)
#     elif gt_explored == True and sc_explored == False:
#         print("You wake up the next day alone after resting in the canyon. Only when you wake do you realise you have been robbed! You have lost: Goblet Of Fire, Enchanted Ring")
#         inventory.remove("Goblet Of Fire")
#         inventory.remove("Enchanted Ring")
#         print(inventory )
# island_introduction()

# # This section allows encourages the player to make a defined choice on their journey.
# def hidden_village(): 
#     print("You enter into a dense wooded area that has an opening leading to hidden camp in a wooden fort surrounded and protected by the children of hydra on the ramparts, skeletons armed with swords, shields and spears who are impervious to any form of attack - your confronted by the camp elder and his personal Praetorian guard.")

# def unmarked_cave (): 
#     print("You fall down some scree into the entrance to what seems to be a Unmarked Cave. There is a tree just outside the entrance with what seems to be a golden rams fleece draped over it. You go to take a further look only for someone to call to you ‘gis a job, gis a job’ astounded by what your hearing in such a remote place, you enter the cave only to be confronted by a lizard like banshee sorceress with tree eyes and snakes for hair. You are then met with “Who dares to desecrate the sanctity peace and of my Temple!“. What follows is a boulder falling behind you sealing your only exit.")
# def a_fork_in_the_path():
#     print("You leave the bonestrewn canyon and your presented with two paths one to the left and another to the right. ")
#     print("1 for left and 2 for right: [1/2]")
    
#     answer1 = input ("Enter 1 or 2: ")
    
#     if answer1 == ("1"):
#         hidden_village()
#         print("You can’t understand the sanskrit language he uses towards you, the only option you have is to defend or protect yourself with the items you have on your person, you choose: 1. The Enchanted Shield, 2. The Blade, 3. Enchanted Scroll.")
        
#         input == ("Choose 1, 2 or 3 to protect yourself: ")
#         answer2 = input ("Enter 1, 2 or 3: ") 
#         if answer2 == ("1"):
#                 print("The Enchanted Shield - You pull out the shield in attempt to defend yourself from perceived oncoming attacks - the enchantment on the shield means it has a highly reflective surface which the catches the rays from the sun reflecting them onto all in front of you which has a blinding effect.The children of hydra having no eyes aren’t affected and attack slicing you to ribbons, you die a death of 1000 cuts, Game Over!")
#                 game_over()
#         elif answer2 == ("2"):
#                 print("The Enchanted Blade - You select the blade to defend yourself but upon unsheathing you see its made out of glass, still you attempt to attack one of the children of hydra who shatter the blade with all of the shards being directed into your body which spark and suddenly you become engulfed in flames taking your last napalm filled breath, Game Over!")
#                 game_over()
#         elif answer2 == ("3"):
#                 print("The Enchanted Scroll - You grab the enchanted scroll from your satchel and all most with immediacy the Camp Elder and Praetorian Guard, along with the children of hydra and all the camp dwellers fall to their knees, heads bowed in servitude and, in chorus, being to chant one singular word toward you Deva, deva, deva unbeknownst to you by being in possession of this Enchanted Scroll you have just been proclaimed “heavenly, divine and everything of excellence by the Hidden Camp Dwellers proclaiming you as their one and only God incarnate - You’ve Completed your quest!")
#         else:
#             ()
#     elif answer1 == ("2"):
#         unmarked_cave()
#         print("You search your person for something to protect or defend yourself with, you have 1. The Amulet of Reflection, 2. The Potion of Healing, 3. A Crystal Shard and you choose: ")
#         input == ("Choose 1, 2 or 3 to protect yourself: ")
#         answer3 = input ("Enter 1, 2 or 3: ") 
#         if answer3 == ("1"):
#             print("The Amulet of Reflection - The sorceress tries to entrap and entice you with her bewitching glare, but you put the amulet of reflection before you, reflecting her enchantment back at her, there’s a bloodcurdling scream reaching a tone only a banshee is capable of achieving, shattering the boulder that blocks your exit, just before the lizard like sorceress turns into a solid gold statute with ruby eyes. You manage to get this statue and the golden fleece to some abandoned docks on the far side of the island where you buy a merchant boat with your new found wealth and escape the island, your quest being complete!")
#         elif answer3 == ("2"):
#             print("The Potion of Healing - You select the potion of healing and drink it almost immediately bolstering your health, ready for a fight, after a weary time traveling. The sorceress lets out an almighty whale, temporarily incapacitating you and throwing you into the cave wall. This doesn’t totally deplete your energy so you stand up again, only to be hit with the sound wave of a second shriek, this one cuts like a blade deep into your flesh severing you in half vertically, Game over!")
#             game_over()
#         elif answer3 == ("3"):
#             print("The Crystal Shard - You grab the crystal shard in hand, forming it as a weapon in your defense. The sorceress lets out a deafening shriek which somehow actives a pox held within the crystal shard which starts to melt and then crystallize your hands, then moving up to your arms and torso, down your legs, up your neck then into your open mouth encasing you in a crystallized chasm for all of eternity somewhere between death and life, Game Over!")
#             game_over()
#         else:
#             ()
#     else:   
#         a_fork_in_the_path()





# a_fork_in_the_path()

# inventory = []
# sc_inventory = ["Amulet Of Relflection", "Potion Of Healing", "Crystal Shard", "Woodcutter's Axe", "Scythe"]
# gt_inventory = ["Enchanted Blade", "Enchatnted Shield", "Enchanted Scroll", "Goblet Of Fire", "Enchanted Ring"]
# These globals will enable inventory list's to be added to the main inventory global
# sc_explored = False
# gt_explored = False
# These globals will identify which area the player has explored and what items have been recoved throughout the game
# def island_introduction():
#     print("You are a part of an envoy of ships at sail, of which is decimated by a gigantic 8 headed hydra of which emerges out of the ocean. You are thrown into the sea when it smashes through the ship of which you are on, you manage to get onto a piece of driftwood but loose consciousness shortly thereafter…")
#     print("When you awaken, you find yourself in a large campsite surrounded by tall stockade fences. This campsite you notice, is filled with soldiers (mostly humans and minotaur’s). A Feline woman approaches you and identifies herself as Kyolie, “You’re fortunate, most that washed up were already dead, now that you seem rested, I expect that you will be leaving our camp today.” After she explains that this is a campsite for a rebellion against a tyrant (Although your main concern is escaping the island). You leave the camp and walk along a winding path until you reach a crossroad, one path takes you to a Forest, and the other leads into the Mountains.")
#     print("Would you like to go through the forest or the mountains?")
#     print("Select 1 for the forest or 2 for the mountains.")
#     answer1 = input(">> ")
#     if answer1 == ("1"):
#         forest()
#     elif answer1 == ("2"):
#         mountains()
#     else:
#         island_introduction()
# This should print the intro and provide first IfElse Staement Selection (Player Input)
# def forest():
#     print("You enter the forest, you notice a largely overgrown path through the forest, you also notice a ritual being performed through some trees away from the overgrown path.")
#     print("Select 1 to go down the overgrown path, or 2 to interrupt the ritual.")
#     answer2 = input(">> ")
#     if answer2 == ("1"):
#         secluded_cabin()
#     elif answer2 == ("2"):
#         ritual()
#     else:
#         island_introduction()
# This is the same to intro code.

# def mountains():
#     print("You come to the mountains, you notice a small overhang a small stream and a winding path up to what you notice to be a Grand temple in the mountains. You also notice a reptilian searching through around half a dozen corpses.")
#     print("Select 1 to continue along the path to the Grand Temple, or 2 to attempt to loot one of the corpses.")
#     answer3 = input(">> ")
#     if answer3 == ("1"):
#         grand_temple()
#     elif answer3 == ("2"):
#         reptillian_encounter()
#     else:
        # mountains()
# This is the same to intro code.
# def secluded_cabin():
#     global sc_explored
#     print("You enter the Secluded cabin, and immediately notice that the house is mostly ransacked (It doesn’t look like anyone has lived here in a while. You search the cabin thoroughly and find a small list of items : Amulet of Reflection, Potion of Healing, Crystal Shard, Woodcutters axe, and a Scythe. You spend the night in one of the more secure room of the cabin. The next day you move on to the Bonestrewn Canyon.")
#     inventory.extend(sc_inventory)
#     inventory.sort()
#     sc_explored = True
# This should update the inventory with the sc inventory and set the True/False Global function to True
#     print("Your Inventory now contains:", inventory)
#     Encounter()
# def ritual():
#     print("You attempt to interrupt the ritual being performed, and are quickly murdered by the coven.")
#     print("Game Over")
#     game_over()
# def game_over():
#     print("Press 0 to restart the game.")
#     answer_r = input(">> ")
#     if answer_r == ("0"):
#         island_introduction()
#     else:
#         game_over()
# def grand_temple():
#     global gt_explored
#     print("You enter the Grand Temple, of which you notice to be remarkable empty, aside from one High priestess, she immediately notices and identifies herself as Kynessa, “I have seen your coming to this temple, and believe these items will be of use to you” she hands you a pack of items of which contains :  A Enchanted blade, An Enchanted Shield, An Enchanted Scroll, A Goblet of fire, and an Enchanted Ring. After spending the night at the temple you move Bonestrewn Canyon.")
#     inventory.extend(gt_inventory)
#     inventory.sort()
# # Forgot to input this .sort into initial code, remember to mention
#     gt_explored = True
#     print("Your inventory now contains:", inventory)
#     Encounter()
# def reptillian_encounter():
#     print("You attempt to loot one of the corpses, the reptillian quickly approaches and murders you before you have any chance to respond.")
#     print("Game Over")
#     game_over()
# def Encounter():
#     print("You enter the Bonestrewn Canyon where there are the remains of skeletons from battles from all time. You are aware that you are not alone as people rise from bedding of all descriptions. The bones are used to make coverings with tarpaulins; horse carcasses used to cover two or three people at a time. Human leg bones and arms to burn for fires. Skulls stacked as walls to shelter behind.You encounter 3 people who may be able to help you escape the canyon")
#     print("You need to find your way out of the canyon. The canyon has high walls that cannot be climbed, you need to converse with those who have been left here in the canyon.Not all speak your language so you must be careful to make the correct contacts to escape the Bonestrewn Canyon")
#     contact()
# def contact():
#     print("Select 1, select 2, or select 3 ")
#     answer1 = input(">> ")
#     if answer1 == ("1"):
#         ignorant()
#     elif answer1 == ("2"):
#         friendly()
#     elif answer1 == ("3"):
#         thief()
#     else:
#         contact()
# def ignorant():
#     print("Ignores You!")
#     contact()
# def friendly():
#     print("Hello, Can I help you?")
#     answer2 =  input("1 for Yes! or 2 for No! >> ")
#     if answer2 == ("1"):
#         print("If you are a good reader; you can find your way to a Hidden Camp; However, On refection, I can advise you that there could be an Unmarked Cave nearby! ")
#         next_day()
#     elif answer2 == ("2"):
#         print("No!...Ok then you will be sorry!")
#         game_over()
#     else:
#         contact()
# def thief():
#     print("Is sleeping")
#     contact()
# def next_day():
#     global sc_explored
#     global gt_explored
#     if sc_explored == True and gt_explored == False:
#         print("You wake up the next day alone after resting in the canyon. Only when you wake do you realise you have been robbed! You have lost: Wood cutters axe and Scythe ")
#         inventory.remove("Woodcutter's Axe")
#         inventory.remove("Scythe")
#         print(inventory)
#         a_fork_in_the_path()
#     elif gt_explored == True and sc_explored == False:
#         print("You wake up the next day alone after resting in the canyon. Only when you wake do you realise you have been robbed! You have lost: Goblet Of Fire, Enchanted Ring")
#         inventory.remove("Goblet Of Fire")
#         inventory.remove("Enchanted Ring")
#         print(inventory )
#         a_fork_in_the_path()

# # This section allows encourages the player to make a defined choice on their journey.
# def hidden_village(): 
#     print("You enter into a dense wooded area that has an opening leading to hidden camp in a wooden fort surrounded and protected by the children of hydra on the ramparts, skeletons armed with swords, shields and spears who are impervious to any form of attack - your confronted by the camp elder and his personal Praetorian guard.")
# def unmarked_cave (): 
#     print("You fall down some scree into the entrance to what seems to be a Unmarked Cave. There is a tree just outside the entrance with what seems to be a golden rams fleece draped over it. You go to take a further look only for someone to call to you ‘gis a job, gis a job’ astounded by what your hearing in such a remote place, you enter the cave only to be confronted by a lizard like banshee sorceress with tree eyes and snakes for hair. You are then met with “Who dares to desecrate the sanctity peace and of my Temple!“. What follows is a boulder falling behind you sealing your only exit.")
# def a_fork_in_the_path():
#     print("You leave the bonstrewn canyon and your presented with two paths one to the left and another to the right. ")
#     print("1 for left and 2 for right: [1/2]")
    
#     answer1 = input ("Enter 1 or 2: ")
    
#     if answer1 == ("1"):
#         hidden_village()
#         print("You can’t understand the sanskrit language he uses towards you, the only option you have is to defend or protect yourself with the items you have on your person, you choose: 1. The Enchanted Shield, 2. The Blade, 3. Enchanted Scroll.")
        
#         input == ("Choose 1, 2 or 3 to protect yourself: ")
#         answer2 = input ("Enter 1, 2 or 3: ") 
#         if answer2 == ("1"):
#                 print("The Enchanted Shield - You pull out the shield in attempt to defend yourself from perceived oncoming attacks - the enchantment on the shield means it has a highly reflective surface which the catches the rays from the sun reflecting them onto all in front of you which has a blinding effect.The children of hydra having no eyes aren’t affected and attack slicing you to ribbons, you die a death of 1000 cuts, Game Over!")
#                 game_over()
            
#         elif answer2 == ("2"):
#                 print("The Enchanted Blade - You select the blade to defend yourself but upon unsheathing you see its made out of glass, still you attempt to attack one of the children of hydra who shatter the blade with all of the shards being directed into your body which spark and suddenly you become engulfed in flames taking your last napalm filled breath, Game Over!")
#                 game_over()
#         elif answer2 == ("3"):
#                 print("The Enchanted Scroll - You grab the enchanted scroll from your satchel and all most with immediacy the Camp Elder and Praetorian Guard, along with the children of hydra and all the camp dwellers fall to their knees, heads bowed in servitude and, in chorus, being to chant one singular word toward you Deva, deva, deva unbeknownst to you by being in possession of this Enchanted Scroll you have just been proclaimed “heavenly, divine and everything of excellence by the Hidden Camp Dwellers proclaiming you as their one and only God incarnate - You’ve Completed your quest!")
#         else:
#             ()
#     elif answer1 == ("2"):
#         unmarked_cave()
#         print("You search your person for something to protect or defend yourself with, you have 1. The Amulet of Reflection, 2. The Potion of Healing, 3. A Crystal Shard and you choose: ")
#         input == ("Choose 1, 2 or 3 to protect yourself: ")
#         answer3 = input ("Enter 1, 2 or 3: ") 
#         if answer3 == ("1"):
#             print("The Amulet of Reflection - The sorceress tries to entrap and entice you with her bewitching glare, but you put the amulet of reflection before you, reflecting her enchantment back at her, there’s a bloodcurdling scream reaching a tone only a banshee is capable of achieving, shattering the boulder that blocks your exit, just before the lizard like sorceress turns into a solid gold statute with ruby eyes. You manage to get this statue and the golden fleece to some abandoned docks on the far side of the island where you buy a merchant boat with your new found wealth and escape the island, your quest being complete!")
#         elif answer3 == ("2"):
#             print("The Potion of Healing - You select the potion of healing and drink it almost immediately bolstering your health, ready for a fight, after a weary time traveling. The sorceress lets out an almighty whale, temporarily incapacitating you and throwing you into the cave wall. This doesn’t totally deplete your energy so you stand up again, only to be hit with the sound wave of a second shriek, this one cuts like a blade deep into your flesh severing you in half vertically, Game over!")
#             game_over()
#         elif answer3 == ("3"):
#             print("The Crystal Shard - You grab the crystal shard in hand, forming it as a weapon in your defense. The sorceress lets out a deafening shriek which somehow actives a pox held within the crystal shard which starts to melt and then crystallize your hands, then moving up to your arms and torso, down your legs, up your neck then into your open mouth encasing you in a crystallized chasm for all of eternity somewhere between death and life, Game Over!")
#             game_over()
#         else:
#             ()
#     else:   
#         a_fork_in_the_path()
# island_introduction()

inventory = []
sc_inventory = ["Amulet Of Relflection", "Potion Of Healing", "Crystal Shard", "Woodcutter's Axe", "Scythe"]
gt_inventory = ["Enchanted Blade", "Enchatnted Shield", "Enchanted Scroll", "Goblet Of Fire", "Enchanted Ring"]
# These globals will enable inventory list's to be added to the main inventory global
sc_explored = False
gt_explored = False
# These globals will identify which area the player has explored and what items have been recoved throughout the game
def island_introduction():
    print("You are a part of an envoy of ships at sail, of which is decimated by a gigantic 8 headed hydra of which emerges out of the ocean. You are thrown into the sea when it smashes through the ship of which you are on, you manage to get onto a piece of driftwood but loose consciousness shortly thereafter…")
    print("When you awaken, you find yourself in a large campsite surrounded by tall stockade fences. This campsite you notice, is filled with soldiers (mostly humans and minotaur’s). A Feline woman approaches you and identifies herself as Kyolie, “You’re fortunate, most that washed up were already dead, now that you seem rested, I expect that you will be leaving our camp today.” After she explains that this is a campsite for a rebellion against a tyrant (Although your main concern is escaping the island). You leave the camp and walk along a winding path until you reach a crossroad, one path takes you to a Forest, and the other leads into the Mountains.")
    print("Would you like to go through the forest or the mountains?")
    print("Select 1 for the forest or 2 for the mountains.")
    answer1 = input(">> ")
    if answer1 == ("1"):
        forest()
    elif answer1 == ("2"):
        mountains()
    else:
        island_introduction()
# This should print the intro and provide first IfElse Staement Selection (Player Input)
def forest():
    print("You enter the forest, you notice a largely overgrown path through the forest, you also notice a ritual being performed through some trees away from the overgrown path.")
    print("Select 1 to go down the overgrown path, or 2 to interrupt the ritual.")
    answer2 = input(">> ")
    if answer2 == ("1"):
        secluded_cabin()
    elif answer2 == ("2"):
        ritual()
    else:
        forest()
# This is the same to intro code.

def mountains():
    print("You come to the mountains, you notice a small overhang a small stream and a winding path up to what you notice to be a Grand temple in the mountains. You also notice a reptilian searching through around half a dozen corpses.")
    print("Select 1 to continue along the path to the Grand Temple, or 2 to attempt to loot one of the corpses.")
    answer3 = input(">> ")
    if answer3 == ("1"):
        grand_temple()
    elif answer3 == ("2"):
        reptillian_encounter()
    else:
        mountains()
# This is the same to intro code.

def secluded_cabin():
    global sc_explored
    print("You enter the Secluded cabin, and immediately notice that the house is mostly ransacked (It doesn’t look like anyone has lived here in a while. You search the cabin thoroughly and find a small list of items : Amulet of Reflection, Potion of Healing, Crystal Shard, Woodcutters axe, and a Scythe. You spend the night in one of the more secure room of the cabin. The next day you move on to the Bonestrewn Canyon.")
    inventory.extend(sc_inventory)
    inventory.sort()
    sc_explored = True
# This should update the inventory with the sc inventory and set the True/False Global function to True

    print("Your Inventory now contains:", inventory)
    Encounter()
def ritual():
    print("You attempt to interrupt the ritual being performed, and are quickly murdered by the coven.")
    print("Game Over")
    game_over()
def game_over():
    print("You died!")
    print("Press 0 to restart the game.")
    answer_r = input(">> ")
    if answer_r == ("0"):
        island_introduction()
    else:
        game_over()
def grand_temple():
    global gt_explored
    print("You enter the Grand Temple, of which you notice to be remarkable empty, aside from one High priestess, she immediately notices and identifies herself as Kynessa, “I have seen your coming to this temple, and believe these items will be of use to you” she hands you a pack of items of which contains :  A Enchanted blade, An Enchanted Shield, An Enchanted Scroll, A Goblet of fire, and an Enchanted Ring. After spending the night at the temple you move Bonestrewn Canyon.")
    inventory.extend(gt_inventory)
    inventory.sort()
    gt_explored = True
    print("Your inventory now contains:", inventory)
    Encounter()
def reptillian_encounter():
    print("You attempt to loot one of the corpses, the reptillian quickly approaches and murders you before you have any chance to respond.")
    print("Game Over")
    game_over()
# End of section 1
# Beginning of section 2
def Encounter():
    print("You enter the Bonestrewn Canyon where there are the remains of skeletons from battles from all time. You are aware that you are not alone as people rise from bedding of all descriptions. The bones are used to make coverings with tarpaulins; horse carcasses used to cover two or three people at a time. Human leg bones and arms to burn for fires. Skulls stacked as walls to shelter behind.You encounter 3 people who may be able to help you escape the canyon")
    print("You need to find your way out of the canyon. The canyon has high walls that cannot be climbed, you need to converse with those who have been left here in the canyon.Not all speak your language so you must be careful to make the correct contacts to escape the Bonestrewn Canyon")
    contact()
def contact():
    print("Select 1, select 2, or select 3 ")
    answer1 = input(">> ")
    if answer1 == ("1"):
        ignorant()
    elif answer1 == ("2"):
        friendly()
    elif answer1 == ("3"):
        thief()
    else:
        contact()
def ignorant():
    print("Ignores You!")
    contact()
def friendly():
    print("Hello, Can I help you?")
    answer2 =  input("1 for Yes! or 2 for No! >> ")
    if answer2 == ("1"):
        print("If you are a good reader; you can find your way to a Hidden Camp; However, On reflection, I can advise you that there could be an Unmarked Cave nearby!")
        next_day()
    elif answer2 == ("2"):
        print("No!...Ok then you will be sorry!")
        game_over()
    else:
        contact()
def thief():
    print("Is sleeping")
    contact()
def next_day():
    global sc_explored
    global gt_explored
    if sc_explored == True and gt_explored == False:
        print("You wake up the next day alone after resting in the canyon. Only when you wake do you realise you have been robbed! You have lost: Wood cutters axe and Scythe ")
        inventory.remove("Woodcutter's Axe")
        inventory.remove("Scythe")
        print(inventory)
        a_fork_in_the_path()
    elif gt_explored == True and sc_explored == False:
        print("You wake up the next day alone after resting in the canyon. Only when you wake do you realise you have been robbed! You have lost: Goblet Of Fire, Enchanted Ring")
        inventory.remove("Goblet Of Fire")
        inventory.remove("Enchanted Ring")
        print(inventory )
        a_fork_in_the_path()
# End of section 2
# Beginning of section 3
# This section allows encourages the player to make a defined choice on their journey.
def hidden_village(): 
    print("You enter into a dense wooded area that has an opening leading to hidden camp in a wooden fort surrounded and protected by the children of hydra on the ramparts, skeletons armed with swords, shields and spears who are impervious to any form of attack - your confronted by the camp elder and his personal Praetorian guard.")
def unmarked_cave (): 
    print("You fall down some scree into the entrance to what seems to be a Unmarked Cave. There is a tree just outside the entrance with what seems to be a golden rams fleece draped over it. You go to take a further look only for someone to call to you ‘gis a job, gis a job’ astounded by what your hearing in such a remote place, you enter the cave only to be confronted by a lizard like banshee sorceress with tree eyes and snakes for hair. You are then met with “Who dares to desecrate the sanctity peace and of my Temple!“. What follows is a boulder falling behind you sealing your only exit.")
def a_fork_in_the_path():
    global sc_explored
    global gt_explored
    print("You leave the bonstrewn canyon and your presented with two paths one to the left and another to the right. ")
    print("1 for left and 2 for right: [1/2]")
    
    answer1 = input ("Enter 1 or 2: ")
    
    if answer1 == ("1") and gt_explored == True:
        hidden_village()
        print("You can’t understand the sanskrit language he uses towards you, the only option you have is to defend or protect yourself with the items you have on your person, you choose: 1. The Enchanted Shield, 2. The Blade, 3. Enchanted Scroll.")
        
        input == ("Choose 1, 2 or 3 to protect yourself: ")
        answer2 = input ("Enter 1, 2 or 3: ") 
        if answer2 == ("1"):
                print("The Enchanted Shield - You pull out the shield in attempt to defend yourself from perceived oncoming attacks - the enchantment on the shield means it has a highly reflective surface which the catches the rays from the sun reflecting them onto all in front of you which has a blinding effect.The children of hydra having no eyes aren’t affected and attack slicing you to ribbons, you die a death of 1000 cuts, Game Over!")
                game_over()
            
        elif answer2 == ("2"):
                print("The Enchanted Blade - You select the blade to defend yourself but upon unsheathing you see its made out of glass, still you attempt to attack one of the children of hydra who shatter the blade with all of the shards being directed into your body which spark and suddenly you become engulfed in flames taking your last napalm filled breath, Game Over!")
                game_over()
        elif answer2 == ("3"):
                print("The Enchanted Scroll - You grab the enchanted scroll from your satchel and all most with immediacy the Camp Elder and Praetorian Guard, along with the children of hydra and all the camp dwellers fall to their knees, heads bowed in servitude and, in chorus, being to chant one singular word toward you Deva, deva, deva unbeknownst to you by being in possession of this Enchanted Scroll you have just been proclaimed “heavenly, divine and everything of excellence by the Hidden Camp Dwellers proclaiming you as their one and only God incarnate - You’ve Completed your quest!")
        else:
            a_fork_in_the_path()
    elif answer1 == ("2") and sc_explored == True:
        unmarked_cave()
        print("You search your person for something to protect or defend yourself with, you have 1. The Amulet of Reflection, 2. The Potion of Healing, 3. A Crystal Shard and you choose: ")
        input == ("Choose 1, 2 or 3 to protect yourself: ")
        answer3 = input ("Enter 1, 2 or 3: ") 
        if answer3 == ("1"):
            print("The Amulet of Reflection - The sorceress tries to entrap and entice you with her bewitching glare, but you put the amulet of reflection before you, reflecting her enchantment back at her, there’s a bloodcurdling scream reaching a tone only a banshee is capable of achieving, shattering the boulder that blocks your exit, just before the lizard like sorceress turns into a solid gold statute with ruby eyes. You manage to get this statue and the golden fleece to some abandoned docks on the far side of the island where you buy a merchant boat with your new found wealth and escape the island, your quest being complete!")
        elif answer3 == ("2"):
            print("The Potion of Healing - You select the potion of healing and drink it almost immediately bolstering your health, ready for a fight, after a weary time traveling. The sorceress lets out an almighty whale, temporarily incapacitating you and throwing you into the cave wall. This doesn’t totally deplete your energy so you stand up again, only to be hit with the sound wave of a second shriek, this one cuts like a blade deep into your flesh severing you in half vertically, Game over!")
            game_over()
        elif answer3 == ("3"):
            print("The Crystal Shard - You grab the crystal shard in hand, forming it as a weapon in your defense. The sorceress lets out a deafening shriek which somehow actives a pox held within the crystal shard which starts to melt and then crystallize your hands, then moving up to your arms and torso, down your legs, up your neck then into your open mouth encasing you in a crystallized chasm for all of eternity somewhere between death and life, Game Over!")
            game_over()
        else:
            a_fork_in_the_path()
    else:
        print("None of the items you have recovered are of any use in the next area and as a result:")   
        game_over()
island_introduction()