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
        "*knock knock knock knock*"
        papierwaite "I'm coming!!"
        "skreeeekkk"
        papierwaite "Oh"
        papierwaite "It's you"
        cmax "That's a warm welcome I have ever heard one"
        sam "I hope we're not interrupting anything though"
        norrington "No, not really"
        papierwaite "Well, there's a giant colored hole in the fabric of reality which appeared at my library"
        norrington "But it would be safe to assume you guys have something to do with it"
        cmax "More or less"
        sam "The commissioner asked us to investigate dimension destroying kind of annomalies"
        sam "We're here because a weird shadowy creature with yellow hues told us he was here a couple of hours before"
        norrington "Oh, so that's what happened with *********** then"
        sam "Do you know his name?"
        norrington "It's seems something on reality changed that I cannot pronounce his name anymore"
        sam "It must be pretty severe if it's affecting you, since you are a elder god and all"
        norrington "I'm sadly in such weakened state I'm affected by the changing currents of reality as you mortals are"
        cmax "There it go to figure out their names"
        sam "We do have their hues though"
        papierwaite "You go and talk with their brother, he's at the library"
        papierwaite "I'll be at my office, I need to cancel some... activities..."
        cmax "Activities"
        sam "Something else to figure out while we find out about the colored holes then"
        cmax "The plot thickens..."
        $ museum3FirstTime = True
    call screen museum3 with dissolve

label museum3Desoto:
    if straightAndNarrow3Angela:
        sam "Now I'm thinking about it..."
        cmax "Don't do that, it's bad for your health"
        sam "Where's Angela?"
        cmax "What?!"
        cmax "She's not here?"
        sam "Max..."
        cmax "Uh?"
        cmax "It's not my fault!" 
        cmax "How you dare to think is my fault!"
        sam "This is not a good look"
        cmax "Which look?"
        $ museum3AngelaNotCar = True
        menu:
            "We better go to pick her up":
                sam "I hope she doesn't believe something terrible about me"
                cmax "Hey!"
                cmax "What's about me?"
                play music "audio/music/02 The Office.mp3" fadeout 2 fadein 1
                $ museum3AngelaBack = True
                jump straightAndNarrow3Back
            "To the Week without Sleep Memorial Park" if library3IchimatsuTalks == 4:
                jump library3ToTheMemorialPark
            "Ehhh... maybe later":
                cmax "Too much for care about her"
                sam "It's not that Max..."
                cmax "It's not that Max"
                jump museum3Start

    else:
        cmax "Where we going Sam?"
        menu:
            "Back to the Street":
                sam "Maybe there's something else we can find there"
                cmax "Not if I do first!"
                play music "audio/music/02 The Office.mp3" fadeout 2 fadein 1
                jump straightAndNarrow3Back
            "To the Week without Sleep Memorial Park" if library3IchimatsuTalks == 4:
                label library3ToTheMemorialPark:
                    sam "To the park to find a building with a weird red shadow!"
                    "Car starts"
                    "Sounds of electricity"
                    cmax "What just happened?"
                    sam "There's a barrier which impide us to go directly from here"
                    sam "Not even the Demon possesed Desoto can go there"
                    cmax "That's bad, right?"
                    sam "Yes!"
                    sam "Yesterday it went around there to pick up some prius"
                    sam "So, I don't know why it can't go there anymore"
                    cmax "I would say it's embarrased of something"
                    cmax "But I know its less shameful than I'm"
                    sam "That one way to say it little buddy"
                    jump museum3Start
            "Nowhere":
                sam "Just considering options"
                cmax "Meandering around is a good technique"
                cmax "I use it all the time"
                jump museum3Start

