#!/bin/python3

# Starter Code for Project 1 Phase 2 of UPRM CIIC 3015 Fall 2023 

# Repeated symbol count for header messages
BORDER_COUNT = 25
# Repeats the symbol for formatted text borders
ASTERISK = "*" * BORDER_COUNT
UNDERSCORE = "-" * BORDER_COUNT

# Menu options to compare with choice
DEPOSIT_FUNDS_MENU_CHOICE = "1"
WITHDRAW_FUNDS_MENU_CHOICE = "2"
VIEW_BALANCE_MENU_CHOICE = "3"

# Only shown if balance is greater than or equal to zero
CLOSE_ACCOUNT_MENU_CHOICE = "4"

# Counters
penalty_cnt = 0
withdrawal_cnt = 0
deposit_cnt = 0

print("\n" + ASTERISK + "\nWelcome to Banco Popular!\n" + ASTERISK)

#
# Setup Account
#

print("\n" + UNDERSCORE + "\nAccount Setup\n" + UNDERSCORE + "\n")
name = input("Account Name: ")

#
# Starting Balance Loop
#

STARTING_BALANCE = 0
while STARTING_BALANCE <= 0:
    balance_str = input("Starting balance: $")
    try:
        input_amount = float(balance_str)
        if input_amount >= 0:
            if balance_str == format(input_amount, ".0f") or balance_str == format(input_amount, ".2f"):
                STARTING_BALANCE = input_amount
            else:
                continue

    except ValueError:
        continue

print(
    "\nWelcome new account member!\n"
    f"Account{name} created with starting balance: ${STARTING_BALANCE:.2f}")

#
# Main Account Menu and Loop
#

