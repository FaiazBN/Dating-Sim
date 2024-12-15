# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Self-Talk")
define story = Character("")
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
    # protagonist "A dimly lit bar. I stand nervously by the counter, nursing a soda."
    protagonist "Why did I come here? No one comes to bars for the soda. Just... act natural. Stand casually. "
    protagonist "Yeah, because this is what casual feels like."


    story "(He glances around. A soft-spoken woman in athletic wear approaches the bar with a gentle smile.)"
    show raina norm at half_size,midright
       
    protagonist "Okay, I can do this. Just be casual. Just be normal. And maybe don’t spill your drink this time."

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



    # Transition to the next encounter
    scene bg booth with fade:
        zoom 4
        blur 15

    story "(She leaves, and the protagonist exhales sharply.)"
    protagonist "Okay, one down, but there’s plenty of other opportunities around here. I mean, she was practically a yoga class in human form anyways, so maybe I’ll have better luck over there?"
    
    # protagonist "I spot a woman with glasses and dark short hair sitting alone at a booth. She seems approachable but mysterious."
    story "A woman with glasses and dark short hair sits alone at a booth. She is approachable but mysterious."
    show dayonetta norm at half_size, midright
    dayonetta "Hello darling, terribly sorry to see you strike out over there. If you need to learn to talk to a lady… why not ask me!"

    $ dayonetta_option1 = tracery("#convo_with_dayonetta#")
    $ dayonetta_option2 = tracery("#convo_with_dayonetta#")
    $ dayonetta_option3 = tracery("#convo_with_dayonetta#")
    menu:
        "[dayonetta_option1]":
            e "#origin#::option1"
            dayonetta "Demon got your tongue? It’s alright darling, shall we start you off with a cosmopolitan? Maybe that will give the confidence to slay some angels, or at least get a word out."

        "[dayonetta_option2]":
            e "#origin#::option2"
            dayonetta " Demon got your tongue? It’s alright darling, shall we start you off with a cosmopolitan? Maybe that will give the confidence to slay some angels, or at least get a word out."

        "[dayonetta_option3]":
            e "#origin#::option3"
            dayonetta " Demon got your tongue? It’s alright darling, shall we start you off with a cosmopolitan? Maybe that will give the confidence to slay some angels, or at least get a word out."

    story "She winks and walks away. That could have gone better… or worse."

    # Transition to the final encounter
    scene bg booth_motorbike with fade:
        zoom 5
        blur 15

    protagonist "Wow. I really thought I’d be better at this. Well, third time’s the charm I suppose. I think that  woman over there came in on a motorbike, maybe she’s cool enough for my style."
    story "(You approach the woman in another booth nearby, she is blonde with her orange and green motorcycle helmet on the table beside her)"

    show justina norm at half_size, midright
    justina "Ugh, what do you want?"


    $ justina_option1 = tracery("#convo_with_justina#")
    $ justina_option2 = tracery("#convo_with_justina#")

    menu:
        "[justina_option1]":
            e "#origin#::option1"
            justina "Great, another creep. Look buddy I’m just trying to enjoy the one night I have to relax before my next mission, so if you were looking to waste my time I suggest you get moving."

        "[justina_option2]":
            e "#origin#::option2"
            justina "Great, another creep. Look buddy I’m just trying to enjoy the one night I have to relax before my next mission, so if you were looking to waste my time I suggest you get moving."

        
        "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?":
            e "#origin#::option3"
            # protagonist "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?"
            justina "Great, another creep. Look buddy I’m just trying to enjoy the one night I have to relax before my next mission, so if you were looking to waste my time I suggest you get moving."


    menu:
        "Playing hard to get I see? You know, deadly is just my type.":
            justina "Alright, I’ll admit, that was a pretty honest attempt. Nervousness and all, at least you’re not like the usual creeps I run into."
            protagonist "Really? I mean… thank you! I promise, I’m not trying to bother you—I just thought you seemed… interesting."
            justina "Interesting, huh? Well, I guess I could use a decent conversation tonight. Alright, I’ll bite. But you’d better not make me regret this."
            protagonist "You won’t! I swear!"
            justina "Alright, then. Pull up a seat. Just don’t try anything fnny—deadly isn’t just my type, it’s also what I am."
            protagonist "Noted! Drinks on me?"
            justina "You’ve got five minutes to impress me. Let’s see if you’re worth more than just a drink"


            # alternate ending

            stop music
            # End the game
            scene bg outsidebar:
                blur 100

            story "The rest of the night pased by in a blur. Only if the censorship laws were relaxed would we be able to tell you what happened. The protagonist can't remember what happened, but he does remember that he ..."
            story "..."
            story "(He tries to show his face, and the game ends.)"
            return

        "No, please! This is a misunderstanding and I’m just so nervous I can’t even get a word out. I’m sorry to disturb you during your night out, I was just looking to make a friend.":
            justina "Well, if stammering was a competition, you'd have gold by now. But hey, points for effort. Good luck next time—now scoot before my patience runs out."

        "What’s the use? Erm…uhhh…durrrr.":
            justina "Well, if stammering was a competition, you'd have gold by now. But hey, points for effort. Good luck next time—now scoot before my patience runs out."

    

    stop music
    play sound "thwack-06.wav"

    # End the game
    scene bg outsidebar:
        blur 10
    play music "crickets.mp3"
    protagonist "I’ve been thrown out of the bar. Maybe I need to rethink my strategy."
    
    return