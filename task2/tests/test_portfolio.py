
import csv
import tempfile
import unittest
from pathlib import Path

from task2.portfolio import calculate_holding, load_prices, write_summary


class PortfolioTests(unittest.TestCase):

    def test_load_prices(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "prices.csv"
            path.write_text(
                "ticker,current_price\nAAPL,100\nMSFT,200\n",
                encoding="utf-8"
            )
            self.assertEqual(
                load_prices(path),
                {"AAPL": 100.0, "MSFT": 200.0}
            )

    def test_profit_calculation(self):
        result = calculate_holding("aapl", 3, 100, 120)
        self.assertEqual(result["ticker"], "AAPL")
        self.assertEqual(result["invested_value"], 300)
        self.assertEqual(result["current_value"], 360)
        self.assertEqual(result["profit_loss"], 60)
        self.assertEqual(result["return_pct"], 20)

    def test_loss_calculation(self):
        result = calculate_holding("MSFT", 2, 150, 120)
        self.assertEqual(result["profit_loss"], -60)
        self.assertEqual(result["return_pct"], -20)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            calculate_holding("AAPL", 0, 100, 120)

    def test_csv_total(self):
        holding = calculate_holding("AAPL", 2, 100, 125)

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "summary.csv"
            write_summary([holding], path)

            with path.open(newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(rows[-1]["ticker"], "TOTAL")
            self.assertEqual(rows[-1]["invested_value"], "200")
            self.assertEqual(rows[-1]["current_value"], "250")
            self.assertEqual(rows[-1]["profit_loss"], "50")


if __name__ == "__main__":
    unittest.main()