while True:

    # If the account balance is negative, the "Close Account" option will not appear
    if STARTING_BALANCE < 0:
        choice = input(
            "\nSelect option:\n"
            "(1) Deposit funds\n"
            "(2) Withdraw funds\n"
            "(3) View bank account balance\n"
        )
    else:
        choice = input(
            "\nSelect option:\n"
            "(1) Deposit funds\n"
            "(2) Withdraw funds\n"
            "(3) View bank account balance\n"
            "(4) Close account\n"
        )

    #
    # Deposit Funds
    #

    if choice == DEPOSIT_FUNDS_MENU_CHOICE:
        print("\n" + ("-" * BORDER_COUNT) + "\nDeposit funds\n" + ("-" * BORDER_COUNT))

        while True:
            try:
                deposit_input = input("\nAmount to deposit: $")
                deposit_amount = float(deposit_input)
                # The following if statement will only accept whole numbers or numbers with 2 decimal spaces
                if ((format(deposit_amount, ".0f") != deposit_input and format(deposit_amount, ".2f") != deposit_input)
                        or deposit_amount <= 0):
                    print("Transaction failed: Invalid deposit amount.")
                    break
                else:
                    STARTING_BALANCE += deposit_amount
                    deposit_cnt += 1

                    print(f"Account Name: {name}")
                    print(f"Deposit Amount: ${deposit_amount:.2f}")
                    print(f"New Balance: ${STARTING_BALANCE:.2f}\n")
                    break
            except ValueError:
                print("Transaction failed: Invalid deposit amount.")
                break

    #
    # Withdraw Funds
    #

    if choice == WITHDRAW_FUNDS_MENU_CHOICE:
        print("\n" + ('-' * BORDER_COUNT) + "\nWithdraw Funds\n" + ("-" * BORDER_COUNT + "\n"))

        while True:
            try:
                withdrawal_input = input("Amount to withdraw: $")
                withdrawal_amount = float(withdrawal_input)

                if ((format(withdrawal_amount, ".0f") != withdrawal_input
                     and format(withdrawal_amount, ".2f") != withdrawal_input) or withdrawal_amount <= 0):
                    print("Transaction failed: Invalid withdrawal amount.")
                    break
                else:
                    temp_balance = STARTING_BALANCE - withdrawal_amount
                    penalty_amount = 0

                    if temp_balance <= -5000:
                        print("Transaction failed: withdrawal amount exceeds overdraft limit.")
                        break
                    elif -1000 >= temp_balance > -5000:
                        penalty_amount = withdrawal_amount * 0.03
                        print("withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.")
                        penalty_cnt += 1
                    elif -100 > temp_balance > -1000:
                        penalty_amount = withdrawal_amount * 0.01
                        print("withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.")
                        penalty_cnt += 1

                    withdrawal_cnt += 1
                    STARTING_BALANCE -= (withdrawal_amount + penalty_amount)
                    print(f"Account name: {name}")
                    print(f"Withdrawal Amount: ${withdrawal_amount:.2f}")
                    print(f"Penalties: ${penalty_amount:.2f}")
                    print(f"New Balance: ${STARTING_BALANCE:.2f}")

                    remaining_cents = round(withdrawal_amount * 100)

                    hundred_dollar_bills = remaining_cents // 10000
                    remaining_cents %= 10000

                    fifty_dollar_bills = remaining_cents // 5000
                    remaining_cents %= 5000

                    ten_dollar_bills = remaining_cents // 1000
                    remaining_cents %= 1000

                    five_dollar_bills = remaining_cents // 500
                    remaining_cents %= 500

                    one_dollar_bills = remaining_cents // 100
                    remaining_cents %= 100

                    quarters = remaining_cents // 25
                    remaining_cents %= 25

                    dimes = remaining_cents // 10
                    remaining_cents %= 10

                    nickels = remaining_cents // 5
                    remaining_cents %= 5

                    pennies = remaining_cents

                    print("Currency withdrawn:")
                    if hundred_dollar_bills > 0:
                        print(f"$100s: {int(hundred_dollar_bills)}")
                    if five_dollar_bills > 0:
                        print(f"$50s: {int(fifty_dollar_bills)}")
                    if ten_dollar_bills > 0:
                        print(f"$10s: {int(ten_dollar_bills)}")
                    if five_dollar_bills > 0:
                        print(f"$5s: {int(five_dollar_bills)}")
                    if one_dollar_bills > 0:
                        print(f"$1s: {int(one_dollar_bills)}")
                    if quarters > 0:
                        print(f"quarters: {int(quarters)}")
                    if dimes > 0:
                        print(f"dimes: {int(dimes)}")
                    if nickels > 0:
                        print(f"nickels: {int(nickels)}")
                    if pennies > 0:
                        print(f"pennies: {int(pennies)}")
                    print("")
                break
            except ValueError:
                print("Transaction failed: Invalid withdrawal amount.")
                break

            #
    # View Account Balance
    #
    if choice == VIEW_BALANCE_MENU_CHOICE:
        print("\n" + ('-' * BORDER_COUNT) + "\nAccount Balance\n" + ("-" * BORDER_COUNT))
        print(f"Account name: {name}")
        print(f"Balance: ${STARTING_BALANCE:.2f}")

    #
    # Close Account
    #

    if choice == CLOSE_ACCOUNT_MENU_CHOICE:
        if STARTING_BALANCE < 0:
            continue
        else:

            percent_change = ((STARTING_BALANCE - input_amount) * 100 / input_amount)
            sign = '+' if percent_change >= 0 else ""

            print("\n" + ASTERISK + "\nClosing Account\n" + ASTERISK)
            print("\n" + ("-" * BORDER_COUNT) + "\nFinal Account Statement\n" + ("-" * BORDER_COUNT))
            print(f"Account name: {name}")
            print(f"Initial balance: ${input_amount:.2f}")
            print(f"Final balance: ${STARTING_BALANCE:.2f} ({sign}{percent_change:.2f}%)")
            print(f"Deposit count: {deposit_cnt}")
            print(f"Withdrawal count: {withdrawal_cnt}")
            print(f"Overdraft penalty count: {penalty_cnt}")
            print("\nThank you for banking with Banco Popular!")
            break
