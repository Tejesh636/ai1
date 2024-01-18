def on_button_pressed_a():
    record.start_recording(record.BlockingState.BLOCKING)
    record.set_mic_gain(record.AudioLevels.HIGH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    record.play_audio(record.BlockingState.BLOCKING)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Welcome")

def on_forever():
    if 0 < input.acceleration(Dimension.X):
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_string("S")
basic.forever(on_forever)
