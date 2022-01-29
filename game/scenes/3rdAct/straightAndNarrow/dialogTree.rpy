define straightAndNarrow3MatsuVisited = False 
define straightAndNarrow3MatsuLibrary = False 
define straightAndNarrow3Angela = False 
define straightAndNarrow3ScaredSuperball = False 

label straightAndNarrow3Back:
    scene straightAndNarrow3 background with dissolve
    if museum3AngelaBack:
        angela "Oh.."
        angela "Hello guys..."
        $ museum3AngelaBack = False
    call screen straightAndNarrow3 with dissolve

label straightAndNarrow3FastTravel:
    scene straightAndNarrow3 background with dissolve
    show cmax neutral flip with dissolve:
        xpos 0.4
    cmax "Where we going Sam?"
    show sam neutral flip with dissolve:
        xpos 0.0
    if straightAndNarrow3MatsuLibrary:
        menu: 
            "Nowhere":
                show sam neutral with dissolve
                sam "Nowhere right now"
                cmax "Ok"
            "The Museum of Mostly Natural History":
                sam "The Museum of Mostly Natural History"
                cmax "Yeah, I also need a nap"
                if straightAndNarrow3ScaredSuperball and straightAndNarrow3Angela:
                    angela "This is good bye then"
                    sam "What?"
                    angela "I'm checking the time, and I need to be somewhere else"
                    angela "But I know with you guys the case is in good hands"
                    cmax "Do she really knows you?"
                    sam "But... but I thought..."
                    angela "I'll call later Sam"
                    sam "You said the same when you went on a roaring rampage of revenge of those years ago!"
                    angela "..."
                    angela "I was worried about the cartels..."
                    sam "We can handle that"
                    cmax "Why are you assuming I have any interest on this?"
                    angela "I'll call tomorrow"
                    angela "If I don't call, you ask the comissioner"
                    sam "Well..."
                    sam "Oh, alright"
                    angela "Take care guys!"
                    angela "And smash those dimension annomalies!"
                    $ straightAndNarrow3Angela = False
                    $ museum3AngelaStays = True

                stop music fadeout 2
                jump museum3Start
                
    else:
        sam "Nowhere"
        sam "I just noticed we have a new blood stain in the passenger seat"
        cmax "How did you figure out that?"
        cmax "The interior is red!"
        show sam neutral with dissolve
        sam "Max..."
        cmax "Fine fine, I was poking an eyeball I got last night after the raid at the yogurt factory"
        sam "It's ok Max, next time just don't do that with a leaky one, at least in the car"
    hide cmax
    hide sam
    with dissolve
    call screen straightAndNarrow3 with dissolve

label straightAndNarrow3Matsu:
    scene straightAndNarrow3 background with dissolve
    show sam neutral:
        xpos -0.1
    show cmax neutral:
        xpos 0.1
    with dissolve
    sam "Good afternoon dear squatter"
    show jyushimatsu neutral flip with dissolve:
        xpos 0.5
    jyushimatsu "Good afternoon to you as well"
    if not straightAndNarrow3MatsuVisited:
        cmax "It's just my idea Sam, or the shadow lost coloring"
        sam "Maybe he just stayed too long at the sun"
        show jyushimatsu sarcastic flip with dissolve
        jyushimatsu "That's not funny"
        jyushimatsu "I had been an undeterminated but very long all the same time without seeing any light"
        show jyushimatsu sad flip with dissolve
        jyushimatsu "I miss playing baseball..."
        show cmax bored with dissolve
        cmax "Fine fine"
        show cmax neutral with dissolve
        cmax "but why are you now of a different color? As far I can notice with my cute little eyes"
        show jyushimatsu neutral flip with dissolve
        jyushimatsu "Funny rabbit funny"
        jyushimatsu "I have always been like this..."
        jyushimatsu "Maybe you met one of my brothers"
        jyushimatsu "Which color he was?"
        show sam unsure with dissolve
        sam "He was more of a pink hue"
        jyushimatsu "That must be my little brother, *********"
        show sam suspicious with dissolve
        sam "Come again?"
        jyushimatsu "*********"
        "..."
        show jyushimatsu worried flip with dissolve
        jyushimatsu "AH, AH, AH, AH, AH, AH"
        show jyushimatsu sarcastic flip with dissolve
        jyushimatsu "I swear I could said his name before!"
        show sam unsure with dissolve
        sam "And which is your name?"
        jyushimatsu "I'm ***********"
        show cmax thinking with dissolve
        cmax "So, you guys are two brothers with the same name?"
        show jyushimatsu worried flip with dissolve
        jyushimatsu "NO NO"
        jyushimatsu "I could say his name like 5 minutes ago"
        show jyushimatsu worried with dissolve
        jyushimatsu "Also mine!"
        show jyushimatsu worried flip with dissolve
        jyushimatsu "This is bad, bad, bad, bad, bad"
        $ straightAndNarrow3MatsuVisited = True

    jump straightAndNarrow3MatsuTree
    call screen straightAndNarrow3 with dissolve

