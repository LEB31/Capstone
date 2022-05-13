# Lily Bain  Verion 1.3 Capstone Project
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(("Miriam"), color ="#f09199")

define y = Character(("You"), color ="#a48de8")


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

    m "Just like the ones mom had!"
    hide happy3
    show idle1
    y "If I didn't know better I would think they were the same ones"
    hide idle1 
    show happy2
    m "Exactly!"
    hide happy2 
    "You two hang out at the park for the afternoon"
    menu: 
        "Where to next?"
        "Cafe":
            jump cafe 
        "Library":
            jump library

label cafe:
    scene cafe 
    show idle1 
    "You two grab a quick cup of coffee and some sweets."
    "Another hour passes full of laughter."
    hide idle1 
    show sad1
    m "It's getting pretty late..."
    menu: 
        "Note: This decision is critical, please consider all options."
        "Offer to walk her home":
            jump walk
        "Say nothing":
            jump gone

label library:
    scene library
    show idle1 
    "You and Miriam browse and read books for an hour"
    hide idle1 
    show sad1
    m "It's getting pretty late..."
    menu: 
        "Note: This decision is critical, please consider all options."
        "Offer to walk her home":
            jump walk
        "Say nothing":
            jump gone

label walk: 
    scene walk 
    "You get her home safely, then go back to your apartment to rest for the night"
    "GAME OVER"
    return

label gone:
    scene gone
    hide sad1
    "Miriam left by herself that night..."
    "She was never seen again"
    "GAME OVER"
    return

label seen:
    scene park

    hide happy2 
    show angry2

    m "You're joking"
    hide angry2 
    show angry1
    m "These flowers are perfect!"
    scene blocked
    hide angry1
    "Miriam goes home frustrated. You are unable to contact her."
    "GAME OVER"
    return

# This ends the game.
