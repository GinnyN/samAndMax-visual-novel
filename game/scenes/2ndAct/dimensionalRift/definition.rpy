image dimensionalRift background = "images/backgrounds/stinky2/idle.png"
image dimensionalRift background transition = "images/backgrounds/stinky2/ground.png"

screen dimensionalRift():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/stinky2/ground.png"
        idle "images/backgrounds/stinky2/ground.png"
        hover "images/backgrounds/stinky2/hover.png"

        hotspot(565, 1, 713, 714) clicked Call("dimensionalRift"): # Dimensional Rift
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/dimension-portal.mp3"
        hotspot(2, 2, 314, 659) clicked Call("changeSceneToStraightAndNarrow"): # Change Scene to straight and narrow
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"