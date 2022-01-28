pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

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
    game_started = True
    if P1Cheated and P2Cheated:
        show("C")
    elif P1Cheated:
        show("B")
    elif P2Cheated:
        show("A")
    else:
        basic.show_icon(IconNames.YES, 0)
        music.play_tone(Note.C, 1500)
control.in_background(main)

def PressedP1():
    global game_started, P1Cheated, P2Cheated
    if game_started:
        #dodělat remízu a lock
        basic.show_number(1, 0)
        new_game()
    else:
        P1Cheated = True
input.on_pin_pressed(TouchPin.P1, PressedP1)

def PressedP2():
    global game_started, P1Cheated, P2Cheated
    if game_started:
        #dodělat remízu a lock
        basic.show_number(2, 0)
        new_game()
    else:
        P2Cheated = True
input.on_pin_pressed(TouchPin.P2, PressedP2)

def new_game():
    basic.pause(3000)
    main()

def show(value):
    basic.show_string(value, 0)
    music.play_tone(Note.C, 1500)
    new_game()