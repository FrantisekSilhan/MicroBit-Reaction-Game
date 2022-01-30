game_started = False
P1Cheated = False
P2Cheated = False

def main():
    global game_started, P1Cheated, P2Cheated#, P1Won, P2Won
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
        if pins.digitalReadPin(DigitalPin.P1) == 1 and pins.digitalReadPin(DigitalPin.P2) == 1:
            basic.show_string("R", 0)
            game_started = False
        if pins.digitalReadPin(DigitalPin.P1) == 1 and pins.digitalReadPin(DigitalPin.P2) == 0:
            basic.show_number(1, 0)
            game_started = False
        if pins.digitalReadPin(DigitalPin.P2) == 1 and pins.digitalReadPin(DigitalPin.P1) == 0:
            basic.show_number(2, 0)
            game_started = False
        new_game()
    else:
        if pins.digitalReadPin(DigitalPin.P1) == 1:
            P1Cheated = True
        if pins.digitalReadPin(DigitalPin.P2) == 1:
            P2Cheated = True
input.on_pin_pressed(TouchPin.P1, check)
input.on_pin_pressed(TouchPin.P2, check)

def new_game():
    basic.pause(3000)
    main()

def show(value):
    basic.show_string(value, 0)
    music.play_tone(Note.C, 1500)
    new_game()