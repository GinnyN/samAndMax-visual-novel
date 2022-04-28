define library3IchimatsuTalks = 0
define ichiShoot = False
define library3IchimatsuKnock = False
image ichimatsu-shoot = "images/cinematic/shoot-ichimatsu.png"
label library3Start:

    scene library3 background with dissolve
    call screen library3 with dissolve

label library3Rift:
    show sam neutral with dissolve:
        xpos -0.1
    sam "Whoa"
    sam "Another hole"
    show cmax neutral with dissolve:
        xpos 0.1
    cmax "I wonder if its feels as weird as the other one"
    sam "Maybe"
    sam "Let's find out"
    hide cmax 
    show sam neutral:
        xpos 0.3
    with dissolve
    play sound "audio/sounds/thermos-slide.mp3"
    "* zzoopppp *"
    sam "Anything unusual little buddy?"
    cmax "AAannnGGnnAADDGGrrrRrrMMM"
    sam "Oh, so it's the same"
    show sam flip neutral
    show cmax neutral:
        xpos 0.1
    with dissolve
    play sound "audio/sounds/zit-pop.mp3"
    "* pop! *"
    sam "That's dissapointing"
    cmax "Let's me go again!"
    sam "Maybe when my muscles don't scream of pain trying to get you out Max"
    hide sam
    hide cmax
    with dissolve
    jump library3Start

label library3Ichimatsu:
    if library3IchimatsuKnock:
        show sam neutral flip:
            xpos 0.4
        show cmax neutral flip:
            xpos 0.3
        with dissolve
        sam "We're back"
        cmax "You better don't move or else I'll break all your toes"
        show ichimatsu smile:
            xpos -0.1
        with dissolve
        ichimatsu "......"
        jump library3IchimatsuMenu
    else:
        $ library3IchimatsuKnock = True
        show sam neutral flip:
            xpos 0.4
        show cmax neutral flip:
            xpos 0.3
        with dissolve
        sam "Somebody there?"
        ichimatsu "I'm sleeping!"
        cmax "Oh, another shadow!"
        if museum3MaddieTalk:
            sam "We should be expecting something like this by now"
        show ichimatsu neutral:
            xpos -0.1
        with dissolve
        ichimatsu "Go away!"
        sam "Nothing can do"
        sam "We're Sam and Max, Freelance Police"
        ichimatsu "The police..."
        sam "And we're the ones doing the questions, mister"
        show cmax menacing flip with dissolve
        cmax "So, start talking, or else I'm going to get serious"
        ichimatsu "......."

