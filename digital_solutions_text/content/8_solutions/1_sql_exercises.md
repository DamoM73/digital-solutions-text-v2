# SQL Exercises

## SELECT Exercises

### Movies database

Display the name of all the directors

```sql
SELECT dirname
FROM director
```

Display the name of all the members

```sql
SELECT memname
FROM members
```

Display the details in the movie table

```sql
SELECT *
FROM movie
```

Display all the years of release with no duplications

```sql
SELECT DISTINCT year
FROM movie
```

Display the number of all movies on hire and when they are due back

```sql
SELECT movienumber, duedate
FROM movies_onhire
```

## WHERE Exercises

### Movies Database

Display the name of all the US directors

```sql
SELECT dirname
FROM director
WHERE country = 'US'
```

Display the name of the all non-US directors

```sql
SELECT dirname
FROM director
WHERE country != 'US'
```

or

```sql
SELECT dirname
FROM director
WHERE NOT country = 'US'
```

Display the name of all the members who owe money

```sql
SELECT memname
FROM members
WHERE owes IS NOT NULL
```

Display all the movies that have 'the' in their title

```sql
SELECT movname
FROM movie
WHERE movname LIKE "%the%"
```

Display all the movies that start with Z

```sql
SELECT movname
FROM movie
WHERE movname LIKE "Z%"
```

### Repairs database

List the owners whose repair is ready to collect

```sql
SELECT owner
FROM repair
WHERE ready = "Yes"
```

List the owners whose iMac is still being repaired

```sql
SELECT owner
FROM repair
WHERE type = "iMac" AND ready = "No"
```

### World database

Which countries have not achieved independence but still have a capital

```sql
SELECT CountryName
FROM country
WHERE IndepenYear IS NULL AND Capital IS NOT NULL
```

Which countries are missing information?

```sql
SELECT CountryName
FROM country
WHERE CountryName IS NULL OR
    Continent IS NULL OR
    Region IS NULL OR
    Area IS NULL OR
    Population IS NULL OR
    LifeExp IS NULL OR
    GNP IS NULL OR
    Government IS NULL
```

List countries that are either constitutional monarchies or republics

```sql
SELECT CountryName
FROM country
WHERE Government LIKE "Constitutional Monarchy%" OR Government LIKE "%Republic"
```

## Filters and Aggregators exercises

### Movies Database

How many directors are there from Australia?

```sql
SELECT count(dirnumb)
FROM director
WHERE country = "Australia"
```

How many directors have the name John?

```sql
SELECT count(dirnumb)
FROM director
WHERE dirname LIKE "%John"
```

What is the longest movie?

```sql
SELECT max(length)
FROM movie
```

If I was to watch all the movies, back-to-back, how many minutes will I need (no pausing for toilet stops)

```sql
SELECT sum(length)
FROM movie
```

### Repairs Database

What is the average repair rate?

```sql
SELECT avg(rate)
FROM devices
```

How many repairs are waiting to be picked up?

```sql
SELECT count(job_numb)
FROM repair
WHERE ready = "Yes"
```

### Shares Database

How many companies are there in the high risk category?

```sql
SELECT count(CoCode)
FROM company
WHERE Risk = "High"
```

Which company has the biggest difference between their highest and lowest price?

```sql
SELECT CoName, max(YearHigh - YearLow)
FROM company
```

What is the cheapest, medium or low risk share on the New York Stock Exchange?

```sql
SELECT CoName, min(CurPrice)
FROM company
WHERE (Risk = "Low" OR Risk = "Med") AND Exchange = "NYSE"
```

List all shares that are currently within 10% of their highest price?

```sql
SELECT CoName
FROM company
WHERE CurPrice > YearHigh * 0.9
```

## ORDER BY Exercises

### Movies Database

List all the movies names in alphabetical order

```sql
SELECT movname
FROM movie
ORDER BY movname
```

What is the 5 oldest movie in stock?

```sql
SELECT movname, year
FROM movie
ORDER BY year
LIMIT 5
```

Display the movies in chronological order, and then alphabetical order within each year.

```sql
SELECT year, movname
FROM movie
ORDER BY year, movname
```

### School Database

List the name of the grade 6 students in alphabetical order

```sql
SELECT stname
FROM student
WHERE grade = 6
ORDER BY stname
```

What is the top three results in percentage

```sql
SELECT percent
FROM results
ORDER BY percent DESC
LIMIT 3
```

List all the boys' birthdays in order, then all the girls' birthdays in order, with their names

```sql
SELECT stname, born
FROM student
ORDER BY gender DESC, born
```

## GROUP BY and HAVING Exercises

### Movies Database

How many directors are there from each country?

```sql
SELECT country, COUNT(dirnumb)
FROM director
GROUP BY country
```

How many movies does each member number have on hire?

```sql
SELECT memberid, COUNT(movienumber)
FROM movies_onhire
GROUP BY memberid 
```

How many movies are stocked from each year?

```sql
SELECT year, COUNT(movienumb)
FROM movie
GROUP BY year
```

### School Database

What is the average result for each subject(code)?

```sql
SELECT subjnumb, AVG(percent)
FROM results
GROUP BY subjnumb
```

How many boys and girls in each grade?

```sql
SELECT gender, COUNT(stnumb)
FROM student
GROUP BY grade, gender
```

### Shares Database

How many companies are there in each risk category?

```sql
SELECT risk, COUNT(CoCode)
FROM company
GROUP BY risk
```

