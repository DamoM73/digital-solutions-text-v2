# Good Practice

![xkcd goto](./assets/goto.png)

The are many good practices to following when programming. These need to be applied right from when the algorithms are first being developed.

## Dependability

In systems engineering, dependability is a measure of a system's maintainability and reliability.

### Maintainability

![code quality XKCD](assets/code_quality.png)

Within developer circles, it is frequently said that code is read more often than it is written. This is especially true when there are multiple programmers working on the same code. But it is also relevant in our situation where the other programmer may be a classmate or teacher lending assistance, or even the 'future' you trying to work out what 'present' you has done.

```{admonition} What is cognative load?
:class: tip
Cognitive load refers to the mental effort and capacity required for processing information and completing tasks. It can be caused by complex or poorly organized information, which can overwhelm a person's cognitive abilities. 

Reducing cognitive load is essential because it helps improve learning, problem-solving, and overall task performance. To reduce cognitive load, you can simplify information presentation, use clear and concise language, provide step-by-step instructions, and minimize distractions to make tasks more manageable and less mentally taxing.
```

Maintainability is about writing code that is easy-to-read and dissect. It reduces other programmers cognitive load by limiting the amount of information they need to memorise in order to understand your code. This way, other programmers can easily modify the parts related to a required change, without risking a chain reaction of errors in dependant modules.

```{admonition} What dependant modules?
:class: tip
If your code import and uses another module, your code is dependant on this module. This means any changes to the functioning of the imported module *can* break your code. This can be future complicated by the fact that the module you imported is most likely dependant on other modules, and these modules may also be dependant on other modules.

The series of libraries or modules where each one relies on the functionality provided by the previous one is call a **dependancy chain**.
```

![dependency XKCD](assets/dependency.png)

There are some simple steps that you can take to improve your code's maintainability:

- **follow the style guide**
  - provides consistency from one set of code to another (eg. indentation is always 4 spaces)
  - Python has a clear guide about how you should layout your code, it is called **<a href="https://peps.python.org/pep-0008/" target="_blank">PEP 8</a>**
  - fortunately, many style issues will be identified and highlighted by Python Extension in VSCode
  - additionally we will use the **Black** formatter to ensure our code is PEP 8 compliant
- **naming conventions**
  - these are normally found in the style guide, but are important enough to require there own mention
  - naming conventions can provide a great deal of information, for example, the type of object being named
  - there are more details further down this page.
- **function size**
  - appropriate modularisation of your code has a significant impact on its maintainability
  - simple rule of thumb &rarr; each function should only do one thing.
  - we will be using **Sourcery** to assess our functions and indicate if they are too unwieldly
- **comments**
  - code comments are useful for explaining what your code does
  - there are more details about comments further down this page

### Reliability

Reliability is the probability of a program producing an error or failing to process a task;

- In Digital Solutions, testing and useability considerations contribute to reliability.
- For example, predicting where errors are likely to occur (whether user or systems related) can inform mindful use programming constructs.

---

## Efficiency

A situation in which a system or machine uses minimal resources such as time and processing power while still achieving its goals; there are two types of efficiency:

### Algorithmic Efficiency

Algorithmic efficiency refers to the reliability, speed and programming methodology for developing succinct structures within an application

### Code Efficiency

Code efficiency is directly linked with algorithmic efficiency and the speed of runtime execution for software, and is the key element in ensuring high performance. Its goal is to reduce resource consumption and completion time as much as possible with minimum risk to the business or operating environment, e.g. using a FOR loop instead of repetitive IF, THEN and ELSE statements where appropriate.

---

## Effectiveness

A measure of the success of the algorithm to solve an identified problem; depending on the complexity of the problem, this could be tested with a desk check, but generally, the effectiveness of an algorithm can only be determined after the code has been generated and then tested within the appropriate context;

---

## Testing

Testing is the process of systematically verifying that your code works correctly. There are three types of testing which occur during the development and generation of code:

