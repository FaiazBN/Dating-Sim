# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Muscle Mommy 💪")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Mommy

    # These display lines of dialogue.

    e "Why did I come here? No one comes to bars for the soda. Just… act natural. Stand casually. Yeah, because this is what casual feels like. 
(He glances around. A soft-spoken woman in athletic wear approaches the bar with a gentle smile.)
"

    e "Okay, I can do this. Just be casual. Just be normal. And maybe don’t spill your drink this time.
(He glances around nervously. A soft-spoken woman in athletic wear approaches the bar with a gentle smile.)
"

    # This ends the game.

    return
