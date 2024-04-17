# Coding

In coding you will be taking the algorithms from the develop phase and converting them into Python code. Remember you will be creating a program that is using **[](mvc)**.

## View

You will need to develop your UI (view) using **[](qt_designer)**. The videos below will show you how to use QT Designer and covers most of the concepts.

```{admonition} PyQt version
:class: danger
These videos are using PyQt5 while we are using PyQt6. Since PyQt6 is backwards compatible we will have access to all the features shown below.

The one difference is you need to use **`pyuic6`** instead of `pyuic5` when converting the `.ui` file to a `.py` file.
```

### Introduction

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7HwGQQXuxnI?si=xpqtqQGDBHvGrDvW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Menu Bar and Status

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Mu9I8qmykSA?si=lJ39oDlkWLbo45-O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Dialogue Box / Message Bos

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vIqw411xoj0?si=9X2IkLEOxgeLpusz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Working with Images

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CAin_TFP_T0?si=_qs8B9gJLvqO3EpH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Taking Input

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/REQsOjJBwbQ?si=nUrvSgBLxHAdGQ4n" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Signals and Slots

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3t8KhIdSGYQ?si=j-uOpJGiKA1mdfOG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Layout Management

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ZyaZvrbZxFA?si=aPC-s_kHCQWLnyGP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Date Widget

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gqilDuCUBmY?si=04AacJ4XPF6YtLrG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Calendar Widget & Progress Bar

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/EeEtSDnE5jY?si=o_cEmLHcCq-Vsmw_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Radio Buttons and Checkbox

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4PTFNVM8Naw?si=AFRG0cc_MUbbds-9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This will be saved to a `.ui` file which you will have to convert to Python script using the following command:

```
pyuic6 <your_file_name>.ui -o <your_file_name>.py
```

## Controller &mdash; Signals and Slots

Once you have created the UI you now need to create the controller. This is where all the program logic should be located. The **[](mvc)** has clear demarcation of responsibilities:

- Model &mdash; this should only deal with saving and retrieving data to and from the hard drive.
- Viewer &mdash; this should only deal with displaying output and collecting input.
- Controller &mdash; this should include all the processing of data.

By it's very nature a UI program is a **[](event_driven)**. This is where the concept of signals and slots comes in. The UI elements creates signals when the user interacts with them, eg. clicking a button. The Controller has code that will detect when a signal is created. It then directs the program towards the appropriate slot (method) for that specific signal.

```{admonition} Unit 1 subject matter covered:
- Generate user interfaces by investigating and applying useability principles
- Understand and use assignment: used to store the value of an expression into a variable
- Understand and use sequence: a number of instructions processed one after the other
- Understand and use selection: the next instruction to be executed depends on a ‘condition’
- Understand and use condition: a logical expression that evaluates to true or false
- Understand and use iteration: a number of instructions are repeated
- Understand and use modularisation: used for reducing the complexity of a system by deconstructing into more or less independent units or modules
- Recognise, describe and use good programming practices, including dependability, efficiency, testing, debugging, error correction, coding conventions including commenting, consistent naming conventions, code simplicity and portability
- Explore programming development tools to understand how to use them effectively
- Explore the use of a procedural text-based language for writing and modifying code and using existing code blocks or statements
- Explore the use of a procedural text-based language for interpreting programming language rules and syntax
- Explore the use of a procedural text-based language for analysing and critiquing the end result of code statements using input or output evidence, i.e. runtime evidence
- Explore functions and procedures with efficient and maintainable code that includes reusable coded components
- Explore functions and procedures with efficient and maintainable code that responds to keyboard and mouse events
- Explore functions and procedures with efficient and maintainable code that uses variables, selection structures, counted loops, while loops and single, multi-branch and nested conditional logic/statements
- Explore functions and procedures with efficient and maintainable code that uses operators, including arithmetic (+, –, *, /, integer, modulus, exponent), comparison (<, >, <=, >=, equal, not equal) and logical (AND, OR, NOT)
- Explore the purpose of code statements by writing code and using existing code blocks or statements
- Explore object/event triggers and develop explanations about their effect/s on user interfaces
- communicate and clarify knowledge and understanding about the purpose of code statements using code comments.
- Apply the use of operators, arithmetic: +, –, *, /, integer, modulus, exponent
- Apply the use of operators, comparison: <, >, <=, >=, equal, not equal
- Apply the use of operators, logical: AND, OR, NOT
- Output information to the screen in text-based or visual formats
- Generate components of a solution by using existing code or writing new code statements
- Generate modified code in response to new or existing information
- Generate functions/procedures with efficient and maintainable code that includes reusable code blocks or statements and responses to keyboard and mouse events
- Generate selection structures, counted loops, while loops, and single, multi-branch and nested conditional logic statements
- Generate local and global variables
- Generate a prototype digital solution in response to a problem
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```

