define doYouHaveAny = 0
define whatDoYouGot = 0

label straightAndNarrowBuySomethingTree:
    menu:
        "What do you got?" if whatDoYouGot == 0:
            angela "What do you got?"
            show todomatsu eh flip with dissolve
            todomatsu "Well..."
            todomatsu "The only thing not gross from everything here is this box"
            todomatsu "It's says 'advanced lockpicking tools'"
            show angela thinking with dissolve
            angela "Well, that is convenient"
            show todomatsu neutral flip with dissolve
            todomatsu "Do you want it?"
            angela "I left my original ones at the headquarters"
            angela "Having an extra one is going to be useful"
            todomatsu "30 bucks"
            show angela proud with dissolve
            angela "Deal!"
            "..."
            show angela thinking with dissolve
            "..."
            show angela unsure with dissolve
            angela "This is a library card of some guy called Bosco"
            show todomatsu eh flip with dissolve
            todomatsu "I don't know about anything in here, I just cannot move for some weird reason, give me a break"
            show angela scared with dissolve
            angela "Fine fine..."
            $ whatDoYouGot = 1
            $ libraryCard = True
        "Do you have any..." if doYouHaveAny == 0:
            show angela thinking with dissolve
            angela "Do you have any... magic flutes with the power of transportation?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        "Do you have any..." if doYouHaveAny == 1:
            show angela thinking with dissolve
            angela "Do you have any... computers which became alive with the power of a thunderstorm?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        "Do you have any..." if doYouHaveAny == 2:
            show angela thinking with dissolve
            angela "Do you have any... tortillas made by blue grouches?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        "Do you have any..." if doYouHaveAny == 3:
            show angela thinking with dissolve
            angela "robot dogs?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        
        "Do you have any..." if doYouHaveAny == 4:
            show angela thinking with dissolve
            angela "tortillas made by orange grouches?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        "Do you have any..." if doYouHaveAny == 5:
            show angela thinking with dissolve
            angela "vodka made by blue spirits of the backyard?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        "Do you have any..." if doYouHaveAny == 6:
            show angela thinking with dissolve
            angela "evil planner machine to finally defeat that pesky blue elf?"
            show todomatsu neutral flip with dissolve
            todomatsu "No..."
            $ doYouHaveAny = doYouHaveAny + 1
        "Do you have any..." if doYouHaveAny == 7:
            show angela thinking with dissolve
            angela "Ah... I ran out of ideas"
            show todomatsu neutral flip with dissolve
            todomatsu "Thanks Akat..."
            show angela neutral with dissolve
            angela "I can start again though"
            show todomatsu angry flip with dissolve
            todomatsu "Why?! It's there any reason to do this?"
            angela "No"
            show angela happy with dissolve
            angela "I like the joke though"
            show todomatsu why flip with dissolve
            todomatsu "Why????"
            $ doYouHaveAny = 0
        "Nothing Else":
            show angela neutral with dissolve
            angela "Nothing else thanks you"
            show todomatsu neutral flip with dissolve
            todomatsu "Ok..."
            return


    jump straightAndNarrowBuySomethingTree