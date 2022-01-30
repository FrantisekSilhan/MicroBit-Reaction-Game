let game_started = false
let P1Cheated = false
let P2Cheated = false
// P1Won = False
// P2Won = False
function main() {
    
    // , P1Won, P2Won
    P1Cheated = false
    P2Cheated = false
    game_started = false
    // P1Won = False
    // P2Won = False
    basic.clearScreen()
    basic.pause(randint(30, 100) * 100)
    if (P1Cheated && P2Cheated) {
        show("C")
    } else if (P1Cheated) {
        show("B")
    } else if (P2Cheated) {
        show("A")
    } else {
        game_started = true
        basic.showIcon(IconNames.Yes, 0)
        music.playTone(Note.C, 1500)
    }
    
}

control.inBackground(main)
function check() {
    
    if (game_started) {
        if (pins.digitalReadPin(DigitalPin.P1) == 1 && pins.digitalReadPin(DigitalPin.P2) == 1) {
            basic.showString("R", 0)
            game_started = false
        } else if (pins.digitalReadPin(DigitalPin.P1) == 1) {
            basic.showNumber(1, 0)
            game_started = false
        } else if (pins.digitalReadPin(DigitalPin.P2) == 1) {
            basic.showNumber(2, 0)
            game_started = false
        }
        
        new_game()
    } else {
        if (pins.digitalReadPin(DigitalPin.P1) == 1) {
            P1Cheated = true
        }
        
        if (pins.digitalReadPin(DigitalPin.P2) == 1) {
            P2Cheated = true
        }
        
    }
    
}

input.onPinPressed(TouchPin.P1, check)
input.onPinPressed(TouchPin.P2, check)
// def PressedP1():
//     global game_started, P1Cheated, P1Won, P2Won
//     if game_started:
//         if P2Won == False:
//             P1Won = True
//             basic.show_number(1, 0)
//             new_game()
//     else:
//         P1Cheated = True
// input.on_pin_pressed(TouchPin.P1, PressedP1)
// 
// def PressedP2():
//     global game_started, P2Cheated, P1Won, P2Won
//     if game_started:
//         if P1Won == False:
//             P2Won = True
//             basic.show_number(2, 0)
//             new_game()
//     else:
//         P2Cheated = True
// input.on_pin_pressed(TouchPin.P2, PressedP2)
function new_game() {
    basic.pause(3000)
    main()
}

function show(value: string) {
    basic.showString(value, 0)
    music.playTone(Note.C, 1500)
    new_game()
}

