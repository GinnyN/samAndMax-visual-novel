label dimensionalRift3Intro:
    scene dimensionalRift3 background with dissolve
    call screen dimensionalRift3 with dissolve

label dimensionalRift3:
    show sam neutral with dissolve:
        xpos -0.1
    sam "Look at that"
    show cmax neutral with dissolve:
        xpos 0.1
    cmax "It looks like one of your orders from the pizza place"
    cmax "Just a bit less radioactive"
    show sam suspicious with dissolve
    sam "I don't think this is something that should be happening"
    show cmax excited with dissolve
    cmax "Maybe it has something to do with the comissioner assignment!"
    show sam neutral with dissolve
    sam "You just want me to shove your head inside to see the colors, right?"
    cmax "You know how much I love colorful life or dead situations!"
    sam "Max..."

label dimensionalRift3Menu:
    menu:
        "Shove Max Head Inside the Rift":
            hide angela with dissolve
            sam "Here you go little buddy"
            hide cmax with dissolve
            cmax "WHEEEEEEE"
            play sound "audio/sounds/thermos-slide.mp3"
            show sam neutral with dissolve:
                xpos 0.2
            pause 0.5
            sam "Can you see anything Max?"
            cmax "AAannnGGnnAADDGGrrrRrrMMM"
            show sam happy with dissolve
            sam "You seem to be having fun in there"
            cmax "JJddd<sgErrwfvfSDgdgereDDsafwqwqe"
            show sam neutral with dissolve
            sam "Ok, enough fun"
            "..."
            sam "Argh..."
            "..."
            show sam serious with dissolve
            sam "Grrrrrrrrrrr"
            "..."
            show sam neutral with dissolve
            sam "Haive hoooooooooooo"
            play sound "audio/sounds/zit-pop.mp3"
            "POP!"
            show sam neutral flip with dissolve:
                xpos 0.2
            show cmax neutral with dissolve:
                xpos 0.1
            sam "Good thing you came back little buddy"
            sam "My arms were developing muscular pains in muscles I didn't remember existed"
            show cmax excited with dissolve
            cmax "It was so weird!"
            cmax "From inside you cannot see any kind of colors"
            show cmax thinking with dissolve
            cmax "It's kind of shallow?"
            sam "Like a puddle from a storm in Los Angeles?"
            cmax "Not really..."
            show cmax ohyeah with dissolve
            cmax "It felt kinda like going thru one of your Granma sweaters she send us for Christmas"
            cmax "After I accidently I strunk them in a laundry accident"
            show sam surprised flip with dissolve
            sam "You did what?"
            show cmax neutral with dissolve
            cmax "You know what I mean?"
            show sam neutral flip with dissolve
            sam "No"
            sam "Not really"
            sam "But if we talk with an actual expert about this they could point us to something useful"
            show cmax excited with dissolve
            cmax "Like a good softener for sweaters?"
            show sam serious flip with dissolve
            sam "A Dimension expert bubblehead"
            sam "You can explain to my granny what happened AFTER the case"
            show cmax neutral with dissolve
            cmax "Oh"
        "What do you think" if straightAndNarrow3Angela:
            show sam neutral flip with dissolve:
                xpos 0.2
            sam "Hey, Angela"
            show cmax neutral flip with dissolve
            sam "Do you have any idea about this colorful but unusual conumdrum?"
            show angela unsure with dissolve:
                xpos -0.1
            angela "No idea"
            angela "The comissioner never tell anyone what's in the documents he sends to you"
            show angela thinking with dissolve
            angela "The only thing I heard about was some ramblings about the secret service which has been annoying him the last 5 years or 4..."
            angela "I dunno"
            show angela neutral with dissolve
            angela "I started working there last year"
            cmax "Do you want to be shoved into the void to see what's inside?"
            show angela happy with dissolve
            angela "I tried something similar once"
            show angela unsure with dissolve
            angela "I returned everything I ate in the last 4 days" 
            angela "I'm not risking it again"
            show angela neutral with dissolve
            angela "It looks like it closing though"
            show sam neutral with dissolve
            sam "Do you think that?"
            angela "Like sew a sweater and then pulling the yarn"
            show cmax surprise flip with dissolve
            cmax "Do you know a good softener for sweaters?"
            show angela unsure with dissolve
            angela "I don't use sweaters, never get used to it"
            angela "My dad's skin always got rashy and red and then he scrached himself until he drew blood"
            show angela thinking with dissolve
            angela "I think I saw muscle once"
            show angela neutral
            show cmax ohyeah flip 
            with dissolve
            angela "So, we banned sweaters from our family ever since"
            show sam neutral flip
            show cmax neutral 
            with dissolve
            sam "At least that sounds like good news"
            sam "If it's trying to close, we need to find what's happening it's affecting that behaviour"
            show angela happy with dissolve
            angela "I hope it involves a lot of shooting so you guys have fun"
            sam "We always hope the same"
            sam "Never works though"
            show cmax excited with dissolve
            cmax "But I try my best!"
        "Go Back":
            hide sam
            hide angela
            hide cmax
            with dissolve
            call screen dimensionalRift3 with dissolve
    jump dimensionalRift3Menu

label changeSceneToStraightAndNarrow3:
    jump straightAndNarrow3Back