define traveler = Character("[player_name]")
define keqing = Character("Keqing")

label start:
    $ player_name = renpy.input("What is your name?", length=32)
    jump keqing
