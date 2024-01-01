# Programming Paradigms

## Object Orientated Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes and models software as a collection of objects, each representing a real-world entity or concept. In OOP, an **object** is an **instance** of a **class**, which serves as a blueprint for creating objects. Objects can have **attributes** (data) and **methods** (functions) that define their behaviour.

The four main principles of OOP are:

1. **Encapsulation**: Encapsulation hides the internal details of an object and exposes only the necessary functionalities through methods. It helps in data protection and abstraction.

2. **Inheritance**: Inheritance allows one class (subclass or derived class) to inherit properties and methods from another class (superclass or base class). It promotes code reusability.

3. **Polymorphism**: Polymorphism enables objects of different classes to be treated as objects of a common superclass. It allows for flexibility and dynamic method invocation.

4. **Abstraction**: Abstraction focuses on representing essential features of an object while hiding unnecessary details. It simplifies complex systems by modelling them at a higher level.

OOP promotes the organization of code into modular, reusable, and maintainable components, making it a widely used programming paradigm in software development.

Python is one of the leading OOP languages currently in use.

We have covered OOP in the **<a href="https://damom73.github.io/python-oop-with-deepest-dungeon/" target="_blank">Deepest Dungeon course</a>**. If you need a refresher, start with the **<a href="https://damom73.github.io/python-oop-with-deepest-dungeon/oop_introduction.html" target="_blank">OOP Primer</a>**.

---

## Event Driven Programming

Event-driven programming is a programming paradigm where the flow of a computer program is determined by events, which can be user actions (like clicking a button), sensor inputs, or messages from other parts of the program. In event-driven programming, the program responds to these events by executing specific code (event handlers) associated with each event. 

Key concepts in event-driven programming include:

1. **Events:** Events are occurrences that trigger the execution of code. They can be generated by user interactions (e.g., mouse clicks, keyboard presses), system notifications (e.g., a file is downloaded), or timers.

2. **Event Handlers:** Event handlers are functions or methods that are executed in response to specific events. They define what happens when an event occurs.

3. **Event Loop:** An event loop is a central part of event-driven programs. It continuously listens for events and dispatches them to the appropriate event handlers.

Event-driven programming is commonly used in graphical user interfaces (GUIs), web development (e.g., handling user interactions on a web page), game development, and many other applications where the program's behaviour needs to respond to various external stimuli. Popular programming languages for event-driven programming include JavaScript (for web development), Python (with libraries like Tkinter for GUIs), and languages that support event-driven frameworks like C# with Windows Forms.

---

## MVC Architecture Pattern

The MVC architecture pattern turns complex application development into a much more manageable process. It is example of modularization and decomposition.

MVC stands for model-view-controller. Here's what each of those components mean:

- **Model:** The backend that contains all the data logic
- **View:** The frontend or user interface (UI)
- **Controller:** The brains of the application that controls how data is displayed

![MVC architecture](./assets/mvc.png)

### Why use MVC?

We use MVC to establish **separation of concerns(SoC)**.

The MVC pattern helps you break up the frontend and backend code into separate components. This way, it's much easier to manage and make changes to either side without them interfering with each other.

But this is easier said than done, especially when several developers need to update, modify, or debug a full-blown application simultaneously.

### Model (Data)

The model's job is to simply manage the data. Whether the data is from a database, API, JSON object or local file, the model is responsible for managing it.

### Views (UI)

The view's job is to decide what the user will see on their screen, and how.

### Controller (Brain)

The controller's responsibility is to pull, modify, and provide data to the user. Essentially, the controller is the link between the view and model.

Through **getter** and **setter** functions, the controller pulls data from the model and initializes the views.

If there are any updates from the views, it modifies the data with a setter function.



```{admonition} Unit 1 subject matter covered:
- Identify and describe code object/event triggers and their effect on user interfaces.
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```