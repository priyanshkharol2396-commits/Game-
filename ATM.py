balance = 7000
pin = '1234'
attempts = 0  # count wrong attempts

while attempts < 3:
    user_pin = input("enter your pin : ")

    if user_pin == pin:
        print("your balance is :", balance)
        amount = int(input("enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("congrats! amount received.", "new balance is :", balance)
        else:
            print("insufficient balance!")
        break
    else:
        print("incorrect pin!")
        attempts += 1
        print("attempts left:", 3 - attempts)

if attempts == 3:
    print("account locked")
