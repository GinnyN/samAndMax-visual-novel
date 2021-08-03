label dimensionalRiftIntro:
    scene dimensionalRift background with dissolve
    call screen dimensionalRift with dissolve

label dimensionalRift:
    show sam neutral with dissolve:
        xpos -0.1
    sam "Look at that"
    show cmax neutral with dissolve:
        xpos 0.1
    cmax "It looks like one of your orders from the pizza place"
    cmax "Just a bit less radioactive"
    show sam suspicious with dissolve
    sam "I don't think this is something that should be happening"
    show sam neutral with dissolve
    sam "But at the same time we have to find the commissioner informant first"
    show cmax aww with dissolve
    cmax "Awww"
    cmax "I was looking forward to see beyond the horrors behind those colors"
    sam "Soon enough little buddy"
    hide sam
    hide cmax
    with dissolve
    sam "Soon enough"
    call screen dimensionalRift with dissolve

label changeSceneToStraightAndNarrow:
    jump straightAndNarrow2Back