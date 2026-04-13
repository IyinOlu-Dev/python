# add the asci art in between the three single quotation marks
#DO TRY TO MAKE THIS AS COMPLICATED AS POSSIBLE
#UPDATE THE GAME SO IT ACTUALLY ACCEPTS WORDS AND NOT JUST YES OR NO
#print(''' 
# ''')

print("Welcome to your adventure")
print('This game is a series of yes or no question\n Select "Y" or "y" for yes and "N" or "n" for no')
game_over = False 
while game_over == False:
    start = input("Are you ready for you adventure: ").lower()
    if start != "y":
        game_over = True
        print("How sad. I really wished you had some advneture.\n Maybe next time")
    else:
        map = input("You have found a map leading to a treasure in the forest of the lost\n Do you satisfy your curiosity and pick it up?:  ").lower()
        if map != "y":    
            game_over = True
            print("How sad. I really wished you had some adventure.\nMaybe next time")
        else:
            print("I see you are not a coward, Well go on. Entertain me")
            print("You realize you have no idea how to navigate the forest of the lost, but you have a map.")
            move = input("Do you go enter the forest anyway?: ").lower()
            if move != 'n':
                print("HAHHAHAHA.....\nYou got lost\nIt's called the forest of the lost for a reason stupid")
                game_over = True
            else:
                print("You asked the sorounding villagers for a guide and they provide you with matata\n You follow matata into the forest but lost him along the way")
                reward = input("You feel close to the treasure\n Do you keeo going for the treasure?: ").lower()
                if reward != "n":
                    print("HAHHAHAHA.....\n you got lost\n It's called the forest of the lost for a reason stupid")
                    game_over = True
                else: 
                    print("Congratulations, you now know you care about an unknown treasure than a human life")
