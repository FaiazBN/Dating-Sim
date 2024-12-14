# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Self-Talk")
define raina = Character("Raina")
define dayonetta = Character("Dayonetta")
define justina = Character("Justina")

#sprites are too big
transform half_size: 
    zoom 0.5 #adjust as required

transform midright:
    yalign 1.0
    xcenter 0.5

init -1 python:
    from renpy_tracery import TraceryCharacter as TC
    from generator import menu_grammar
    from generator import i_cant_speak_grammar
    from renpy_tracery import TraceryGen
    # Define Tracery grammar for rambling.
    
    tracery = TraceryGen(menu_grammar)
    

# Define Tracery characters
define e = TC("You", grammar=i_cant_speak_grammar)

# Start the game
label start:
    # Scene setup
    scene bg bar with fade:
        zoom 2.5

        blur 15
    play music "A-Cloudy-Morning-2012.mp3"


    # Internal monologue and scene setup
    protagonist "A dimly lit bar. I stand nervously by the counter, nursing a soda."
    protagonist "Why did I come here? No one comes to bars for the soda. Just... act natural. Stand casually. Yeah, because this is what casual feels like."
    show raina norm at half_size,midright
       
    protagonist "I glance around nervously. A soft-spoken woman in athletic wear approaches the bar with a gentle smile."

    raina "Hi there! My name's Raina. You seem... tense. Everything okay?"

    $ option1 = tracery("#conversation_starter#")
    $ option2 = tracery("#conversation_starter#")
    $ option3 = tracery("#conversation_starter#")
    menu:
        "[option1]":
            e "#origin#::option1"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "[option2]":
            e "#origin#::option2"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "[option3]":
            e "#origin#::option3"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

    protagonist "Is she… meditating? In a bar? Should I join her? I’ll look weird if I don’t. But also weird if I do. Oh no, what do I do with my hands?"

    raina "Now that was a great workout! You know... maybe you should come down to my studio sometime and I could give you a private lesson?"


    $ rain_option1 = tracery("#convo_with_raina#")
    $ rain_option2 = tracery("#convo_with_raina#")
    $ rain_option3 = tracery("#convo_with_raina#")
    menu:
        "[rain_option1]":
            e "#origin#::option1"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "[rain_option2]":
            e "#origin#::option2"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "[rain_option3]":
            e "#origin#::option3"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

    protagonist "Okay, one down, but there’s plenty of other opportunities around here. I mean, she was practically a yoga class in human form anyways, so maybe I’ll have better luck over there."

    # Transition to the next encounter
    scene bg booth with fade:
        zoom 4
        blur 15

    
    protagonist "I spot a woman with glasses and dark short hair sitting alone at a booth. She seems approachable but mysterious."
    show dayonetta norm at half_size, midright
    dayonetta "Hello darling, terribly sorry to see you strike out over there. If you need to learn to talk to a lady… why not ask me!"

    $ dayonetta_option1 = tracery("#convo_with_dayonetta#")
    $ dayonetta_option2 = tracery("#convo_with_dayonetta#")
    $ dayonetta_option3 = tracery("#convo_with_dayonetta#")
    menu:
        "[dayonetta_option1]":
            e "#origin#::option1"
            dayonetta "Demon got your tongue? It's alright darling. Maybe next time you'll have better luck."

        "[dayonetta_option2]":
            e "#origin#::option2"
            dayonetta "Demon got your tongue? It's alright darling. Maybe next time you'll have better luck."

        "[dayonetta_option3]":
            e "#origin#::option3"
            dayonetta "Shall we start you off with a cosmopolitan? Maybe that will give you the confidence to slay some angels, or at least get a word out."

    protagonist "She winks and walks away. That could have gone better… or worse."

    # Transition to the final encounter
    scene bg booth_motorbike with fade:
        zoom 5
        blur 15

    protagonist "I notice another woman sitting nearby with a motorcycle helmet on the table beside her. She has an intense aura."
    show justina norm at half_size, midright
    justina "Ugh, what do you want?"


    $ justina_option1 = tracery("#convo_with_justina#")
    $ justina_option2 = tracery("#convo_with_justina#")

    menu:
        "[justina_option1]":
            e "#origin#::option1"
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

        "[justina_option2]":
            e "#origin#::option2"
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

        
        "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?":
            e "#origin#::option3"
            # protagonist "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?"
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"
    stop music
    play sound "thwack-06.wav"

    # End the game
    scene bg outsidebar:
        blur 10
    play music "crickets.mp3"
    protagonist "I’ve been thrown out of the bar. Maybe I need to rethink my strategy."
    
    return