label straightAndNarrow3Office:
    scene straightAndNarrow2 background with dissolve
    if straightAndNarrow3ScaredSuperball:
        show cmax neutral flip with dissolve:
            xpos 0.4
        cmax "Hey, Sam"
        cmax "Why did you talk to him alone?"
        cmax "You know I love innecessary violence"
        show sam neutral with dissolve:
            xpos 0.0
        sam "I'm sorry little buddy"
        sam "It kinda..."
        sam "You know"
        sam "Felt right just for this occacion"
        cmax "Do you promise you will not do that again?"
        sam "At least not between 6 months and a year"
        cmax "Oh, that's plenty"
        cmax "I would probably forget everything by tomorrow afternoon anyway"
        sam "You crack me up, little buddy"
        hide sam
        hide cmax
        with dissolve
    else:
        show sam neutral with dissolve:
            xpos 0.0
        sam "Do you believe Superball knows something about dimensional rifts Max?"
        show cmax neutral flip with dissolve:
            xpos 0.4
        cmax "Why he should know something about it Sam?"
        sam "You have a point there little buddy"
        if straightAndNarrow3Angela:
            $ straightAndNarrow3ScaredSuperball = True
            sam "Hey, Angela, do you know anything about him?"
            show angela unsure flip with dissolve:
                xpos 0.6
            angela "Superball?"
            show cmax neutral with dissolve
            sam "It's his Secret Service Codename"
            sam "He was a bouncer"
            sam "Secret Service Humor"
            show angela serious flip with dissolve
            angela "That's why they never smile"
            show angela thinking flip with dissolve
            angela "Maybe he was the guy who didn't let me deliver your assignment"
            sam "I was suspecting the same, maybe you could help us summon him"
            show sam unsure with dissolve
            sam "So to speak"
            show angela neutral flip with dissolve
            angela "Oh sure"
            show cmax excited
            show sam neutral
            with dissolve
            cmax "It do involve blood rituals and human sacrifices?"
            show angela happy flip with dissolve
            angela "I wish"
            show angela neutral flip with dissolve
            angela "But it do involve someone else's library card"
            show cmax bored with dissolve
            cmax "Eh, close enough"
            hide angela
            hide sam
            hide cmax
            with dissolve
            angela "Anddddddd"
            play music "audio/sounds/alarm.mp3"
            "ALARM SOUNDS"
            show angela neutral flip with dissolve:
                xpos 0.5
            angela "Here's come the alarm"
            show sam neutral flip with dissolve:
                xpos 0.6
            sam "I didn't knew we had an alarm in the office"
            show cmax neutral flip with dissolve:
                xpos 0.5
            cmax "Everyday we learn something new about ourselves Sam"
            stop music fadeout 3
            show superball neutral with dissolve:
                xpos 0.0
            superball "Ma'am, we already spoke about thi..."
            superball "..."
            superball "This is extremely worrisome"
            play music "audio/music/03 Good Sam, Bad Max.mp3"
            show screen notification("Good Sam, Bad Max - Jared Emerson-Johnson")
            show sam neutral with dissolve:
                xpos 0.2
            sam "Max, Angela, can you wait outside for a moment?"
            sam "I need to have a conversation with Superball"
            show sam serious flip with dissolve
            sam "Alone"
            superball "This is more than extremely worrisome"
            show cmax surprise flip with dissolve
            cmax "Wait, what?"
            cmax "Ah?"
            show angela scared flip with dissolve
            angela "Uh, ok"
            angela "We'll wait outside"
            hide angela
            hide cmax
            with dissolve
            angela "Come on Sam's little buddy"
            sam "So..."
            sam "Superball..."
            show sam sarcastic flip with dissolve
            sam "How that time traveling is going?"
            superball "Oh dear"
            hide sam
            hide superball
            with dissolve
            scene straightAndNarrow3 cinematic with dissolve
            angela "So, Max"
            angela "Does he always do this?"
            cmax "..."
            angela "Does he sometimes do this?"
            cmax "..."
            angela "Does he rarely do this?"
            cmax "..."
            show angela thinking flip:
                xpos 0.5
            with dissolve
            angela "This is the first he does this, uh?"
            show cmax angrySurprised flip:
                xpos 0.3
            with dissolve
            cmax "I cannot BELIEVE IT!"
            cmax "I'm the bad cop in the interrogations!"
            cmax "What's he trying to do?!"
            cmax "..."
            show cmax surprise flip with dissolve
            cmax "AH!"
            cmax "I know!"
            show cmax angrySurprised with dissolve
            cmax "He's trying to impress you!"
            show angela neutral flip with dissolve
            angela "Nah"
            cmax "You are the only difference in this situation!"
            cmax "You relationship breaking harpy!"
            show angela unsure flip with dissolve
            angela "It's nice of you to believe I have any power on this"
            angela "..."
            show angela thinking flip with dissolve
            angela "If it make you feel any better"
            angela "I can leave and you can tell Sam I had an emergency at the police headquarters"
            stop music
            show cmax surprise with dissolve
            cmax "What?"
            play music "audio/music/Life is for Living Bass.mp3"
            cmax "Really?"
            show angela well flip with dissolve
            angela "To be honest, my lack of opportunity in this whole situation is making me anxious"
            cmax "Wait"
            show cmax thinking with dissolve
            cmax "Do you really have..."
            show angela neutral flip with dissolve
            angela "You could say that"
            stop music
            play sound "audio/sounds/punch1.mp3"
            "* THUMP *"
            show cmax excited flip
            show angela surprised flip
            with dissolve
            angela "UH?!!"
            cmax "What is happening inside?"
            cmax "Wait..."
            cmax "Is he...."
            play sound "audio/sounds/shot.mp3"
            show cmax excited flip:
                xpos -0.1
            show angela surprised flip:
                xpos 0.1
            with dissolve
            pause(0.5)
            play sound "audio/sounds/crashwall.mp3"
            pause(0.5)
            angela "EHHHHHHHHHHHHHHHHHHHHHHH"
            cmax "He has the size to pull it off though"
            angela "I don't think he's doing it for that"
            play music "audio/music/Life is for Living Intruments.mp3"
            show angela proud flip:
                xpos 0.1
            with dissolve
            angela "But he's impressing me"
            show cmax excited with dissolve
            cmax "Me too"
            show angela neutral flip:
                xpos 0.5
            show cmax neutral flip:
                xpos 0.3
            show sam neutral:
                xpos 0.0
            with dissolve
            sam "Ah, that felt nice"
            play sound "audio/sounds/applause.mp3"
            "CLAP! CLAP! CLAP! CLAP! CLAP!"
            sam "Sorry for the wait"
            sam "I hope you weren't too unconfortable"
            cmax "Not at all"
            angela "Nope, nope"
            show sam happy with dissolve
            sam "That's great"
            show sam neutral with dissolve
            sam "I think I got Superball to stop doing pitstops at the office when we're not there"
            hide cmax with dissolve
            sam "Also I got some information about the dimensional rift that the commissioner told us to investigate"
            sam "He said those were always there"
            angela "Really?"
            sam "Like they are part of the universe always and just never notice them"
            angela "So now those got bigger"
            sam "Probably"
            show sam neutral flip with dissolve:
                xpos 0.1
            cmax "Sam?"
            show cmax excited with dissolve:
                xpos 0.0
            cmax "Did you make him cry?"
            show sam unsure flip with dissolve
            sam "Ah..."
            sam "Yes?"
            cmax "SNIFF!"
            cmax "I'm so proud!"
            show sam surprised flip with dissolve
            sam "No, Max, not in front of her!"
            angela "I don't mind"
            hide sam
            hide cmax
            hide angela
            with dissolve
            scene straightAndNarrow3 background with dissolve
            play music "audio/music/02 The Office.mp3" fadeout 2 fadein 1
        else:
            show sam unsure with dissolve
            sam "Still, I want to have a conversation with him but he never appears in front of us since..."
            hide sam with dissolve
            sam "the explosion"
            show cmax annoyed flip with dissolve
            cmax "Why the temperature just dropped right now?"
            sam "Let's go pal"
            show cmax annoyed with dissolve
            cmax "This wasn't funny"
            show cmax angry with dissolve
            cmax "I want a refund!"
            hide cmax with dissolve
    call screen straightAndNarrow3 with dissolve

