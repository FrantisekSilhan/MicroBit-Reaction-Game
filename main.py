game_started = False

def main():
    global game_started
    basic.clear_screen()
    basic.pause(randint(30, 100) * 100)
    game_started = True
    basic.show_icon(IconNames.YES, 0)
    music.play_tone(Note.C, 1500)
control.in_background(main)

def check():
    global game_started
    p1 = pins.digitalReadPin(DigitalPin.P1)
    p2 = pins.digitalReadPin(DigitalPin.P2)
    if game_started:
        if p1 == 0 and p2 == 0:
            basic.show_string("R", 0)
            game_started = False
            basic.pause(3000)
            control.reset()
        elif p1 == 0 and p2 == 1:
            basic.show_number(1, 0)
            game_started = False
            basic.pause(3000)
            control.reset()
        elif p2 == 0 and p1 == 1:
            basic.show_number(2, 0)
            game_started = False
            basic.pause(3000)
            control.reset()
    else:
        if p1 == 0 and p2 == 0:
            basic.show_string("C", 0)
            basic.pause(3000)
            control.reset()
        if p1 == 0:
            basic.show_string("B", 0)
            basic.pause(3000)
            control.reset()
        if p2 == 0:
            basic.show_string("A", 0)
            basic.pause(3000)
            control.reset()
basic.forever(check)
