## 2.1: Programming Basics

### Overview

In this class, students will learn about the basics of Python programming, including pseudocoding, Python syntax, and how to work with variables, different data types, and basic operators. They will also learn how to handle user inputs and apply type casting.

### Class Objectives

By the end of today's class, the students will be able to:

* Use pseudocode to map out a problem.
* Understand how to use code comments.
* Understand Python syntax.
* Create variables.
* Perform calculations with operators.
* Understand basic data types and how to convert them with type casting.
* Print text to the screen.
* Create, use, and manipulate strings.

---

### Instructor Notes

In this module, students will embark on a comprehensive journey into Python programming, starting from the rudimentary concept of pseudocoding and its application in problem-solving. They will learn Python syntax, understand and create variables, and acquaint themselves with Python's fundamental data types. The lesson also delves into the use of code comments, type casting, basic Python functions like `print()`, and the collection of user input. Furthermore, they'll explore simple mathematical operations, string formatting, and manipulations, including f-strings, escape characters, multiline printing, and other string functions. Throughout the lesson, practical activities and regular reviews will reinforce their understanding and enable them to apply these concepts effectively, thus laying a robust foundation for their Python programming skills.

In this module, we use Anaconda environments. This curriculum has been tested with Python 3.10, but updates to packages and variances in student machines can still cause conflicts to occur. If a student has an error that you believe to be related to Python 3.10, at your discretion you can instruct them to create a new environment using a different Python version. If you believe that an update has introduced a bug at a curriculum level, attempt to find a suitable workaround for the moment and submit a report using the Boot Camp Feedback Form.

* Students should have installed Anaconda in the previous module. Today, the students will be using Python from their Anaconda installation. Take a moment to ensure that everyone has installed Anaconda.

* Students may find themselves frustrated by some of the quirks of Python. It’s important that you maintain a positive tone and are prepared to help the class fix whatever bugs they encounter.

* Try to identify confused students who may be reluctant to raise their hands and ask for assistance. Also, regularly encourage the class to ask questions whenever they are confused, and reassure them that confusion is simply part of the learning process.

Although the Python solution files can be run as scripts from the command line using `python script_name.py`, it’s a good idea to introduce each step in these solutions using the command line interpreter, which is covered in the Introduction to Python instructor demonstration. This way, students get a clearer understanding of what each line of code does. You may wish to run the script version after running each line from the command line interpreter.

As debugging and troubleshooting are critical skills for students to learn, take advantage of the errors that come up naturally during class in either your code or your students’ code whenever possible. Encourage students to analyze the problem and suggest solutions to each other. Time constraints can make it difficult to troubleshoot every error that arises, especially with larger class sizes. Encourage students to screenshot their code and the error they are getting as soon as something goes wrong. Have them post the screenshots in the “live” channel in Slack, and have TAs and students who are already finished with the activity attempt to troubleshoot the problem. Have your TAs call out any errors that may deserve dedicated class time for troubleshooting.

Even with these best practices in place, some students will have errors that can’t be solved during class time. Make sure TAs are encouraging students to attend office hours for any debugging that they still need help with at the end of class.

---

### Class Slides

