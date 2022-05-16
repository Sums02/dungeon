playermap = [["|","-","-","-","-","|"],
             ["s",".",".",".",".","|"],
             ["|",".",".",".",".","|"],
             ["|",".",".",".",".","|"],
             ["|",".",".",".",".","e"],
             ["|","-","-","-","-","|"]]

level_1 = [["|","-","-","-","-","|"],
        ["s",".","-","-",".","|"],
        ["|",".","d1",".","t","|"],
        ["|",".",".",".",".","|"],
        ["|","t","|","d2",".","e"],
        ["|","-","-","-","-","|"]]

playermap2 = [["|","-","-","-","-","|"],
             ["s",".",".",".",".","|"],
             ["|",".",".",".",".","|"],
             ["|",".",".",".",".","|"],
             ["|",".",".",".",".","e"],
             ["|","-","-","-","-","|"]]


level_2 = [["|","-","-","-","-","|"],
        ["s",".",".","t","|","|"],
        ["|","d1","|",".",".","|"],
        ["|",".","|","d2",".","|"],
        ["|",".","t",".",".","e"],
        ["|","-","-","-","-","|"]]

def displayMap_1(playermap):
    for x in range(0,6):
        print(playermap[x])

def displayMap_2(playermap2):
    for x in range(0,6):
        print(playermap2[x])
#PSUDOCODE:
#IF player successfully enters details
#DISPLAY player map

mapchoice = level_1
position = mapchoice[0][0]

usernames = []
passwords = []

def login():
    has_login = input("Do you have a log in? (Y/N) ")
    has_login = has_login.lower()
    count = 0
    if has_login == 'n':
        registration()
    elif has_login == 'y':
        login = False
        while login == False:
            username_2 = input("Please enter your username: ")
            password_2 = input("Please enter your password: ")

            if username_2 in usernames or password_2 in passwords:
                login = True
                print("You have successfully entered the dungeon")
                level1(displayMap_1,level_1,position)

            else:
                print("Username or password is wrong. Please try again")
                count -=1
                number_of_tries = 3 + count
                print("You have " + str(number_of_tries) + " tries left")
                login = False
                if number_of_tries == 0 :
                    login = True
                    print("You have no more attempts left, please create a new username and password")
                    registration()

def registration():
    username_1 = input("Please create a suitable username in lowercase: ")
    password_1 = input("Please create a suitable password in lowercase: ")
    usernames.append(username_1)
    passwords.append(password_1)
    login()




    #in parameters should include username and password
    #PSUDOCODE:
    #login = TRUE
    #count = 0
    #INPUT user inputs whether they have a Login
    #IF input = No
    #INPUT user creates username and password
    #ELSE
    #INPUT user inputs their username and password
    #IF username OR password is NOT FOUND THEN
    #login = FALSE
    #OUTPUT 'Invalid username or password please try again'
    #INPUt user inputs username and password
    #REPEAT UNTIL count = 3 OR login = TRUE




def menu():
    menu = input("Would you like to enter the dungeon? (Y/N): ")
    menu = menu.capitalize()
    if menu == 'Y':
        login()

    else:
        print("Sad to see you go :(")
        quit()


#PSUDOCODE:
#INPUT user inputs whether they want to enter the dungeons
#IF answer = yes THEN
#DISPLAY Login details
#ELSE
#TERMINATE



def level1(displayMap_1,level_1,position):
    displayMap_1(playermap)
    mapchoice = level_1
    position = mapchoice[0][0]
    x=0
    y=1
    print(mapchoice[y][x])
    position = 0

    while position != "e":
        movement = input("Please enter the direction you would like to move: L(Left),R(Right),U(Up),D(Down) ")
        movement = movement.upper()
        prevX = x
        prevY = y
            #these are used to move player back to original location if they hit a wall


        if movement == "U":
            y = y-1

        if movement == "D":
            y = y+1

        if movement == "R":
            x = x+1

        if movement == "L":
            x = x-1

        if movement == "MAP":
            displayMap_1(playermap)


        position = mapchoice[y][x]
        playermap[y][x] = "x"

        if position == "e":
            print("You've reach a door, as you step in all you see is darkness... you've entered the second dungeon")
            level_2(displayMap_2,level_2,position)

#PSUDOCODE:
#INPUT user enters name
#INITALISE health = 100
#health<=100
#INPUT user enters L(left) or R(right) or D(down) or U(up)
#IF wall at given pixel THEN
#OUTPUT 'Looks like there's a wall, try a different direction'
#ELSE
#INPUT user enters direction of which pixel they want to move to


def level_2(displayMap_2,level_2,position):
        displayMap_2(playermap2)
        mapchoice = level_2
"""        x=0
        y=1
        print(mapchoice[y][x])
        position = 0"""

"""    while position != "e":
            movement = input("Please enter the direction you would like to move: L(Left),R(Right),U(Up),D(Down) ")
            movement = movement.upper()
            prevX = x
            prevY = y
                #these are used to move player back to original location if they hit a wall


            if movement == "U":
                y = y-1

            if movement == "D":
                y = y+1

            if movement == "R":
                x = x+1

            if movement == "L":
                x = x-1

            if movement == "MAP":
                displayMap_2(playermap2)


            position = mapchoice2[y][x]
            playermap2[y][x] = "x"

            if position == "e":
                print("You've reached the exit and see a ray of sunshine... You've made it out!")"""



def dragon1():
    ''

#PSUDOCODE:
#IF player location within 2 spaces of DRAGON1 THEN
#DISPLAY 'There is a dragon close by'
#START timer
#INPUT ask user to enter location of DRAGON1
#ie [2,3]
# IF input is equal to location of DRAGON1 THEN
# DISPLAY 'You've defeated the dragon!'
# health += 15
# INPUT user enters the direction of which pixel they want to move to
# ELSE
# DISPLAY 'Wrong location, try again!'
# health -= 30
# INPUT ask user to enter location of DRAGON1
# REPEAT UNTIL DRAGON1 is FOUND or timer = 0
#  IF timer = 0
#  DISPLAY 'You were defeated by the dragon'
#  RUN gameover


def dragon2():
    ''

#PSUDOCODE:
#IF player location within 2 spaces of DRAGON2 THEN
#DISPLAY 'There is a dragon close by'
#START timer
#INPUT ask user to enter location of DRAGON2
# IF input is equal to location of DRAGON2 THEN
# DISPLAY 'You've defeated the dragon!'
# health += 10
# INPUT user enters the direction of which pixel they want to move to
# ELSE
# DISPLAY 'Wrong location, try again!'
# health -= 20
# INPUT ask user to enter location of DRAGON2
# REPEAT UNTIL DRAGON2 is FOUND or timer = 0
#  IF timer = 0
#  DISPLAY 'You were defeated by the dragon'
#  RUN gameover



def treasure():
    ''

#PSUDOCODE:
#IF user location = treasure location THEN
#INCREASE health by 20
#ELSE
#ASK player to move



def gameover():
    ''

#INPUT ask user whether they would like to play again or quit
#IF answer = playagain THEN
#DISPLAY map1
#ELSE
#TERMINATE program

menu()
