image straightAndNarrow1 background = "images/backgrounds/straightAndNarrow1/idle.png"
image straightAndNarrow1 foreground = "images/backgrounds/straightAndNarrow1/ground.png"

screen straightAndNarrow1():

    tag gameScene
    use quick_menu

    imagemap:
        ground "images/backgrounds/straightAndNarrow1/ground.png"
        idle "images/backgrounds/straightAndNarrow1/ground.png"
        hover "images/backgrounds/straightAndNarrow1/hover.png"

        hotspot(370, 291, 150, 196) clicked Call("straightAndNarrow1Office") # Sam and Max Office
        hotspot(36, 147, 178, 462) clicked Call("straightAndNarrow1Tardis") # Tardis
        hotspot(852, 339, 115, 245) clicked Call("straightAndNarrow1Matsu") # Bosco's used by Totty