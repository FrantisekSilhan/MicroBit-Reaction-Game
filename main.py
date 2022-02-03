game_started = False
P1Cheated = False
P2Cheated = False

def main():
    global game_started, P1Cheated, P2Cheated
    P1Cheated = False
    P2Cheated = False
    game_started = False
    basic.clear_screen()
    basic.pause(randint(30, 100) * 100)
    if P1Cheated and P2Cheated:
        show("C")
    elif P1Cheated:
        show("B")
    elif P2Cheated:
        show("A")
    else:
        game_started = True
        basic.show_icon(IconNames.YES, 0)
        music.play_tone(Note.C, 1500)
control.in_background(main)

def check():
    global game_started, P1Cheated, P2Cheated
    if game_started:
        if pins.digitalReadPin(DigitalPin.P1) == 0 and pins.digitalReadPin(DigitalPin.P2) == 0:
            basic.show_string("R", 0)
            game_started = False
            basic.pause(3000)
            main()
        if pins.digitalReadPin(DigitalPin.P1) == 0 and pins.digitalReadPin(DigitalPin.P2) == 1:
            basic.show_number(1, 0)
            game_started = False
            basic.pause(3000)
            main()
        if pins.digitalReadPin(DigitalPin.P2) == 0 and pins.digitalReadPin(DigitalPin.P1) == 1:
            basic.show_number(2, 0)
            game_started = False
            basic.pause(3000)
            main()
    else:
        if pins.digitalReadPin(DigitalPin.P1) == 0:
            P1Cheated = True
        if pins.digitalReadPin(DigitalPin.P2) == 0:
            P2Cheated = True
basic.forever(check)

def show(value):
    basic.show_string(value, 0)
    music.play_tone(Note.C, 1500)
    basic.pause(1500)
    main()
