# balance = 500
# correct_pin = 1234

# pin = int(input("Enter your PIN: "))

# if pin != correct_pin:
#     print("Incorrect PIN")

# else:
#     amount = int(input("Enter your amount: "))

#     if amount > balance:
#         print("Insufficient funds")

#     elif amount > 300:
#         print("Daily limit warning")

#     else:
#         result = balance - amount
#         print("New balance:", result)


# The ATM Withdrawal ValidatorReal-world use: Banking security and transaction limits.The Goal: Create a program that simulates an ATM cash withdrawal.

# The Rules:
# Set a starting bank balance (for example, $500) and a correct 4-digit PIN (for example, 1234) in variables.
# Ask the user to input their PIN. If it is wrong, print an error message and stop.If the PIN is right, ask how much money they want to withdraw.

# Check if the withdrawal amount is greater than the balance. If so, print an "Insufficient funds" message.Check if the withdrawal amount is greater than a daily limit of $300.

# If so, print a limit warning.If all checks pass, subtract the amount from the balance and print the new balance.