label library3IchimatsuMenu:
    menu:
        "What are you doing under a table?" if library3IchimatsuTalks == 0:
            show sam unsure flip
            show cmax neutral flip
            show ichimatsu neutral
            with dissolve
            sam "What are you doing under that table?"
            ichimatsu "It's confortable"
            ichimatsu "I don't get seen very well from there"
            show cmax thinking flip
            with dissolve
            cmax "Are you trying to hide?"
            show ichimatsu shy
            with dissolve
            ichimatsu "I'm..."
            ichimatsu "I'm..."
            ichimatsu "A bit shy, I guess"
            sam "I see"
            $ library3IchimatsuTalks = 1
        "Do you know what's going on with this colored hole right here?" if library3IchimatsuTalks == 1:
            show sam neutral flip
            show cmax neutral flip
            show ichimatsu neutral
            with dissolve
            cmax "You know, the one right here"
            ichimatsu "I..."
            show ichimatsu shy
            with dissolve
            ichimatsu "Don't know if I should tell you....."
            show cmax ohyeah flip
            with dissolve
            cmax "Oh, so you know something"
            sam "That's interesting"
            sam "It's there a particular reason why you cannot tell us?"
            show cmax neutral flip
            with dissolve
            cmax "It's a 3 trials thing maybe"
            ichimatsu "I would not object a cat..."
            show ichimatsu neutral
            with dissolve
            ichimatsu "But I would prefer if you were a changeling..."
            $ library3IchimatsuTalks = 2
        "We do know a changeling!" if museum3Changelings > 2 and library3IchimatsuTalks == 2:
            show sam neutral flip
            show cmax neutral flip
            show ichimatsu neutral
            with dissolve
            sam "Well, Papierwaite is a changeling"
            ichimatsu "Who?"
            sam "The curator of the museum"
            cmax "The one who is boring and talks a lot"
            cmax "And also boring"
            ichimatsu "Oh, I think I saw him"
            ichimatsu "But that should not work"
            sam "Why not?"
            ichimatsu "He has a voice from nowhere"
            show cmax thinking flip with dissolve
            cmax "Wait"
            cmax "If he has a voice, it's not from nowhere"
            cmax "It's from him!"
            sam "I'm assuming he's talking about Dr. Norrington"
            show cmax neutral flip with dissolve
            ichimatsu "I..."
            ichimatsu "I can heard both of them having a conversation while I'm an earshot of his voice"
            ichimatsu "I need a changeling without a voice from nowhere"
            sam "Why?!"
            ichimatsu "I don't know exactly"
            ichimatsu "************** said we needed one"
            ichimatsu "Then we should go back to him"
            show cmax ohyeah flip with dissolve
            cmax "OHHHHH"
            cmax "That blob is near where all this dimensional problem started!"
            show sam happy flip with dissolve
            sam "We're getting somewhere!"
            $ library3IchimatsuTalks = 3
        "Please describe this brother of yours and his exact location if you may" if library3IchimatsuTalks == 3:
            show sam neutral flip
            show cmax neutral flip
            show ichimatsu neutral
            with dissolve
            sam "What's his hue and where he is"
            ichimatsu "..."
            ichimatsu "Red"
            ichimatsu "..."
            ichimatsu "And..."
            ichimatsu "I dunno..."
            show sam explain flip with dissolve
            sam "We just need some sort of reference, any sort of reference"
            show cmax menacing flip with dissolve
            cmax "I have in my brain the whole map of the city"
            cmax "Just tell me something like the color and I will know"
            ichimatsu "It's..."
            ichimatsu "A building with a big park on front"
            show cmax neutral flip with dissolve
            cmax "I'm drawing blank"
            show sam neutral flip with dissolve
            sam "It may be a building near the Week without Sleeping Memorial park"
            sam "Near some high voltage cables"
            ichimatsu "I saw some of those"
            sam "Finally, good information!"
            show cmax excited flip with dissolve
            cmax "Let's go to this red hue and get to the bottom of this"
            cmax "Violently!"
            show sam happy flip with dissolve
            sam "That's the spirit little buddy"
            $ library3IchimatsuTalks = 4
        "Let's try with another" if shootingMatsus and not ichiShoot:
            $ ichiShoot = True
            cmax "Let's try shoot him!"
            play sound "audio/sounds/shot.mp3"
            scene ichimatsu-shoot with vpunch
            "* SHOT! *"
            show sam neutral flip:
                xpos 0.4
            show cmax aww flip:
                xpos 0.3
            with dissolve
            cmax "Awww...."
            cmax "It didn't work"
            show ichimatsu scream with dissolve:
                xpos -0.1
            ichimatsu "Wha..."
            ichimatsu "WHAT DID YOU DO?!!!"
            sam "Your yellow brother was spit balling and suggested to try and kill you guys"
            show cmax neutral flip with dissolve
            cmax "I shot him, it didn't work"
            cmax "I shot you, it didn't work either"
            ichimatsu "What?!"
            ichimatsu "I cannot die?"
            show sam unsure flip with dissolve
            sam "Wait, do you wanna die?"
            hide ichimatsu with dissolve
            ichimatsu "It's not because I'm just a coward"
            ichimatsu "I will continue this pitiful existence no matter what I do"
            cmax "Well, I'll keep trying with the rest of your brothers"
            cmax "Maybe shooting one of them will give you back your mortality"
            show sam neutral flip with dissolve
            sam "And if that happens, please stay very far away from knives"
            sam "It's way too slow and not recommended"
            scene library3 background 
            show ichimatsu neutral:
                xpos -0.1
            show sam neutral flip:
                xpos 0.4
            show cmax neutral flip:
                xpos 0.3
            with dissolve
        "Don't move!":
            hide sam
            hide cmax
            with dissolve
            sam "We'll be back!"
            cmax "Don't move or else I'll break your knee caps!"
            ichimatsu "I cannot move..."
            show ichimatsu smile with dissolve
            ichimatsu "But ok"
            hide ichimatsu
            with dissolve
            jump library3Start


    jump library3IchimatsuMenu

label backToMuseum3:
    jump museum3Back