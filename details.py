name = input("Enter your name: ")

pin = []

try:
    # Ensure the PIN is exactly 4 digits
    while len(pin) < 4:
        try: 
            in_pin = input("Enter your four-digit pin: ")
            if len(in_pin) == 4 and in_pin.isdigit():
                pin = list(map(int, in_pin))  # Convert each character into an integer
            else:
                raise ValueError("PIN must be exactly 4 digits!")
        except ValueError as e:
            print(f"Error: {e}")

    # Class for managing transaction, loan, and account details
    class TransLoanAndAcct:
        def __init__(self, salary, expense, year_end_bonus):
            self.salary = salary
            self.expense = expense
            self.year_end_bonus = year_end_bonus
            self.yearly_income = 0
            self.balance = 0

        def account_details(self):
            self.yearly_income = self.salary + self.year_end_bonus
            self.balance = self.yearly_income - self.expense

            print(f'Your take-home yearly income is {self.yearly_income}')
            print(f"After spending, your remaining balance is {self.balance}")
            if self.balance < 0:
                answer = input("Would you like to obtain a loan? ['Yes' or 'No']: ").lower()
                if answer == 'no':
                    print("Good. Thanks for banking with us!")
                elif answer == 'yes':
                    try:
                        loan_amount = int(input("How much loan do you want to obtain?: "))
                        if loan_amount > self.yearly_income:
                            print("You are not eligible for this amount")
                        else:
                            print(f"Your loan of {loan_amount} has been granted.")
                    except ValueError:
                        print("Please enter the loan amount in the correct format.")
                else:
                    print("Invalid response. Please answer with 'Yes' or 'No'.")

    # Create an instance of the class and call the methods
    acc = TransLoanAndAcct(30, 2400000, 450000)
    acc.account_details()
    #acc.loan_account()

except Exception as e:
    print(f"An error occurred: {e}")
