define museum3FirstTime = False 
define museum3AngelaNotCar = False
define museum3AngelaBack = False
define museum3AngelaStays = False

define museum3MaddieTalk = False

define museum3Changelings = 1
define museum3Superball = 1
define museum3ChangelingVoice = 1

label museum3Start:
    scene museum3 background with dissolve
    if not museum3FirstTime:
        play sound "audio/sounds/knock_museum.mp3"
        "*knock knock knock knock*"
        show papierwaite neutral flip zorder 1 with dissolve:
            xpos 0.4
        papierwaite "I'm coming!!"
        hide papierwaite with dissolve
        play sound "audio/sounds/door_open_museum.mp3"
        "*skreeeekkk*"
        show papierwaite annoyed flip zorder 1 with dissolve:
            xpos 0.4
        papierwaite "Oh"
        papierwaite "It's you"
        play music "audio/music/The Museum of Mostly Natural History.mp3"
        show screen notification("The Museum of Mostly Natural History - Jared Emerson-Johnson")
        show sam neutral:
            xpos -0.1
        show cmax neutral:
            xpos 0.1
        with dissolve
        cmax "That's a warm welcome I have ever heard one"
        sam "I hope we're not interrupting anything though"
        show norrington neutral flip zorder 2 with dissolve:
            xpos 0.4
        norrington "No, not really"
        show papierwaite annoyed 
        show norrington neutral
        with dissolve
        papierwaite "Well, there's a giant colored hole in the fabric of reality which appeared at my library"
        show papierwaite neutral flip 
        show norrington neutral flip 
        with dissolve
        norrington "But it would be safe to assume you guys have something to do with it"
        cmax "More or less"
        sam "The commissioner asked us to investigate dimension destroying kind of annomalies"
        sam "We're here because a weird shadowy creature with yellow hues told us he was here a couple of hours before"
        norrington "Oh, so that's what happened with *********** then"
        show sam unsure with dissolve
        sam "Do you know his name?"
        norrington "It's seems something on reality changed that I cannot pronounce his name anymore"
        show sam neutral with dissolve
        sam "It must be pretty severe if it's affecting you, since you are a elder god and all"
        norrington "I'm sadly in such weakened state I'm as affected by the changing currents of reality as you mortals are"
        show cmax aww with dissolve
        cmax "There it go to figure out their names"
        sam "We do have their hues though"
        show cmax neutral
        show papierwaite annoyed
        show norrington neutral
        with dissolve
        papierwaite "You go and talk with their brother, he's at the library"
        papierwaite "I'll be at my office, I need to cancel some... activities..."
        hide papierwaite
        hide norrington
        with dissolve
        cmax "Activities"
        sam "Something else to figure out while we find out about the colored holes then"
        show cmax ohyeah with dissolve
        cmax "The plot thickens!"
        $ museum3FirstTime = True
        hide cmax
        hide sam
        with dissolve
    else:
        play music "audio/music/The Museum of Mostly Natural History.mp3"

label museum3Back:
    scene museum3 background
    call screen museum3 with dissolve

