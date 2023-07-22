print('''                                                                                OREM GAMBLERS INC
                                                                                     $£$
                                                                                try you luck!  
                                                                                tel: +254759192165
                                                                                mail:trilliondirham@gmail.com        
                                                                                              ''')
import random
import time
MAX_LINE=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbols_count={'A':2,'B':4,'C':6,'D':8}
symbols_values={'A':10,'B':3,'C':2,'D':1.5}
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

    else:
        winnings += values[symbol]*bet
        winning_lines.append(lines +1)
    return winnings,winning_lines

#generate symbols count
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
  #values  that go to every column
    columns=[]
    for _  in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#printing the columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" / ")
            else:
                print(column[row], end=" ")
        print() 

#asks user the deposit and verifies it
def deposit():
    while True:
        amount=input('Please enter the deposit amount:$ ')
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print('Amount must be greator than $0.0')
        else:
            print('Please enter a number')
    return amount

#determing number of gambling lines
def get_number_of_lines():
    while True:
        lines=input('Enter the number of lines to bet on (1-'+str(MAX_LINE) +')? ')
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines<=MAX_LINE:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Enter a valid number.')
    return lines

#Geting bet for users
def get_bet():
    while True:
        amount=input('What would you like to bet on each line?$ ')
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f'Amount must be between${MIN_BET}-${MAX_BET}.')
        else:
            print('Enter a number.')
    return amount

#reruning the programme
def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=lines*bet
        if total_bet>balance:
            print(f'You do not have enough money to bet that amount,your current balance is {balance}')
        else:
            break

    print(f'You are beting ${bet}  on  {lines} lines.Your total bet is equal to:${total_bet}')
    slots=get_slot_machine_spin(ROWS,COLS,symbols_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbols_values)
    print(f'You won ${winnings}')
    print(f'you won on lines:',*winning_lines)
    return winnings - total_bet

def main():
    balance=deposit()
    while True:
        print(f'current balance is ${balance}')
        response = input('Press enter to play(q to quit).')
        if response == 'q':
            break
        balance += spin(balance)

    print(f'You left with ${balance}')
    
   
main()
print('''WARNING! Gambling is addictive,
          play responsibly,not allowed to persons under age of majority''')
print('Receipt as at:',time.asctime(time.localtime()),', Nairobi branch')


