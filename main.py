game_started = False
P1Cheated = False
P2Cheated = False
#P1Won = False
#P2Won = False
def main():
    global game_started, P1Cheated, P2Cheated#, P1Won, P2Won
    P1Cheated = False
    P2Cheated = False
    game_started = False
    #P1Won = False
    #P2Won = False
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

#def PressedP1():
#    global game_started, P1Cheated, P1Won, P2Won
#    if game_started:
#        if P2Won == False:
#            P1Won = True
#            basic.show_number(1, 0)
#            new_game()
#    else:
#        P1Cheated = True
#input.on_pin_pressed(TouchPin.P1, PressedP1)
#
#def PressedP2():
#    global game_started, P2Cheated, P1Won, P2Won
#    if game_started:
#        if P1Won == False:
#            P2Won = True
#            basic.show_number(2, 0)
#            new_game()
#    else:
#        P2Cheated = True
#input.on_pin_pressed(TouchPin.P2, PressedP2)

def new_game():
    basic.pause(3000)
    main()

def show(value):
    basic.show_string(value, 0)
    music.play_tone(Note.C, 1500)
    new_game()