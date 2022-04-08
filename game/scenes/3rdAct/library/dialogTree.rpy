define library3IchimatsuTalks = 0
define ichiShoot = False
define library3IchimatsuKnock = False
label library3Start:

    scene library3 background with dissolve
    call screen library3 with dissolve

label library3Rift:
    sam "Whoa"
    sam "Another hole"
    cmax "I wonder if its feels as weird as the other one"
    sam "Maybe"
    sam "Let's find out"
    play sound "audio/sounds/thermos-slide.mp3"
    "* zzoopppp *"
    sam "Anything unusual little buddy?"
    cmax "AAannnGGnnAADDGGrrrRrrMMM"
    sam "Oh, so it's the same"
    play sound "audio/sounds/zit-pop.mp3"
    "* pop! *"
    sam "That's dissapointing"
    cmax "Let's me go again!"
    sam "Maybe when my muscles don't scream of pain trying to get you out Max"
    jump library3Start

label library3Ichimatsu:
    if library3IchimatsuKnock:
        sam "We're back"
        cmax "You better don't move or else I'll break all your toes"
        ichimatsu "......"
        jump library3IchimatsuMenu
    else:
        $ library3IchimatsuKnock = True
        sam "Somebody there?"
        ichimatsu "I'm sleeping!"
        cmax "Oh, another shadow!"
        if museum3MaddieTalk:
            sam "We should be expecting something like this by now"
        ichimatsu "Go away!"
        sam "Nothing can do"
        sam "We're Sam and Max, Freelance Police"
        ichimatsu "The police?!"
        sam "And we're the ones doing the questions, mister"
        cmax "So, start talking, or else I'm going to get serious"
        ichimatsu "......."

label library3IchimatsuMenu:
    menu:
        "What are you doing under a table?" if library3IchimatsuTalks == 0:
            sam "What are you doing under that table?"
            ichimatsu "It's confortable"
            ichimatsu "I don't get seen very well from there"
            cmax "Are you trying to hide?"
            ichimatsu "I'm..."
            ichimatsu "I'm..."
            ichimatsu "A bit shy, I guess"
            sam "I see"
            $ library3IchimatsuTalks = 1
        "Do you know what's going on with this colored hole right here?" if library3IchimatsuTalks == 1:
            cmax "You know, the one right here"
            ichimatsu "I..."
            ichimatsu "Don't know if I should tell you....."
            cmax "Oh, so you know something"
            sam "That's interesting"
            sam "It's there a particular reason why you cannot tell us?"
            cmax "It's a 3 trials thing maybe"
            ichimatsu "I would not object a cat..."
            ichimatsu "But I would prefer if you were a changeling..."
            $ library3IchimatsuTalks = 2
        "We do know a changeling!" if museum3Changelings == 3 and library3IchimatsuTalks == 2:
            sam "Well, Papierwaite is a changeling"
            ichimatsu "Who?"
            sam "The curator of the museum"
            cmax "The one who is boring and talks a lot"
            cmax "And also boring"
            ichimatsu "Oh, I think I saw him"
            ichimatsu "But that should not work"
            sam "Why not?"
            ichimatsu "He has a voice from nowhere"
            cmax "Wait"
            cmax "If he has a voice, it's not from nowhere"
            cmax "It's from him!"
            sam "I'm assuming he's talking about Dr. Norrington"
            ichimatsu "I..."
            ichimatsu "I can heard both of them having a conversation while I'm an earshot of his voice"
            ichimatsu "I need a changeling without a voice from nowhere"
            sam "Why?!"
            ichimatsu "I don't know exactly"
            ichimatsu "************** said we needed one"
            ichimatsu "Then we should go back to him"
            cmax "OHHHHH"
            cmax "That blob is near where all this dimensional problem started!"
            sam "We're getting somewhere!"
            $ library3IchimatsuTalks = 3
        "Please describe this brother of yours and his exact location if you may" if library3IchimatsuTalks == 3:
            sam "What's his hue and where he is"
            ichimatsu "..."
            ichimatsu "Red"
            ichimatsu "..."
            ichimatsu "And..."
            ichimatsu "I dunno..."
            sam "We just need some sort of reference, any sort of reference"
            cmax "I have in my brain the whole map of the city"
            cmax "Just tell me something like the color and I will know"
            ichimatsu "It's..."
            ichimatsu "A building with a big park on front"
            cmax "I'm drawing blank"
            sam "It may be a building near the Week without Sleeping Memorial park"
            sam "Near some high voltage cables"
            ichimatsu "I saw some of those"
            sam "Finally, good information!"
            cmax "Let's go to this red hue and get to the bottom of this"
            cmax "Violently!"
            sam "That's the spirit little buddy"
            $ library3IchimatsuTalks = 4
        "Let's try with another" if shootingMatsus and not ichiShoot:
            $ ichiShoot = True
            cmax "Let's try shoot him!"
            "* SHOT! *"
            cmax "Awww...."
            cmax "It didn't work"
            ichimatsu "Wha..."
            ichimatsu "WHAT DID YOU DO?!!!"
            sam "Your yellow brother was spit balling and suggested to try and kill you guys"
            cmax "I shot him, it didn't work"
            cmax "I shot you, it didn't work either"
            ichimatsu "What?!"
            ichimatsu "I cannot die?"
            sam "Wait, do you wanna die?"
            ichimatsu "It's not because I'm just a coward"
            ichimatsu "I will continue this pitiful existence no matter what I do"
            cmax "Well, I'll keep trying with the rest of your brothers"
            cmax "Maybe shooting one of them will give you back your mortality"
            sam "And it's that happens, please stay very far away from knives"
            sam "It's way too slow and not recommended"
        "Don't move!":
            sam "We'll be back!"
            cmax "Don't move or else I'll break your knee caps!"
            ichimatsu "I cannot move..."
            ichimatsu "But ok"
            jump library3Start


    jump library3IchimatsuMenu

label backToMuseum3:
    jump museum3Start