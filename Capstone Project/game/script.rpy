# Characters made by svstudioart
# Bookstore by Martin Adams
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miriam")

define y = Character("You")


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

    "You and your friend Miriam are trying to decide where to go today."

    show happy 

    y "Why don't we go to the movies?"

    show angry 

    m "Are you insane?! There is way to many people!"

    # This ends the game.

    return