```{admonition} Unit 2 subject matter covered:
- Communicate and clarify knowledge and understanding about the purpose of code statements using code comments.
- Understand SQL syntax and use SQL statements to solve a problem
- Generate SQL SELECT statements, including WHERE, GROUP BY, HAVING, ORDER BY, COUNT, MIN, MAX, AVG, IN, inner-joins and sub-queries to retrieve appropriate data from existing databases
- Generate SQL CREATE, INSERT, UPDATE and DELETE statements to create database tables and views, and modify stored data
- Generate a prototype digital solution to access, manipulate and display data in a website, mobile application or interactive media that enables data to be inserted, updated, retrieved and deleted from single and multiple tables
- Generate a prototype digital solution to access, manipulate and display data in a website, mobile application or interactive media that validates the data to be entered for reliability to ensure that the data is valid for use and storage
- Generate a prototype digital solution to access, manipulate and display data in a website, mobile application or interactive media that includes user interfaces that will enable the insertion, updating and selection of data from/to a database
- Generate a prototype digital solution to access, manipulate and display data in a website, mobile application or interactive media that creates procedural code to control user interaction, data validation, execution of SQL queries, manipulation and display of query results through the user interface
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```

```{admonition} Unit 3 subject matter covered:
- Recognise and compare different file formats and data structures appropriate to the context
- Determine file formats and data structures appropriate to the technology context
- Explore programming development tools to understand how to use them effectively
- Explore flexible development methods to support a variety of user profiles
- Explore methods of synthesising user interface, processing and data components to generate a prototype digital solution
- Analyse modularity and readability of program modules
- Explain code steps using comment syntax appropriate to the programming language
- Apply computational thinking processes, e.g. creating, debugging, persevering and collaborating to identify possible algorithmic approaches
- Apply data algorithms for cleaning and merging data sources and iterating through data records
- Generate algorithms as simple programs by using programming development tools
- Generate code that creates, reads, writes, opens and closes a file
- Generate data structures using SQL statements to INSERT, UPDATE and DELETE rows in a database
- Generate data structures using SQL CREATE, DROP and ALTER statements
- Generate data structures using SQL SELECT query, including WHERE, GROUP BY, HAVING, ORDER BY, sub-selection and inner-joins clauses
- Generate program modules that interact with users
- Generate program modules that interact with 2D data sources
- Generate program modules that validate data inputs
- Generate program modules that control the interactions in a digital solution
- Communicate and clarify knowledge and understanding about the purpose of code statements using code comments
- Synthesise user interface, processing and data components to generate a prototype digital solution
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```

```{admonition} Unit 4 subject matter covered:
- Generate a prototype digital solution that uses appropriate data structures including JSON or XML, to exchange data
- Explain the purpose of code and/or algorithm statements using code comments and annotations
- Use a suitable programming environment to implement algorithms using modularisation
- Use a suitable programming environment to receive data from an external source, and process and display the data in an appropriate format
- Use a suitable programming environment to incorporate existing code libraries (where applicable)
- Manipulate data from an external source
- Generate data structures using SQL CREATE, DROP and ALTER statements
- Generate data structures using SQL INSERT and UPDATE
- Generate data structures using SQL SELECT query, including WHERE, GROUP BY, HAVING, ORDER BY, sub-selection and inner-joins clauses
- Generate within programmed methods sequence
- Generate within programmed methods selection, i.e. use of single and nested, simple or compound conditions
- Generate within programmed methods iterations, including nesting or simple or compound conditions
- Generate within programmed methods use of code-specific arithmetic comparison and logical operators, including real division, integer division, modulus
- Generate within programmed methods use of data types, error-checking functions and conversions
- Generate within programmed methods use of structures, including one-dimensional collections, e.g. arrays and lists
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```