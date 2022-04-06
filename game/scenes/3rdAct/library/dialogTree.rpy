define library3IchimatsuTalks = 0:
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
    ""
    jump library3IchimatsuMenu

label backToMuseum3:
    jump museum3Start