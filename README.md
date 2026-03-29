# SQL Data Retrieval and Transformation Lab

## Overview

This project demonstrates foundational techniques for querying and transforming relational data using **SQL within Python**. The lab interacts with a **SQLite database** containing fictional company records and uses **Pandas** to load and manipulate query results.

The primary objective is to practice writing SQL queries that retrieve, transform, and organize data for analytical purposes. Throughout the exercise, SQL statements are executed directly from Python and returned as **Pandas DataFrames**, allowing further analysis or inspection.

The dataset represents the fictional **Northwind Company**, which contains employee and order records. In this lab, the focus is primarily on the **employees**, **orderDetails**, and **orders** tables.

This exercise simulates a scenario in which a data analyst in the company's HR department needs to retrieve and restructure employee records and perform basic transformations for reporting.

---

# Technologies Used

- Python  
- SQLite  
- Pandas  
- Pytest (for validation)

---

# Project Structure

sql_select_lab/
│
├── main.py
├── data.sqlite
├── test_main.py
├── Pipfile
└── README.md
### File Descriptions

**main.py**  
Contains the SQL queries used to retrieve and transform data from the database.

**data.sqlite**  
SQLite database containing fictional company data.

**test_main.py**  
Automated tests used to validate that the SQL queries return the correct outputs.

**Pipfile**  
Lists the project dependencies.

---

# Setup Instructions
1. Clone the repository
git clone <repo-url>
cd sql_select_lab
2. Install dependencies
pipenv install
3. Activate the virtual environment
pipenv shell
4. Run the program
python main.py
5. Run tests
pytest

The tests verify that each SQL query produces the expected result.

# Database Connection

The program connects to a local SQLite database using the Python sqlite3 module.

import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

SQL queries are executed using Pandas:

pd.read_sql("SELECT * FROM employees", conn)

This loads query results directly into a DataFrame.

# Key Concepts Demonstrated
1. Basic SQL Selection

Retrieve specific columns from the employees table.

Example:

SELECT employeeNumber, lastName
FROM employees

This allows analysts to limit queries to only the data needed.

2. Column Ordering

The order of columns returned can be customized.

SELECT lastName, employeeNumber
FROM employees
3. Column Aliasing

SQL aliases improve readability and allow renaming of columns.

SELECT lastName, employeeNumber AS ID
FROM employees

Aliases are commonly used in reporting and dashboards.

4. Conditional Categorization with CASE

The CASE statement creates conditional categories based on data values.

Example:

SELECT jobTitle,
       CASE
           WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing')
           THEN 'Executive'
           ELSE 'Not Executive'
       END AS role
FROM employees

This categorizes employees into executive and non-executive roles.

5. String Functions

SQL includes functions for manipulating text values.

Calculating string length
SELECT LENGTH(lastName) AS name_length
FROM employees
Extracting substrings
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees

These functions are useful for formatting or analyzing text data.

6. Numeric Calculations

Order data includes price and quantity fields. The total price for each order line is calculated as:

priceEach × quantityOrdered

The lab calculates the sum of rounded order totals:

SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderDetails

The resulting values are then summed using Pandas to compute the total revenue.

7. Date Extraction

SQL date functions allow components of a date to be extracted individually.

Example:

SELECT orderDate,
       strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM orders

This produces separate day, month, and year columns from the original date.

# Example Output

When the script is run, the program prints sample data from the database to the console:

---------------------Employee Data---------------------
...
-------------------End Employee Data-------------------

and

------------------Order Details Data------------------
...
----------------End Order Details Data----------------

These outputs help verify that the database connection and queries are functioning correctly.

# Closing the Database Connection

Once all queries are completed, the connection to the database is closed:

conn.close()

Closing connections is a good practice to prevent resource leaks.

# Skills Practiced

This lab strengthens practical skills in:

SQL query writing
Relational database interaction
Data transformation using SQL functions
Integrating SQL queries with Python
Working with Pandas DataFrames
Writing code that passes automated tests
# Future Improvements

Possible extensions for this project include:

Adding filtering with WHERE clauses
Grouping and aggregation using GROUP BY
Joining multiple tables
Creating summary reports for HR analytics
Visualizing query results using Python libraries such as Matplotlib or Seaborn

# Author

Lydia Khasoa