* The slides for this lesson can be viewed on Google Drive here: [Lesson 2.1 Slides](https://docs.google.com/presentation/d/14nI-x9hLDCTo9m-z_S1iTWvheriGRmcYula8_q4jIjo/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit).

**Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

---

### Time Tracker

| Start Time | Number | Activity                                           | Duration |
| ---------- | ------ | -------------------------------------------------- | -------- |
| 6:30 PM    | 1      | Instructor Do: Introduction to Class               | 0:05     |
| 6:35 PM    | 2      | Instructor Do: Introduction to Pseudocoding        | 0:15     |
| 6:50 PM    | 3      | Students Do: Pseudocoding Practice                 | 0:10     |
| 7:00 PM    | 4      | Review: Pseudocoding Practice                      | 0:05     |
| 7:05 PM    | 5      | Instructor Do: Introduction to Python              | 0:10     |
| 7:15 PM    | 6      | Students Do: Variables                             | 0:10     |
| 7:25 PM    | 7      | Review: Variables                                  | 0:05     |
| 7:30 PM    | 8      | Instructor Do: Inputs and Prompts                  | 0:15     |
| 7:45 PM    | 9      | Students Do: Input Order                           | 0:15     |
| 8:00 PM    | 10     | Review: Input Order                                | 0:05     |
| 8:05 PM    | 11     | BREAK                                              | 0:15     |
| 8:20 PM    | 12     | Instructor Do: Perform Calculations with Python    | 0:15     |
| 8:35 PM    | 13     | Students Do: Basic Calculator                      | 0:15     |
| 8:50 PM    | 14     | Review: Basic Calculator                           | 0:05     |
| 8:55 PM    | 15     | Instructor Do: Printing Complex Strings            | 0:10     |
| 9:05 PM    | 16     | Students Do: Print Presentation                    | 0:15     |
| 9:20 PM    | 17     | Review: Print Presentation                         | 0:05     |
| 9:25 PM    | 18     | Instructor Do: Class Wrap Up                       | 0:05     |
| 9:30 PM    |        | END                                                |          |

### 1. Instructor Do: Introduction to Class (5 min)

Open the slideshow as you cover the following talking points:

* Welcome students, and explain that this lesson will introduce them to coding basics in Python, an industry standard, high-level, and readable programming language commonly used for machine learning and AI applications.

* Before getting into Python, they will be introduced to fundamental coding concepts via pseudocoding.

---

### 2. Instructor Do: Introduction to Pseudocoding (15 min)

**Corresponding Activity:** [01-Ins_Pseudocoding](Activities/01-Ins_Pseudocoding/)

You may use the solution in the corresponding activity folder to assist you in this introduction to pseudocode, however the text is also provided in the slides.

Explain to students that before jumping into code, we will define computational thinking and practice this way of thinking in everyday life.

Continue using the slideshow to accompany this demonstration.

#### Computational Thinking

Explain that computational thinking is the process of understanding a complex problem by breaking that problem into smaller parts, and then developing possible solutions that can be clearly presented in a way that computers and/or humans can understand.

This framework for tackling problems helps with foundational concepts as people learn how to code, and will continue to serve programmers as they encounter increasingly complex problems.

The four cornerstones of computational thinking are:

* Decomposition
* Pattern recognition
* Abstraction
* Testing and debugging algorithms

#### Pseudocode

Explain that these cornerstones will be explored in greater depth by practicing computational thinking to accomplish a simple daily task.

In this activity, you will reverse-engineer pseudocode, which is a plain-language description of what our code will do, to write an algorithm for putting away the dishes. Afterwards, students will get more practice by writing an algorithm for another common task. But first they will watch a short video (included in the slides) on computational thinking and pseudocode to further familiarize themselves with the process:

#### Putting Away the Dishes the Computational Way

Explain to students that computational thinking is an essential tool for developers, but it can also be used to solve problems that we encounter every day. In order to become more comfortable with the computational thinking framework, we will practice using it by applying it to a problem that we commonly encounter: a load of clean dishes that need putting away.
Here, you will again go through the four cornerstones of computational thinking to break down the task of putting away the dishes:

* Decomposition
* Pattern recognition
* Abstraction
* Testing and debugging algorithms

Mention that in order to do this you will be making use of pseudocode.

**Setup for activity:**

User story:

* As a member of a household, I want to use computational thinking to develop an algorithm for putting away the dishes.

Acceptance criteria:

* It is done when I have read through the Code Demo and can apply the four cornerstones of computational thinking (decomposition, pattern recognition, abstraction, and algorithms) to a regularly repeated task.

* It is done when I have identified a task that I complete regularly.

* It is done when I have used pseudocoding to apply the four cornerstones of computational thinking to the daily task.

Explain that you will be creating an algorithm, or a step-by-step solution to the problem of putting away the dishes that can be easily replicated. In order to do this, you will also use pseudocoding and code snippets to address the other three pillars of computational thinking, starting with decomposition, to set us up to create an algorithm.

Point out that a code snippet is a portion of code. We will use Python syntax to pseudocode our process, just like we would if we were working in a Python file.

#### Decomposition

Explain that decomposition refers to breaking down a problem into smaller tasks. Breaking a complex problem into smaller problems or subtasks makes solving the larger problem more manageable.

Since the problem that you are working on is putting away the dishes, you can show the image of the kinds of dishes you are working with to get an idea of what we are putting away.

Here students should see that there are three types of dishes that we need to put away: plain plates, fancy plates, and bowls. When you pseudocode these subtasks, it might look like the following:

```python
# Tasks:
# Stack plain plates
# Stack fancy plates
# Stack plain bowls
```

Now you have organized your subtasks into a list to help us think about what we need to accomplish. When we attempt to solve the larger problem of putting away the dishes, now we have three subtasks that we can focus on completing in order to solve the larger problem.

#### Pattern Recognition

Now demonstrate the problem through pattern recognition, or thinking about how these subtasks have been solved previously and finding any patterns that might help solve this particular problem this time. Our example explains that our cupboard space is limited and we only have two shelves to work with.

Explain that, in the past, this problem was solved by first stacking the fancy plates on the top shelf so that they are protected. Then we stacked the plain plates on the bottom shelf, and stacked the plain bowls on top of the plain plates. Now that we've revisited patterns that we've used to solve this problem in the past, let's pseudocode it:

```python
# Pattern recognition:
# Plain plates go on the bottom shelf
# Fancy plates go on the top shelf
# Bowls go on the top of plain plates
```

Here, we've pseudocoded the process that we've used to put away plates in the past so that we can use this same pattern to solve the problem of putting the dishes away.

#### Abstraction

Next, move on to abstraction. Explain to students that, in this step, you will make sure that you are only focusing on relevant information and that you are disregarding details that won't help solve this problem. Point out that there is a towel on the drying rack and a knife. Neither of these details will help us solve the problem of putting away the dishes, so there is an opportunity to add some pseudocode to note that these details are irrelevant to the solution:

```python
# Abstraction:
# Ignore knife
# Ignore towel
```

#### Sequencing

Begin by revealing that you now have enough information to design the solution.

Explain that the problem has been broken down into manageable parts, patterns have been identified, and irrelevant information eliminated. This brings you to the point of beginning to write and test your code.

Point out that an algorithm is essentially a sequence of steps or rules that we can use to solve our problem. In this case, it will be the sequence of events that will occur in order to complete the task of putting away the dishes so that they resemble the earlier image of the stacked cupboard:

![An image of a cupboard with two levels, plain plates and bowls are stacked on the bottom and fancy plates are stacked on the top.](Images/dishes_in_cupboard.png)

Identify the following points:

* In the image, the fancy plates are on the top shelf and the plain plates and plain bowls on the bottom shelf.

* In order to stack the plain bowls on top of the plain plates, putting away plates will have to come first in our sequence, followed by putting away bowls.

When you begin to pseudocode this sequence, the initial sequence could look something like the following:

```python
# Sequence:
# 1. Event 1: Put away plates:
# 2. Event 2: Put away bowls:
```

Point out that we have created two separate events for putting away plates and bowls so that we know to stack the bowls second. This is called an **event trigger**, because the completion of the first event will trigger the second event.

Continue by mentioning that while this is a start it doesn’t meet all the requirements. We don't want the plain plates to get mixed up with the fancy plates. We need to add steps under the first event that will help us remember to sort the two.

When we pseudocode this out, our new sequence might look something like the following:

```python
# Sequence:
# 1. Event 1: Put away plates:
#    Conditional: If (a plate is fancy)
#                    stack it on the top shelf
#                 Else
#                    stack it on the bottom shelf
```

Explain that here we've added what is known as a **conditional statement**. Students will learn more about conditional statements in the next class. For now, all they need to understand is that conditional statements allow us to make decisions based on conditions in our code. Here, if a plate meets the condition of being fancy, we will make the decision to stack it on the top shelf. Otherwise, we can assume that a plate is plain and should be stacked on the bottom shelf.

#### Debugging

Explain that while the last conditional statement would probably work at first, it is important to think of edge cases, such as exceptions or unusual scenarios, that might occur so that they too are covered by your conditional statements. For example, what if we stumble across a plate that is chipped or broken?

We can modify the conditional statement to include additional conditions for broken plates, which might look like:

```python
# Sequence:
# 1. Event 1: Put away plates: A fancy plate has a crack in it - what do we do?
#    Conditional: If (a plate is fancy)
#                    put it on the top shelf
#                 Else if (a plate is plain)
#                    put it on the bottom shelf
#                 Else if (a plate is cracked)
#                    put it in the trash
```

Point out how here we have added a new and improved conditional statement that includes the new conditions for whether a plate is broken. Now, if we encounter a plain plate or a plate that is cracked, our conditional statement tells us what we should do!

Mention that changing our original algorithm after finding a mistake or a potential mistake in our pseudocode is called **debugging**. Students will learn how to debug throughout the course, as they encounter problems and errors in their code when running it.

#### Sequencing our Second Event

Point out that now that you have pseudocoded the sequence for the first event, you can move on to the second event.

In this case, there is only one type of bowl, so you don't have to worry about making decisions based on certain conditions since you know that they are all going to be stacked in the same place.

Explain that instead of a conditional statement, you can use something called a **`for` loop**, or an action that will repeat over and over again until a condition is met. When we pseudocode our loop, it might look something like this:

```python
# Sequence:
# 2. Event 2: Put away bowls:
#    Loop: for (each bowl on the dish rack):
#                 stack it on the bottom shelf on top of the plain plates
```

Point out that this `for` loop directs you to stack each bowl on the bottom shelf and on top of the plates.

Show the whole pseudocode sequence, which at this point looks like this:

```python
# Algorithm: Put away clean dishes

# Tasks:
# Stack plain plates
# Stack fancy plates
# Stack plain bowls

# Pattern recognition:
# Plain plates go on the bottom shelf
# Fancy plates go on the top shelf
# Bowls go on the top of plain plates

# Abstraction:
# Ignore knife
# Ignore towel

# Sequence:
# 1. Event 1: Put away plates: A fancy plate has a crack in it - what do we do?
#    Conditional: If (a plate is fancy)
#                    put it on the top shelf
#                 Else if (a plate is plain)
#                    put it on the bottom shelf
#                 Else if (a plate is cracked)
#                    put it in the trash
# 2. Event 2: Put away bowls:
#    Loop: for (each bowl on the dish rack):
#                 stack it on the bottom shelf on top of the plain plates
```

Remind students of the iterative nature of writing algorithms. We could think of other edge cases to incorporate into this sequence and add steps to make it more detailed. If we tested out this algorithm, we might also find that there are ways to improve on the sequence that we've outlined.

Ask if anyone notices any problems with the code as it exists.

* The issue is that some of the code isn’t reachable, particularly the code that checks whether a plate is cracked or not. Congratulate them if they notice the problem, and reveal what it was if not.

How could we improve the logic of this statement?

Break the problem down. All of the plates are either fancy or plain. In the first statement, if the plate is fancy, we put it on the top shelf. In the second statement, if the plate is plain, we put it on the bottom shelf.

At this point, all of the plates are now on shelves and the program ends!

But what if we wanted to throw our cracked plates away? Right now, it looks like the cracked plates would end up on the shelves and not in the trash, because the code for cracked plates is unreachable!

Ask the students if they can figure out how to fix this.

* If a plate is cracked, it doesn't matter if it's fancy or plain&mdash;we just want to put the cracked plate in the trash.

* If we move our statement about cracked plates to the beginning, we can check for cracked plates first. Then, once all the cracked plates are thrown away, we can sort the plain and fancy plates to the right shelves, as demonstrated in the following pseudocode.

    ```python
    if (plate is cracked)
        put in trash
    else if (plate is fancy)
        put on top shelf
    else if (plate is plain)
        put on bottom shelf
    ```

Emphasize that checking your logic to make sure that all the code is reachable and you're getting the results you want is an important part of being a developer.

Ask students whether they have questions and address any that come up before you prompt students that they will be practicing writing pseudocode on their own in a short activity.

Send out the solution file so that the students can use it as a guide as they complete the next activity.

---

### 3. Students Do: Pseudocoding Practice (10 min)

**Corresponding Activity:** [02-Stu_Pseudocoding_Practice](Activities/02-Stu_Pseudocoding_Practice/)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will allow students to practice writing pseudocode for the common problem of sorting and washing laundry.

---

### 4. Review: Pseudocoding Practice (5 min)

**Corresponding Activity:** [02-Stu_Pseudocoding_Practice](Activities/02-Stu_Pseudocoding_Practice/)

Open the solution, share the file with the students, and go over it with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

* In our first event, delicate clothes take precedence over red and white clothes, because these clothes could also have delicate items that should not be included in the normal laundry load. Therefore, delicates should be the first check in the conditional statement.

* We have a sequence inside the `for` loop in the second event. This commonly occurs when writing code. There is often more than one action to perform inside a loop or conditional.

* One of the actions in the sequence inside the `for` loop is another conditional. Sometimes we need to check conditions inside loops or other conditional statements. We will explore how to do this in more detail in the next class.

Ask the students if they have any questions before moving on.

---

### 5. Instructor Do: Introduction to Python (10 min)

**Corresponding Activity:** [03-Ins_Python_Intro](Activities/03-Ins_Python_Intro/)

Follow the slides as a guide to introduce students to working with Python.

#### Understand how to use comments in Python code

**Note:** Bookmark the [PEP8 Style Guide](https://peps.python.org/pep-0008/) for yourself, as you will be introducing students to parts of it throughout the course as they become relevant.

Remind students of the pseudocode syntax you used in the previous example and reveal that the same hashes, `#`, are used to denote comments in Python.

Explain that comments are bits of clarifying text in a given file used for a number of possible reasons, from explaining specific functions or portions of code, to leaving reminders or questions for oneself or team members.

Also point out some basic commenting conventions, and feel free to include more from your own experience:

* No comments are better than bad comments.

* Keep comments up to date when code changes to avoid confusion.

* Use complete, clear sentences.

* Prioritize block comments (paragraphs or lines in their own right) over inline comments (in the same line as the relevant portion of code).

* Use inline comments sparingly and only where absolutely necessary for clarification purposes.

#### Data Types

Explain to the students that you will be introducing some of the basics of the Python language.

The first thing you will do is go over the data types students are most likely to encounter in any coding project. Knowing how to identify the data types you are working with is key, because only certain data types can be used for certain calculations.

There are a variety of data types in Python. Because you need to be prepared to handle different types of data, let's discuss a few key data types: integers, floating-point decimal numbers, strings, and Boolean values.

Follow the next sections along with the slides and demonstrate how to determine data types as instructed.

##### Integers

Integers are positive or negative whole numbers used to perform mathematical calculations. The length of an integer is constrained by the amount of RAM memory on your computer. For example, a computer with 8 GB of RAM will have 8,000,000,000 bytes. The integer 10,000,000,000,000,000,000, or 10 quintillion, will only take up 36 bytes of memory.

Note that when typing integer values greater than 999, a thousands separator, or comma, should not be used. Inserting commas can make the whole number you thought you were typing something different.

##### Floating-Point Decimal Numbers

Like integers, floating-point decimal numbers are used to perform mathematical calculations. Floating-point decimal numbers specify numbers that have a decimal point, like 73.81.

##### Strings

String variables can be text or numbers wrapped by either single or double quotes, or delimiters. A delimiter is any non-alphabetical character used to specify the boundary between plain text or other numbers, like the single or double quotes, or opening and closing parentheses. All characters between the quotes are part of the string; for example, `'Hello        World'` or `"Hello World"`.

Clarify empty strings: Sometimes, you may come across empty strings that contain no text or numbers between the delimiters. A string that is empty is written as `''`, or `""`. Because there are opening and closing single or double quotes, the data type is still a string.

Point out that unlike integers and floating-point decimal numbers, strings cannot be used to perform mathematical calculations. Also, it's important to note that if an integer or a floating-point decimal number is wrapped in quotes, it's considered to be a string, not an integer or decimal number. Later in this module, we'll go over how to change data types when necessary.

##### Boolean Values

Boolean data types can have one of two values: `True` or `False`.

Explain that even though the values are words, they must not be enclosed in quotation marks like strings. Emphasize that the values must always be capitalized when written in code.

**Note:** For more information on data types, students can read the official documentation on Python: [Numeric Types](https://docs.python.org/3.10/library/stdtypes.html#numeric-types-int-float-complex), [Text Sequence Type](https://docs.python.org/3.10/library/stdtypes.html#text-sequence-type-str), and [Boolean Values](https://docs.python.org/3.10/library/stdtypes.html#boolean-values).

#### Using Variables

Explain that variables are a core component of any coding project. They are data items with changeable values used for any number of processes or calculations in your code. You can use the example of a box or container that can be filled with different things throughout the runtime of the program.

##### Creating a Variable

Explain that to create a variable in Python, you give it a name. Giving a name to a variable is known as **declaring** it. This name is how you’ll refer to the variable throughout the remainder of the Python program. Returning to the previous dish clearing example, we may use variables for the plates, which could have the value of being fancy, plain, or cracked by simply typing `plate`.

You can create as many variables in a Python program as you require, and they can be created at any point in the program.

##### Naming Conventions

Emphasize that it is important to assign descriptive names to variables, so that both you and any other programmers will know what the variable name represents. Well-named variables significantly increase the readability of Python code.

For example, instead of naming variables `score_a` and `score_b`, we could use the more descriptive names `home_team_score` and `away_team_score`. Or in place of a vague name like `portfolio`, we should name the variable something like `microfinance_loan_portfolio`.

**Important:** Variables in Python are declared in snake_case. This means that, for multi-word variable names, each word is separated by one underscore (_) character and no spaces, and each element's initial letter is lowercase.

The next step is to assign the variable some data.

Once you have a descriptive name for your variable, you can assign data to that variable the equals sign, also known as an assignment operator, to set the variable equal to a value.

For example:
`home_team_score = 15`, or `plate = “fancy”`

Here, we've assigned the integer value 15 to the variable `home_team_score` and the string value “fancy” to the variable `plate`.

A cool thing about variables is that you can assign almost anything to them&mdash;even other variables!

See the following example:

```python
home_team_score = 15
home_team_final_score = home_team_score
```

Here, we have a variable named `home_team_score`, which equals 15. On the next line, we can create a new variable called `home_team_final_score` and set that equal to `home_team_score` at the end of the current game. Thus, `home_team_final_score` will have the same value, 15.

Demonstrate how to assign each of our different data types to a variable using the command line. To get started, open the command line, activate your Anaconda `dev` environment, and launch the Python interpreter.

**Note:** To launch the Python command line interpreter, open Terminal (macOS) or Anaconda Prompt (Windows) and type `python` *or* `python3`, then press Enter.

To assign an integer to a variable, we simply have to name the variable, assign the value using the equals sign (`=`), and type the integer, as follows:

```python
years = 20
```

A floating-point decimal number is assigned the same way, with the only difference being that it includes a decimal point:

```python
hourly_wage = 72.12
```

Next, assign a string to a variable using double quotation marks. As mentioned previously, single quotation marks also work. Explain that we will cover more complex string assignments later on in this class.

```python
profession = "software engineer"
```

Finally, assign a Boolean value to a variable:

```python
expert_status = True
```

Emphasize that while variables might seem like a basic concept in a programming language, they are the foundation of data storage.

#### Use the `print()` Function to Print a String and/or Variable

Now that students know how to assign variables, we can move on to how to print them to the screen.

If we run the following code, the Python program will print the values that are stored in the variables we assigned previously, along with the text strings contained inside the `print()` function:

```python
# Print a statement with the 'profession' string
print("Nakia is a professional", profession)

# Print a statement with the 'years' integer
print("They have been working for", years, "years")

# Print a statement with the 'hourly_wage' float
print("Their hourly wage is", hourly_wage)

# Print a statement with the 'expert_status' Boolean
print("Expert status:", expert_status)
```

The result from running this code appears below:

```text
Nakia is a professional software engineer
They have been working for 20 years
Their hourly wage is 72.12
Expert status: True
```

Point out that the comma between the text strings and the variable inside the `print()` function automatically adds a space, so we don’t need to add another space in the text string.

Once you have demonstrated this code in the command line interpreter, exit the interpreter by typing `exit()`, and then running the whole script from the command line by navigating to the activity solution folder in your Terminal and typing `python variables_solution.py`.

Explain to the students that they may use the command line interpreter or run scripts from the command line for today’s activities, but when we get to more complex coding over the next couple of days, it will be necessary to run code from Python scripts.

Ask students whether they have questions and address any that come up before you prompt students that they will be practicing working with variables on their own in a short activity.

Send out the solution file so that the students can use it as a guide as they complete the next activity.

---

### 6. Students Do: Variables (10 min)

**Corresponding Activity:** [04-Stu_Variables](Activities/04-Stu_Variables/)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will give students the opportunity to practice assigning variables in Python and printing them to the screen.

---

### 7. Review: Variables (5 min)

**Corresponding Activity:** [04-Stu_Variables](Activities/04-Stu_Variables/)

Open the solution, share the file with the students, and go over it with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

* Reiterate that the commas inside the `print()` function between strings and variables insert a space between them when printing to the string.

* Note that it is possible to print multiple parts in the `print()` function, separated by a comma, as shown in the following code:

    ```python
    # Print out a sentence with the number of vacation days
    print("You want to travel for", days, "days")
    ```

Ask the students if they have any questions and send out the solution before moving on.

---

### 8. Instructor Do: Inputs and Prompts (15 min)

**Corresponding Activity:** [05-Ins_Prompts](Activities/05-Ins_Prompts/)

Continue through the slideshow to facilitate discussion of the next topic.

Explain that we will be introducing two new useful functions: `type()` and `input()`.

Demonstrate these functions from the Python command line interpreter.

Explain that the `type()` function is used to determine data type. Inside this function, add the integer or other value to determine the data type. For example, let's say we want to find the data type of the integer 3. Type `type(3)` after the Python interpreter prompt, as shown, and then press Enter.

```python
type(3)
```

The output shows that the data type for the number 3 is an integer, as denoted by the 'int'.

```text
>>> type(3)
<class 'int'>
```

Other data types will be demonstrated within the `print()` function during this demonstration.

Next, explain that we use the `input()` function to get input from the user. Demonstrate this function with a string, explaining that we can use the content inside the brackets in the same way that we would use the `print()` function. That means that it is also possible to include variables, though in this case we are just going to use a string.

```python
input("What is your name? ")
```

Type in a name and press Enter to demonstrate that this will automatically print out the name you typed inside single quotes. This isn’t especially useful to us this way, so we want to assign our user inputs to variables.

Open the solution file, demonstrate and run the code within the Python command line interpreter, line by line:

```python
# Collect the user's input for the prompt "What is your name?"
user_name = input("What is your name? ")
```

* Make note of the space after the question mark. Without this space, the user would type their answer right next to the question mark.

* Point out that we assign the user’s input to the variable `user_name` using the same variable assignment method that we used previously, with the equals (`=`) sign. However, instead of typing an actual value with a specific data type, we use the `input()` function.

* The interpreter will prompt for your name. Type an answer and hit Enter to demonstrate that there is no output this time. Then run the next line of code.

    ```python
    # Print the data type of user_name
    print("user_name is type", type(user_name))
    ```

    The output of this will be the following text:

    ```text
    user_name is type <class 'str'>
    ```

* Here, we use the `type()` function to tell us the data type of `user_name`.

* Point out that we have used the `type()` function inside the `print()` function. It is possible to make use of functions within functions like this, if they are compatible.

Next, introduce type casting. Type casting is when we convert one data type into another. For example, converting an integer into a string, or vice versa. To do this, demonstrate converting a string of a number into an integer.

```python
int("20")
```

The output shows the number 20 without the quotation marks that we used in the input.

```text
>>> int("20")
20
```

To compare, we can type `"20"` directly into the Python interpreter, which outputs the number inside single quotes.

Return to the solution code to demonstrate type casting within the user input context.

```python
# Collect the user's input for the prompt "How old are you?" and convert the
# string to an integer.
age = int(input("How old are you? "))
```

* Explain that every response to an input is stored as a string regardless of the characters entered. Therefore, variables that are intended as integers must be cast as integers to be used in calculations.

* Point out that we wrap the `int()` function around the `input()` function in order to convert the user input string to an integer.

* Type a string into the input prompt to demonstrate the error that occurs when a number is not entered. The output should look something like the following text.

    ```text
    >>> age = int(input("How old are you? "))
    How old are you? Ninety
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'Ninety'
    ```

    * Explain that when we use type casting this way, there is no way to check if the input is valid. Python has different methods to check if the code you want to perform will run without error. We will cover the basics of input validation in the next class, and more advanced methods in a future module. For now, we just need to make sure that we type something that will be correctly converted.

Enter the `age = int(input("How old are you? "))` code again, this time entering a number that can be converted with the `int()` function, then proceed with the following line of code.

```python
# Print the data type of age
print("age is type", type(age))
```

The output of this will be the following text:

```text
age is type <class 'int'>
```

The next part of the demonstration covers the same content, except for floats rather than integers. Demonstrate what happens when you copy all of this code into the Python interpreter at once.

```python
# Collect the user's input for the prompt "What is your average weekly grocery
# bill?" and convert the string to a float.
grocery_bill = float(input("What's your average weekly grocery bill? "))

# Print the data type of grocery_bill
print("grocery_bill is type", type(grocery_bill))
```

The output will look like the following text:

```text
>>> # Collect the user's input for the prompt "What is your average weekly grocery
>>> # bill?" and convert the string to a float.
>>> grocery_bill = float(input("What's your average weekly grocery bill? "))
What's your average weekly grocery bill?
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: ''
>>> # Print the data type of grocery_bill
>>> print("grocery_bill is type", type(grocery_bill))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'grocery_bill' is not defined
```

* Explain that the interpreter thought the empty line in the code was the user’s input that should be converted to a float using `float()`. This is why, when we’re using the command line interpreter, we must copy each line of code separately. The code would not produce the same error if the entire script was being run from the command line, so you should demonstrate that at the end of this walkthrough with the interpreter.

Now that the error has been demonstrated, copy each line of code separately to go through the example for floats.

The output should look something like the following text:

```text
>>> # Collect the user's input for the prompt "What is your average weekly grocery
>>> # bill?" and convert the string to a float.
>>> grocery_bill = float(input("What's your average weekly grocery bill? "))
What's your average weekly grocery bill? 87.45
>>> print("grocery_bill is type", type(grocery_bill))
grocery_bill is type <class 'float'>
```

The last data type to demonstrate is the Boolean data type. Explain that using the `bool()` function with our input conversion works a little differently than our string and number examples. Demonstrate two examples for the input for the following code:

```python
# Collect the user's input for the prompt "Will you type an input?" and
# convert it to a boolean. Note that non-zero, non-empty objects return True.
true_or_false = bool(input("Will you type an input? "))
```

The first time you run this code, type “No” and press Enter.

Then enter the variable in the interpreter to print out the value it was converted to:

```python
true_or_false
```

The output this produces is `True`, even though we wrote “No”. This is because any character input entered would return True. To produce a `False` result, we need to just hit Enter without typing anything.

Run `true_or_false = bool(input("Will you type an input? "))` again and then press Enter. Then, type `true_or_false` to print out the value, which should result in `False` this time.

Now run the code that prints out the variable’s data type:

```python
# Print the data type of true_or_false
print("true_or_false is type", type(true_or_false))
```

The output of this will be the following text:

```text
true_or_false is type <class 'bool'>
```

Now that we have correctly converted each of our input data types, demonstrate how to print these variables to the screen using **string concatenation**.

String concatenation is when we combine strings with a plus (`+`) symbol. Demonstrate string concatenation with the following code:

```python
"Hello!" + " Welcome to Python class!"
```

This will produce the following output:

```text
'Hello! Welcome to Python class!'
```

* Point out that we needed to include a space at the beginning of our second string, because unlike using the comma in our print statements, the plus sign does not add a space between strings.

Explain that when we use string concatenation, we cannot use a variable of another data type without first casting the data type as a string.

First, demonstrate a way that will produce an error. For example:

```python
"Hello!" + 4
```

This will produce the following error:

```text
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Now demonstrate how this works with the input variables we created earlier.

```python
# Create four print statements that displays text about the user's inputs
print("My name is " + user_name)
print("I am " + str(age) + " years old.")
print("I spend an average of $" + str(grocery_bill) + " per week on groceries")
print("The input was converted to " + str(true_or_false))
```

An example of the output of this code follows:

```text
>>> print("My name is " + user_name)
My name is Michelle Yeoh
>>> print("I am " + str(age) + " years old.")
I am 26 years old.
>>> print("I spend an average of $" + str(grocery_bill) + " per week on groceries")
I spend an average of $87.45 per week on groceries
>>> print("The input was converted to " + str(true_or_false))
The input was converted to False
```

* Point out that we use the `str()` function to cast our integer, float, and Boolean values to a string when using string concatenation.

If you’d like to demonstrate the code running from the script, either exit the command line interpreter, or open a new Terminal window or tab, then navigate to the activity folder and run the script with the command `python inputs_solution.py`.

You may bring up the slide that covers the data types and functions for type casting that we used in this activity for students’ reference.

| Data Type | Python Classification | Type Casting Function |
| ---------- | ------ | ------ |
| Integers | `<class 'int'>` | `int()` |
| Float point numbers | `<class 'float'>` | `float()` |
| Strings | `<class 'str'>` | `str()` |
| Boolean | `<class 'bool'>` | `bool()` |

Ask students whether they have questions and address any that come up before you prompt them that they will be practicing working with inputs on their own in a short activity.

Send out the solution file so that the students can use it as a guide as they complete the next activity.

---

### 9. Students Do: Input Order (15 min)

**Corresponding Activity:** [06-Stu_Input_Order](Activities/06-Stu_Input_Order/)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will give students the opportunity to practice saving inputs from the command line as variables, using string concatenation, and converting data types.

---

### 10. Review: Input Order (5 min)

**Corresponding Activity:** [06-Stu_Input_Order](Activities/06-Stu_Input_Order/)

Open the solution, share the file with the students, and go over it with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

* When we use string concatenation and want to print out a variable’s data type, we must cast the result of the `type()` function as a string first, as in the following code:

    ```python
    # Print the item cost along with its data type
    print("The data type of " + str(item_cost) + " is " + str(type(item_cost)))
    ```

* If we want to stick to the Python PEP8 style guide convention and limit our code to 79 characters in a single line, sometimes we need to use multiple lines to perform a single action, as in the following code:

    ```python
    item_quantity = int(input("What quantity of " + item + " would you like to "
                              + "purchase? "))
    ```

* The PEP8 style guide tells us to start the new line with the `+` operator when there is an addition calculation or concatenation to be performed. It is also best practice for the new line to line up with the beginning of the parenthesis the new line belongs to.

* Anything enclosed inside a set of parentheses is considered part of the same section of code and will be performed together regardless of how many lines they cover. Without the enclosing parentheses, if an action should be spread across multiple lines, a backslash (`\`) at the end of the line can be used to instruct the Python interpreter to continue on the next line, though this is not preferred according to the PEP8 style guide.

Send out the following links for PEP8 guidelines:
[Maximum Line Length](https://peps.python.org/pep-0008/#maximum-line-length)
[Indentation](https://peps.python.org/pep-0008/#indentation)
[Should a Line Break Before or After a Binary Operator?](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)

Ask the students if they have any questions and send out the solution before taking the students into their break. Tell the students that after the break, you will be covering basic calculations and more complex string printing and manipulation.

---

### 11. BREAK (15 min)

---

### 12. Instructor Do: Perform Calculations with Python (15 min)

**Corresponding Activity:** [07-Ins_Calculation_Operators](Activities/07-Ins_Calculation_Operators/)

Continue using the slideshow to accompany this demonstration.

#### Calculations Functions

Now that students are more familiar with integers and floating-point decimal numbers, introduce them to performing both simple and complex mathematical calculations in Python. Some mathematical operations will look familiar, but there are some operations that might be new to students who don't have prior Python programming experience.

Many real-world coding programs require mathematical calculations like addition, subtraction, multiplication, and division. To perform these calculations in Python, several arithmetic operators are used. The following table lists these arithmetic operators, their meanings, and how they are used.

| Operator | Meaning | Use |
|-----|-----|-----|
| + | Adds two numbers. | x + y |
| - | Subtracts one number from another. | x - y |
| * | Multiplies two numbers.|x * y|
| / | Divides one number by another. This always results in a floating-point decimal number (float) | x / y |
| % | The “%” is known as the modulus. When used in place of “/” it will divide one number by another, and return the remainder of the division | x % y (remainder of x/y) |
| // | Divides one number by another and returns an integer. This is known as floor division | x // y |
| ** | Raises a number to a power | x ** y (x to the power of y) |

#### Order of Precedence

Bring students attention to the fact that when you need to perform more complex mathematical expressions that include any combination of division, multiplication, addition, and subtraction, you must follow the order of precedence (operations) for arithmetic operators. Different students from different countries will be familiar with different acronyms but it all comes down to the same thing.

The order of precedence in Python, which follows the same guidelines as in mathematics, is:

1. Operations enclosed in parentheses are performed first.

2. Exponentiations (i.e., raising a number to a power) are performed next.

3. Multiplication and division operations are performed from left to right: *, /, //, and %.

4. Finally, addition and subtraction operations are performed from left to right.

In a mathematical calculation, you can group expressions in parentheses to indicate that those expressions should be performed before operations that are not in parentheses.

Treat these calculations just like algebraic expressions: if parentheses are enclosed within parentheses, work from the inside out.

If you think it necessary, open the Python interpreter and demonstrate the different answers to a few of the following mathematical expressions:

* `5 + 2 * 3` and `(5 + 2) * 3`
* `8 // 5 - 3` and `(8 // 5) - 3`
* `8 + 22 * 2 - 4` and `8 + (22 * (2 - 4))`
* `16 - 3 / 2 + 7 - 1` and `16 - 3 / (2 + 7) - 1`
* `3 ** 3 % 5` and `3 ** (3 % 5)`
* `5 + 9 * 3 / 2 - 4` and `5 + (9 * 3 / 2 - 4)`

Now that students understand each of these operators, open up the solution file associated with this demonstration and go through the code in the Python interpreter, demonstrating how we can perform calculations and assign the result to a variable.

Exit the Python interpreter, or use a different Terminal window, and run the Python script from the command line. Students will need to be able to do this for the solution to the next activity.

Ask students whether they have questions and address any that come up before you send out the solution file for their reference and prompt them that they will be practicing working with calculations on their own in a short activity.

---

### 13. Students Do: Basic Calculator (15 min)

**Corresponding Activity:** [08-Stu_Basic_Calculator](Activities/08-Stu_Basic_Calculator/)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will give students practice performing calculations in Python, by developing an application that can help a user make decisions about their vacation. The students should start with the starter code provided and add their calculations to the script using the variables that are assigned in the beginning of the script.

---

### 14. Review: Basic Calculator (5 min)

**Corresponding Activity:** [08-Stu_Basic_Calculator](Activities/08-Stu_Basic_Calculator/)

Open the solution, share the file with the students, and go over it with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

* Some students may have less experience with mathematical equations than others, or haven’t needed to use what they learned in school for a long time. Though it’s more common to encounter problems that only require addition, subtraction, multiplication, and division, the students got some practical use with floor division, exponents, and modulus. Check in with the students how they felt about using these mathematical equations in this context.

Ask the students if they have any questions and send out the solution before moving on to the next activity.

---

### 15. Instructor Do: Printing Complex Strings (10 min)

**Corresponding Activity:** [09-Ins_Complex_Strings](Activities/09-Ins_Complex_Strings/)

In this last section we will be exploring further ways to manipulate and play around with strings and outputs.

Go through the slides, explaining the following formatting methods and demonstrating the code snippets from the solution file in the Python command line interpreter. The final slide in this section can serve as a reference for students if they need it.

#### Quotation Marks, Escape Characters, and Multiline Strings

Explain that strings can be wrapped inside single quotes (') or double quotes (") as long as it’s the same on both ends of the string. Sometimes it’s a matter of personal preference, sometimes it’s because you want to be able to use the other type of quotation mark inside the string. For example:

```python
print("I'm having a great day!")
print('Mary said, "This is my home."')
```

Point out that there would be an issue if you want to use both single and double quotes in a string. There are two potential solutions to this problem.

* You can use triple quotes (""") to open and close the string. For example:

    ```python
    print("""Jose said, "My son's bringing dinner home tonight." """)
    ```

* Or you can use the backslash escape character. For example:

    ```python
    print('Jose said, "My son\'s bringing dinner home tonight."')
    ```

Explain that triple quotes also allow you to create strings across multiple lines. For example:

```python
print("""Name: Michelle Yeoh
Date of Birth: August 6, 1962
Birth place: Ipoh, Malaysia""")
```

Often, we don't want to use triple quotes to store text across multiple lines, as the text can't be indented without inserting useless whitespace when we get to complex decisions. In those situations, we can insert a new line character instead. The backslash escape character is also used for adding a new line character to a string with `\n`. E.g.:

```python
print("Welcome to Python!\nHow are you enjoying class so far?")
```

This allows a single line of code to print text on separate lines.

Next, demonstrate concatenating a new line character to the end of an input string:

```python
input_string = input("What is your answer? ") + "\n"
```

We will use this input variable in the next part of the demonstration on f-strings and string manipulation, so be sure to type an answer that includes alphabetical characters in both upper and lowercase, and not necessarily grammatically correct.

#### F-string Literals

Explain that f-string literals are a Python feature that makes printing outputs very streamlined and can be used in place of more traditional concatenation. They let us embed variable values in the text that we want to print.

Illustrate the general format for f-strings is as follows:

* The f-string begins with an `f` followed by a string contained within quotes. (The term f-string comes from the leading "f" character preceding the string literal.)

* In the f-string, curly braces are used to add variables or expressions to the f-string.

Demonstrate this f-string format with our input string:

```python
print(f"You said: {input_string}")
```

Break down what's happening in the code snippet for the students.

1. First, we create an f-string by starting the text string with the character `f`. This tells Python that the following text may have variables embedded inside.

2. Next, notice that the variable is enclosed in curly braces, or brackets: `{input_string}`. This special syntax tells Python to insert whatever is inside the curly braces directly into the text.
In this case, Python finds the value stored in the `input_string` variable and inserts it directly into the text string.

Explain that, even though `input_string` is also a string, the f-string allows us to include a variable of any data type or expression without first converting it to a string with the `str()` function, unlike string concatenation. We’ll get to some examples of these shortly. First, let’s look at some string manipulation methods and print them out using f-strings.

#### String Manipulation

Explain and demonstrate some common string manipulation methods:

* The multiplication asterisk, `*`, will allow you to print a string multiple times

    ```python
    print(f"Let's print your answer 5 times:\n{input_string * 5}")
    ```

    * Point out that since we concatenated our input string with a new line character, this code will print the input 5 times, starting on a new line each time. If we had not added the new line character, the string would have been repeated on the same line without any spaces between the repeated strings.

* `lower()` converts a string to lowercase

    ```python
    print(f"Lowercase: {input_string.lower()}")
    ```

* `upper()` converts a string to UPPERCASE

    ```python
    print(f"Uppercase: {input_string.upper()}")
    ```

* `title()` converts a string to Title Case

    ```python
    print(f"Title case: {input_string.title()}")
    ```

#### Multiline F-strings and Formatting Floats

For this example, explain that we will look at using calculations for a circle. Walk the students through the following code and output:

```python
radius = 4
pi = 3.14159265358979323846
print(f"Radius: {radius}cm\n"
      + f"Circumference: {2 * pi * radius}cm\n"
      + f"Area: {pi * radius ** 2}cm\n")
```

```text
Radius: 4cm
Circumference: 25.132741228718345cm
Area: 50.26548245743669cm
```

* Here, the `f"Radius: {radius}cm\n"` line embeds a float variable `radius` inside an f-string with a new line character.

* Point out that the next line uses string concatenation and requires us to open the next string with a leading `f` again.

* Both the second and third f-strings use mathematical expressions inside the curly braces. Inside the curly braces, the f-string performs the calculations and formats the value as a string. There is no need to perform the calculation and save it as a variable before using it in the f-string. This has the benefit of making the code more concise and easy to read.

Note that the floats that were printed out are quite long, and we’ll often want to shorten them for readability. This can be solved with formatting the output f-string by specifying a decimal precision. Demonstrate this with printing the value of pi to two decimal places.

```python
print(f"Pi to two decimal places is {pi:.2f}\n")
```

The general structure to format a value inside the curly braces in an f-string is as follows:

`f'{value:{width}.{precision}}'`

Explain the following:

* In the format, the `width` specifies the number of characters used to display the value. However, if a value needs more space than the width specifies, the additional space is used.

* The precision indicates the number of decimal places to format the value. For example, to format pi to two decimal places, we used `.2f`, where `f` means "floating-point decimal format".

When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the `{width}`.

`f'{value:{width},.{precision}}'`

Now demonstrate this by adding a thousands separator to an f-string with a large integer:

```python
print(f"I have ${3500:,} to spend on my vacation this year.")
```

This produces the following output:

```text
I have $3,500 to spend on my vacation this year.
```

We can also turn the triple quote string into an f-string with `f"""Some text {a_variable}"""`. Open up the solution code in VS Code to show the students the example within. Then, run the full script from the command line to demonstrate the output. You will need to type an input again, and the script pauses in the middle, asking you to press Enter to print all of the output from a single string variable.

Explain that Python files lack a graphical user interface. One advantage to this is that creating text-based interfaces for Python programs will allow you to develop accessible applications for visually impaired people who use software called a screen reader to interact with computer systems.

Ask students whether they have questions and address any that come up before you send out the solution and prompt students that they will be practicing with strings on their own in a short activity.

---

### 16. Students Do: Print Presentation (15 min)

**Corresponding Activity:** [10-Stu_Print_Presentation](Activities/10-Stu_Print_Presentation/)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will give students practice printing more complex strings, along with reinforcing other Python skills from this class.

---

### 17. Review: Print Presentation (5 min)

**Corresponding Activity:** [10-Stu_Print_Presentation](Activities/10-Stu_Print_Presentation/)

Open the solution, share the file with the students, and go over it with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

* We use `\n` to insert a new line character.

* The backslash can be used as an escape character to print quotation marks in a string.

* Inputs that are used in calculations must be converted to integers or floats to avoid an error.

* We can use f-string formatting next to a calculation inside the curly braces:

    ```python
    sphere_details = f"""Radius: {radius}
    Surface area: {4 * pi * radius ** 2:.4f}
    Volume: {4/3 * pi * radius ** 3:.4f}
    """

    print(sphere_details)
    ```

Ask the students if they have any questions and send out the solution before moving on to wrap up the class and introduce the challenge.

---

### 18. Instructor Do: Class Wrap Up (5 min)

Congratulate students on getting to the end of the day’s lesson, ask them how they’re feeling about the topics covered in this class and remind them that they can join office hours if they need additional help.

Preview the week’s challenge instructions and requirements for students:

* This week’s challenge will involve creating an interactive menu for a food truck for customers to order from, which will print the customer’s order and total cost once the order is complete.

* Relate this challenge to how coding skills are useful in programming for AI:

    * When building AI applications, we often ask for user inputs and process information before retrieving results.

    * Building machine learning models happens after we collect sufficient data, which can be used to find insights about the data. In this challenge, students will be collecting information from customers that could be stored in a database and used to generate insights for a machine learning model, such as “How much food should be ordered in a given week?” or “How much profit is expected in this time period?”

### End Class
---


© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
