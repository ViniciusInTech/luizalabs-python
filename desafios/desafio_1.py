from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from itertools import count

menu = """

[u] Register user
[c] Create account
[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """

WITHDRAW_LIMIT = Decimal("500")
WITHDRAW_MAX_COUNT = 3

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class Account:
    id: int
    user_id: int
    number: str
    balance: Decimal = Decimal("0")
    statement: List[str] = field(default_factory=list)
    withdraw_count: int = 0

USERS: List[User] = []
ACCOUNTS: List[Account] = []

_user_seq = count(start=1)
_account_seq = count(start=1)

def find_user_by_email(email: str) -> Optional[User]:
    for u in USERS:
        if u.email.lower().strip() == email.lower().strip():
            return u
    return None

def find_account_by_number(number: str) -> Optional[Account]:
    for a in ACCOUNTS:
        if a.number.strip() == number.strip():
            return a
    return None

def register_user() -> None:
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    if not name or not email:
        print("Invalid data.")
        return
    if find_user_by_email(email):
        print("Email already registered.")
        return
    user = User(id=next(_user_seq), name=name, email=email)
    USERS.append(user)
    print(f"User created with id {user.id}")

def create_account() -> None:
    email = input("Email of the user: ").strip()
    user = find_user_by_email(email)
    if not user:
        print("User not found.")
        return
    number = f"ACC-{next(_account_seq):06d}"
    account = Account(id=len(ACCOUNTS) + 1, user_id=user.id, number=number)
    ACCOUNTS.append(account)
    print(f"Account created with number {account.number} for user id {user.id}")

def deposit() -> None:
    number = input("Account number: ").strip()
    account = find_account_by_number(number)
    if not account:
        print("Account not found.")
        return
    value_str = input("Amount to deposit: ").strip()
    try:
        value = Decimal(value_str)
    except:
        print("Invalid amount.")
        return
    if value <= 0:
        print("Invalid amount.")
        return
    account.balance += value
    account.statement.append(f"Deposit: R$ {value:.2f}")
    print("Deposit completed.")

def withdraw() -> None:
    number = input("Account number: ").strip()
    account = find_account_by_number(number)
    if not account:
        print("Account not found.")
        return
    value_str = input("Amount to withdraw: ").strip()
    try:
        value = Decimal(value_str)
    except:
        print("Invalid amount.")
        return
    if value <= 0:
        print("Invalid amount.")
        return
    if value > WITHDRAW_LIMIT:
        print("Withdrawal exceeds per-transaction limit.")
        return
    if account.withdraw_count >= WITHDRAW_MAX_COUNT:
        print("Daily withdrawal limit reached.")
        return
    if account.balance < value:
        print("Insufficient funds.")
        return
    account.balance -= value
    account.withdraw_count += 1
    account.statement.append(f"Withdraw: R$ {value:.2f}")
    print("Withdrawal completed.")

def show_statement() -> None:
    number = input("Account number: ").strip()
    account = find_account_by_number(number)
    if not account:
        print("Account not found.")
        return
    print("\n=========== STATEMENT ===========")
    if not account.statement:
        print("No transactions.")
    else:
        for line in account.statement:
            print(line)
    print(f"\nBalance: R$ {account.balance:.2f}")
    print("=================================")

def main() -> None:
    while True:
        option = input(menu).strip().lower()
        if option == "u":
            register_user()
        elif option == "c":
            create_account()
        elif option == "d":
            deposit()
        elif option == "w":
            withdraw()
        elif option == "s":
            show_statement()
        elif option == "q":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
