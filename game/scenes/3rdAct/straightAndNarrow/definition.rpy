image straightAndNarrow3 background = "images/backgrounds/straightAndNarrow2/idle.png"
image straightAndNarrow3 background crash = "images/backgrounds/straightAndNarrow2/ground.png"
image straightAndNarrow3 cinematic = "images/cinematic/outoffice.png"

screen straightAndNarrow3():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/straightAndNarrow2/ground.png"
        idle "images/backgrounds/straightAndNarrow2/ground.png"
        hover "images/backgrounds/straightAndNarrow2/hover.png"

        hotspot(370, 291, 150, 196) clicked Call("straightAndNarrow3Office") # Sam and Max Office
        hotspot(45, 167, 160, 389) clicked Call("straightAndNarrow3Tardis") # Tardis
        hotspot(852, 339, 115, 245) clicked Call("straightAndNarrow3Matsu") # Bosco's used by Jyushi
        hotspot(136, 540, 400, 179) clicked Call("straightAndNarrow3FastTravel") # Desoto
        hotspot(1095, 2, 182, 611) clicked Call("changeSceneToDimensionalRift3") # Change Scene to dimensional rift