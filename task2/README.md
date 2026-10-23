

\# Task 2 — Stock Portfolio Performance Tracker



A Python terminal application created for the Datheon Python Programming Internship.



\## Features



\- Interactive stock ticker, purchase price, and quantity input.

\- Offline sample stock prices loaded from CSV.

\- Calculates invested capital and current portfolio value.

\- Calculates profit/loss and percentage return per holding.

\- Exports results and a TOTAL row to `portfolio\_summary.csv`.

\- Validates tickers, prices, and share quantities.



\## Requirements



\- Python 3.8 or newer.

\- No external packages required.



\## Run the application



From the repository root in PowerShell:



```powershell

python .\\task2\\portfolio.py

```



Follow the prompts and enter stock holdings. The generated report is saved to `task2/portfolio\_summary.csv`.



\## Run tests



```powershell

python -m unittest discover -s task2\\tests -v

```



\## Files



\- `portfolio.py` — application logic.

\- `sample\_prices.csv` — offline demonstration prices.

\- `portfolio\_summary.csv` — generated report.

\- `tests/test\_portfolio.py` — automated tests.



\*\*Note:\*\* The supplied prices are illustrative values and are not live market quotes or investment advice.

