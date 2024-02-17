from .modules import getch

def input_custom(message: str=": ",
                 hint: str="Input",
                 quit: str="\x1b"):
    message = "\033[?25l" + message
    osize = len(message)
    print(message, end="")
    print(f"\033[0;2m{hint}\033[0m", end="\r")
    while True:
        ch = getch()
        if ch == '':
            continue
        if ch == quit:
            if getch(timeout=0.1) == "[":
                match getch():
                    case "A":
                        print("Up")
                    case "B":
                        print("Down")
                    case "C":
                        print("Left")
                    case "D":
                        print("Right")
            else:
                break
        elif ord(ch) == 13:
            print("\033[?25h")
            return message[osize:]
        elif ch == "\x7f":
            if len(message) >= 12:
                message = message[:-1]
        else:
            message += str(ch)
        print("\033[K" + message, end="\r")

    print("\033[?25h")
    return None
