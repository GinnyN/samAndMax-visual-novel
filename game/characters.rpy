init python:
    def typewriter(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sounds/typewritter1.mp3", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

define angela = Character("Angela", callback=typewriter)
define sam = Character("Sam", callback=typewriter)
define cmax = Character("Max", callback=typewriter)

define todomatsu = Character("Pinkish Shadow", callback=typewriter)
define jyushimatsu = Character("Yellowish Shadow", callback=typewriter)
define superball = Character("Secret Agent", callback=typewriter)