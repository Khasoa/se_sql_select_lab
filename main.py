import sqlite3
import pandas as pd 

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Select all columns and rows from the employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# Assign the variable df_first_five to the employee number and last name from all employees in the employees table in the database.
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# Have the last name come before the employee number and assign to df_five_reverse.
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# Repeat the previous step, but this time use an alias to rename the employee number column as 'ID' and assign it to df_alias
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# Use CASE to bin where the jobTitles of President, VP Sales, or VP Marketing have the 'role' of "Executive", and the rest of the employees are "Not Executive".
df_executive = pd.read_sql("""SELECT jobTitle, 
                           CASE 
                           WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') 
                           THEN 'Executive' 
                           ELSE 'Not Executive' 
                           END AS role 
                           FROM employees""", conn)


# Find the length of the last name for all employees, and return only this data as a new column called name_length.
df_name_length = pd.read_sql("""SELECT lastName, LENGTH(lastName) AS name_length FROM employees""", conn)

# Return only one new column called short_title, that contains the first two letters of each person's job title
df_short_title = pd.read_sql("""SELECT jobTitle, SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)

# New table with data about orders placed with the company
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# Find the total amount for all orders, calculated as the sum of rounded total prices, where the total price for each order is the priceEach multiplied by the quantityOrdered. Make sure you are rounding this internal product result.
sum_total_price = pd.Series([pd.read_sql("""SELECT ROUND(priceEach * quantityOrdered) AS total_price FROM orderDetails""", conn)['total_price'].sum()])

# Return the original order date column, followed by three new columns that display the order date in this format, with column names 'day', 'month', and 'year', respectively.
df_day_month_year = pd.read_sql("""SELECT orderDate,
                                  strftime('%d', orderDate) AS day,
                                  strftime('%m', orderDate) AS month,
                                  strftime('%Y', orderDate) AS year
                                  FROM orders""", conn)

conn.close()