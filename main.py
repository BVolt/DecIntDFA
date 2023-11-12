states = ["q1", "q2", "q3", "q4", "q5", "q6"] # Set of States of decimal integer DFA
acceptstates = ["q2", "q3"] # Set of accept States of decimal integer DFA
start_state = "q1" # initial state
alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"] # alphabet for decimal integer
transition = { # transition function for all states
    "q1": lambda c: "q2" if nonzeroDigit(c) else("q3" if c=="0" else "q6"), 
    "q2": lambda c: "q2" if isDigit(c) else("q4" if c=="_" else "q6"),
    "q3": lambda c: "q3" if c == "0" else ("q5" if c=="_" else "q6"),
    "q4": lambda c: "q2" if isDigit(c) else "q6",
    "q5": lambda c: "q3" if c == "0" else "q6",
    "q6": lambda c: "q6"
    }

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