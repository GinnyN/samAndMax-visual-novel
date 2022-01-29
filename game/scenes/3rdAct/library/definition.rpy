image library3 background = "images/backgrounds/library/idle.png"

screen library3():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/library/ground.png"
        idle "images/backgrounds/library/ground.png"
        hover "images/backgrounds/library/hover.png"

        hotspot(284, 430, 281, 175) clicked Call("straightAndNarrow3Office"): # Ichimatsu under the Table
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/knock-wood.mp3"
        hotspot(766, 0, 512, 715) clicked Call("straightAndNarrow3Tardis"): # Dimensional Hole
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/dimension-portal.mp3"
        hotspot(5, 6, 255, 710) clicked Call("backToMuseum3"): #Back to the hall
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"
