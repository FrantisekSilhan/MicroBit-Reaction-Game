let game_started = false
let P1Cheated = false
let P2Cheated = false
function main() {
    
    P1Cheated = false
    P2Cheated = false
    game_started = false
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
        }
        
        if (pins.digitalReadPin(DigitalPin.P1) == 1 && pins.digitalReadPin(DigitalPin.P2) == 0) {
            basic.showNumber(1, 0)
            game_started = false
        }
        
        if (pins.digitalReadPin(DigitalPin.P2) == 1 && pins.digitalReadPin(DigitalPin.P1) == 0) {
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
function new_game() {
    basic.pause(3000)
    main()
}

function show(value: string) {
    basic.showString(value, 0)
    music.playTone(Note.C, 1500)
    new_game()
}

