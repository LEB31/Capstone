# Characters made by svstudioart
# Bookstore by Martin Adams
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jay")
define l = Character("Lisa")
define m = Character("Miriam")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene place

    play sound 'audio/Next to You.mp3'

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show 1 at left

    # These display lines of dialogue.

    "The story starts with a group of friends"

    j "You ready to go?"

    show 2 at truecenter

    l "Yeah but we should wait for Miriam"

    "10 minutes later..."

    show 9 at right

    m "Hey guys! Sorry about the wait."

    # This ends the game.

    return

