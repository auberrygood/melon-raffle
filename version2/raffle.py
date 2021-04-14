"""Randomly pick customer and print customer info"""

# Add code starting here
import random

# Hint: remember to import any functions you need from
# other files or libraries
from customers import get_customers_from_file



def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)
    
    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


if __name__ == "__main__":       # only do the following if the program is run directly (i.e. python3 raffle.py versus running some other program with run_raffle() being an imported function)
    run_raffle()                 # read customers.txt, organize data and store customers in customer list, then pick winner  