label museum3Desoto:
    if straightAndNarrow3Angela:
        show sam neutral flip:
            xpos 0.1
        show cmax neutral flip:
            xpos 0.4
        with dissolve
        sam "Now I'm thinking about it..."
        cmax "Don't do that, it's bad for your health"
        show sam neutral with dissolve
        sam "Where's Angela?"
        show cmax surprise flip with dissolve
        cmax "What?!"
        cmax "She's not here?"
        show sam suspicious with dissolve
        sam "Max..."
        show cmax bored flip with dissolve
        cmax "It's not my fault!" 
        cmax "How you dare to think is my fault!"
        sam "This is not a good look"
        cmax "Which look?"
        $ museum3AngelaNotCar = True
        menu:
            "We better go to pick her up":
                hide sam with dissolve
                sam "I hope she doesn't believe something terrible about me"
                hide cmax with dissolve
                cmax "Hey!"
                cmax "What's about me?"
                play music "audio/music/02 The Office.mp3" fadeout 2 fadein 1
                $ museum3AngelaBack = True
                jump straightAndNarrow3Back
            "To the Week without Sleep Memorial Park" if library3IchimatsuTalks == 4:
                jump library3ToTheMemorialPark
            "Ehhh... maybe later":
                show cmax neutral with dissolve
                cmax "Too much for care about her"
                hide sam with dissolve
                sam "It's not that Max..."
                hide cmax with dissolve
                cmax "It's not that Max"
                jump museum3Back

    else:
        show sam neutral flip:
            xpos 0.1
        show cmax neutral flip:
            xpos 0.4
        with dissolve
        cmax "Where we going Sam?"
        menu:
            "Back to the Street":
                show sam neutral with dissolve
                sam "Maybe there's something else we can find there"
                hide cmax with dissolve
                cmax "Not if I do first!"
                hide sam with dissolve
                play sound "audio/sounds/car_driveoff.mp3"
                pause 1
                play music "audio/music/02 The Office.mp3" fadeout 2 fadein 1
                jump straightAndNarrow3Back
            "To the Week without Sleep Memorial Park" if library3IchimatsuTalks == 4:
                label library3ToTheMemorialPark:
                    sam "To the park to find a building with a weird red shadow!"
                    hide cmax
                    hide sam
                    with dissolve
                    play sound "audio/sounds/car_driveoff.mp3"
                    "Car starts"
                    play sound "audio/sounds/electricity.mp3"
                    "Sounds of electricity"
                    play sound "audio/sounds/tires-squeal.mp3"
                    pause 1
                    show sam neutral:
                        xpos 0.4
                    show cmax angrySurprised flip:
                        xpos 0.1
                    with dissolve
                    cmax "What just happened?"
                    sam "There's a barrier which impide us to go directly from here"
                    show sam neutral flip
                    show cmax neutral
                    with dissolve
                    sam "Not even the Demon possesed Desoto can go there"               
                    cmax "That's bad, right?"
                    sam "Yes!"
                    sam "Yesterday it went around there to pick up some prius"
                    sam "So, I don't know why it can't go there anymore"
                    cmax "I would say it's embarrased of something"
                    cmax "But I know its less shameful than I'm"
                    sam "That one way to say it little buddy"
                    jump museum3Back
            "Nowhere":
                sam "Just considering options"
                cmax "Meandering around is a good technique"
                cmax "I use it all the time"
                jump museum3Back

