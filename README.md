# Data Storage and Management — Assignment 1

## Project Overview

This project demonstrates basic operations with **SQLite** using the **University Rankings dataset** (2012–2015). The main objectives are:

1. Explore and understand the dataset.
2. Perform CRUD (Create, Read, Update, Delete) operations.
3. Document all steps and results.

The project uses **Python** for database interaction and printing outputs, providing a clear and reproducible workflow.

---

## SQLite Setup and Verification

1. **Check SQLite installation:**

```bash
sqlite3 --version
Verify database connection in Python:
import sqlite3
conn = sqlite3.connect("university_database.db")
cursor = conn.cursor()
This confirms the database file is accessible and ready for queries.
Why Python Was Used
Python was chosen because:
It allows programmatic execution of multiple SQL queries.
Printing results is simple and clear, making it easy to document changes.
Sequential CRUD operations can be executed and verified immediately.
It provides a reproducible workflow for future modifications.
Python Script: university_crud.py
The script performs both data exploration and CRUD operations on the database.
Functions / Operations in the Script
Database Connection
Connects to the SQLite database using sqlite3.connect.
Check Table Schema
PRAGMA table_info(university_rankings);
Lists all columns and their data types.
Preview Data
SELECT * FROM university_rankings LIMIT 15;
Shows the first 15 rows of the dataset.
Data Summary
SELECT DISTINCT year FROM university_rankings ORDER BY year;
SELECT COUNT(*) FROM university_rankings;
SELECT MIN(score), MAX(score), ROUND(AVG(score),2) FROM university_rankings;
Lists available years, total universities, and score statistics.
Top Universities by Score (2014)
SELECT world_rank, institution, country, score
FROM university_rankings
WHERE year = 2014
ORDER BY score DESC
LIMIT 5;
INSERT Operation
INSERT INTO university_rankings (year, world_rank, institution, country, score)
VALUES (2014, 350, 'Duke Tech', 'USA', 60.5);
Adds the new university "Duke Tech" for 2014.
SELECT Operation
SELECT COUNT(*) FROM university_rankings
WHERE year=2013 AND country='Japan' AND world_rank <= 200;
Counts Japanese universities in the global top 200 for 2013.
UPDATE Operation
UPDATE university_rankings
SET score = score + 1.2
WHERE institution LIKE '%Oxford%' AND year=2014;
Corrects University of Oxford’s 2014 score.
DELETE Operation
DELETE FROM university_rankings
WHERE year=2015 AND score < 45;
Removes universities from 2015 with scores below 45.
Verification / Inspection
SELECT * FROM university_rankings LIMIT 5;
Shows sample rows after CRUD operations.
Commit and Close Connection
Saves changes and closes the database connection.
How to Run
Ensure SQLite is installed.
Place university_database.db and university_crud.py in the same folder.
Open terminal in VS Code (or any terminal) and run:
python university_crud.py
Observe the printed outputs:
First rows of the dataset
Total universities and years
Min, max, and average scores
Verification of insert, update, and delete operations
Files in Repository
university_database.db — SQLite database file.
university_crud.py — Python script with all queries and operations.
README.md — Project documentation.
Summary of Operations Performed
Operation	Description
INSERT	Added Duke Tech (2014, USA, world_rank 350, score 60.5)
SELECT	Counted Japanese universities in top 200 (2013)
UPDATE	Increased University of Oxford 2014 score by 1.2
DELETE	Removed 2015 universities with score < 45
DATA CHECK	Previewed first 15 rows, summary statistics, top universities by score
Notes
All operations were executed using the Python sqlite3 module to automate query execution and output verification.
SQL statements can also be executed directly in SQLite CLI if desired.
Outputs from Python can be copied to the README or used for further documentation.
