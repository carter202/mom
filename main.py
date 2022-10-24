def on_button_pressed_a():
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_melody("G B A G C5 B A B ", 120)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            200,
            600,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

for index in range(4):
    basic.show_leds("""
        . # # # .
                . . # . .
                . . # . .
                . . # . .
                . # # # .
    """)
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        # . . . #
                # . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                # . # . #
                # . # . #
                # . . . #
    """)
    basic.show_leds("""
        . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                # . # . #
                # . # . #
                # . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . # # # .
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                # . . . .
                # # # . .
                # . . # .
                # . . # .
    """)
    basic.show_leds("""
        . . . # .
                . . . # .
                . # # # .
                . # . # .
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . #
                . . . . #
                . . # # #
                . . # . #
                . . # # #
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . # # # .
                . # . # .
    """)
    basic.show_leds("""
        . . . . #
                . . . . #
                . . # # #
                . . # . #
                . . # # #
    """)
    basic.show_icon(IconNames.SMALL_HEART)

def on_forever():
    pass
basic.forever(on_forever)
