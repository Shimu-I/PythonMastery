# Exercise 1: The "Data Janitor" (Cleaning & Transformation)

### Scenario: You just received a messy inventory export. Before you can calculate net worth, you need to "scrub" the data.

## Your Tasks:

1. Import & Deduplicate: Load the CSV and remove the duplicate entry for the Laptop.

2. Fix Inconsistency: In the Category column, standardize "ELECTRO-NICS" to "Electronics" using .replace().

3. Handle Missing Values: * Fill the missing Price for the Toaster with the mean price of all items.

- Fill the missing Quantity for the Keyboard with 0.

4. Standardize Text: Make all Product names lowercase to keep them uniform.

5. Type Casting: Convert the In_Stock column (0s and 1s) into actual Boolean (True/False) values.


---

# Exercise 2: The "Business Analyst" (Selection & Aggregation)

### Scenario: Now that the data is clean, the shop owner wants to know which categories are performing best and which items need reordering.

## Your Tasks:

1. Selection: Create a new DataFrame called electronics_df that only contains the Product, Price, and Quantity for items in the "Electronics" category.

2. Calculated Column: Add a new column called Total_Value which is Price multiplied by Quantity.

3. Filtering: Find all products where the Quantity is less than 5 (items that need restocking).

4. Grouping: * Group the data by Category.

- Calculate the total (sum) Total_Value for each category.

- Find the average (mean) Price per category.

5. Specific Query: Use .loc or .iloc to print the details of the most expensive item in the inventory.