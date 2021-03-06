define straightAndNarrowVisited = False
define straightAndNarrow1OfficeVisited = False
define straightAndNarrow1TardisVisited = False
define straightAndNarrow1MatsuVisited = False
define libraryCard = False

label straightAndNarrow1Start:

    scene straightAndNarrow1 background with dissolve

    if not straightAndNarrowVisited:
        show angela thinking with dissolve:
            xpos -0.0
        angela "Yes"
        angela "This is the crossing between Straight and Narrow"
        angela "The office of the Freelance Police must be in this building at my left"
        show angela neutral with dissolve
        angela "The commissioner told me I have to give this briefing to them and they will know what to do"
        angela "I better hurry"
        play music "audio/music/Let's Make It Easy.mp3"
        hide angela with dissolve
        show screen notification("Let's Make It Easy - Nocturnal Spirits")

    call screen straightAndNarrow1 with dissolve

label straightAndNarrow1Office:
    show angela thinking flip with dissolve:
        xpos 0.4

    if not straightAndNarrow1OfficeVisited:
        angela "The door it's locked"
        angela "And it seems there no one at the office"
        angela "What to do..."
        $ straightAndNarrow1OfficeVisited = True

label straightAndNarrow1OfficeMenu:
    if not straightAndNarrow1SuperballOfficeVisited:
        menu:
            "Pick Lock and leave briefing inside":
                if not libraryCard:
                    show angela neutral flip with dissolve
                    angela "I cannot do that"
                    show angela happy flip with dissolve
                    angela "I left my lockpicking tools at my desk at the police headquarters"
                    angela "And if I go back I'm going to get an earful"
                    show angela thinking flip with dissolve
                    angela "There must be an alternative somewhere"
                    jump straightAndNarrow1OfficeMenu
                else:
                    angela "Ok..."
                    hide angela with dissolve
                    play sound "audio/sounds/door_open.mp3"
                    pause 0.5
                    angela "Maybe this library card will be...."
                    play music "audio/sounds/alarm.mp3"
                    show angela unsure flip with dissolve:
                        xpos 0.4
                    angela "What the..."
                    jump straightAndNarrow1SuperballOffice
            "Back to the street":
                hide angela with dissolve
                call screen straightAndNarrow1 with dissolve
    else:
        jump straightAndNarrow1SuperballOffice

label straightAndNarrow1Tardis:

    show angela unsure flip with dissolve:
            xpos -0.1
    if not straightAndNarrow1TardisVisited:
        angela "It's this..."
        angela "A time machine??"
        show angela neutral flip with dissolve
        angela "No, it's a phonebooth"
        show angela thinking flip with dissolve
        angela "Who install phonebooths at this place and age?"
        $ straightAndNarrow1TardisVisited = True

label straightAndNarrow1TardisMenu: 

    menu: 
        "Call the commissioner":
            show angela neutral flip with dissolve
            angela "I cannot do that"
            show angela serious flip with dissolve
            angela "The phones at the headquarters have been hacked and we cannot use them"
            angela "If I call this phone will also be compromised"
            jump straightAndNarrow1TardisMenu
        "Call the Freelance Police" if straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree < 2:
            show angela neutral flip with dissolve
            angela "I cannot do that"
            angela "I don't have their number"
            pause(2)
            show angela unsure flip with dissolve
            angela "Yes, I know it's my fault"
            jump straightAndNarrow1TardisMenu
        "Call the Freelance Police" if straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree == 2:
            show angela unsure flip with dissolve
            angela "Ok..."
            stop music fadeout 1
            angela "Mmm..."
            angela "This is not a celular number though..."
            scene straightAndNarrow1 foreground
            # $ renpy.movie_cutscene("video/enterSamAndMax.webm")
            jump straightAndNarrow2Start
        "Back to the street":
            hide angela with dissolve
            call screen straightAndNarrow1 with dissolve   

label straightAndNarrow1Matsu:

    if not straightAndNarrow1MatsuVisited:
        show angela neutral with dissolve:
            xpos -0.0
        angela "Hello??"
        show todomatsu neutral flip with dissolve:
            xpos 0.5
        todomatsu "Ahh.. What are you doing here?"
        angela "The door was open"
        todomatsu "Of course, you go inside all doors which are open"
        show angela scared with dissolve
        angela "You shouldn't be here either"
        angela "I think this building was slated for demolition some time ago"
        show todomatsu eh flip with dissolve
        todomatsu "I cannot move away"
        todomatsu "I already tried"
        todomatsu "There's good cellphone coverage though"
        show angela thinking with dissolve
        angela "I see.."
        $ straightAndNarrow1MatsuVisited = True
    else:
        show angela neutral:
            xpos -0.0
        show todomatsu neutral flip:
            xpos 0.5
        with dissolve

label straightAndNarrow1MatsuMenu:   
    menu:
        "Do you know about the Freelance Police?":
            show angela serious with dissolve
            angela "Do you know about the guys who work at the building next door?"
            show todomatsu eh flip with dissolve
            todomatsu "Do you mean the guys who sometimes make a ruckus with their guns and do not care for my sleep at 4th in the morning?"
            angela "I'm not really sure but probably"
            show todomatsu neutral flip with dissolve
            todomatsu "Never seem them"
            show angela thinking with dissolve
            angela "Ok"

        "I wanna buy something":
            show angela serious with dissolve
            angela "I wanna buy something"
            show todomatsu eh flip with dissolve
            todomatsu "This is not my store..." 
            todomatsu "and I'm technically squatting..."
            show todomatsu neutral flip with dissolve
            todomatsu "but ok, give me money"
            call straightAndNarrowBuySomethingTree from _call_straightAndNarrowBuySomethingTree
            
        "Back to the street":
            show angela neutral with dissolve
            angela "Thanks for your help citizen"
            hide angela
            show todomatsu neutral flip
            with dissolve
            todomatsu "Yeah, yeah, yeah, sure"
            hide todomatsu with dissolve
            call screen straightAndNarrow1 with dissolve
            
    
    jump straightAndNarrow1MatsuMenu