What is the cheapest, medium risk and cheapest low risk share on the New York Stock Exchange?

```sql
SELECT risk, CoName, MIN(CurPrice)
FROM company
WHERE (risk = 'Low' OR risk = 'Med') AND exchange = "NYSE"
GROUP BY risk
```

### Chinook Database

How many customers are there from each country?

```sql
SELECT Country, COUNT(CustomerId)
FROM customers
GROUP BY Country
```

How many customers in each city?

```sql
SELECT City, COUNT(CustomerId)
FROM customers
GROUP BY City
```

How much were the sales for each country?

```sql
SELECT BillingCountry, SUM(Total)
FROM invoices
GROUP BY BillingCountry
```

## Subqueries Exercises

### School Database

What are the percentage results for students in grade 7?

```sql
SELECT percent
FROM results
WHERE stnumb IN (
    SELECT stnumb
    FROM student
    WHERE grade = 7)
```

What subject is taught by the teacher in room A2?

```sql
SELECT subjname
FROM subject
WHERE tname IN (
    SELECT tname
    FROM teacher
    WHERE room = 'A2')
```

In which subjects did students score over 90%?

```sql
SELECT subjname
FROM subject
WHERE subjnumb IN (
    SELECT subjnumb
    FROM results
    WHERE percent > 90)
```

List the names of the students in grades 4 or 5 who scored over 50% for language.

```sql
SELECT stname
FROM student
WHERE (grade=4 OR grade=5) AND stnumb IN (
    SELECT stnumb
    FROM results
    WHERE percent > 50 AND subjnumb IN (
        SELECT subjnumb
        FROM subject
        WHERE subjname = 'language'))
```

List the names of students who do science.

```sql
SELECT stname
FROM student
WHERE stnumb IN (
    SELECT stnumb
    FROM results
    WHERE subjnumb IN (
        SELECT subjnumb
        FROM subject
        WHERE subjname = 'science'))
```

### Repairs Database

Who owns devices being repaired by Ted Carrol?

```sql
SELECT owner
FROM repair
WHERE id_numb IN (
    SELECT id_numb
    FROM technicians
    WHERE name = 'Carrol')
```

What are the names of the technicians who are still not expert (N) at repairing Macs?

```sql
SELECT name
FROM technicians
WHERE id_numb IN (
    SELECT id_numb
    FROM experience
    WHERE type = 'iMac' AND NOT qualification='E')
```

What rate will Byrne be charged for repairs?

```sql
SELECT rate
FROM devices
WHERE type IN (
    SELECT type
    FROM repair
    WHERE owner = 'Byrne')
```

List the owners whose devices have a high (H) priority for repair.

```sql
SELECT owner
FROM repair
WHERE type IN (
    SELECT type
    FROM devices
    WHERE priority = 'H')
```

What level of qualification has the technician who is doing James' repair job?

```sql
SELECT qualification
FROM experience
WHERE type IN (
    SELECT type
    FROM repair
    WHERE owner = 'James')
AND id_numb IN (
    SELECT id_numb
    FROM repair
    WHERE owner = 'James')
```

## JOIN Exercises

### Schools Database

What is the average percentage of the students for each teacher

```sql
SELECT subject.tname, AVG(results.percent)
FROM subject
INNER JOIN results
ON subject.subjnumb = results.subjnumb
GROUP BY subject.tname
```

List all the students taught by Mr Simms

```sql
SELECT student.stname
FROM subject
INNER JOIN results
ON subject.subjnumb = results.subjnumb
INNER JOIN student
ON results.stnumb = student.stnumb
WHERE subject.tname = 'Simms,G'
```

### Chinook Database
List all albums, including artist name

```sql
SELECT albums.Title, artists.name
FROM albums
INNER JOIN artists
ON albums.ArtistId = artists.ArtistId
```

List the name of all the tacks in the metal genre
```sql
SELECT tracks.Name
FROM tracks
INNER JOIN genres
ON tracks.GenreId = genres.GenreId
WHERE genres.Name = 'Metal'
```

List all the details of all Def Leppard tracks. 
```sql
SELECT *
FROM tracks
INNER JOIN albums
ON tracks.AlbumId = albums.AlbumId
WHERE albums.ArtistId IN (
    SELECT ArtistId
    FROM artists
    WHERE artists.Name = "Def Leppard")
```

## Record Management Exercises

### Movies Database

Add a new director record for Australian director Rachael Perkins

```sql
INSERT INTO director
VALUES (137,'Rachael Perkins','Australia')
```

Add a new member record. Name: Melissa Small, Address: 38 Loggers Ln

```sql
INSERT INTO members (memberid,memname,address)
VALUES (5065,'Melissa Small', '38 Loggers Ln')
```

Add movies on hire for Aliens being hired to Reis,E return date is in two weeks.

```sql
INSERT INTO movies_onhire
VALUES (1033,5024,'2019-09-9')
```

Update Fitzgerald,F's address to 13 Elms St

```sql
UPDATE members
SET address = '13 Elms St'
WHERE memname = 'Fitzgerald,F'
```

Lennon,S has paid her fees, adjust the database appropriately

```sql
UPDATE members
SET owes = NULL
WHERE memname = 'Lennon,S'
```

The store is doing a cull and getting rid of all movies before 1970, adjust the database appropriately.

```sql
DELETE FROM movies_onhire
WHERE movienumber IN (
    SELECT movienumb
    FROM movie
    WHERE year < 1970)

DELETE FROM movie
WHERE year < 1970
```