label museum3Madie:
    if not museum3MaddieTalk:
        $ museum3MaddieTalk = True
        show sam neutral:
            xpos 0.4
        show cmax neutral flip:
            xpos 0.3
        with dissolve
        sam "The new place is really big"
        cmax "But still has the same weird smell"
        show maddie neutral:
            xpos -0.1
        with dissolve
        maddieB "Hey!"
        maddieB "I like smell"
        show cmax isAdorable flip
        with dissolve
        cmax "!!!!"
        show sam neutral flip
        with dissolve
        sam "Oh.."
        sam "Nice to meet you, young lady"
        show cmax isAdorable flip:
            xpos 0.27
        with dissolve
        cmax "{size=-10}She's so small{/size}"
        sam "We're Sam and Max, freelance police"
        sam "We're investigating some dimension space annomalies"
        maddieB "Giant hole... library?"
        sam "Exactly!"
        sam "Do you know anything about it?"
        maddieB "Ah..."
        maddieB "No!"
        show cmax isAdorable flip:
            xpos 0.25
        with dissolve
        cmax "{size=-10}She's so bad at lying I want to squeeze her{/size}"
        sam "Did you said?"
        maddieB "Eh..."
        maddieB "Shadows near... holes..."
        maddieB "They... like... same stuff as..."
        sam "Oh, so are saying they are part of a nearest hole..."
        sam "Or another hole..."
        maddieB "Made of the same!"
        show cmax isAdorable flip:
            xpos 0.2
        with dissolve
        cmax "Let me pet you, little precious..."
        show sam neutral flip:
            xpos 0.3
        with dissolve
        sam "No Max, you cannot pet little kids without their consent"
        play sound "audio/sounds/crash.ogg"
        show sam neutral:
            xpos 0.3
        hide cmax
        with dissolve
        pause 1.0
        sam "They might bite you"
        show sam neutral flip:
            xpos 0.3
        with dissolve
        sam "We have to leave, thanks for the information miss"
        hide sam
        with dissolve
        sam "Now Max, please, you know what happened at the Violet Grapevine school for the musically enabled that one time..."
        cmaxSpirit "Well, that was weird"
        show maddie neutral flip
        with dissolve
        maddieB "*I was more scared about talking about you by mistake*"
        cmaxSpirit "Nah.."
        cmaxSpirit "Don't worry Maddie, we're going to find it before they get to know anything about it"
        maddie "*He's big*"
        cmaxSpirit "Why, yes, he's big"
        show maddie smile flip
        with dissolve
        maddie "*Can I pet him?*"
        cmaxSpirit "No"
        show maddie neutral flip
        with dissolve
        maddie "Awww...."
        cmaxSpirit "He really dislike pets"
        hide maddie with dissolve
    else:
        show sam neutral flip:
            xpos 0.4
        show cmax thinking flip:
            xpos 0.3
        show maddie neutral:
            xpos -0.1
        with dissolve
        cmax "I have a question now"
        maddie "Question?"
        cmax "How do we know your name now if you never told us?"
        sam "Max, we got over this already"
        sam "If the player knows her name, we know her name"
        sam "I already explained you that"
        cmax "Ok..."
        show cmax annoyed flip with dissolve
        cmax "But who said it?"
        show maddie angry with dissolve
        maddie "*Not telling*"
        sam "She's not telling..."
        show cmax aww flip with dissolve
        cmax "I thought we had a clue"
        sam "The 4th wall is a harsh mistress"
        hide cmax
        hide sam
        hide maddie
        with dissolve
    jump museum3Back

label museum3Planetarium:
    show sam neutral:
        xpos 0.0
    show cmax neutral flip:
        xpos 0.4
    with dissolve
    sam "That up there is the Planetarium"
    show cmax thinking flip with dissolve
    cmax "I think I was there before???"
    sam "As a brain in a jar, more or less"
    show cmax annoyed flip with dissolve
    cmax "More or less?"
    sam "More, actually"
    show cmax neutral flip with dissolve
    cmax "I don't wanna go there"
    sam "That's something I can respect"
    hide sam
    hide cmax
    with dissolve
    jump museum3Back

label museum3Paperwaite:
    show sam neutral flip:
        xpos 0.4
    show cmax neutral flip:
        xpos 0.3
    with dissolve
    sam "Helouuu"
    show papierwaite angry:
        xpos 0.0
    with dissolve
    papierwaite "What are you two doing?"
    papierwaite "I already told you I need to make some arrangements before I can help you with anything"
    sam "It's only a couple of short questions"
    show papierwaite annoyed with dissolve
    papierwaite "Those never are"

