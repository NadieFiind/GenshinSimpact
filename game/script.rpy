define traveler = Character("[player_name]", color="#feebbc")
define keqing = Character("Keqing", color="#9478aa")

label start:
    $ player_name = renpy.input("What is your name?", length=32)
    
    show bg start
    with Fade(1, 1, 1)
    
    traveler "Hello!"
    keqing "Hi!"
