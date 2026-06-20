# Stock Portfolio Tracker

## Goal
Build a simple stock tracker that calculates total investment based on manually defined stock prices.

## Scope
- User inputs stock names and quantity.
- Uses a hardcoded dictionary for stock prices (e.g., AAPL: 180, TSLA: 250).
- Displays total investment value and optionally saves the result to a .txt or .csv file.

## Key Concepts Used
- Dictionary — to store stock symbols and their prices
- Input/Output — to take user input and display results
- Basic arithmetic — to calculate subtotal and total investment
- File handling (optional) — to save the summary as .txt or .csv

## How It Works
1. The program shows a list of available stocks with their prices.
2. The user enters stock symbols and quantities one by one.
3. The program calculates the subtotal for each stock and the total investment.
4. A summary table is displayed showing stock, quantity, price, and subtotal.
5. The user can choose to save the summary as a `.txt` or `.csv` file.

## How to Run
```bash
python3 task2_stock_tracker.py
```

## Sample Output
==================================================

PORTFOLIO SUMMARY
Stock     Qty     Price     Subtotal
AAPL      10      ₹180      ₹1800

TSLA      5       ₹250      ₹1250
TOTAL INVESTMENT: ₹3050

## File Structure
STOCK TRACKER.PY

## Possible Future Improvements
- Fetch live stock prices using an API
- Add input from a CSV file instead of manual entry
- Track profit/loss based on buy and current price
