def on_received_number_deprecated(receivedNumber):
    global Recieved
    Recieved = receivedNumber
radio.on_received_number_deprecated(on_received_number_deprecated)

Recieved = 0
radio.set_group(44)
Recieved = 0
basic.show_leds("""
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    """)
LEDs = neopixel.create(DigitalPin.P1, 6, NeoPixelMode.RGB)
LEDs.set_brightness(10)
LEDs.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
LEDs.set_pixel_color(4, neopixel.colors(NeoPixelColors.ORANGE))
LEDs.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
LEDs.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLUE))
LEDs.set_pixel_color(1, neopixel.colors(NeoPixelColors.PURPLE))
LEDs.set_pixel_color(0, neopixel.colors(NeoPixelColors.YELLOW))
LEDs.show()
basic.pause(100)

def on_button_pressed_a():
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(784, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_forever():
    global LEDs
    LEDs = neopixel.create(DigitalPin.P1, 6, NeoPixelMode.RGB)
    if Recieved == 1:
        basic.show_leds("""
            . . # . .
            . # . # .
            . # # # .
            . # . # .
            . . . . .
            """)
        for index in range(4):
            LEDs.set_brightness(10)
            LEDs.show()
            LEDs.set_brightness(125)
            LEDs.set_pixel_color(5, neopixel.colors(NeoPixelColors.WHITE))
            LEDs.show()
            basic.pause(750)
            LEDs.set_brightness(10)
            LEDs.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
            LEDs.show()
            LEDs.set_brightness(125)
            LEDs.set_pixel_color(4, neopixel.colors(NeoPixelColors.WHITE))
            LEDs.show()
            basic.pause(750)
            LEDs.set_brightness(10)
            LEDs.set_pixel_color(4, neopixel.colors(NeoPixelColors.ORANGE))
            LEDs.show()
            LEDs.set_brightness(125)
            LEDs.set_pixel_color(3, neopixel.colors(NeoPixelColors.WHITE))
            LEDs.show()
            basic.pause(750)
            LEDs.set_brightness(10)
            LEDs.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
            LEDs.show()
            LEDs.set_brightness(125)
            LEDs.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
            LEDs.show()
            basic.pause(750)
            LEDs.set_brightness(10)
            LEDs.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLUE))
            LEDs.show()
            LEDs.set_brightness(125)
            LEDs.set_pixel_color(1, neopixel.colors(NeoPixelColors.WHITE))
            LEDs.show()
            basic.pause(750)
            LEDs.set_brightness(10)
            LEDs.set_pixel_color(1, neopixel.colors(NeoPixelColors.PURPLE))
            LEDs.show()
            LEDs.set_brightness(125)
            LEDs.set_pixel_color(0, neopixel.colors(NeoPixelColors.WHITE))
            LEDs.show()
            basic.pause(750)
            LEDs.set_brightness(10)
            LEDs.set_pixel_color(0, neopixel.colors(NeoPixelColors.YELLOW))
            LEDs.show()
            basic.pause(750)
    elif Recieved == 2:
        basic.show_leds("""
            # # . . .
            # . # . .
            # # # . .
            # . # . .
            # # . . .
            """)
        LEDs.set_brightness(7)
        LEDs.show_color(neopixel.colors(NeoPixelColors.RED))
        LEDs.show()
        basic.pause(2000)
        LEDs.set_brightness(7)
        LEDs.show_color(neopixel.colors(NeoPixelColors.GREEN))
        LEDs.show()
        basic.pause(2000)
        LEDs.set_brightness(7)
        LEDs.show_color(neopixel.colors(NeoPixelColors.BLUE))
        LEDs.show()
        basic.pause(2000)
        LEDs.set_brightness(7)
        LEDs.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        LEDs.show()
        basic.pause(2000)
        LEDs.set_brightness(7)
        LEDs.show_color(neopixel.colors(NeoPixelColors.INDIGO))
        LEDs.show()
        basic.pause(2000)
        LEDs.set_brightness(7)
        LEDs.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        LEDs.show()
        basic.pause(2000)
    elif Recieved == 3:
        basic.show_leds("""
            . # # . .
            # . . # .
            # . . . .
            # . . # .
            . # # . .
            """)
        LEDs = neopixel.create(DigitalPin.P1, 6, NeoPixelMode.RGB)
        LEDs.set_brightness(7)
        LEDs.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
        LEDs.set_pixel_color(4, neopixel.colors(NeoPixelColors.GREEN))
        LEDs.set_pixel_color(3, neopixel.colors(NeoPixelColors.RED))
        LEDs.set_pixel_color(2, neopixel.colors(NeoPixelColors.GREEN))
        LEDs.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
        LEDs.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
        LEDs.show()
        basic.pause(100)
    elif Recieved == 4:
        LEDs.set_brightness(10)
        basic.show_leds("""
            # # # . .
            # . . # .
            # . . # .
            # . . # .
            # # # . .
            """)
        LEDs.set_brightness(10)
        LEDs.show_rainbow(1, 360)
        for index2 in range(50):
            LEDs.set_brightness(10)
            LEDs.rotate(1)
            LEDs.show()
            basic.pause(500)
    elif Recieved == 5:
        basic.show_leds("""
            # . . . #
            . . # . .
            . . . . .
            . # # # .
            # . . . #
            """)
        LEDs.set_brightness(7)
        LEDs.show()
        basic.pause(100)
basic.forever(on_forever)
