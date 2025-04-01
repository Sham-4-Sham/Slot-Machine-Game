import random

def spin_reel():
    symbols = ['🍒', '🔔', '7️⃣ ', "BAR", '💎']
    return random.choice(symbols)

def check_win(reel1, reel2, reel3):
    if reel1 == reel2 == reel3:
        print("$$ JACKPOT $$")
        return "$$ JACKPOT $$"
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        print("Partial Match")
        return "Partial Match"
    else:
        print("No Match")
        return "No Match"

def slot_machine():
    too_low = 100
    cash = 1000
    fee = 100
    partial = 200
    jackpot = 400
    print("----------------------------------------------------------------------")
    print(f"---- Welcome your starting amount is ${cash}, playing fee is ${fee} ---- ")
    print(f"-- A partial match is worth ${partial} while a Jackpot is worth ${jackpot} --")
    

    while True:
        print("----------------------------------------------------------------------")
        if cash < too_low:
            print(f"Insufficient Funds, balance is ${cash}")
            break
        else:
            pass
        print(f"Your balance is ${cash}")
        if input("Press ENTER to play(or type 'exit' to quit). ") == 'exit':
            break
        
        reel1, reel2, reel3 = spin_reel(),spin_reel(),spin_reel()
        print("SPINNING......")
        cash = cash - fee
        print(f"[{reel1}]   [{reel2}]    [{reel3}]")

        message = check_win(reel1, reel2, reel3)

        
        if message == "Partial Match":
            cash = cash + partial
        elif message == "$$ JACKPOT $$":
            cash = cash + jackpot
        else:
            cash = cash
        


if __name__ =="__main__":
    slot_machine()

        
