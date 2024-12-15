# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
style test_style:
    color "#000000"
    size 25
    font "TurretRoad-Medium.ttf"    

define protagonist = Character("Self-Talk")
# define e = Character("Self-Talk")
# define e_3d = Character("Self-Talk")
# define eb = Character("Self-Talk")
define story = Character("")
define raina = Character("Raina")
define dayonetta = Character("Dayonetta")
define justina = Character("Betroid")

#sprites are too big
transform half_size: 
    zoom 0.75 #adjust as required

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



    # e "Wanna see some new text effects I've been making?"
    # e "Here's one {atl=bounce}ATL based text tag in use.{/atl}"
    # e "Here's one using {atl=rotate_text~0.5, bounce_text~10}ATL to do the bounce effect.{/atl}"
    # e "Here's a rotate using {atl=0.1,rotate_text~0.8}ATL as a tag thingy.{/atl}"
    # e "Here's a {atl=0.3,drop_text~#~ 1.5, bounce_text~10}dripping text ATL example.{/atl}"
    # camera threeD_text:
    #     perspective True
    # e_3d "Here's a {atl=-0.1, text_rotate_3d}3D ATL text effect.{/atl}"
    # "Here's a normal line with an override to {atl=-0.1, text_rotate_3d}allow for 3D Text.{/atl}" (show_layer="threeD_text")
    # camera threeD_text
    # e "Here's a fade in {atl=-#,#,fade_in_text~1.0}atl text tag along with another atl text tag{/atl}"
    # e "Here's some {explode}exploding text.{/explode} Just give it a sec."
    # e "Here's some {explodehalf=2-2.0}position exploding text{/explodehalf}."
    # e "Here's a {glitch=1.1}{color=#0f0}{b}Glitch{/b}{/color} Tag{/glitch}"
    # # I know these first couple are a bit of an eye sore but wanted to show here how to apply styles to the effects.
    # # And how previous styling won't be applied through them...
    # eb "Here is some {bt=h10-s0.5-p10.0}wavy bouncey{/bt} text"
    # e "Here is some {sc}{b}{i}{font=FOT-PopJoyStd-B.otf}{=test_style}scared{/b} sha{/font}key{/i}{/=test_style}{/sc} text"
    # e "Here is some {rotat}spinning rotation{/rotat} text"
    # e "Here is a {gradient=#ff0000-#00ff00}fancy gradient{/gradient} {gradient=#00ff00-#0000ff}with every color{/gradient} {gradient=#0000ff-#ff0000}of the rainbow{/gradient}!!"
    # e "Here is a {gradient2=6-#ff0000-#ffff00-10-#ffff00-#00ff00-10-#00ff00-#00ffff-10-#00ffff-#0000ff-10-#0000ff-#ff00ff-10-#ff00ff-#ff0000-10}fancy gradient with every color of the rainbow{/gradient2}!!"
    # e "{fi=0-0.5}Here is some fade in text{/fi}"
    # e "Here is some more selective {fi=13-1.5-20}fade in{/fi} text"
    # e "Here is some {move}{b}moveable sliding{/move} text. Move your mouse near it to see!!"
    # e "I'm having conflicting feelings about this..."
    # e "{bt=2}There still seems to be some bugs. Like if I just keep typing this, this text will continue off the screen and you won't be able to read it.{/bt}"
    # e "{bt=2}But if we insert a paragraph tag into our line, we'll be able to tell \nthe text displayable to make a new paragraph to avoid the issue! \nHuzzah!!{/bt}"
    # e "I want to {swap=love@hate@1.0}{bt}feel{/bt}{/swap} it."
    # e "And I feel something bad is about to {chaos}happen...{/chaos}"
    # e "{chaos}Helllllp Mmeeeee!!!{/chaos}"
    # # This is mostly to demonstrate that the tags can stack. However this does cause lag the more you apply
    # # If you wish to apply this many, I advise you make a single Class that does all the effects itself or...
    # e "{bt}{sc}{rotat}{chaos}Oh god NOooooo{/rotat}{/sc}{/bt}"
    # # You could do this. Have them nest directly without as many render callbacks through Text displayables
    # e "{omega=BT=5@SC=10@FI=20-0.5@ROT=400@CH}Oh god NOooooo{/omega}"
    # e "{bt=20}{fi=20-1.5}Must{/fi} {rotat}gain{/rotat} {sc=10}control!!! For [playername]!!!{/sc}{/bt}"
    # # They can be applied to menu options as well
    # menu:
    #     "{bt}Breath{/bt}":
    #         e "*breathe*"
    #         e "{bt=1}*breathe*...{/bt}"
    #     "{chaos}Panic More{/chaos}":
    #         e "{sc=10}That probably won't help.{/sc}"
    #         e "{sc=3}I'ma just {/sc}{sc=1}calm down{/sc} now..." 
    # e "How did you like them?"
    # e "I hope you can come up with even more clever ones!"
    # e "If you do, be sure to share them! I'd {bt=4}love{/bt} to see them~"
    # # Internal monologue and scene setup
    # protagonist "A dimly lit bar. I stand nervously by the counter, nursing a soda."
    protagonist "Why did I come here? No one comes to bars for the soda. Just... act natural. Stand casually. "
    # protagonist "Here's one {atl=bounce}ATL based text tag in use.{/atl}"
    protagonist "Yeah, because this is what casual feels like."


    story "(He glances around. A soft-spoken woman in athletic wear approaches the bar with a gentle smile.)"
    show raina meditate at half_size,midright
       
    protagonist "Okay, I can do this. Just be {explodehalf=1-1.0}casual{/explodehalf}. Just be {rotat}normal{/rotat}. And maybe don’t spill your drink this time."

    show raina neutral at half_size,midright
    raina "Hi there! My name's Raina. You seem...  {glitch=1.1}tense{/glitch}. Everything okay?"

    $ option1 = tracery("#conversation_starter#")
    $ option2 = tracery("#conversation_starter#")
    $ option3 = tracery("#conversation_starter#")
    menu:
        "[option1]":
            e "#origin#::option1"
            show raina meditate at half_size,midright
            raina "Relaxing is important. Here, let’s practice our {bt=2}breathing{/bt} and {bt=2}calm down{/bt}!"

        "[option2]":
            e "#origin#::option2"
            show raina meditate at half_size,midright

            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

        "[option3]":
            e "#origin#::option3"
            show raina meditate at half_size,midright
            raina "Relaxing is important. Here, let’s practice our breathing and calm down!"

    show raina meditate at half_size,midright
    protagonist "Is she… meditating? In a bar? Should I join her? I’ll look weird if I don’t. But also weird if I do. Oh no, what do I do with my {sc}hands?{sc}"

    show raina cheerful at half_size,midright
    raina "Now that was a great workout! You know... maybe you should come down to my studio sometime and I could give you a private lesson?"


    $ rain_option1 = tracery("#convo_with_raina#")
    $ rain_option2 = tracery("#convo_with_raina#")
    $ rain_option3 = tracery("#convo_with_raina#")
    menu:
        "[rain_option1]":
            e "#origin#::option1"
            show raina confused at half_size,midright
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "[rain_option2]":
            e "#origin#::option2"
            show raina confused at half_size,midright
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"

        "[rain_option3]":
            e "#origin#::option3"
            show raina confused at half_size,midright
            raina "Well… maybe another time then… remember to stretch your legs and focus on balance. Maybe one day, you’ll be able to lift 350 pounds like me!"



    # Transition to the next encounter
    scene bg booth with fade:
        zoom 4
        blur 15

    story "(She leaves, and the protagonist exhales sharply.)"
    protagonist "Okay, one down, but there’s plenty of other opportunities around here. I mean, she was practically a yoga class in human form anyways, so maybe I’ll have better luck over there?"
    
    # protagonist "I spot a woman with glasses and dark short hair sitting alone at a booth. She seems approachable but mysterious."
    show dayonetta neutral at half_size, midright
    story "A woman with glasses and dark short hair sits alone at a booth. She is approachable but mysterious."
    show dayonetta amused at half_size, midright
    dayonetta "Hello darling, terribly sorry to see you strike out over there. If you need to learn to talk to a lady… why not ask me!"
    show dayonetta amused at half_size, midright

    $ dayonetta_option1 = tracery("#convo_with_dayonetta#")
    $ dayonetta_option2 = tracery("#convo_with_dayonetta#")
    $ dayonetta_option3 = tracery("#convo_with_dayonetta#")
    menu:
        "[dayonetta_option1]":
            e "#origin#::option1"
            show dayonetta confused at half_size, midright
            dayonetta "Demon got your tongue? It’s alright darling, shall we start you off with a cosmopolitan? Maybe that will give the confidence to slay some angels, or at least get a word out."

        "[dayonetta_option2]":
            e "#origin#::option2"
            show dayonetta confused at half_size, midright
            dayonetta " Demon got your tongue? It’s alright darling, shall we start you off with a cosmopolitan? Maybe that will give the confidence to slay some angels, or at least get a word out."

        "[dayonetta_option3]":
            e "#origin#::option3"
            show dayonetta confused at half_size, midright
            dayonetta " Demon got your tongue? It’s alright darling, shall we start you off with a cosmopolitan? Maybe that will give the confidence to slay some angels, or at least get a word out."

    show dayonetta flirt at half_size, midright
    story "She winks and walks away. That could have gone better… or worse."

    # Transition to the final encounter
    scene bg booth_motorbike with fade:
        zoom 5
        blur 15

    protagonist "Wow. I really thought I’d be better at this. Well, third time’s the charm I suppose. I think that woman over there came in on a motorbike, maybe she’s cool enough for my style."
    story "(You approach the woman in another booth nearby, she is blonde with her orange and green motorcycle helmet on the table beside her)"

    show betroid neutral at half_size, midright
    justina "Ugh, what do you want?"


    $ justina_option1 = tracery("#convo_with_justina#")
    $ justina_option2 = tracery("#convo_with_justina#")

    menu:
        "[justina_option1]":
            e "#origin#::option1"
            show betroid angry at half_size, midright

            justina "Great, another creep. Look buddy I’m just trying to enjoy the one night I have to relax before my next mission, so if you were looking to waste my time I suggest you get moving."

        "[justina_option2]":
            e "#origin#::option2"
            show betroid angry at half_size, midright
            justina "Great, another creep. Look buddy I’m just trying to enjoy the one night I have to relax before my next mission, so if you were looking to waste my time I suggest you get moving."

        
        "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?":
            e "#origin#::option3"
            show betroid angry at half_size, midright
            # protagonist "I’ll be honest. I saw you sitting alone from across the bar and there was just something about you that called me over here. Your eyes are so gentle and your lips are so soft I feel fortunate just to witness them. Forgive me if this is too forward, but might I sit with you here and spend the evening with you?"
            justina "Great, another creep. Look buddy I’m just trying to enjoy the one night I have to relax before my next mission, so if you were looking to waste my time I suggest you get moving."


    menu:
        
        "Playing hard to get I see? You know, deadly is just my type.":
            stop music
            play music "domingodeguardia.mp3"
            show betroid confused at half_size, midright
            justina "Alright, I’ll admit, that was a pretty honest attempt. Nervousness and all, at least you’re not like the usual creeps I run into."
            protagonist "Really? I mean… thank you! I promise, I’m not trying to bother you—I just thought you seemed… interesting."
            show betroid neutral at half_size, midright
            justina "Interesting, huh? Well, I guess I could use a decent conversation tonight. Alright, I’ll bite. But you’d better not make me regret this."
            protagonist "You won’t! I swear!"
            show betroid confused at half_size, midright
            justina "Alright, then. Pull up a seat. Just don’t try anything fnny—deadly isn’t just my type, it’s also what I am."
            protagonist "Noted! Drinks on me?"
            show betroid neutral at half_size, midright
            justina "You’ve got five minutes to impress me. Let’s see if you’re worth more than just a drink"


            # alternate ending

            stop music
            play music "Deliciously-Sour.mp3"
            # End the game
            scene bg outsidebar:
                blur 100

            story "The rest of the night pased by in a blur. Only if the censorship laws were relaxed would we be able to tell you what happened. The protagonist can't remember what happened, but they do remember that tjey ..."
            story "..."
            story "You wake up in a hospital bed. Doctors said you had a panic attack last night and a blonde girl dropped you off. Betroid is nowhere to be found."
            return

        "No, please! This is a misunderstanding and I’m just so nervous I can’t even get a word out. I’m sorry to disturb you during your night out, I was just looking to make a friend.":
            show betroid disinterested at half_size, midright
            justina "Well, if stammering was a competition, you'd have gold by now. But hey, points for effort. Good luck next time—now scoot before my patience runs out."

        "What’s the use?{sc} Erm…uhhh…durrrr{sc}.":
            show betroid disinterested at half_size, midright
            justina "Well, if stammering was a competition, you'd have gold by now. But hey, points for effort. Good luck next time—now scoot before my patience runs out."

    

    stop music
    play sound "thwack-06.wav"

    # End the game
    scene bg outsidebar:
        blur 10
    play music "crickets.mp3"
    protagonist "{sc}I’ve been thrown out of the bar. Maybe I need to rethink my strategy.{/sc}"
    #    protagonist "{bt}{sc}{rotat}I’ve been thrown out of the bar. Maybe I need to rethink my strategy.{bt}{sc}{rotat}"

    return