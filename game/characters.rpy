init python:
    def typewriter(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sounds/typewritter1.mp3", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

define sam = Character("Sam", callback=typewriter)
define cmax = Character("Max", callback=typewriter)

define angela = Character("Angela", callback=typewriter)
define maddie = Character("Maddie", callback=typewriter)
define cmaxSpirit = Character("", callback=typewriter)
define maddieB = Character("Little Girl", callback=typewriter)

define todomatsu = Character("Pinkish Shadow", callback=typewriter)
define jyushimatsu = Character("Yellowish Shadow", callback=typewriter)
define ichimatsu = Character("Purpleish Shadow", callback=typewriter)

define superball = Character("Superball", callback=typewriter)
define papierwaite = Character("Papierwaite", callback=typewriter)
define norrington = Character("Dr. Norrington", callback=typewriter)