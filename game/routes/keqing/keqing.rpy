define keqing = Character("Keqing")

image bg aether 0 = Frame(im.Blur("aether 0.jpeg", 8))
image bg aether 1 = Frame(im.Blur("aether 1.jpeg", 8))
image bg aether 2 = Frame(im.Blur("aether 2.jpeg", 8))
image bg keqing 1 = Frame(im.Blur("keqing/keqing 1.jpeg", 8))
image bg keqing 3 = Frame(im.Blur("keqing/keqing 3.jpeg", 8))
image bg keqing 4 = Frame(im.Blur("keqing/keqing 4.jpeg", 8))
image bg keqing 5 = Frame(im.Blur("keqing/keqing 5.jpeg", 8))
image bg keqing 6 = Frame(im.Blur("keqing/keqing 6.jpeg", 8))
image bg keqing 7 = Frame(im.Blur("keqing/keqing 7.jpeg", 8))
image bg keqing 8 = Frame(im.Blur("keqing/keqing 8.jpeg", 8))

label keqing:
    scene bg aether 0
    show aether 0
    with Fade(1, 1, 1)

    traveler "Another day another commission to take care of."
    traveler "Paimon, I choose you!"
    with Fade(1, 0.5, -0.01)

    $ renpy.movie_cutscene("paimon 1.ogv")
    with Fade(-0.01, 0.5, 1)

    traveler "Done."

    scene bg aether 1
    show aether 1:
        zoom 2
        xalign 0.5
        yalign 0.5
    with dissolve

    traveler "This is bad..."
    traveler "It took me the whole day to finish all my commissions."
    traveler "Today is the Lantern Rite festival."
    traveler "I promised Keqing that we will watch the fireworks together."
    traveler "But I'm too late... I'm sorry Keqing."

    show keqing 0
    with Fade(1, 1, 1)

    keqing "[traveler]... Where are you?"
    keqing "The fireworks display is over and you are still not here."
    keqing "I am really missing you. I hope you're fine."
    keqing "At least you should have seen my new dress."
    keqing "I've put in a lot of thought to this because I want you to like how I look."
    keqing "I guess I'll just go back home now."

    scene bg aether 2
    show aether 2:
        zoom 2
        xalign 0.5
        yalign 0.5
    with Fade(1, 1, 1)

    traveler "I didn't see Keqing anywhere. I need to hurry. Maybe she already went home."
    traveler "I need to apologize to her."

    scene bg keqing 1
    show keqing 1:
        yalign 1.0
        xalign 0.5
        ease 10.0 yalign 0.0
    with Fade(1, 1, 1)

    keqing "[traveler] hasn't seen my new outfit yet."
    keqing "It's too sad that I have to remove my clothes already."
    keqing "..."
    "*knock* *knock* *knock*"
    keqing "Huh?"
    keqing "Who's there?"
    traveler "Keqing! It's me."

    scene keqing 2:
        zoom 1.5
    with dissolve

    keqing "[traveler]!?!"
    traveler "I am really sorry Keqing. Can I come in?"
    keqing "S-sure!!"

    scene bg keqing 3
    show keqing 3:
        zoom 0.8
        yalign 1.0
        xalign 0.5
        ease 5 yalign 0.0
    with dissolve

    keqing "H-hello [traveler]..."
    traveler "Hi Keqing. I am really sorry."
    keqing "Hmph..."
    traveler "I want to get back to you... so do you want to go for a date with me tomorrow?"

    scene keqing 2:
        zoom 1.5
    with dissolve

    keqing "D-date!?!"

    scene bg keqing 4
    show keqing 4:
        zoom 0.4
        yalign 1.0
        xalign 0.5
        ease 3 yalign 0.0
    with dissolve

    keqing "Really??"
    keqing "I would love to!"
    traveler "It's set then!"

    scene bg keqing 3
    show keqing 3:
        zoom 0.8
        yalign 1.0
        xalign 0.5
        ease 5 yalign 0.0
    with dissolve

    keqing "B-by the way..."
    keqing "How do I look?"
    traveler "..."
    traveler "(I immediately got hard when I first saw her. But I can't say that to her!)"
    traveler "Y-you look so good in your dress Keqing."

    scene keqing 2:
        zoom 1.5
    with dissolve

    keqing "R-really??"
    keqing "Thanks!"

    scene bg keqing 4
    show keqing 4:
        zoom 0.4
        yalign 1.0
        xalign 0.5
        ease 3 yalign 0.0
    with dissolve

    keqing "I will wear this again tomorrow since you didn't have the chance to look at my dress more."
    traveler "I am looking forward to it!"
    keqing "Yes. I'm excited!"
    traveler "(She's just too hot. I can't stop looking at her.)"
    keqing "[traveler]? Are you okay?"

    scene keqing 2:
        zoom 1.5
    with dissolve

    keqing "(He's staring at me so much! This is embarrassing but I'm really glad that he liked my new dress.)"

    scene bg keqing 5
    show keqing 5:
        zoom 1.5
        yalign 1.0
        xalign 0.5
        ease 5 yalign 0.0
    with dissolve

    traveler "..."
    keqing "..."
    traveler "..."
    keqing "..."

    scene bg keqing 6
    show keqing 6:
        yalign 1.0
        xalign 0.5
        ease 5 yalign 0.0
    with dissolve

    pause 5.0

    scene bg keqing 7
    show keqing 7:
        zoom 1.1
        xalign 0.5
    with dissolve

    keqing "..."

    scene bg keqing 8
    show keqing 8:
        zoom 1.3
        yalign 1.0
        xalign 0.5
        ease 10.0 yalign 0.0
    with Fade(1, 1, 1)

    pause 5.0

    keqing "I'm ready [traveler]..."
