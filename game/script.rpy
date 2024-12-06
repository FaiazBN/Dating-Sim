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
    # Define Tracery grammar for rambling.
    tracery_grammar = {
        "origin":["#nearby##line#"],
        "line":["#mood.capitalize# could I just say, #compliment#, ohmygoshIsucksomuch #attempt#. No, wait, please! Don't look at me like that! *breathes heavily* #fail#"],
        "nearby":["Y'see, #fail#", "Errrr", "Salutations, greetings, wait no", "Geez, shit, wait I'm trying to say"],
        "compliment":["you're fine, deadly I hope, which is just my type", " your eyes are gentle and lips soft, and I am the happiest soul alive to witness that", "aww, shucks, well I just want to sit and spend the evening with you", "I'm kinda embarrassed...you seem very nice and I would love some advice, o-only if you don't mind", "are you a witch? Cause' you've put a spell on me", "hubba bubba"],
        "mood":["I'm fine, decent even, but", "Oh hellllooooo Angel? Demon? Too much?", "I'm well, um..uhhhh pretty gooood", "Errr, great but also omgI'msoembarrassedIcoulddie, should I order an Uber? Wait no,"],
        "fail":["before you showed up I was unhindered by these petty mortal feelings.", "I only hang out in basements.", "actually I 100% totally positively talk to plenty of women I personally find more attractive than you.", "uhhh...I think you've had a few too many martinis.", "erm...umm....durrr...fuck.", "this is a misunderstanding and I'msonervousIcan'tevengetawordout.", "well. Um. Can I be your friend?"],
        "attempt":["I'll buy your next round", "get me an old fashioned waiter!", "I saw you sitting alone from across the bar and there was just something about you that called me over", "I apologize for disturbing your night out but can I, possibly, maybe, errr getyournumber?"]
    }

# Define Tracery characters
define e = TC("You", grammar=tracery_grammar)

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

    menu:
        "I'm doing well. Nice to meet you.":
            # protagonist "I'm _____. Nice to meet you!"
            e "#origin#"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "I'm fine. But you're even finer!":
            # protagonist "I'm fine. But you're even finer!"
            e "#origin#"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "I was better before you showed up (stuttering)":
            # protagonist "I-I w-was b-better..."
            e "#origin#"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

    protagonist "Is she… meditating? In a bar? Should I join her? I’ll look weird if I don’t. But also weird if I do. Oh no, what do I do with my hands?"

    raina "Now that was a great workout! You know... maybe you should come down to my studio sometime and I could give you a private lesson?"

    menu:
        "Studio? No thanks, I only hang out in basements.":
            # protagonist "Studio? No thanks, I only hang out in basements."
            e "#origin#"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "That sounds like fun, why don’t I order us an Uber and we get out of here?":
            # protagonist "That sounds like fun, why don’t I order us an Uber and we get out of here?"
            e "#origin#"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "CHAT LETS GOOO WE’RE GOING HOME WITH HER (stuttering)":
            # protagonist "Uhh… I mean… CHAT LET'S GOOOO!"
            e "#origin#"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

    protagonist "Okay, one down, but there’s plenty of other opportunities around here. I mean, she was practically a yoga class in human form anyways, so maybe I’ll have better luck over there."

    # Transition to the next encounter
    scene bg booth with fade:
        zoom 4
        blur 15

    
    protagonist "I spot a woman with glasses and dark short hair sitting alone at a booth. She seems approachable but mysterious."
    show dayonetta norm at half_size, midright
    dayonetta "Hello darling, terribly sorry to see you strike out over there. If you need to learn to talk to a lady… why not ask me!"

    menu:
        "What’s that? Sorry, no. I talk to plenty of women, hotter than you.":
            # protagonist "What’s that? Sorry, no. I talk to plenty of women, hotter than you."
            e "#origin#"
            dayonetta "Demon got your tongue? It's alright darling. Maybe next time you'll have better luck."

        "Hubba hubba. Are you a witch? Cuz there’s a spell on me for sure.":
            # protagonist "Hubba hubba. Are you a witch? Cuz there’s a spell on me for sure."
            e "#origin#"
            dayonetta "Demon got your tongue? It's alright darling. Maybe next time you'll have better luck."

        "Oh yea… that was quite embarrassing… you seem very nice, I would love some advice if you don’t mind.":
            # protagonist "Oh yea… that was quite embarrassing… you seem very nice, I would love some advice if you don’t mind."
            e "#origin#"
            dayonetta "Shall we start you off with a cosmopolitan? Maybe that will give you the confidence to slay some angels, or at least get a word out."

    protagonist "She winks and walks away. That could have gone better… or worse."

    # Transition to the final encounter
    scene bg booth_motorbike with fade:
        zoom 5
        blur 15

    protagonist "I notice another woman sitting nearby with a motorcycle helmet on the table beside her. She has an intense aura."
    show justina norm at half_size, midright
    justina "Ugh, what do you want?"

    menu:
        "Just your number baby, and maybe a kiss while you’re at it.":
            e "#origin#"
            # protagonist "Just your number baby, and maybe a kiss while you’re at it."
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

        "Sorry to bother you, I can get out of your way now.":
            e "#origin#"
            # protagonist "Sorry to bother you, I can get out of your way now."
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

        "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?":
            e "#origin#"
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