label straightAndNarrow3Tardis:
    if straightAndNarrow3Angela:
        show cmax thinking flip zorder 1 with dissolve:
            xpos 0.4
        cmax "What is this I'm feeling inside me?"
        cmax "It's like I wanna strangle her"
        show angela neutral flip zorder 0 with dissolve:
            xpos 0.6
        cmax "But at the same time I'm not doing it because Sam would be..."
        cmax "sad?"
        cmax "Why it hurts so much?"
        show angela happy flip with dissolve
        angela "You really care about him"
        hide angela with dissolve
        show cmax surprise with dissolve
        angela "I really hope you will be together for a long time"
        hide cmax with dissolve
        cmax "Wait, wait, what did you say?"
    else:
        angela "Hello??"
        show sam unsure flip with dissolve:
            xpos 0.3
        sam "Max??"
        sam "Did we forget something?"
        show cmax neutral with dissolve:
            xpos 0.1
        cmax "Besides my boxing glove and your sense fashion, no, I don't think so..."
        sam "Mmmm"
        angela "Hey! The car has..."
        angela "Trapped me in the..."
        show sam neutral flip with dissolve:
            xpos 0.0
        show cmax neutral flip with dissolve:
            xpos 0.3
        sam "Wait"
        play sound "audio/sounds/crashwall.mp3"
        "* CRASH *"
        sam "Are you alright?"
        show angela neutral with dissolve:
            xpos -0.1
        angela "Yes... I'm..."
        stop music
        play sound "audio/sounds/record-scratch.mp3"
        show sam surprised flip:
            xpos 0.2
        show angela surprised
        with dissolve
        "..."
        cmax "Ehh...."
        "..."
        show cmax neutral flip with dissolve:
            xpos 0.5
        cmax "Sam please, you just rescued a girl it's no big deal"
        sam "Angela?"
        angela "Sam?"
        play music "audio/music/Life Is for Living.mp3"
        show sam happy flip
        show angela happy
        show screen notification("Life is for Living - Ivy-Rose Lyon ft. Maja Norming")
        with dissolve
        angela "What a coincidence!"
        angela "The commissioner never told me you were part of the Freelance Police!"
        show angela thinking
        with dissolve
        angela "I mean, he doesn't have a reason to"
        show angela happy
        with dissolve
        angela "But at least he could told me your names"
        show sam neutral flip with dissolve
        sam "The commissioner?"
        show angela neutral
        with dissolve
        sam "Are you working with the police?"
        angela "Yeah..."
        angela "I open doors..."
        angela "Deliver or retrieve documents..."
        angela "Once they ask me to be bait"
        show sam happy flip with dissolve
        sam "Those evil doers had no idea with who were messing with"
        angela "I have a taser"
        angela "I had to use it directly in their b.."
        stop music
        play sound "audio/sounds/record-scratch.mp3"
        show cmax annoyed flip with dissolve
        cmax "EJEM!"
        show sam neutral with dissolve
        cmax "Sam???"
        sam "Oh, sorry little buddy"
        sam "This is Angela, she's an old friend of mine"
        show sam neutral flip with dissolve
        sam "Angela, this is Max"
        sam "He's my partner at the"
        show cmax angrySurprised flip with dissolve
        cmax "An OLD friend of yours?"
        show sam neutral with dissolve
        cmax "An old GIRL friend of yours?"
        cmax "An old girlfriend of yours I DON'T KNOW?"
        sam "We met each other at Flight Stewardess School"
        show cmax surprise flip with dissolve
        cmax "What"
        play music "audio/music/Life is for Living Intruments.mp3" fadein 1
        angela "We lost contact after I had to drop out for a family emergency"
        show sam neutral flip with dissolve
        sam "Everything is ok now, I hope"
        show angela thinking
        with dissolve
        angela "I mean, dad have been pushing daisies for quite a while"
        show angela proud
        with dissolve
        angela "But the culprit recieved justice at least"
        show sam sarcastic flip with dissolve
        sam "I cannot begin to imagine how was that"
        show angela neutral
        with dissolve
        angela "I recieved a couple of offers from the mafia, but I decided to accept the commissioner offer instead"
        angela "I want to stay at least in denial that I'm in the side of justice"
        show sam neutral flip with dissolve
        sam "That why we went freelance with my little buddy"
        sam "There's certain things I just couldn't compromise"
        show angela happy
        with dissolve
        angela "Like shooting your gun randomly when trying to solve a problem?"
        sam "After all this time without talking with each other and you still know me so well"
        show angela neutral
        with dissolve
        angela "The commissioner doesn't want to give me a gun"
        angela "But I'm going to get one someday"
        show cmax angrySurprised flip with dissolve
        cmax "EJEM!"
        show sam neutral with dissolve
        show cmax aww flip with dissolve
        cmax "I cannot believe I'm the one who is saying this but"
        show cmax angrySurprised flip with dissolve
        cmax "SAM?!"
        show sam surprised
        show angela happy
        with dissolve
        cmax "THE CASE?!"
        show sam neutral with dissolve
        sam "I'm sorry little buddy"
        sam "It's just..."
        sam "It's not everyday you find a good friend from your recent to far past"
        show angela neutral
        with dissolve
        angela "He's right, I'm just distracting you"
        show sam neutral flip with dissolve
        sam "Ah? No, of course not"
        sam "Do you have free the afternoon?"
        sam "You can help us with the case if you want"
        cmax "No"
        angela "Ok, I don't have anything better to do"
        hide sam
        hide angela
        with dissolve
        show cmax surprise flip with dissolve
        cmax "WAIT!"
        show cmax surprise with dissolve
        cmax "SAM!?"
        hide cmax with dissolve
        $ straightAndNarrow3Angela = True
        play music "audio/music/02 The Office.mp3" fadeout 2 fadein 1
    call screen straightAndNarrow3 with dissolve


label changeSceneToDimensionalRift3:
    jump dimensionalRift3Intro