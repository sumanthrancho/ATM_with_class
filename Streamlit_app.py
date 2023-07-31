import streamlit as st

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        st.write(f"Amount {amount:.2f} credited to your account. Current balance: {self.balance:.2f}")

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            st.write(f"Amount {amount:.2f} debited from your account. Current balance: {self.balance:.2f}")
        else:
            st.error("Insufficient balance.")

    def check_balance(self):
        st.write(f"Your account balance: {self.balance:.2f}")

    def change_pin(self, new_pin):
        self.pin = new_pin
        st.write("PIN changed successfully.")

def main():
    st.title("Bank Account ATM Operations")

    account_number = "123456789"
    pin = "1234"
    account1 = BankAccount(account_number, pin, 1000)

    entered_pin = st.text_input("Enter your PIN:", type="password")

    if st.button("Proceed"):
        if entered_pin != account1.pin:
            st.error("Wrong PIN. Transaction canceled.")
            return

        while True:
            st.write("ATM Operations:")
            st.write("1. Credit (Deposit) Money")
            st.write("2. Debit (Withdraw) Money")
            st.write("3. Check Balance")
            st.write("4. Change PIN")
            st.write("5. Exit")

            choice = st.number_input("Enter your choice (1-5):", min_value=1, max_value=5, step=1)

            if choice == 1:
                amount = st.number_input("Enter the amount to credit:", step=0.01, format="%.2f")
                account1.credit(amount)
            elif choice == 2:
                amount = st.number_input("Enter the amount to debit:", step=0.01, format="%.2f")
                account1.debit(amount)
            elif choice == 3:
                account1.check_balance()
            elif choice == 4:
                new_pin = st.text_input("Enter your new PIN:", type="password")
                account1.change_pin(new_pin)
            elif choice == 5:
                st.write("Thank you for using the ATM. Goodbye!")
                break
            else:
                st.error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
