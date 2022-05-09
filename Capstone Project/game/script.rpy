# Characters made by svstudioart
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jay")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg

    play sound 'audio/the_field_of_dreams.mp3'

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show 1

    # These display lines of dialogue.

    "The story starts with a group of friends"

    j "I'm not doing the dishes tonight."

    j "That's your problem."

    # This ends the game.

    return
