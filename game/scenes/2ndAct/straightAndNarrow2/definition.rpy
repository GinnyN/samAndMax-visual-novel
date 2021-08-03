image straightAndNarrow2 background = "images/backgrounds/straightAndNarrow2/idle.png"
image straightAndNarrow2 background crash = "images/backgrounds/straightAndNarrow2/ground.png"

screen straightAndNarrow2():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/straightAndNarrow2/ground.png"
        idle "images/backgrounds/straightAndNarrow2/ground.png"
        hover "images/backgrounds/straightAndNarrow2/hover.png"

        hotspot(370, 291, 150, 196) clicked Call("straightAndNarrow2Office") # Sam and Max Office
        hotspot(45, 167, 160, 389) clicked Call("straightAndNarrow2Tardis") # Tardis
        hotspot(852, 339, 115, 245) clicked Call("straightAndNarrow2Matsu") # Bosco's used by Totty or Jyushi
        hotspot(136, 540, 400, 179) clicked Call("straightAndNarrowFastTravel") # Desoto
        hotspot(1095, 2, 182, 611) clicked Call("changeSceneToDimensionalRift") # Change Scene to dimensional rift