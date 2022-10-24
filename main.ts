input.onButtonPressed(Button.A, function () {
    music.playTone(494, music.beat(BeatFraction.Whole))
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.playTone(523, music.beat(BeatFraction.Whole))
    music.playMelody("G B A G C5 B A B ", 120)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
})
for (let index = 0; index < 4; index++) {
    basic.showLeds(`
        . # # # .
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        `)
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        # . # . #
        # . # . #
        # . . . #
        `)
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        # . # . #
        # . # . #
        # . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        # # # . .
        # . . # .
        # . . # .
        `)
    basic.showLeds(`
        . . . # .
        . . . # .
        . # # # .
        . # . # .
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . #
        . . . . #
        . . # # #
        . . # . #
        . . # # #
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        `)
    basic.showLeds(`
        . . . . #
        . . . . #
        . . # # #
        . . # . #
        . . # # #
        `)
    basic.showIcon(IconNames.SmallHeart)
}
basic.forever(function () {
	
})
