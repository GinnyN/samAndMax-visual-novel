image straightAndNarrow3 background = "images/backgrounds/straightAndNarrow2/idle.png"
image straightAndNarrow3 background crash = "images/backgrounds/straightAndNarrow2/ground.png"
image straightAndNarrow3 cinematic = "images/cinematic/outoffice.png"

image shootJyushimatsu = "images/cinematic/shoot-jyushimatsu.png"

screen straightAndNarrow3():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/straightAndNarrow2/ground.png"
        idle "images/backgrounds/straightAndNarrow2/ground.png"
        hover "images/backgrounds/straightAndNarrow2/hover.png"

        hotspot(370, 291, 150, 196) clicked Call("straightAndNarrow3Office"): # Sam and Max Office
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"
        hotspot(45, 167, 160, 389) clicked Call("straightAndNarrow3Tardis"): # Tardis
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/gate-open.mp3"
        hotspot(852, 339, 115, 245) clicked Call("straightAndNarrow3Matsu"): # Bosco's used by Jyushi
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/steps-glass.mp3"
        hotspot(136, 540, 400, 179) clicked Call("straightAndNarrow3FastTravel"): # Desoto
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/car-door-handle.mp3"
        hotspot(1095, 2, 182, 611) clicked Call("changeSceneToDimensionalRift3"): # Change Scene to dimensional rift
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"