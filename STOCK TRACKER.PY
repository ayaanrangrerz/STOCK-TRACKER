"""
TASK 2: Stock Portfolio Tracker
Goal: Calculate total investment based on manually defined stock prices.
Scope: User inputs stock names + quantity, hardcoded price dictionary,
       display total investment, optionally save to .txt or .csv.
Key Concepts: dictionary, input/output, basic arithmetic, file handling (optional)
"""

import csv

# Hardcoded stock prices (per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "INFY": 1500,
    "TCS": 3800,
}


def show_available_stocks():
    print("Available stocks and prices (per share):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ₹{price}")


def get_portfolio_input():
    portfolio = {}  # symbol -> quantity

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found in price list. Please choose from the available stocks.")
            continue

        qty_input = input(f"Enter quantity of {symbol}: ").strip()
        if not qty_input.isdigit():
            print("Please enter a valid whole number for quantity.")
            continue

        quantity = int(qty_input)
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        # If stock already entered, add to existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_investment(portfolio):
    details = []  # list of (symbol, quantity, price, subtotal)
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = price * quantity
        total += subtotal
        details.append((symbol, quantity, price, subtotal))

    return details, total


def display_summary(details, total):
    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Subtotal':<12}")
    print("-" * 50)
    for symbol, quantity, price, subtotal in details:
        print(f"{symbol:<10}{quantity:<8}₹{price:<9}₹{subtotal:<11}")
    print("-" * 50)
    print(f"TOTAL INVESTMENT: ₹{total}")
    print("=" * 50)


def save_to_txt(details, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("PORTFOLIO SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Subtotal':<12}\n")
        f.write("-" * 50 + "\n")
        for symbol, quantity, price, subtotal in details:
            f.write(f"{symbol:<10}{quantity:<8}Rs.{price:<8}Rs.{subtotal:<10}\n")
        f.write("-" * 50 + "\n")
        f.write(f"TOTAL INVESTMENT: Rs.{total}\n")
    print(f"Saved summary to {filename}")


def save_to_csv(details, total, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Subtotal"])
        for symbol, quantity, price, subtotal in details:
            writer.writerow([symbol, quantity, price, subtotal])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    print(f"Saved summary to {filename}")


def main():
    print("=" * 50)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    show_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    details, total = calculate_investment(portfolio)
    display_summary(details, total)

    choice = input("\nSave summary to file? (txt/csv/no): ").strip().lower()
    if choice == "txt":
        save_to_txt(details, total)
    elif choice == "csv":
        save_to_csv(details, total)
    else:
        print("Summary not saved.")


if __name__ == "__main__":
    main()