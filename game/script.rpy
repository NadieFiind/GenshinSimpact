define traveler = Character("[player_name]")

label start:
    scene expression "#000"
    with Fade(0.5, 0.5, 0.5)
    $ player_name = renpy.input("What is your name?", length=32)
    jump keqing
