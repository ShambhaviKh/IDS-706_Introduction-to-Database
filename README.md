# Data Storage and Management — Assignment 1

## Project Overview

This project demonstrates basic operations with SQLite using the University Rankings dataset (2012–2015). The main objectives are:

1. Explore and understand the dataset.  
2. Perform CRUD (Create, Read, Update, Delete) operations.  
3. Document all steps and results.  

The project uses Python for database interaction and printing outputs, providing a clear and reproducible workflow.

---

## SQLite Setup and Verification

1. Checked SQLite installation to ensure the system can run database queries.  
2. Verified database connection in Python to confirm the database file is accessible and ready for queries.

---

## Why Python Was Used

Python was chosen because:

- It allows programmatic execution of multiple SQL queries.  
- Printing results is simple and clear, making it easy to document changes.  
- Sequential CRUD operations can be executed and verified immediately.  
- It provides a reproducible workflow for future modifications.  

---

## Python Script: `university_crud.py`

The script performs both data exploration and CRUD operations on the database.

### Functions / Operations in the Script

1. **Database Connection** – Connects to the SQLite database.  
2. **Check Table Schema** – Lists all columns and their data types in the university rankings table.  
3. **Preview Data** – Displays the first 15 rows of the dataset.  
4. **Data Summary** – Shows available years, total number of universities, and minimum, maximum, and average scores.  
5. **Top Universities by Score (2014)** – Lists the top 5 universities of 2014 by score.  
6. **INSERT Operation** – Adds a new university record, "Duke Tech" for 2014.  
7. **SELECT Operation** – Counts Japanese universities in the global top 200 for 2013.  
8. **UPDATE Operation** – Increases University of Oxford’s 2014 score by 1.2.  
9. **DELETE Operation** – Removes universities from 2015 with scores below 45.  
10. **Verification / Inspection** – Checks sample rows after performing CRUD operations.  
11. **Commit and Close Connection** – Saves all changes and closes the database connection.

---

## How to Run

1. Ensure SQLite is installed.  
2. Place `university_database.db` and `university_crud.py` in the same folder.  
3. Run the Python script from the terminal.  
4. Observe the outputs for dataset preview, summary statistics, and verification of insert, update, and delete operations.  

---

## Files in Repository

- `university_database.db` — SQLite database file  
- `university_crud.py` — Python script with all queries and operations  
- `README.md` — Project documentation  

---

## Summary of Operations Performed

| Operation  | Description                                               |
|------------|-----------------------------------------------------------|
| INSERT     | Added Duke Tech (2014, USA, world_rank 350, score 60.5) |
| SELECT     | Counted Japanese universities in top 200 (2013)          |
| UPDATE     | Increased University of Oxford 2014 score by 1.2         |
| DELETE     | Removed 2015 universities with score < 45                |
| DATA CHECK | Previewed first 15 rows, summary statistics, top universities by score |

---

## Notes

- All operations were executed using Python's sqlite3 module to automate query execution and output verification.  
- SQL statements also executed directly in the SQLite CLI.  
