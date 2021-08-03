define straightAndNarrow3MatsuTeleport = 0
define straightAndNarrow3MatsuFamily = 0

label straightAndNarrow3MatsuTree:

    menu:
        "We wanna buy something":
            call wannaBuySomething3
        "How did you arrived here?" if straightAndNarrow3MatsuTeleport == 0:
            call arrivedHere31
            $ straightAndNarrow3MatsuTeleport = 1
        "When did you arrived here?" if straightAndNarrow3MatsuTeleport == 1:
            call arrivedHere32
            $ straightAndNarrow3MatsuTeleport = 2
        "Which Library exactly?" if straightAndNarrow3MatsuTeleport == 2:
            call arrivedHere33
            $ straightAndNarrow3MatsuLibrary = True
        "Do you have an extended family?" if straightAndNarrow3MatsuFamily == 0:
            call matsuFamily31
            $ straightAndNarrow3MatsuFamily = 1
        "Do you have assigned colors?" if straightAndNarrow3MatsuFamily == 1:
            call matsuFamily32
        "Good Bye":
            show sam neutral
            show cmax neutral
            with dissolve
            sam "Thanks a lot for the conversation"
            show jyushimatsu neutral flip with dissolve
            jyushimatsu "AHHHHHH"
            jyushimatsu "Ok!"
            hide cmax
            hide sam
            hide jyushimatsu
            with dissolve
            jump straightAndNarrow3Back

    jump straightAndNarrow3MatsuTree
return

label matsuFamily31:
    show sam unsure
    show cmax neutral
    with dissolve
    sam "You seem to have more family than just a very dark shadow with pink hues"
    show cmax bored with dissolve
    cmax "A very cranky shadow with pink hues"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "That sounds like *********"
    show sam neutral with dissolve
    sam "Is it there more like you?"
    jyushimatsu "It can be"
    jyushimatsu "I haven't seen them recently though"
    sam "How many of you are around?"
    jyushimatsu "*"
    show cmax surprise with dissolve
    cmax "What?!"
    cmax "That is ALSO censored?"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "Maybe if I said our names"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "*************************************************************"
    show sam unsure with dissolve
    sam "All of you ALSO have a combined big name?"
    show jyushimatsu worried flip with dissolve
    jyushimatsu "It also redacted the spaces between!"
    jyushimatsu "This is bad, bad, bad, bad, bad, bad"
    return

label matsuFamily32:
    show sam unsure
    show cmax neutral
    with dissolve
    sam "The fact that you have assigned colors lead me to believe there's a lot of you"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "I still don't know how dad pays for all of us"
    show sam neutral with dissolve
    sam "Maybe if you give us some reference using that"
    jyushimatsu "Colors of the rainbow"
    sam "There's 7 of you?"
    jyushimatsu "Colors of the rainbow less orange"
    show cmax thinking with dissolve
    cmax "So... those were Magenta hues, not Pink hues?"
    jyushimatsu "Beats me"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "He choose his color because he's cute"
    show sam unsure
    show cmax bored
    with dissolve
    sam "Really?"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "He doesn't have a heart"
    return

label wannaBuySomething3:
    show sam neutral
    show cmax neutral
    with dissolve
    sam "We wanna buy something"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "I have nothing here"
    show cmax surprise with dissolve
    cmax "But this is a store"
    show jyushimatsu worried flip with dissolve
    jyushimatsu "I didn't knew that!"
    sam "What did you think it was?"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "An underground bunker already raided by cazadores after the apocalypse?"
    show sam surprised with dissolve
    sam "Why I didn't think of that?"
    return

label arrivedHere31:
    show sam unsure
    show cmax neutral
    with dissolve
    sam "Did you said you haven't seen the sun for a long time, correct?"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "Huh"
    show sam neutral with dissolve
    sam "Then how did you arrived here?"
    jyushimatsu "I did"
    sam "Ok, but how?"
    jyushimatsu "By doing it"
    show cmax thinking with dissolve
    cmax "Teleportation, kidnapping, a long night of inebriated fun which you cannot remember an actual thing?"
    jyushimatsu "Yes"
    show cmax surprise with dissolve
    cmax "So, we can just choose how did you arrived here?"
    jyushimatsu "Probably"
    show cmax thinking with dissolve
    cmax "Why I feel outplayed in my own game now?"
    show sam surprised with dissolve
    sam "Don't look at me, everybody always says I'm the straight man"
    jyushimatsu "AHHH"
    jyushimatsu "That's not always set in stone"
    show jyushimatsu sad flip with dissolve
    jyushimatsu "********** was originally the tsukkomi, but once I had to play that part versus him as the boke"
    jyushimatsu "It was weird"
    show sam unsure
    show cmax neutral
    with dissolve
    jyushimatsu "But in my defense he was being very creppy"
    return

label arrivedHere32:
    show sam neutral
    show cmax neutral
    with dissolve
    sam "When did you arrived here?"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "I think like 1 minute ago"
    show jyushimatsu sad flip with dissolve
    jyushimatsu "But it feels like a year..."
    jyushimatsu "I wanna play baseball"
    show cmax thinking with dissolve
    cmax "You haven't seen the sun since 1 minute ago?"
    sam "Did you arrive somewhere else before arriving here?"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "I think it was a library"
    jyushimatsu "Those were a lot of books without any pictures"
    jyushimatsu "And a big weird hole with pretty colors"
    show cmax excited with dissolve
    cmax "Do you think that`s impressive?"
    cmax "You should see the colors when the annual ilegal radioactive dump takes place!"
    show cmax ohyeah with dissolve
    cmax "The following malign tumor is totally worth it!"
    show jyushimatsu worried flip with dissolve
    jyushimatsu "Ahhhh"
    show sam happy with dissolve
    sam "And Max got his revenge"
    return

label arrivedHere33:
    show sam neutral
    show cmax neutral
    with dissolve
    sam "Can you remember anything particular about the library?"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "Uh Uh"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "Except there was a guy who was talking with a very weird french accent?"
    show sam unsure with dissolve
    sam "A library with a guy with a french accent as the librarian"
    cmax "Doesn't ring any bells"
    show jyushimatsu worried flip with dissolve
    jyushimatsu "He wasn't even hot!"
    jyushimatsu "I was sooo dissapointed"
    show cmax surprise with dissolve
    cmax "Papierwaite?"
    show sam neutral
    show cmax neutral flip
    with dissolve
    sam "Well, yes, the Museum of Mostly Natural History has a library attached to it"
    sam "It makes sense Papierwaite did some of his investigation there"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "He stayed looking at the hole with pretty colors all the time"
    show jyushimatsu sarcastic flip with dissolve
    jyushimatsu "But needed some privacy!"
    show jyushimatsu neutral flip with dissolve
    jyushimatsu "I found the best bug book I had found in my life"
    show cmax thinking with dissolve
    cmax "Why do you need privacy with a book about bugs?"
    jyushimatsu "It's make me"
    sam "On second thought, I don't wanna know"
    show cmax excited with dissolve
    cmax "I wanna know!"
    sam "You don't wanna know Max"
    show jyushimatsu sad flip with dissolve
    jyushimatsu "I just needed to relieve myself!"
    return