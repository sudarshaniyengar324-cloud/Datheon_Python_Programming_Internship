
"""Datheon Task 2: Stock Portfolio Performance Tracker."""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PRICE_FILE = BASE_DIR / "sample_prices.csv"
SUMMARY_FILE = BASE_DIR / "portfolio_summary.csv"

FIELDS = [
    "ticker", "shares", "buy_price", "current_price",
    "invested_value", "current_value", "profit_loss", "return_pct"
]


def load_prices(path=PRICE_FILE):
    """Load sample stock prices from a CSV file."""
    prices = {}

    with open(path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not {
            "ticker", "current_price"
        }.issubset({name.strip().lower() for name in reader.fieldnames}):
            raise ValueError("CSV must contain ticker,current_price columns")

        reader.fieldnames = [
            name.strip().lower() for name in reader.fieldnames
        ]

        for row in reader:
            ticker = (row.get("ticker") or "").strip().upper()
            if not ticker:
                continue

            price = float(row["current_price"])
            if price <= 0:
                raise ValueError("Stock prices must be greater than zero")

            prices[ticker] = price

    if not prices:
        raise ValueError("No stock prices found")

    return prices


def calculate_holding(ticker, shares, buy_price, current_price):
    """Calculate the performance of one stock holding."""
    ticker = ticker.strip().upper()

    if not ticker:
        raise ValueError("Ticker cannot be empty")
    if not isinstance(shares, int) or isinstance(shares, bool) or shares <= 0:
        raise ValueError("Shares must be a positive whole number")
    if buy_price <= 0 or current_price <= 0:
        raise ValueError("Prices must be greater than zero")

    invested = shares * buy_price
    current = shares * current_price
    profit = current - invested

    return {
        "ticker": ticker,
        "shares": shares,
        "buy_price": round(buy_price, 2),
        "current_price": round(current_price, 2),
        "invested_value": round(invested, 2),
        "current_value": round(current, 2),
        "profit_loss": round(profit, 2),
        "return_pct": round(profit / invested * 100, 2),
    }


def write_summary(holdings, path=SUMMARY_FILE):
    """Write holdings and a portfolio total to CSV."""
    invested = sum(item["invested_value"] for item in holdings)
    current = sum(item["current_value"] for item in holdings)
    profit = current - invested
    percentage = profit / invested * 100 if invested else 0

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(holdings)

        writer.writerow({
            "ticker": "TOTAL",
            "shares": "",
            "buy_price": "",
            "current_price": "",
            "invested_value": round(invested, 2),
            "current_value": round(current, 2),
            "profit_loss": round(profit, 2),
            "return_pct": round(percentage, 2),
        })

    return path


def ask_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Enter a valid number greater than zero.")


def ask_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Enter a positive whole number.")


def main():
    try:
        prices = load_prices()
    except (OSError, ValueError) as error:
        print(f"Unable to load prices: {error}")
        return

    holdings = []

    print("\nSTOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 45)
    print("Offline sample prices; these are not live quotes.")
    print("Available tickers:", ", ".join(sorted(prices)))

    while True:
        ticker = input("\nStock ticker: ").strip().upper()

        if ticker not in prices:
            print("Unknown ticker. Choose from the available list.")
            continue

        buy_price = ask_positive_float("Purchase price per share ($): ")
        shares = ask_positive_integer("Number of shares: ")

        holding = calculate_holding(
            ticker, shares, buy_price, prices[ticker]
        )
        holdings.append(holding)

        print(
            f"{ticker}: invested ${holding['invested_value']:,.2f}, "
            f"current value ${holding['current_value']:,.2f}, "
            f"return {holding['return_pct']:+.2f}%"
        )

        if input("Add another holding? (y/n): ").strip().lower() not in {
            "y", "yes"
        }:
            break

    if not holdings:
        print("No holdings entered.")
        return

    print("\nPORTFOLIO SUMMARY")
    print("-" * 72)
    print(
        f"{'TICKER':<10}{'SHARES':>8}{'BUY PRICE':>13}"
        f"{'CURRENT':>13}{'P/L':>13}{'RETURN':>12}"
    )

    for item in holdings:
        print(
            f"{item['ticker']:<10}{item['shares']:>8}"
            f"${item['buy_price']:>11,.2f}"
            f"${item['current_price']:>11,.2f}"
            f"${item['profit_loss']:>11,.2f}"
            f"{item['return_pct']:>+10.2f}%"
        )

    invested = sum(item["invested_value"] for item in holdings)
    current = sum(item["current_value"] for item in holdings)
    profit = current - invested
    percentage = profit / invested * 100

    print("-" * 72)
    print(f"Total invested: ${invested:,.2f}")
    print(f"Current value:  ${current:,.2f}")
    print(f"Total profit/loss: ${profit:,.2f} ({percentage:+.2f}%)")

    try:
        output = write_summary(holdings)
        print(f"\nCSV report saved to: {output}")
    except OSError as error:
        print(f"Unable to save CSV report: {error}")


if __name__ == "__main__":
    main()