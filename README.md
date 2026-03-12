# Daily Sales Register

## Problem

A local store currently records sales manually on paper. This makes it difficult to quickly calculate:

- Which products were sold
- How many units of each product were sold
- The total revenue generated during the day

To solve this problem, a Python script was developed to automate the daily sales registration process.

---

## Solution

The program allows the user to register multiple sales from the terminal.

Each sale includes:

- Product name
- Unit price
- Quantity sold

All sales are stored in a list using dictionaries.

The system is divided into three main functions:

- Sales registration
- Total calculation
- Final sales summary generation

---

## Project Structure

```bash
daily-sales/
│
├── main.py
├── sales_register.py
├── sales_totals.py
├── sales_summary.py
└── README.md

