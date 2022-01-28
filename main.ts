pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let game_started = false
let P1Cheated = false
let P2Cheated = false
let P1W = false
let P2W = false
function main() {
    
    P1Cheated = false
    P2Cheated = false
    game_started = false
    P1W = false
    P2W = false
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
input.onPinPressed(TouchPin.P1, function PressedP1() {
    
    if (game_started) {
        if (P2W == false) {
            P1W = true
            basic.showNumber(1, 0)
            new_game()
        }
        
    } else {
        P1Cheated = true
    }
    
})
input.onPinPressed(TouchPin.P2, function PressedP2() {
    
    if (game_started) {
        if (P1W == false) {
            P2W = true
            basic.showNumber(2, 0)
            new_game()
        }
        
    } else {
        P2Cheated = true
    }
    
})
function new_game() {
    basic.pause(3000)
    main()
}

function show(value: string) {
    basic.showString(value, 0)
    music.playTone(Note.C, 1500)
    new_game()
}

