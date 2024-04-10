# Task_1
def positive_number_check(func):
    def wrapper(num):
        if num < 0:
            raise ValueError("Number must be positive")
        else:
            return func(num)
    return wrapper


@positive_number_check
def return_number(num):
    return num


try:
    result = return_number(-5)
    print(result)
except ValueError as e:
    print(e)


# Task_2
class PositiveNumberCheck:
    def __call__(self, func):
        def wrapper(num):
            if num < 0:
                raise ValueError("Number must be positive")
            else:
                return func(num)
        return wrapper


@PositiveNumberCheck()
def return_number(num):
    return num


try:
    result = return_number(-5)
    print(result)
except ValueError as e:
    print(e)


# Task_3
def commission_deduction(func):
    def wrapper(balance, amount):
        commission = 1  # Commission amount
        deducted_balance = balance - commission
        return func(deducted_balance, amount)  # Pass the deducted balance and amount to the function
    return wrapper


@commission_deduction
def transaction(balance, amount):
    if balance < amount:
        return "Error: Not enough balance"
    else:
        new_balance = balance - amount
        return f"Transaction successful. Remaining balance: {new_balance}"


balance = 100
amount_to_pay = 50
result = transaction(balance, amount_to_pay)
print(result)

balance = 10
amount_to_pay = 20
result = transaction(balance, amount_to_pay)
print(result)


