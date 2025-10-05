-- 1. Show table schema
PRAGMA table_info(university_rankings);

-- 2. View first 15 rows
SELECT * FROM university_rankings
LIMIT 15;

-- 3. List distinct years
SELECT DISTINCT year
FROM university_rankings
ORDER BY year;

-- 4. Count total universities
SELECT COUNT(*) AS total_universities
FROM university_rankings;

-- 5. Check min, max, average score
SELECT MIN(score) AS min_score,
       MAX(score) AS max_score,
       ROUND(AVG(score),2) AS avg_score
FROM university_rankings;

-- 6. Check top 5 universities by score in 2014
SELECT world_rank, institution, country, score
FROM university_rankings
WHERE year = 2014
ORDER BY score DESC
LIMIT 5;

-- 7. Insert new university "Duke Tech" (2014)
INSERT INTO university_rankings (year, world_rank, institution, country, score)
VALUES (2014, 350, 'Duke Tech', 'USA', 60.5);

-- Verify insertion
SELECT * FROM university_rankings
WHERE institution='Duke Tech' AND year=2014;

-- 8. Count Japanese universities in top 200 (2013)
SELECT COUNT(*) AS japan_top200_2013
FROM university_rankings
WHERE year=2013 AND country='Japan' AND world_rank <= 200;

-- 9. Update University of Oxford score by +1.2 in 2014
-- Show current score before update
SELECT institution, score
FROM university_rankings
WHERE institution LIKE '%Oxford%' AND year=2014;

-- Update score
UPDATE university_rankings
SET score = score + 1.2
WHERE institution LIKE '%Oxford%' AND year=2014;

-- Verify update
SELECT institution, score
FROM university_rankings
WHERE institution LIKE '%Oxford%' AND year=2014;

-- 10. Delete universities in 2015 with score < 45
DELETE FROM university_rankings
WHERE year=2015 AND score < 45;

-- 11. Show top 5 rows for inspection
SELECT * FROM university_rankings
LIMIT 5;
