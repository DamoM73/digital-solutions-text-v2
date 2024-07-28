# Coding &mdash; Unit 2

## SQL

SQL (Structured Query Language) is a standard programming language specifically designed for managing and manipulating relational databases. It allows users to create, read, update, and delete data within a database, as well as to define and manage database structures. SQL is used to perform tasks such as querying data to retrieve specific information, inserting new data records, updating existing data, and deleting unwanted data. Additionally, SQL enables the creation of database schemas, the definition of relationships between different data tables, and the implementation of security measures to control access to the data. Its powerful and versatile nature makes SQL an essential tool for database management and analysis.

According to Stack Overflow's 2023 Developer Survey {cite}`stackoverflow_2023_stack`, SQL-based databases dominate the database management system (DBMS) market. It is estimated that approximately 90% or more of databases use SQL.

### Database Resources

For the following SQL section we will be using the following databases:

- [Chinook database](./assets/chinook.db)
- [Movies database](./assets/moives.db)
- [Repairs database](./assets/repairs.db)
- [School database](./assets/school.db)
- [Shares database](./assets/shares.db)
- [World database](./assets/world.db)

Below is the Relational Schemas for these databases

![relational schemas](./assets/relational_schemas.png)

### SELECT Statement

The SQL `SELECT` statement is used to retrieve specific data from tables within a relational database. The data is return in the form of a table.

#### SELECT Tutorials

Complete:

- [W3schools Tutorial](https://www.w3schools.com/sql/sql_select.asp) on the `SELECT` statement
- [W3schools Tutorial](https://www.w3schools.com/sql/sql_distinct.asp) on the `SELECT DISTINCT` statement

#### SELECT Exercises

Using the **Movies** database:

- Display the name of all the directors
- Display the name of all the members
- Display the details in the movie table
- Display all the years of release with no duplications
- Display the number of all movies on hire and when they are due back

### WHERE clause

The SQL `WHERE` clause is used to filter records in a database query to include only those that meet specified conditions.

#### WHERE Tutorials

Complete

- [W3schools Tutorial](https://www.w3schools.com/sql/sql_where.asp) on the `WHERE` clause
- [W3schools Tutorial](https://www.w3schools.com/sql/sql_and_or.asp) on the `AND`, `OR` and `NOT` operators
- [W3schools Tutorial](https://www.w3schools.com/sql/sql_like.asp) on the `LIKE` operator
- [W3schools Tutorial](https://www.w3schools.com/sql/sql_null_values.asp) on `NULL` values

#### WHERE Exercises

Using the Movies database

- Display the name of all the US directors
- Display the name of the all non-US directors
- Display the name of all the members who owe money
- Display all the movies that have 'the' in their title
- Display all the movies that start with Z

Using the Repairs database

- List the owners whose repair is ready to collect
- List the owners whose iMac is still being repaired

Using the World database

- Which countries have not achieved independence but still have a capital
- Which countries are missing information?
- List countries that are either constitutional monarchies or republics

### Calculations and functions

### ORDER BY

### GROUP BY

### Subqueries

### Join tables

### Record Management

## Converting datastore to a database

One of the advantages of using MVC Architecture is ease of refactoring. You can change any of the three modules, as long as calling the methods that interconnect the modules remain the same. For example, if you want to change the datastore module so it uses a database, you can change that one module and leave the main and UI module alone.

The videos below build on our **[hangman game from Unit 1](2-1_coding_unit_1.md)** by changing the datastore to an SQLite database. The use of a database allows for other features like recording results and having multiple user, so the other two modules are adjusted to include these features. These video also provide an example of a **<a href="https://youtu.be/Vq1laKeSk9M?si=Jj15sQKSG8DpizUp" target="_blank">stacked widget</a>**.

**[Repository for the tutorial resources](https://github.com/DamoM73/gui_hangman_with_sql_starter)**

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=z4FVl8anWQUm8UJH&amp;list=PLXCOpHy94WuY2zt6lfl3sJmikB3Jj57r-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>