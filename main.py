def main():
    state = start_state # set start state
    str = input(">>") # read input string
    for char in str: # Step through characters in input
        state = transition[state](char) # apply lambda based on state
    if state in acceptstates: 
        print("Accept") # accept if final state is in accept states
    else:
        print("Reject")

def nonzeroDigit(c):
    match c:
        case "1":
            return True
        case "2":
            return True
        case "3":
            return True
        case "4":
            return True
        case "5":
            return True
        case "6":
            return True
        case "7":
            return True
        case "8":
            return True
        case "9":
            return True
        case _:
            return False     

def isDigit(c):
    match c:
        case "0":
            return True
        case "1":
            return True
        case "2":
            return True
        case "3":
            return True
        case "4":
            return True
        case "5":
            return True
        case "6":
            return True
        case "7":
            return True
        case "8":
            return True
        case "9":
            return True
        case _:
            return False

if __name__ == "__main__":
    main()