- **exploratory testing:** a form of testing that is done without a plan. In an exploratory test, you're just exploring the application. For example, checking and experimenting with the features when you run your application for the first time?
- **unit testing** testing that single components operate in the right way.
- **integrated testing:** testing multiple components at the same time.

---

## Debugging

In computer programming and software development, debugging is the process of finding and resolving bugs (defects or problems that prevent correct operation) within computer programs, software, or systems. Many programming languages and software development tools also offer programs to aid in debugging, known as debuggers.

---

## Error Correction

![xkcd error fixing](./assets/fixing_problems.png)

Dealing with errors is an integral part of any development process, to the point where seasoned coders eventually become experts at navigating and fixing the errors they create. 

When developing programs there are three types of error that can occur.

### Syntax errors

Syntax errors occur when the code given does not follow the syntax rules of the programming language. A program cannot run if it has syntax errors. Any such errors must be fixed first. A good integrated development environment (IDE) usually points out any syntax errors to the programmer.

Examples include:

- misspelling a statement, eg. writing pint instead of print
- using a variable before it has been declared
- missing brackets, eg. opening a bracket, but not closing it

### Logic errors

A logic errors is an error in the way a program works. The program can run but does not do what it is expected to do. Unlike a syntax error, a logic error does not usually stop a program from running. The program will run, but not function as expected.

Logic errors can be caused by the programmer:

- incorrectly using logical operators, eg. expecting a program to stop when the value of a variable reaches `5`, but you use `< 5` instead of `<= 5`
- incorrectly using Boolean operators
- unintentionally creating a situation where an infinite loop may occur
- incorrectly using brackets in calculations
- unintentionally using the same variable name at different points in the program for different purposes
- using incorrect program design

### Runtime errors

A runtime errors is an error that takes place during the running of a program. For example, writing a program that tries to access the sixth item in a list that only contains five items. A runtime error is likely to crash the program.

---

## Coding Conventions

### Code Simplicity

Code simplicity refers to the practice of writing computer programs in a clear, understandable, and straightforward manner. It involves using straightforward logic, clear and meaningful variable names, and minimizing unnecessary complexity. Simple code is easier to read, debug, and maintain, which makes it more efficient and less error-prone.

(naming_conventions)=
### Naming Conventions

Python has naming rules and naming conventions.

**Naming rules** will cause an error if they are not followed.

Naming rules:
  
- names can only contain letters, numbers and the `_` character
- names cannot contain spaces
- names cannot start with a number
- names are case sensitive (eg. `age` is not the same as `Age`)

**Naming conventions** are about conveying extra information to the reader. Not following naming conventions will not stop the programming from running, but the loss of the extra information will reduce the maintainability of the code.

Naming conventions:

- use descriptive names that explain the value stored in them:
  - `d = 30` &rarr; bad
  - `degrees = 30` &rarr; better
  - `degrees_celsius` = 30 &rarr; best
- normally use snake case for multiple word names:
  - replace the spaces with the `_` character
  - only use lower case letters
  - `this_is_snake_case`
- Capitalize all letter for names of constants (variables whose value will not change)
- use camel case for class name
  - Capitalise the first letter of each word
  - remove all spaces
  - `ThisIsCamelCase`
- Do not use the names of keywords (eg. `print`, `for`, `while` and so on)

(commenting)=
### Commenting

![commenting comic](./assets/future_self.png)

If your follow the naming convention of using meaningful names, most of your code should make sense without comments. Never-the-less, there are two places where comments are still needed:

- **doc strings** &mdash; the comment that comes straight after a function definition. It explains a function's inputs, processes and outputs.
- **block comments** &mdash; these are used when your code is tricky and it is not obvious how it works.

### Code Portability

Code portability is writing code that can run on different platforms and systems without modification. This enhances its usefulness. We will be using Python, a language that can be run on Windows, macOS, Linux and well as embedded systems, iOS, Android and the web.

```{admonition} Unit 1 subject matter covered:
- Recognise, describe and use good programming practices, including dependability, efficiency, testing, debugging, error correction, coding conventions including commenting, consistent naming conventions, code simplicity and portability
{cite}`qcaa_2017_digital`
```