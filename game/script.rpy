# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Protagonist")
define raina = Character("Raina")
define dayonetta = Character("Dayonetta")
define justina = Character("Justina")

# Start the game
label start:
    # Scene setup
    scene bg bar with fade

    # Internal monologue and scene setup
    protagonist "|Internal Monologue| A dimly lit bar. I stand nervously by the counter, nursing a soda."
    protagonist "|Internal Monologue| Why did I come here? No one comes to bars for the soda. Just... act natural. Stand casually. Yeah, because this is what casual feels like."
    protagonist "|Internal Monologue| I glance around nervously. A soft-spoken woman in athletic wear approaches the bar with a gentle smile."

    raina "Hi there! My name's Raina. You seem... tense. Everything okay?"

    menu:
        "I'm ____ nice to meet you":
            protagonist "I'm _____. Nice to meet you!"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "I'm fine. But you're even finer!":
            protagonist "I'm fine. But you're even finer!"
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "I was better before you showed up (stuttering)":
            protagonist "I-I w-was b-better..."
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

    protagonist "|Internal Monologue| Is she… meditating? In a bar? Should I join her? I’ll look weird if I don’t. But also weird if I do. Oh no, what do I do with my hands?"

    raina "Now that was a great workout! You know... maybe you should come down to my studio sometime and I could give you a private lesson?"

    menu:
        "Studio? No thanks, I only hang out in basements.":
            protagonist "Studio? No thanks, I only hang out in basements."
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "That sounds like fun, why don’t I order us an Uber and we get out of here?":
            protagonist "That sounds like fun, why don’t I order us an Uber and we get out of here?"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "CHAT LETS GOOO WE’RE GOING HOME WITH HER (stuttering)":
            protagonist "Uhh… I mean… CHAT LET'S GOOOO!"
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

    protagonist "Okay, one down, but there’s plenty of other opportunities around here. I mean, she was practically a yoga class in human form anyways, so maybe I’ll have better luck over there."

    # Transition to the next encounter
    scene bg booth with fade
    protagonist "I spot a woman with glasses and dark short hair sitting alone at a booth. She seems approachable but mysterious."

    dayonetta "Hello darling, terribly sorry to see you strike out over there. If you need to learn to talk to a lady… why not ask me!"

    menu:
        "What’s that? Sorry, no. I talk to plenty of women, hotter than you.":
            protagonist "What’s that? Sorry, no. I talk to plenty of women, hotter than you."
            dayonetta "Demon got your tongue? It's alright darling. Maybe next time you'll have better luck."

        "Hubba hubba. Are you a witch? Cuz there’s a spell on me for sure.":
            protagonist "Hubba hubba. Are you a witch? Cuz there’s a spell on me for sure."
            dayonetta "Demon got your tongue? It's alright darling. Maybe next time you'll have better luck."

        "Oh yea… that was quite embarrassing… you seem very nice, I would love some advice if you don’t mind.":
            protagonist "Oh yea… that was quite embarrassing… you seem very nice, I would love some advice if you don’t mind."
            dayonetta "Shall we start you off with a cosmopolitan? Maybe that will give you the confidence to slay some angels, or at least get a word out."

    protagonist "She winks and walks away. That could have gone better… or worse."

    # Transition to the final encounter
    scene bg booth_motorbike with fade
    protagonist "I notice another woman sitting nearby with a motorcycle helmet on the table beside her. She has an intense aura."

    justina "Ugh, what do you want?"

    menu:
        "Just your number baby, and maybe a kiss while you’re at it.":
            protagonist "Just your number baby, and maybe a kiss while you’re at it."
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

        "Sorry to bother you, I can get out of your way now.":
            protagonist "Sorry to bother you, I can get out of your way now."
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

        "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?":
            protagonist "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?"
            justina "That’s it. You’ve bothered enough girls tonight. You’re out of here!"

    # End the game
    scene bg black
    protagonist "I’ve been thrown out of the bar. Maybe I need to rethink my strategy."

    return