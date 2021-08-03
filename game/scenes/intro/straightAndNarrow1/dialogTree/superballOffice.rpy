define straightAndNarrow1SuperballOfficeVisited = False
define straightAndNarrow1SuperballOfficeFreelancePoliceTree = 0
define straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree = 0

label straightAndNarrow1SuperballOffice:
    if not straightAndNarrow1SuperballOfficeVisited:
        show angela neutral flip with dissolve
        angela "They do have a very good alarm system"
        show superball neutral with dissolve:
            xpos 0.0
        superball "Please explain your motives to be here, before I have to get physical"
        show angela unsure flip with dissolve
        angela "The secret service?"
        angela "You don't have any jurisdiction in this city"
        superball "I do at the oval office, ma'am"
        angela "Oval office?"
        show angela serious flip with dissolve
        angela "Didn't the oval office went back to the White House after the former president went lovecraftian and had to be destroyed in a grusome fashion?"
        superball "We did publicly"
        superball "But, officially..."
        superball "We still trying to figure out the paperwork"
        show angela neutral flip with dissolve
        angela "Well, that's explain why you haven't demolished this building yet"
        superball "We do believe the former president eated it"
    else:
        show superball neutral with dissolve:
            xpos 0.0
        
    $ straightAndNarrow1SuperballOfficeVisited = True

label straightAndNarrow1SuperballOfficeMenu:
    menu:
        "I'll leave this folder right here" if straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree == 0:
            show angela neutral flip with dissolve
            angela "Well, I'll leave this folder right here..."
            superball "I'm afraid I cannot let you do that ma'am"
            show angela unsure flip with dissolve
            angela "Uh? Why not?"
            superball "That folder could contain poison"
            superball "anthrax"
            superball "any other dangerous substance which can endanger the life of the former president and his assistant"
            angela "Isn't he dead?"
            superball "Yes, of course he is"
            $ straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree = 1 + straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree
        "Can I at least communicate with them?" if straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree == 1:
            show angela thinking flip with dissolve
            angela "If you are not going to let me leave the folder on their desk"
            show angela serious flip with dissolve
            angela "Can you help me to contact with them?"
            angela "Our phones got hacked and I cannot see my contacts anymore"
            superball "No can't do ma'am"
            show angela unsure flip with dissolve
            angela "You can't give me the work phone number of the Freelance Police because???"
            superball "I have to protect the former president and his loved ones"
            superball "That's my duty"
            show angela neutral flip with dissolve
            angela "That's nice"
            angela "I guess I'll just grab some of this flyers with a phone number and call it a day"
            superball "That was an oversight"
            $ straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree = 1 + straightAndNarrow1SuperballOfficeFreelancePoliceFolderTree
        "Isn't this the office of the Freelance Police?" if straightAndNarrow1SuperballOfficeFreelancePoliceTree == 0:
            show angela serious flip with dissolve
            angela "Isn't this the office of the Freelance Police though"
            superball "That's correct"
            show angela unsure flip with dissolve
            angela "But it's also the oval office?"
            superball "Affirmative ma'am"
            show angela thinking flip with dissolve
            angela "So, the former president is sharing office with the Freelance Police?"
            superball "With all due respect ma'am, how do you not know about the former president and his record 10 impeachment trials?"
            show angela neutral flip with dissolve
            angela "I don't watch TV"
            angela "I watch half to an hour video essays about critical theory analysing movies and video games I'll never going to watch or play"
            superball "Of course"
            $  straightAndNarrow1SuperballOfficeFreelancePoliceTree = 1 + straightAndNarrow1SuperballOfficeFreelancePoliceTree
        "Do the carpet match the drapes?" if straightAndNarrow1SuperballOfficeFreelancePoliceTree == 1:
            superball "If I can do the questions now ma'am"
            show angela neutral flip with dissolve
            angela "I do not remember allowing that"
            superball "Why did you lockpicked the door to enter here?"
            angela "The commissioner allow the informants to the Freelance Police to do that"
            angela "So we can left the folder in one of their desks"
            superball "Why do you not simply throw it under the door?"
            angela "The rats will nibble on it"
            superball "That sensible I suppose"
            $  straightAndNarrow1SuperballOfficeFreelancePoliceTree = 1 + straightAndNarrow1SuperballOfficeFreelancePoliceTree
        "Go back to the street":
            hide angela with dissolve
            angela "I'll better go away before he decides I cannot defeat him in mortal combat"
            superball "Roger That"
            hide superball with dissolve
            call screen straightAndNarrow1 with dissolve



    jump straightAndNarrow1SuperballOfficeMenu