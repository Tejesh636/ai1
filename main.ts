input.onButtonPressed(Button.A, function () {
    record.startRecording(record.BlockingState.Blocking)
    record.setMicGain(record.AudioLevels.High)
})
input.onButtonPressed(Button.B, function () {
    record.playAudio(record.BlockingState.Blocking)
})
basic.showString("Welcome")
basic.forever(function () {
    if (500 < input.acceleration(Dimension.X)) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showString("S")
    }
})