label museum3Madie:
    if not museum3MaddieTalk:
        $ museum3MaddieTalk = True
        sam "The new place is really big"
        cmax "But still has the same weird smell"
        maddieB "Hey!"
        maddieB "I like that smell"
        cmax "!!!!"
        sam "Oh.."
        sam "Nice to meet you, young lady"
        cmax "{size=-10}She's so small{/size}"
        sam "We're Sam and Max, freelance police"
        sam "We're investigating some dimension space annomalies"
        maddieB "Like the giant colored hole in the library?"
        sam "Exactly!"
        sam "Do you know anything about it?"
        maddieB "Ah..."
        maddieB "No!"
        cmax "{size=-10}She's so bad at lying I want to squeeze her{/size}"
        sam "Did you said?"
        maddieB "Eh..."
        maddieB "You know, those shadows which are near to the holes..."
        maddieB "They are... like... made of the same stuff as them..."
        sam "Oh, so are saying they are part of a nearest hole..."
        sam "Or another hole..."
        maddieB "Made of the same!"
        cmax "Let me pet you, little precious..."
        sam "No Max, you cannot pet little kids without their consent"
        sam "They might bite you"
        sam "We have to leave, thanks for the information miss"
        sam "Now Max, please, you know what happened at the school that one time..."
        cmaxSpirit "Well, that was weird"
        maddieB "*I was more scared about talking about you by mistake*"
        cmaxSpirit "Nah.."
        cmaxSpirit "Don't worry Maddie, we're going to find it before they get to know anything about it"
        maddie "*He's big*"
        cmaxSpirit "Why, yes, he's big"
        maddie "*Can I pet him?*"
        cmaxSpirit "No"
        maddie "Awww...."
        cmaxSpirit "He really dislike pets"
    else:
        cmax "I have a question now"
        maddie "A question?"
        cmax "How do we know your name now if you never told us?"
        sam "Max, we got over this already"
        sam "If the player knows her name, we know her name"
        sam "I already explained you that"
        cmax "Ok..."
        cmax "But who said it?"
        maddie "*Not telling*"
        sam "She's not telling..."
        cmax "I thought we had a clue"
        sam "The 4th wall is a harsh mistress"
    jump museum3Start

label museum3Planetarium:
    sam "That up there is the Planetarium"
    cmax "I think I was there before???"
    sam "As a brain in a jar, more or less"
    cmax "More or less?"
    sam "More, actually"
    cmax "I don't wanna go there"
    sam "That's something I can respect"
    jump museum3Start

label museum3Paperwaite:
    sam "Helouuu"
    papierwaite "What are you two doing?"
    papierwaite "I already told you I need to make some arrangements before I can help you with anything"
    sam "It's only a couple of short questions"
    papierwaite "Those never are"

