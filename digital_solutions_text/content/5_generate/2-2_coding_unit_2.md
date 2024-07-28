# Coding &mdash; Unit 2

## SQL

SQL (Structured Query Language) is a standard programming language specifically designed for managing and manipulating relational databases. It allows users to create, read, update, and delete data within a database, as well as to define and manage database structures. SQL is used to perform tasks such as querying data to retrieve specific information, inserting new data records, updating existing data, and deleting unwanted data. Additionally, SQL enables the creation of database schemas, the definition of relationships between different data tables, and the implementation of security measures to control access to the data. Its powerful and versatile nature makes SQL an essential tool for database management and analysis.

According to Stack Overflow's 2023 Developer Survey {cite}`stackoverflow_2023_stack`, SQL-based databases dominate the database management system (DBMS) market. It is estimated that approximately 90% or more of databases use SQL.

## Converting datastore to a database

One of the advantages of using MVC Architecture is ease of refactoring. You can change any of the three modules, as long as calling the methods that interconnect the modules remain the same. For example, if you want to change the datastore module so it uses a database, you can change that one module and leave the main and UI module alone.

The videos below build on our **[hangman game from Unit 1](2-1_coding_unit_1.md)** by changing the datastore to an SQLite database. The use of a database allows for other features like recording results and having multiple user, so the other two modules are adjusted to include these features. These video also provide an example of a **<a href="https://youtu.be/Vq1laKeSk9M?si=Jj15sQKSG8DpizUp" target="_blank">stacked widget</a>**.

**[Repository for the tutorial resources](https://github.com/DamoM73/gui_hangman_with_sql_starter)**

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=z4FVl8anWQUm8UJH&amp;list=PLXCOpHy94WuY2zt6lfl3sJmikB3Jj57r-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>