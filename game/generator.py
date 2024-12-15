# This file contains all the grammars and syntax rules for Tracery.
# It should only contain the constants and grammars that are used in
# the game. 

# The logic of the game is contained in the script.rpy file.


# Kai's grammar when the player is rambling
i_cant_speak_grammar = {
    "origin":["#nearby# #line#"],
    "line":["#mood.capitalize# could I just say, #compliment#, {sc}ohmygoshIsucksomuch{/sc} #attempt#. No, wait, please! Don't look at me like that! *breathes heavily* #fail#"],
    "nearby":["Y'see, #fail#", "Errrr", "Salutations, greetings, wait no", "Geez, shit, wait I'm trying to say"],
    "compliment":["you're fine, deadly I hope, which is just my type", " your eyes are gentle and lips soft, and I am the happiest soul alive to witness that", "aww, shucks, well I just want to sit and spend the evening with you", "I'm kinda embarrassed...you seem very nice and I would love some advice, o-only if you don't mind", "are you a witch? Cause' you've put a spell on me", "hubba bubba"],
    "mood":["I'm fine, decent even, but", "Oh hellllooooo Angel? Demon? Too much?", "I'm well, um..uhhhh pretty gooood", "Errr, great but also omgI'msoembarrassedIcoulddie, should I order an Uber? Wait no,"],
    "fail":["before you showed up I was unhindered by these petty mortal feelings.", "I only hang out in basements.", "actually I 100% totally positively talk to plenty of women I personally find more attractive than you.", "uhhh...I think you've had a few too many martinis.", "erm...umm....durrr...fuck.", "this is a misunderstanding and I'msonervousIcan'tevengetawordout.", "well. Um. Can I be your friend?"],
    "attempt":["I'll buy your next round", "get me an old fashioned waiter!", "I saw you sitting alone from across the bar and there was just something about you that called me over", "I apologize for disturbing your night out but can I, possibly, maybe, errr getyournumber?"]
}


# Menu 1 grammar rules
# Idea: find the right balance between randomness and consistency
# How to do this?
# a good sentnce structure,
#   1. first a good sentence starter
#   2. some randomizable follow-up
# 
# 1. I'm good, but you? Making my day brie-ght" 
#    "I'm good, but you?" + funny compliment
# 2. 



# "Not bad on my end. And yourself? Looking [pun]."
# "Doing alright. Meanwhile, you're [punny description]."
# "Surviving the day. Though you? Total [wordplay compliment]."
# "Can't complain. You, however? Absolutely [silly descriptor]."
# "Holding steady. Your vibe? [Ridiculous pun-based praise]."
# "Just another day. But you're something [comically exaggerated]."
# "Managing somehow. You? Straight-up [absurd compliment]."
# "Existing, basically. You're [ludicrous description]."
# "Treading water here. You? Peak [silly metaphor]."
# "Standard operations. You? Peak [punny excellence]."



# Punny Descriptions:

# Mint condition
# Sharp as a tack
# A cut above the rest
# Butter than expected
# Grated to perfection

# Silly Descriptors:

# Corny masterpiece
# Cheesy champion
# Gouda-mazing
# Radish-ly impressive
# Pickle of perfection

# Ridiculous Puns:

# Brew-tiful specimen
# Tea-rific vision
# Slice of awesome
# Poppin' fresh
# Cool as a cucumber

# Absurd Compliments:

# Spice of life
# Prime time fine
# Saucy sensation
# Crop top of excellence
# Kernel of greatness

# Ludicrous Metaphors:

# Walking pun-derpiece
# Human highlight reel
# Cosmic comedy
# Living meme
# Walking inside joke

punny_description = [
    "mint condition",
    "sharp as a tack",
    "a cut above the rest",
    "butter than expected",
]

silly_descriptor = [
    "corny masterpiece",
    "cheesy champion",
    "gouda-mazing",
    "radish-ly impressive",
    "pickle of perfection",
]

ridiculous_pun = [
    "brew-tiful specimen",
    "tea-rific vision",
    "slice of awesome",
    "poppin' fresh",
    "cool as a cucumber",
]
absurd_compliment = [
    "spice of life",
    "prime time fine",
    "saucy sensation",
    "crop top of excellence",
    "kernel of greatness",
]

ludicrous_metaphor = [
    "walking pun-derpiece",
    "human highlight reel",
    "cosmic comedy",
    "living meme",
    "walking inside joke",
]