label museum3PaperwaiteMenu:
    menu: 
        "What's those arrangements for?" if museum3Changelings == 1:
            sam "It's something you need to do eventually I guess"
            papierwaite "It's not something I need to do exactly"
            sam "Dr. Norrington then?"
            cmax "It must be difficult to do when you are a talking tumor on someone else chest"
            norrington "Please, don't even joke about it"
            papierwaite "They have found ways to do it without me third wheeling the whole time"
            papierwaite "I'm graceful for that"
            papierwaite "But I have to anyway make all the coordination and what not"
            sam "Wait"
            sam "This is a date"
            cmax "There's other elders gods on earth for you to date"
            papierwaite "Of course not!"
            papierwaite "The great and powerful Yog Soggoth is the only elder god still on earth!"
            norrington "Yes... and... I really don't want them so see me like this"
            norrington "It's a bit embarrasing"
            $ museum3Changelings = museum3Changelings + 1
        "If it's not an elder god, what is it?" if museum3Changelings == 2:
            sam "Another fish based monstruosity perhaps?"
            norrington "No, no, no"
            norrington "She's... she's... well"
            cmax "An enthusiast of classic japanese paintings?"
            norrington "A changeling"
            sam "What's that?"
            norrington "The spirit of a fairy that has replaced the spirit of the human in its human body"
            norrington "The fairies that do the change"
            cmax "Ohhhhhhhhhhh"
            norrington "Bring the original human spirit as fuel for their houses, while they leave in their place an old fairy who's ready to die"
            norrington "Since humans live for a very short time compared to the fairies, a human life span is more than enough for them"
            sam "Ok... so..."
            sam "They are normal human bodies walking around zombie like with the spirit of tinkerbell grandmother from her fathers side"
            cmax "Do they look exactly like humans?"
            norrington "Yes, yes, of course"
            norrington "Some have some, well, more specific minor changes in the looks of their host body"
            norrington "But they look exactly like humans, you will never figure out unless you know what to search for"
            sam "Is it there any techniques you can give us to figure out who's a changeling?"
            norrington "Most of the time is a waste of time unless you really need one"
            norrington "But one way to do it is..."
            norrington "Ask them about something they like and they will talk about about it for 2 hours and a half without preparation whatsoever"
            papierwaite "My record was 2 hours, 36 minutes and 46 seconds exactly"
            $ museum3Changelings = museum3Changelings + 1
        "Wait, Papierwaite is a changeling?" if museum3Changelings == 3:
            norrington "It's always the one you least expect"
            norrington "Until you read anything about it and then you figure out at least 30%% of the people you know probably is"
            sam "Has that anything to do with you been stuck in his chest?"
            norrington "Yes, it has everything to do with it"
            norrington "I can share this body with him because his spirit is not that glued to this body"
            norrington "If it were an actual human which summoned me, I would probably still be in our dimension"
            norrington "But, in a way, humans with humans spirits have basically 0 chance to summon me"
            norrington "Because they are usually unable to obtain the required knowledge"
            papierwaite "I have told him several times this has nothing to do with it"
            norrington "You read about obscure incantations from books that took you 20 years to track down"
            norrington "For fun"
            papierwaite "I just take my job as your follower very seriously"
            norrington "That incantation had nothing to do with me"
            norrington "You just like to know about incantations"
            cmax "I feel like an artifact here"
            sam "Yeah, but we don't need to always be the ones carrying the conversations"
            cmax "Eh, I just don't like it"
            $ museum3Changelings = museum3Changelings + 1
        "Do you know about a Voice from Nowhere?" if library3IchimatsuTalks > 2 and museum3ChangelingVoice == 1:
            papierwaite "It's the first time I heard that concept"
            papierwaite "Where did you heard it?"
            sam "The Purple Shadow from the Library says you have a Voice from Nowhere with you, or something"
            norrington "Oh.... ********* is talking about me"
            norrington "He can heard me when I try to talk on Papierwaite's Brain in his presence"
            norrington "I guess that's why he's saying I'm a voice from nowhere"
            cmax "I think because the Visual Novel Writer forgot how to write a word!"
            norrington "That also"
            papierwaite "Why are you asking about it?"
            sam "The Purple one says his brother the red one knows how to solve this"
            sam "He only knows they need a 'Changeling without a Voice from Nowhere'"
            papierwaite "I knew it"
            $ museum3ChangelingVoice = 2
        "You knew what?!" if museum3ChangelingVoice == 2:
            papierwaite "That they need a body to trap anything they workship"
            cmax "How do you know they are workshiping anything?"
            papierwaite "..."
            papierwaite "I'm a cult member"
            cmax "oh..."
        "Have you heard about Superball?" if straightAndNarrow3ScaredSuperball == False:
            norrington "Why are you asking about him?"
            sam "You see..."
            sam "It feels like he's spending way too much time in the office for my liking"
            papierwaite "Isn't still the oval office?"
            sam "Yes, but it was before my office"
            papierwaite "We're not friends, so we haven't talk again since Sybil children was born"
            papierwaite "Do you think he might know something about this dimensional rifts?"
            sam "I mean, I'm fairly sure he knows a lot about time traveling"
            sam "It wouldn't be too much of a stretch to believe he knows about dimensional rifts"
            cmax "I don't know where he got that idea"
            sam "Oh, remember Max"
            sam "While we were also traveling in time, we chat with 2 versions of him separated by time frames way too apart to not be suspicious"
            cmax "..."
            cmax "I don't remember that"
            sam "Oh, right, you shouldn't remember that any way"
            sam "But that happened"
            papierwaite "Ok...."
            papierwaite "Just tell me next time if you find something interesting talking to him"
        "I did have a chat with Superball... mostly" if straightAndNarrow3ScaredSuperball == True and museum3Superball == 1:
            papierwaite "What did he said?"
            sam "Apart of promise me several times he will be not going to camp at our office again"
            cmax "And that was AWESOME"
            sam "He said something among the lines of..."
            sam "Those holes have always existed"
            papierwaite "Like a long standing failure of our existence?"
            sam "More like those holes were always there, but really small"
            papierwaite "Then those holes are not really the problem"
            cmax "Come again?"
            papierwaite "More like something else is affecting the holes and that's our real problem"
            cmax "How do you know that?"
            norrington "About 5 years ago he got obssesed with dimensional stability and read everything about it"
            papierwaite "I knew some day will paid off!"
            sam "So, this theory has some legs to stand on?"
            papierwaite "Most of the knowledge about dimensions is mostly theories which may be true"
            papierwaite "One theory says dimensions have always small imperfections which can be made worse by the powers of beings from another place"
            sam "Like Dr. Norrington"
            norrington "Ah, yes, but, for just to create this holes, it has to be way less powerful than my real form"
            papierwaite "Yog Soggoth's real form would have destroyed the fabric completely and decend our plane to its pure form"
            papierwaite "CHAOS"
            sam "Wait"
            sam "Did you summon him fully knowing that just his presence will basically end the world?"
            papierwaite "That was the idea!"
            cmax "Good to know!"
            $ museum3Superball = museum3Superball + 1
        "To Recap" if museum3ChangelingVoice == 2 and museum3Superball > 1 and museum3MaddieTalk:
            sam "Superball says the holes always existed"
            sam "You say the only way that holes are getting bigger is because some super natural being is trying to conquer the earth"
            sam "And that little girl says that the shadows are from the holes"
            norrington "Maddie said that?"
            cmax "Yes?"
            sam "You know her?"
            norrington "Of course"
            norrington "She's a changeling"
            norrington "She's semi verbal though, so every single time she comes to the museum, I end up reading her brain when she needs something"
            papierwaite "I have told her to bring a notebook"
            papierwaite "She's very expressive in writing form"
            sam "I know it's your job to talk with people visiting the museum, but..."
            sam "This feels really bad"
            papierwaite "Why?!"
            cmax "You are a cult member"
            papierwaite "Oh"
            sam "Anyway..."
            sam "It seems a powerful spirit came to earth"
            sam "Opened those dimensions holes to create the shadows"
            sam "So they could find a body to possess"
            sam "And only can be a Changeling that cannot be already possesed by something else"
            norrington "This spirit cannot be too strong yet"
            norrington "The ******* brothers cannot move from their position"
            cmax "Random thought"
            cmax "What about we find a changedlily without alucinations as a bait" 
            cmax "so the shadows will guide us to their boss"
            sam "That's a plan"
            sam "We only need something else to trap the spirit which is not the changeling"
            sam "Any idea you two?"
            "..."
            sam "Why so nervious..."
            papierwaite "I... need... to... check... some... books... to find... something..."
            cmax "Oh, good!"
            cmax "Now we need to find a switchling without inner voices!"
            cmax "Do you know one?!"
            "..."
            sam "The doctor's date doesn't have voices, isn't it?"
            cmax "You already knew everything Sam just said!"
            norrington "Her soul is so fragile, I don't want to involve her on this"
            sam "At least let us ASK her"
            norrington "I... I..."
        "See you later!" :
            papierwaite "Fine fine..."
            papierwaite "Just let me finish with this call..."
            jump museum3Start


    jump museum3PaperwaiteMenu


label museum3Matsu:
    jump library3Start
                
