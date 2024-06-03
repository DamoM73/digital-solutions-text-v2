# Coding &mdash; Unit 1

The first step of your coding will always be setting up a new development environment. Instead of starting from scratch you will be provided with a code template. This is called boilerplate code in the industry.

## Boilerplate development environment

The Boilerplate for your code is hosted on GitHub, so we will fork this repo and create your own repo

To do this:

1. Go to the **[PyQt6 Boiler Plate repo](https://github.com/DamoM73/PyQt6-Boiler-Plate)**
2. Click on the green **Code** button
3. Click on the **copy** button beside the https url

![GitHub clone repo](assets/gh_clone_repo.png)

4. Open **GitHub Desktop**
5. Open the **File** menu
6. Click **Clone Repository**

![GitHub Desktop clone repo](assets/ghdt_clone_repo.png)

7. Choose the **URL** tab
8. Paste repo URL into **URL or username/repository** box
9.  Click **Clone**

![Github desktop clone repo dialogue](assets/ghdt_cloning_dialogue.png) 

The repo should now be copied onto your computer and ready for use.

## Opening repo in VS Code

We're going to use GitHub Desktop to coordinate our programming. We will use it to:

- Open our code in VS Code and set up the workspace correctly
- Save (commit) our finished code to our local repo
- Sync (Push) our committed code up to GitHub (origin)

```{admonition} Git and GitHub terminology
:class: note
Git and GitHub uses a range of different terminology. Here are some of the terms we will be using:

- **Repository or repo**: A repository is a special folder that stores all the files and their history for a project.
- **Commit**: When you make changes to files in a repository, a commit is takes a snapshot of those changes. Each commit has a unique name and a message explaining what changes were made.
- **Pull**: Pulling means getting the latest changes made by others and adding them to your own copy of the project.
- **Push**: Pushing is when you share your changes with others by sending them to a central place, like a website or server.
- **Remote**: A remote is a way to connect your local copy of the project with the online version. weare using GitHub. It allows you to share your work and collaborate with others.
- **Clone**: Cloning is making a copy of a project from a remote location to your own computer so you can work on it.
- **Local**: the copy of the repo that is on your computer
- **Origin**: the copy of the repo that is on a remote location
- **Fork**: making your own copy of someone else's project.

Note: the *other* that you could be working with might be you on another computer.
```

To use GitHub Desktop to open VS Code:

1. Open GitHub Desktop
2. Make sure the **Current repository** (top lefthand) is **PyQt6-Boiler-Plate**
3. Click **Open Visual Studio Code**

![Launch with GitHub Desktop](assets/launch_with_ghdt.png)

VS Code should now launch and you file panel of the lefthand side should show:

- PYQT6-BOILER-PLATE
- all the files in the image below

![Initial directory files](assets/initial_directory.png)

## Virtual Environment

Python virtual environments enables you to designate distinct areas for various Python projects. It's like having various rooms in your home, each with its unique furnishings and accents. You can work on various projects in a virtual environment without their interfering with one another. Each project gets a special "playground" with its own Python installation and particular libraries. A virtual environment is similar to walking into a specific room, and any Python programmes or libraries you use are exclusive to that project once you enter it. You can easily work on numerous Python projects because everything is kept organised and conflicts between projects are avoided.

```{admonition} requirements.txt
:class: note
The `requirements.txt` file lists all the external libraries that we need to install for this project. 

You can add extra libraries to this file, but to install them you will need to run the command:

- Windows: `pip install -r requirements.txt`
- macOS: `pip3 install -r requirements.txt`
```

### Create Virtual Environment

```{admonition} Windows Users
:class: error
If you are a Windows user, you might need to run a Powershell command before you create a virtual environment for the first time.

To do this:

1. Open Powershell **as Adminstrator**
2. Type the following: `Set-ExecutionPolicy Unrestricted -Force` then Enter

You shouldn't need to do this again, unless you get a new computer.
```

To create a virtual environment for this project:

1. Press `Ctrl` + `Shift` + `P` (Windows) / `Shift` + `Command` + `P` (macOS)
2. Type `Python` at the top and choose `Python: Create Environment...`

![Create venv 1](assets/create_venv_1.png)

3. At the top choose the **Venv** option

![Create venv 2](assets/create_venv_2.png)

4. Then choose the latest version of Python that you just installed

![Create venv 3](assets/create_venv_3.png)

5. Tick the box beside **requirements.txt** and then **ok**

![Create venv 4](assets/create_venv_4.png)

VS Code will now:

- create your virtual environment
- perform any necessary updates
- install the libraries in the **requirements.txt** file
- activate your virtual environment

## Make first commit and push

1. Change the text in README.md to the text below and then save it:

```
# FIA2 Project

This is my code for my FIA2 Project
```

2. In GitHub desktop write "Made first change" in the **Summary (required)** box
3. Then click **Commit to main**

![GitHub Desktop first commit](assets/ghdt_first_commit.png)

4. Click **Push origin** (you will receive an error)

![GitHub Desktop fist push](assets/ghtd_first_push.png)

5. Choose to **Fork this repository**
6. Choose **For my own purposes** and **Continue**
7. Click **Push origin** again


## Creating MVC Programs

In Unit 1 you will be creating a productivity application (desktop app) using the **[MVC Architecture](mvc)**. The videos below will introduce the concepts behind developing a MVC program using PyQt.

**[Repository for the tutorial resources](https://github.com/DamoM73/gui_hangman_starter)**

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/WZsdUKVdVsQ?si=4BgXfiwUj4aJ39hD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/T66K5Wasgww?si=LfN2_tmMosonsu7V" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/dMItEGj9cxg?si=l3c5wPty0M8Jf3dh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/MICrltBXE7E?si=Vrp9iCgzD0REdN6L" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/LL-8G63Wkik?si=KPdQFOFleJN8HNQI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/XKxy1b2x6ZU?si=RRqVTTLyR-A5lrkW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Programming Habits

The videos below show good Python programming practice.

### 5 Good Python Habits

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/I72uD8ED73U?si=IjnKHJQekKQnqlq0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### 5 Useful F-String Tricks In Python

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/EoNOWVYKyo0?si=zDl1_TdThHCqCRGz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