label museum3PaperwaiteMenu:
    menu: 
        "What's those arrangements for?" if museum3Changelings == 1:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite neutral
            with dissolve
            sam "It's something you need to do eventually I guess"
            show papierwaite explaining
            with dissolve
            papierwaite "It's not something I need to do exactly"
            sam "Dr. Norrington then?"
            cmax "It must be difficult to do when you are a talking tumor on someone else chest"
            show norrington neutral:
                xpos 0.0
            with dissolve
            norrington "Please, don't even joke about it"
            show papierwaite neutral
            with dissolve
            papierwaite "They have found ways to do it without me third wheeling the whole time"
            papierwaite "I'm graceful for that"
            show papierwaite annoyed
            with dissolve
            papierwaite "But I have to anyway make all the coordination and what not"
            sam "Wait"
            show sam sarcastic flip with dissolve
            sam "This is a date"
            show cmax excited flip with dissolve
            cmax "There's other elders gods on earth for you to date"
            show papierwaite explaining
            with dissolve
            papierwaite "Of course not!"
            papierwaite "The great and powerful Yog Soggoth is the only elder god still on earth!"
            norrington "Yes... and... I really don't want them so see me like this"
            norrington "It's a bit embarrasing"
            $ museum3Changelings = museum3Changelings + 1
        "If it's not an elder god, what is it?" if museum3Changelings == 2:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite neutral
            show norrington neutral:
                xpos 0.0
            with dissolve
            sam "Another fish based monstruosity perhaps?"
            norrington "No, no, no"
            norrington "She's... she's... well"
            show cmax thinking flip with dissolve
            cmax "An enthusiast of classic japanese paintings?"
            norrington "A changeling"
            sam "What's that?"
            norrington "The spirit of a fairy that has replaced the spirit of the human in its human body"
            norrington "The fairies that do the change"
            show cmax ohyeah flip with dissolve
            cmax "Ohhhhhhhhhhh"
            norrington "Bring the original human spirit as fuel for their houses, while they leave in their place an old fairy who's ready to die"
            norrington "Since humans live for a very short time compared to the fairies, a human life span is more than enough for them"
            sam "Ok... so..."
            sam "They are normal human bodies walking around zombie like with the spirit of tinkerbell grandmother from her fathers side"
            show cmax neutral flip
            with dissolve
            cmax "Do they look exactly like humans?"
            norrington "Yes, yes, of course"
            norrington "Some have some, well, more specific minor changes in the looks of their host body"
            norrington "But they look exactly like humans, you will never figure out unless you know what to search for"
            sam "Is it there any techniques you can give us to figure out who's a changeling?"
            norrington "Most of the time is a waste of time unless you really need one"
            norrington "But one way to do it is..."
            norrington "Ask them about something they like and they will talk about about it for 2 hours and a half without preparation whatsoever"
            show papierwaite explaining
            with dissolve
            papierwaite "My record was 2 hours, 36 minutes and 46 seconds exactly"
            $ museum3Changelings = museum3Changelings + 1
        "Wait, Papierwaite is a changeling?" if museum3Changelings == 3:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite neutral
            show norrington neutral:
                xpos 0.0
            with dissolve
            norrington "It's always the one you least expect"
            norrington "Until you read anything about it and then you figure out at least 30%% of the people you know probably is"
            show sam unsure flip
            with dissolve
            sam "Has that anything to do with you been stuck in his chest?"
            norrington "Yes, it has everything to do with it"
            norrington "I can share this body with him because his spirit is not that glued to this body"
            norrington "If it were an actual human which summoned me, I would probably still be in our dimension"
            norrington "But, in a way, humans with humans spirits have basically 0 chance to summon me"
            norrington "Because they are usually unable to obtain the required knowledge"
            show papierwaite annoyed
            with dissolve
            papierwaite "I have told him several times this has nothing to do with it"
            norrington "You read about obscure incantations from books that took you 20 years to track down"
            norrington "For fun"
            show papierwaite explaining
            with dissolve
            papierwaite "I just take my job as your follower very seriously"
            norrington "That incantation had nothing to do with me"
            norrington "You just like to know about incantations"
            show cmax neutral
            show sam neutral flip
            with dissolve
            cmax "I feel like an artifact here"
            sam "Yeah, but we don't need to always be the ones carrying the conversations"
            show cmax neutral flip
            with dissolve
            cmax "Eh, I just don't like it"
            $ museum3Changelings = museum3Changelings + 1
        "Do you know about a Voice from Nowhere?" if library3IchimatsuTalks > 2 and museum3ChangelingVoice == 1:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite doubts
            hide norrington
            with dissolve
            papierwaite "It's the first time I heard that concept"
            papierwaite "Where did you heard it?"
            sam "The Purple Shadow from the Library says you have a Voice from Nowhere with you, or something"
            show papierwaite neutral
            show norrington neutral:
                xpos 0.0
            with dissolve
            norrington "Oh.... ********* is talking about me"
            norrington "He can heard me when I try to talk on Papierwaite's Brain in his presence"
            norrington "I guess that's why he's saying I'm a voice from nowhere"
            cmax "I think because the Visual Novel Writer forgot how to write a word!"
            norrington "That also"
            papierwaite "Why are you asking about it?"
            sam "The Purple one says his brother the red one knows how to solve this"
            sam "He only knows they need a 'Changeling without a Voice from Nowhere'"
            show papierwaite annoyed with dissolve
            papierwaite "I knew it"
            $ museum3ChangelingVoice = 2
        "You knew what?!" if museum3ChangelingVoice == 2:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite explaining
            hide norrington
            with dissolve
            papierwaite "That they need a body to trap anything they workship"
            show cmax thinking flip with dissolve
            cmax "How do you know they are workshiping anything?"
            show papierwaite annoyed with dissolve
            papierwaite "..."
            show papierwaite neutral with dissolve
            papierwaite "I'm a cult member"
            show cmax ohyeah flip with dissolve
            cmax "oh..."
        "Have you heard about Superball?" if straightAndNarrow3ScaredSuperball == False:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite neutral
            show norrington neutral:
                xpos 0.0
            with dissolve
            norrington "Why are you asking about him?"
            sam "You see..."
            sam "It feels like he's spending way too much time in the office for my liking"
            papierwaite "Isn't still the oval office?"
            show sam suspicious flip
            with dissolve
            sam "Yes, but it was before my office"
            papierwaite "We're not friends, so we haven't met again since Sybil children was born"
            papierwaite "Do you think he might know something about this dimensional rifts?"
            show sam neutral flip
            with dissolve
            sam "I mean, I'm fairly sure he knows a lot about time traveling"
            sam "It wouldn't be too much of a stretch to believe he knows about dimensional rifts"
            cmax "I don't know where he got that idea"
            show sam unsure flip
            with dissolve
            sam "Oh, remember Max"
            show cmax thinking
            with dissolve
            sam "While we were also traveling in time, we chat with 2 versions of him separated by time frames way too apart to not be suspicious"
            cmax "..."
            show cmax neutral
            with dissolve
            cmax "I don't remember that"
            show sam neutral flip
            with dissolve
            sam "Oh, right, you shouldn't remember that any way"
            show cmax neutral flip
            with dissolve
            sam "But that happened"
            papierwaite "Ok...."
            papierwaite "Just tell me next time if you find something interesting talking to him"
        "I did have a chat with Superball... mostly" if straightAndNarrow3ScaredSuperball == True and museum3Superball == 1:
            show sam neutral flip
            show cmax neutral flip
            show papierwaite neutral
            hide norrington
            with dissolve
            papierwaite "What did he said?"
            sam "Apart of promise me several times he will be not going to camp at our office again"
            show cmax excited flip with dissolve
            cmax "And that was AWESOME"
            sam "He said something among the lines of..."
            show sam unsure flip with dissolve
            sam "Those holes have always existed"
            show papierwaite doubts with dissolve
            papierwaite "Like a long standing failure of our existence?"
            sam "More like those holes were always there, but really small"
            papierwaite "Then those holes are not really the problem"
            cmax "Come again?"
            papierwaite "More like something else is affecting the holes and that's our real problem"
            cmax "How do you know that?"
            show norrington neutral with dissolve:
                xpos 0.0
            norrington "About 5 years ago he got obssesed with dimensional stability and read everything about it"
            show papierwaite excited with dissolve
            papierwaite "I knew some day will paid off!"
            sam "So, this theory has some legs to stand on?"
            show papierwaite explaining with dissolve
            papierwaite "Most of the knowledge about dimensions is mostly theories which may be true"
            show papierwaite neutral with dissolve
            papierwaite "One theory says dimensions have always small imperfections which can be made worse by the powers of beings from another place"
            sam "Like Dr. Norrington"
            norrington "Ah, yes, but, for just to create this holes, it has to be way less powerful than my real form"
            papierwaite "Yog Soggoth's real form would have destroyed the fabric completely and decend our plane to its pure form"
            papierwaite "CHAOS"
            sam "Wait"
            sam "Did you summon him fully knowing that just his presence will basically end the world?"
            show papierwaite excited with dissolve
            papierwaite "That was the idea!"
            cmax "Good to know!"
            $ museum3Superball = museum3Superball + 1
        "To Recap" if museum3ChangelingVoice == 2 and museum3Superball > 1 and museum3MaddieTalk:
            show sam explain flip
            show cmax neutral flip
            show papierwaite neutral
            hide norrington
            with dissolve
            sam "Superball says the holes always existed"
            sam "You say the only way that holes are getting bigger is because some super natural being is trying to conquer the earth"
            sam "And that little girl says that the shadows are from the holes"
            show norrington neutral with dissolve:
                xpos 0.0
            norrington "Maddie said that?"
            show cmax thinking flip with dissolve
            cmax "Yes?"
            show sam unsure flip with dissolve
            sam "You know her?"
            norrington "Of course"
            norrington "She's a changeling"
            norrington "She's semi verbal though, so every single time she comes to the museum, I end up reading her brain when she needs something"
            show papierwaite explaining with dissolve
            papierwaite "I have told her to bring a notebook"
            show papierwaite neutral with dissolve
            papierwaite "She's very expressive in writing form"
            show sam neutral flip with dissolve
            sam "I know it's your job to talk with people visiting the museum, but..."
            show sam serious flip with dissolve
            sam "This feels really bad"
            show papierwaite angry with dissolve
            papierwaite "Why?!"
            show cmax neutral flip with dissolve
            cmax "You are a cult member"
            show papierwaite neutral with dissolve
            papierwaite "Oh"
            show sam neutral flip with dissolve
            sam "Anyway..."
            show sam explain flip with dissolve
            sam "It seems a powerful spirit came to earth"
            sam "Opened those dimensions holes to create the shadows"
            sam "So they could find a body to possess"
            sam "And only can be a Changeling that cannot be already possesed by something else"
            norrington "This spirit cannot be too strong yet"
            norrington "The *********** cannot move from their position"
            show cmax ohyeah with dissolve
            cmax "Random thought"
            show cmax neutral with dissolve
            cmax "What about we find a changedlily without alucinations as a bait" 
            show papierwaite surprised
            show norrington surprised
            with dissolve
            cmax "so the shadows will guide us to their boss"
            show sam neutral flip with dissolve
            sam "That's a plan"
            sam "We only need something else to trap the spirit which is not the changeling"
            show cmax neutral flip with dissolve
            sam "Any idea you two?"
            stop music
            "..."
            show sam unsure flip with dissolve
            sam "Why so nervious..."
            show norrington neutral 
            show papierwaite doubts 
            with dissolve
            papierwaite "I... "
            extend "need... "
            extend "to... "
            extend "check... "
            extend "some... "
            extend "books... "
            extend "to find... "
            extend "something..."
            show cmax excited flip with dissolve
            cmax "Oh, good!"
            show cmax neutral with dissolve
            cmax "Now we need to find a switchling without inner voices!"
            show cmax neutral flip with dissolve
            cmax "Do you know one?!"
            "..."
            show sam serious flip 
            show papierwaite surprised
            show norrington surprised
            show cmax angry flip
            with dissolve
            sam "The doctor's date doesn't have voices, isn't it?"
            cmax "You already knew everything Sam just said!"
            show papierwaite annoyed
            show norrington neutral
            with dissolve
            norrington "Her soul is so fragile, I don't want to involve her on this"
            show sam explain flip with dissolve
            sam "At least let us ASK her"
            norrington "I... "
            extend "I..."
            pause 2
            $ renpy.set_return_stack([])
            return
        "See you later!" :
            hide papierwaite
            hide norrington
            with dissolve
            papierwaite "Fine fine..."
            papierwaite "Just let me finish with this call..."
            jump museum3Back


    jump museum3PaperwaiteMenu


label museum3Matsu:
    jump library3Start
                
