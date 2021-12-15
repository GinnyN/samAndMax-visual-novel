image superball neutral = "images/characters/superball/neutral.png"
image superball neutral flip = im.Flip("images/characters/superball/neutral.png", horizontal=True)

image black = "#000000"
image menuImg:
    contains:
        alpha 0.0
        HBox("gui/main_menu.png")
        linear 5 alpha 1.0