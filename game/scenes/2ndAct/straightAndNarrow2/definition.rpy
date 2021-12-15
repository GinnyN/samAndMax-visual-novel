image straightAndNarrow2 background = "images/backgrounds/straightAndNarrow2/idle.png"
image straightAndNarrow2 background crash = "images/backgrounds/straightAndNarrow2/ground.png"

screen straightAndNarrow2():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/straightAndNarrow2/ground.png"
        idle "images/backgrounds/straightAndNarrow2/ground.png"
        hover "images/backgrounds/straightAndNarrow2/hover.png"

        hotspot(370, 291, 150, 196) clicked Call("straightAndNarrow2Office"): # Sam and Max Office
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"
        hotspot(45, 167, 160, 389) clicked Call("straightAndNarrow2Tardis"): # Tardis
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/gate-open.mp3"
        hotspot(852, 339, 115, 245) clicked Call("straightAndNarrow2Matsu"): # Bosco's used by Totty or Jyushi
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/steps-glass.mp3"
        hotspot(136, 540, 400, 179) clicked Call("straightAndNarrowFastTravel"): # Desoto
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/car-door-handle.mp3"
        hotspot(1095, 2, 182, 611) clicked Call("changeSceneToDimensionalRift"): # Change Scene to dimensional rift
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"