first_half = [
    "I'm doing great, ",
    "I'm doing fine, ",
    "I'm alright, ",
    "I'm pretty good, ",
    "I'm hanging in there, ",
    "I'm doing okay, ",
    "I'm feeling good, ",
    "I'm fantastic, ",
    "I'm having a good day, ",
    "I'm doing wonderfully, ",
    "I'm in good spirits, ",
    "I'm feeling awesome, "
]


second_half = [
    "thank you for asking.",
    "How about you?",
    "and you?",
    "Thanks for checking in.",
    "just enjoying the day.",
    "hope you are too.",
    "thanks. How are things on your end?",
    "appreciate it. What about you?",
    "but it's been a busy day!",
    "though there's always room for improvement!"
]


dialogues = [
    "Not bad on my end. And yourself? Looking #punny_description#.",
    "Doing alright. Meanwhile, you're #silly_descriptor#.",
    "Surviving the day. Though you? Total #ridiculous_pun#.",
    "Just another day. But you're something #ludicrous_metaphor#.",
    "Standard operations. You? Peak #absurd_compliment#.",
    "I'm doing well. Nice to meet you.",
    "#first_half# #second_half#",
    "#first_half# #second_half#",
    "#first_half# #second_half#", # repeat so there is more probability of repeating
]

places = [
    "basemants",
    "attics", 
    "treehouses", 
    "libraries", 
    "cellars", 
    "caves", 
    "garages", 
    "rooftops", 
    "cabins", 
    "tunnels"
]

dance_move_or_skill = [
    "tap dance",
    "ballet",
    "jazz",
    "hip hop",
    
    # some other skill
    "sing",
    "play guitar",
    "play piano",
    "play drums",
    "dance",
]

convo_with_raina = [
    "Studio? No thanks, I only hang out in #places#.",
    "That sounds like fun, why don’t I order us an Uber and we get out of here?",
    "CHAT LETS GOOO WE’RE GOING HOME WITH HER",
    
    "A private lesson, huh? You think you can handle me?",
    "I'm not sure I'm ready for that kind of intensity.",
    "You know, I've always wanted to learn how to #dance_move_or_skill#.",
    
    "Sure, I'd love to. When are you free?",
    "Count me in. Let's do it.",
    "Um, I don't know... I'm not very good at that.",
    "I'm flattered, but I don't think I'm good enough."

    "I'll pass. I prefer my workouts to be less... personal."
]


convo_with_dayonetta = [
    "What's that? Sorry, no. I talk to plenty of women, hotter than you.",
    "Hubba hubba. Are you a witch? Cuz there’s a spell on me for sure.",
    "Oh yea… that was quite embarrassing… you seem very nice, I would love some advice if you don’t mind.",
    "I'm not sure I need your help, but I'm always open to learning new things.",
    "I appreciate the offer, but I think I've got this.",
    "I'm flattered, but I'm not interested.",
    "Oh, is that so? Well, I'm sure you have a lot of experience.",
    "I'll keep that in mind. Maybe I'll take you up on that offer.",
    "I'm not sure I'm ready for your advanced techniques.",
    "Thank you for the offer. I'll definitely keep that in mind.",
    "I'm grateful for your kindness. I'll try to do better next time.",
    "I'm a bit embarrassed, but I appreciate your willingness to help."
]

convo_with_justina = [
    "Just your number baby, and maybe a kiss while you’re at it.",
    "Sorry to bother you, I can get out of your way now.",
    "Oh, you caught my eye, didn't you? I've been watching you. And I like what I see. Give me your number, and maybe, just maybe, I'll let you see what I can do",
    "There's something about you. A darkness. A hunger. It's... intoxicating. Let's explore it together.",
    "You know what you want. You know what I want. Stop playing games. Give me your number, or I'll take it."
]

menu_grammar = {
    "conversation_starter":["#dialogue#"],
    "convo_with_raina":convo_with_raina,
    "convo_with_dayonetta":convo_with_dayonetta,
    "convo_with_justina":convo_with_justina,
    "dialogue": dialogues,
    "punny_description": punny_description,
    "silly_descriptor": silly_descriptor,
    "ridiculous_pun": ridiculous_pun,
    "absurd_compliment": absurd_compliment,
    "ludicrous_metaphor": ludicrous_metaphor,
    "first_half": first_half,
    "second_half": second_half,
    "dance_move_or_skill": dance_move_or_skill,
    "places": places
}