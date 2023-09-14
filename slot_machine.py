import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLUMNS = 3

symbol_count = {"A":2,
                "B":4,
                "C":6,
                "D":8
                }

symbol_value = {"A":5,
                "B":4,
                "C":3,
                "D":2
                }

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    
    return winnings,winning_lines
            

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row],end = "")
        print()
            
        

def deposit():
    while True:
        amount = input("what is the amount of deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("amount must be greater than 0")
        else:
            print("please enter a number")
            
    return amount

def get_num_of_lines():
    while True:
        lines = input(f"enter the number of lines to be on from 1 to {MAX_LINES}? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("enter a valid number of lines between 1 and 3")
        else:
            print("please enter a number")
            
    return lines

def get_bet():
    while True:
        amount = input("what is the amount of bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number")
            
    return amount

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"insufficient balance. your current balance is ${balance}")
        else: 
            break
    print(f"you are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLUMNS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    
    print(f"your winnings are ${winnings} and you won on lines", *winning_lines)
    return winnings - total_bet
    

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        ans = input("press enter to play and q to quit: ")
        if ans.lower() == "q":
            break
        balance += spin(balance)
    print(f"your final balance is ${balance}")
   
if __name__ == "__main__": 
    main()