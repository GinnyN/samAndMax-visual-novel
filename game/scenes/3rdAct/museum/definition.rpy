image museum3 background = "images/backgrounds/museum/idle.png"

screen museum3():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/museum/ground.png"
        idle "images/backgrounds/museum/ground.png"
        hover "images/backgrounds/museum/hover.png"

        hotspot(331, 648, 647, 68) clicked Call("museum3Desoto"): # To Straight and Narrow
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/car-door-handle.mp3"
        hotspot(5, 193, 323, 525) clicked Call("museum3Madie"): # Left to meet Madie
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"
        hotspot(1026, 304, 251, 409) clicked Call("museum3Matsu"): # Right to the Library to meet Ichi
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"
        hotspot(785, 403, 138, 227) clicked Call("museum3Paperwaite"): # Paperwaite office
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/knock-wood.mp3"
        hotspot(500, 135, 317, 147) clicked Call("museum3Planetarium"): # Planetarium
            hover_sound "audio/sounds/prepare.mp3"
            activate_sound "audio/sounds/boots-cement.mp3"