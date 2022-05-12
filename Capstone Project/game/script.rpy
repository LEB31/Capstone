# Lily Bain  Verion 1.2  Capstone Project
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

    show idle1

    menu:

        "We should go..."

        "To the movies":

            jump movies

        "To the park":

            jump park

label movies:

    scene movietheater

    show sad1

    m "I don't like it here..."

    m "Let's go the the park instead.."
    jump park



label park:

    scene park

    show happy1

    m "This was a good choice!"
    hide happy1 
    show happy2
    m "The flowers are beautiful!"
    
    menu: 
        "How do I Respond?"
        "Quite beautiful":
            jump beautiful
        "I've seen better":
            jump seen


label beautiful:
    scene park

    show happy3 
    m "They're perfect!"

label seen:
    scene park

    hide happy2 
    show angry2

    m "You're joking"

# This ends the game.

return
