import re
class Card:
    def __init__ (self, owner, seria, balance, password):
        self.owner = owner
        self.seria = seria
        self.balance = balance
        self.password = password
        self.phone = ""


class ATM:
    def __init__ (self, bank):
        self.bank = bank
atm = ATM("NBU")
cards = []
    
def show_cards(s:list):
    count=0
    for card in s:
        count+=1
        print(f"{count}. Owner: {card.owner}, Seria: {card.seria}, Balance: {card.balance}")
def add_user(s:list):
    name = input("Enter user name: ")
    seria = input("Enter card seria: ")
    balance = float(input("Enter initial balance: "))
    password = input("Set a password: ")
    new_card = Card(name, seria, balance, password)
    print(f"User {name} added successfully.")
    new_card = Card(name, seria, balance, password)
    cards.append(new_card)

def deposit(s:list):
    seria = input("Enter card seria: ")
    password = input("Enter password: ")
    for card in s:
        if card.seria == seria and card.password == password:
            action = input("Choose action: 1. Deposit 2. Withdraw: ")
            if action == "1":
                amount = float(input("Enter amount to deposit: "))
                card.balance += amount
                print(f"Deposited {amount}. New balance is {card.balance}.")
            elif action == "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount <= card.balance:
                    card.balance -= amount
                    print(f"Withdrew {amount}. New balance is {card.balance}.")
                else:
                    print("Insufficient funds.")
    print("Card not found or incorrect password.")
def user_update(s:list):
    seria = input("Enter card seria to update: ")
    password = input("Enter password: ")
    for card in s:
        if card.seria == seria and card.password == password:
            action = input("Choose action: 1. Update Phone Number \n 2. Update Password: ")
            if action == "1":
                new_phone = input("Enter new phone number: ")
                card.phone = new_phone
                print(f"Phone number updated to {new_phone}.")
            elif action == "2":
                new_password = input("Enter new password: ")
                card.password = new_password
                print("Password updated successfully.")
    print("Card not found or incorrect password.")

def delete_user(s:list):
    seria = input("Enter card seria to delete: ")
    password = input("Enter password: ")
    for i, card in enumerate(s):
        if card.seria == seria and card.password == password:
            del s[i]
            print("User deleted successfully.")
            return
    print("Card not found or incorrect password.")

def show_exact_card(s:list):
    seria = input("Enter card seria to view details: ")
    password = input("Enter password: ")
    for card in s:
        if card.seria == seria and card.password == password:
            print(f"Owner: {card.owner}, Seria: {card.seria}, Balance: {card.balance}, Password: {card.password}")
            return
    print("Card not found or incorrect password.")

def atm_manager(s:list):
    while True:
        a = input("=== Main Menu === \n 1. add user \n 2. show cards \n 3. deposit/withdraw \n 4. update user info \n 5. delete user \n 6. show exact card \n 7. exit system \n Choose action: ")
        if a == "1":
            add_user(cards)
        elif a == "2":
            show_cards(cards)
        elif a == "3":
            deposit(cards)
        elif a == "4":
            user_update(cards)
        elif a == "5":
            delete_user(cards)
        elif a == "6":
            show_exact_card(cards)
        else:
            break

atm_manager(cards)