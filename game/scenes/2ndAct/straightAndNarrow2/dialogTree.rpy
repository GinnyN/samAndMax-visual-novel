define straightAndNarrow2Started = False

label straightAndNarrow2Start:

    if not straightAndNarrow2Started:
        play sound "audio/sounds/crash.ogg"
        scene straightAndNarrow2 background crash with hpunch
        scene straightAndNarrow2 background with dissolve
        show cmax excited flip with dissolve:
            xpos -0.0
        cmax "I GOT IT! I GOT IT!"
        hide cmax with dissolve
        "crash crash crash crash"
        scene straightAndNarrow2 background with hpunch
        show sam serious flip with dissolve:
            xpos 0.0
        sam "Yes?"
        sam "Yes!"
        sam "Nooo..."
        sam "Sure, sure"
        sam "We'll see, we'll see"
        sam "Ok, bye bye..."
        show cmax neutral flip with dissolve:
            xpos 0.4
        cmax "Who was it?"
        show sam neutral with dissolve
        sam "The Commissioner Informant Max"
        show cmax surprise flip with dissolve
        cmax "The informant?"
        cmax "Did they not just pick up the door and leave everything on your desk?"
        sam "If I have to guess, Superball just made a visit"
        cmax "But he's the president of the United States! Why he keeps coming here?"
        sam "I always suspected he isn't really confortable if he's not guarding a door"
        show cmax neutral flip with dissolve
        cmax "Maybe we should give him a better door to guard, like anything they have at fort knox"
        show sam serious with dissolve
        sam "We'll have to leave that for later Max, the informant said they are calling nearby, so we have to go out and meet them"
        show cmax excited flip with dissolve
        cmax "Oh boy!"
        hide cmax
        hide sam
        with dissolve
        $ straightAndNarrow2Started = True
    else:
        scene straightAndNarrow2 background with dissolve


label straightAndNarrow2Back:
    scene straightAndNarrow2 background with dissolve
    call screen straightAndNarrow2 with dissolve

label straightAndNarrowFastTravel:
    scene straightAndNarrow2 background with dissolve
    show cmax neutral flip with dissolve:
        xpos 0.4
    cmax "Where we going Sam?"
    show sam neutral flip with dissolve:
        xpos 0.0
    sam "Nowhere"
    sam "I just noticed we have a new blood stain in the passenger seat"
    show cmax surprise flip with dissolve
    cmax "How did you figure out that?"
    cmax "The interior is red!"
    show sam sarcastic with dissolve
    sam "Max..."
    show cmax bored flip with dissolve
    cmax "Fine fine, I was poking an eyeball I got last night after the raid at the yogurt factory"
    show sam neutral with dissolve
    sam "It's ok Max, next time just don't do that with a leaky one, at least in the car"
    hide cmax
    hide sam
    with dissolve
    call screen straightAndNarrow2 with dissolve

label straightAndNarrow2Matsu:
    scene straightAndNarrow2 background with dissolve
    show sam neutral with dissolve:
        xpos -0.1
    sam "Hello?"
    show todomatsu shee flip with dissolve:
        xpos 0.5
    todomatsu "***********!"
    show todomatsu angry flip with dissolve
    todomatsu "So YOU are those guys who doesn't let me sleep!"
    show cmax neutral with dissolve:
        xpos 0.1
    cmax "Sam?"
    cmax "Who is this uncolored loser?"
    sam "I don't know Max"
    sam "It can be a tribe from the 3rd layer of earth and this member just got an overreaction while getting a tan"
    todomatsu "No, no, you go out!"
    todomatsu "Last night I couldn't sleep with you igniting fireworks from your roof"
    sam "Those weren't fireworks. Those are prohibited by law to be used by people without a licence"
    show cmax excited with dissolve
    cmax "We were testing our new canon!"
    sam "Max had some ideas for interrogation with subjects"
    cmax "Did you know that watermelons can be cut in half by throwing them at match 3 speed?"
    cmax "They also go way faster if you carve in eyesockets!"
    todomatsu "lalalalalalala"
    todomatsu "I'm not listening"
    todomatsu "Go away"
    show cmax surprise with dissolve
    cmax "But"
    todomatsu "GO AWAY!"
    show todomatsu angry flip:
        xpos 0.1
    hide sam
    hide cmax
    with dissolve
    pause(1)
    hide todomatsu with dissolve
    pause(1)
    show sam serious flip:
        xpos 0.3
    show cmax surprise flip:
        xpos 0.2
    with dissolve
    sam "Well, that was a cranky shadow from the unspeakable dimension of nothingness and loudness"
    show cmax angry with dissolve
    cmax "I say we go there, you'll keep it at gunpoint while I'm trying to find his toenails with my pliers"
    show sam neutral flip with dissolve
    sam "Not now Max"
    sam "We need to find the informant"
    sam "Also, your pliers flew to Canada in a watermelon last night"
    show cmax ohyeah with dissolve
    cmax "So that's why couldn't find them this morning"
    hide cmax
    hide sam
    with dissolve
    call screen straightAndNarrow2 with dissolve

label straightAndNarrow2Office:
    scene straightAndNarrow2 background with dissolve
    show sam neutral with dissolve:
        xpos -0.1
    sam "We don't have time for that now, we need to find the informant"
    hide sam with dissolve
    call screen straightAndNarrow2 with dissolve

label straightAndNarrow2Tardis:
    show cmax excited flip zorder 2 with dissolve:
        xpos 0.1
    cmax "Look at this Sam!"
    show sam surprised flip zorder 1 with dissolve:
        xpos 0.4
    sam "Jumping cars from the dark dimension trying to eat our souls with mayo and a bit pico de gallo!"
    show sam neutral flip with dissolve
    sam "I haven't seen one of this since the Clinton Administration!"
    show cmax excited with dissolve
    cmax "Do you think it jumped from another dimension?"
    sam "Probably"
    sam "Maybe it's a clue of the case the commissioner wants us to investigate"
    show sam suspicious flip with dissolve
    sam "But we still don't know where the informant is"
    angela "Hello?"
    angela "Freelance Police?"
    show sam surprised flip with dissolve
    sam "Did you heard that little buddy?"
    show cmax excited flip with dissolve
    cmax "It came from the blue box"
    angela "I was sent by the commissioner"
    show sam serious flip with dissolve:
        xpos 0.0
    show cmax excited flip with dissolve:
        xpos 0.4
    sam "Are you the informant?"
    show cmax surprise flip with dissolve
    cmax "The blue box is the informant?"
    angela "Yes!"
    angela "And no..."
    angela "Anyway"
    sam "Something is sliding out of the box"
    angela "Here's the briefing"
    angela "Now... can you..."
    show cmax excited flip with dissolve
    cmax "What it says Sam?!"
    show sam neutral with dissolve
    sam "It says there some dimensional related troubles in our neighborhood little buddy"
    show cmax neutral flip with dissolve
    cmax "Maybe it's the time we raced at the river styx with the rats"
    show sam suspicious with dissolve
    sam "I cannot find a formal complain from Satan"
    show sam neutral with dissolve
    sam "While that makes it less likely, I'll keep that in mind"
    sam "Let's go little buddy, there's a dimension rift to investigate"
    show cmax excited flip with dissolve
    cmax "Great!"
    hide sam
    hide cmax
    with dissolve
    "..."
    "..."
    angela "Hello?"
    jump straightAndNarrow3Back


label changeSceneToDimensionalRift:
    jump dimensionalRiftIntro