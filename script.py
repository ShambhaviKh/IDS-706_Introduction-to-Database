import sqlite3

# Connect to the database
conn = sqlite3.connect("university_database.db")
cursor = conn.cursor()
print("Connected to the database.\n")

#Show table schema
cursor.execute("PRAGMA table_info(university_rankings);")
schema = cursor.fetchall()
print("Table schema:")
for col in schema:
    print(col)
print("\n")

#View first 15 rows
cursor.execute("SELECT * FROM university_rankings LIMIT 15;")
rows = cursor.fetchall()
print("First 10 rows:")
for row in rows:
    print(row)
print("\n")

#List distinct years
cursor.execute("SELECT DISTINCT year FROM university_rankings ORDER BY year;")
years = [row[0] for row in cursor.fetchall()]
print(f"Years in dataset: {years}\n")

#Count total universities
cursor.execute("SELECT COUNT(*) FROM university_rankings;")
total = cursor.fetchone()[0]
print(f"Total universities in dataset: {total}\n")

# Check max, min, average score
cursor.execute("""
SELECT MIN(score), MAX(score), ROUND(AVG(score),2) 
FROM university_rankings;
""")
min_score, max_score, avg_score = cursor.fetchone()
print(f"Score statistics - Min: {min_score}, Max: {max_score}, Avg: {avg_score}\n")

#Check top 5 universities by score in 2014
cursor.execute("""
SELECT world_rank, institution, country, score
FROM university_rankings
WHERE year = 2014
ORDER BY score DESC
LIMIT 5;
""")
top_5_2014 = cursor.fetchall()
print("Top 5 universities in 2014 by score:")
for uni in top_5_2014:
    print(uni)
    
#INSERT: Add new university "Duke Tech" (2014)
cursor.execute("""
INSERT INTO university_rankings (year, world_rank, institution, country, score)
VALUES (2014, 350, 'Duke Tech', 'USA', 60.5);
""")
print("Inserted Duke Tech (2014, USA, world_rank 350, score 60.5)")

# Verify insertion
cursor.execute("""
SELECT * FROM university_rankings
WHERE institution='Duke Tech' AND year=2014;
""")
duke_tech = cursor.fetchone()
print(f"Verification of insertion: {duke_tech}\n")

#SELECT: Count Japanese universities in top 200 (2013)
cursor.execute("""
SELECT COUNT(*) FROM university_rankings
WHERE year=2013 AND country='Japan' AND world_rank <= 200;
""")
japan_top200 = cursor.fetchone()[0]
print(f"Number of Japanese universities in global top 200 (2013): {japan_top200}\n")

#UPDATE: Increase University of Oxford score by +1.2 in 2014
# First, show current score
cursor.execute("""
SELECT institution, score FROM university_rankings
WHERE institution LIKE '%Oxford%' AND year=2014;
""")
oxford_before = cursor.fetchone()
print(f"Oxford 2014 score before update: {oxford_before[1]}")

# Update score
cursor.execute("""
UPDATE university_rankings
SET score = score + 1.2
WHERE institution LIKE '%Oxford%' AND year=2014;
""")

#Verify update
cursor.execute("""
SELECT institution, score FROM university_rankings
WHERE institution LIKE '%Oxford%' AND year=2014;
""")
oxford_after = cursor.fetchone()
print(f"Oxford 2014 score after update: {oxford_after[1]}\n")

#DELETE: Remove universities in 2015 with score < 45
cursor.execute("""
DELETE FROM university_rankings
WHERE year=2015 AND score < 45;
""")
deleted_rows = cursor.rowcount
print(f"Deleted {deleted_rows} universities in 2015 with score < 45\n")

#Show top 5 rows for inspection
cursor.execute("SELECT * FROM university_rankings LIMIT 5;")
rows = cursor.fetchall()
print("Sample rows after CRUD operations:")
for row in rows:
    print(row)

# Commit changes and close
conn.commit()
conn.close()
print("\n All operations completed and changes saved.")