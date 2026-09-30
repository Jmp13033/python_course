# Git and GitHub Setup — Windows

This guide will help you set up Git and GitHub on a Windows computer.

By the end, you will be able to:

- Install Git
- Create a GitHub account
- Connect your computer to GitHub
- Configure Git
- Clone a repository
- Check which GitHub repository your project is connected to
- Upload your work to GitHub

---

## 1. What Is Git?

**Git** is a program that keeps track of changes to your code.

Git allows you to:

- Save versions of your work
- See what changed
- Undo changes
- Work with other programmers
- Upload your work to GitHub

## 2. What Is GitHub?

**GitHub** is a website where Git repositories can be stored online.

A simple way to think about it:

```text
Your Computer
     |
     | Git
     ↓
GitHub

Git manages the code on your computer.

GitHub stores a copy of your repository online.
```

## 3. Install Git on Windows

Open a web browser and go to:

https://git-scm.com/download/win

Download Git for Windows.

Run the installer.

For this course, the default installation options are fine.

After the installation finishes, open PowerShell.

Open PowerShell

- Press the Windows key.
- Type PowerShell.
- Open Windows PowerShell.

Check that Git was installed:

```powershell
git --version
```

You should see something similar to:

```text
git version 2.x.x
```

If you see a Git version number, Git is installed correctly.

## 4. Create a GitHub Account

Open a web browser and go to:

https://github.com/

Click **Sign up**.

Create your GitHub account and verify your email address.

You will need:

- A GitHub username
- An email address
- A password

**Important:** Never put your GitHub password inside your Python programs.

## 5. Install GitHub CLI

GitHub CLI is a command-line tool that allows you to work with GitHub from PowerShell.

On Windows, go to:

https://cli.github.com/

Download and install GitHub CLI.

After installing it, close PowerShell and open a new PowerShell window.

Check that GitHub CLI works:

```powershell
gh --version
```

You should see something similar to:

```text
gh version 2.x.x
```

## 6. Connect Your Computer to GitHub

Now we will connect your computer to your GitHub account.

In PowerShell, run:

```powershell
gh auth login
```

GitHub CLI will ask you several questions.

When asked:

```text
What account do you want to log into?
```

Choose:

```text
GitHub.com
```

When asked:

```text
What is your preferred protocol for Git operations?
```

Choose:

```text
HTTPS
```

When asked:

```text
How would you like to authenticate GitHub CLI?
```

Choose:

```text
Login with a web browser
```

GitHub CLI will give you a code.

A browser window may open automatically.

If it does not, open the URL shown in PowerShell and enter the code.

Sign into your GitHub account and authorize GitHub CLI.

## 7. Check Your GitHub Login

After logging in, run:

```powershell
gh auth status
```

You should see information showing that you are logged into GitHub.

For example:

```text
Logged in to github.com
```

If you see this, your computer is connected to your GitHub account.

## 8. Configure Git

Git needs to know your name and email address.

Set your name:

```powershell
git config --global user.name "Your Name"
```

For example:

```powershell
git config --global user.name "Jane Smith"
```

Set your email:

```powershell
git config --global user.email "your-email@example.com"
```

For example:

```powershell
git config --global user.email "jane@example.com"
```

Use the email address associated with your GitHub account.

## 9. Check Your Git Configuration

Run:

```powershell
git config --global --list
```

You should see something similar to:

```text
user.name=Jane Smith
user.email=jane@example.com
```

## 10. Go to Your Documents Folder

We will use your Windows Documents folder for this example.

Run:

```powershell
cd $HOME\Documents
```

You can check where you are with:

```powershell
pwd
```

You should see something similar to:

```text
Path
----
C:\Users\Jane\Documents
```

## 11. Clone a GitHub Repository

A clone downloads a GitHub repository onto your computer.

Your instructor will give you the GitHub repository URL.

For example:

```text
https://github.com/example/python-course.git
```

Run:

```powershell
git clone https://github.com/example/python-course.git
```

Git will download the repository to your computer.

Then enter the repository:

```powershell
cd python-course
```

Replace `python-course` with the actual name of your repository.

## 12. Check Your Repository

Run:

```powershell
git status
```

You should see something similar to:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This means Git is working correctly.

## 13. Find Where Your Repository Is on Your Computer

If you are inside a Git repository, run:

```powershell
git rev-parse --show-toplevel
```

This shows the location of the repository on your computer.

For example:

```text
C:/Users/Jane/Documents/python-course
```

This is the root folder of your Git repository.

## 14. Find Which GitHub Repository You Are Connected To

Run:

```powershell
git remote -v
```

You may see:

```text
origin  https://github.com/example/python-course.git (fetch)
origin  https://github.com/example/python-course.git (push)
```

The word `origin` is the default name Git gives to the remote repository.

The URL tells you which GitHub repository your computer is connected to.

You can also get just the URL:

```powershell
git remote get-url origin
```

## 15. Local Repository vs. GitHub Repository

There are two important locations.

### Local Repository

This is the copy of the project on your computer.

For example:

```text
C:\Users\Jane\Documents\python-course
```

### Remote Repository

This is the copy stored on GitHub.

For example:

```text
https://github.com/example/python-course
```

Git connects the two:

```text
       Your Computer
       Local Repository
              |
              | Git
              ↓
       GitHub Repository
       Remote Repository
```

## 16. The Basic Git Workflow

The basic Git workflow is:

```text
Make changes
     ↓
git status
     ↓
git add
     ↓
git commit
     ↓
git push
```

You will use this workflow frequently.

## 17. Check Your Changes

After working on your Python files, run:

```powershell
git status
```

Git will show you which files have changed.

For example:

```text
modified: Activities/04-Stu_Variables/variables.py
```

## 18. Add Your Changes

To add all of your changes:

```powershell
git add .
```

The `.` means:

Add changes from the current directory and its subdirectories.

## 19. Commit Your Changes

A commit saves a version of your work.

Run:

```powershell
git commit -m "Complete variables activity"
```

Try to describe what you actually changed.

For example:

```powershell
git commit -m "Complete variables activity"
```

or:

```powershell
git commit -m "Complete calculator activity"
```

## 20. Push Your Changes to GitHub

After committing your changes, run:

```powershell
git push
```

This uploads your commits to GitHub.

You can then open your GitHub repository in a web browser and see your changes.

## 21. Get Changes From GitHub

If your instructor has updated the repository, you can download the latest changes with:

```powershell
git pull
```

A common workflow is:

```powershell
git pull
```

Make your changes.

```powershell
git add .
```

Commit your changes:

```powershell
git commit -m "Complete activity"
```

Push your changes:

```powershell
git push
```

## 22. Important Git Commands

| Command | What It Does |
|---------|--------------|
| `git --version` | Checks whether Git is installed |
| `gh --version` | Checks whether GitHub CLI is installed |
| `gh auth login` | Connects your computer to GitHub |
| `gh auth status` | Checks your GitHub login |
| `git status` | Shows the current state of your repository |
| `git add .` | Stages your changes |
| `git commit -m "message"` | Saves your changes |
| `git push` | Uploads your commits to GitHub |
| `git pull` | Downloads changes from GitHub |
| `git clone URL` | Downloads a repository |
| `git remote -v` | Shows the GitHub repository connected to your project |
| `git remote get-url origin` | Shows the GitHub URL |
| `git rev-parse --show-toplevel` | Shows the local repository's root folder |

## 23. Troubleshooting

### Git Is Not Recognized

If PowerShell says:

```text
git : The term 'git' is not recognized
```

Git may not be installed correctly.

Go to:

https://git-scm.com/download/win

Install Git and then open a new PowerShell window.

Try again:

```powershell
git --version
```

### GitHub CLI Is Not Recognized

If PowerShell says:

```text
gh : The term 'gh' is not recognized
```

Install GitHub CLI from:

https://cli.github.com/

Then open a new PowerShell window.

Try:

```powershell
gh --version
```

### I Don't Know Which GitHub Repository I Am Connected To

Run:

```powershell
git remote -v
```

This will show the GitHub repository connected to your project.

### I Don't Know Where the Repository Is on My Computer

Run:

```powershell
git rev-parse --show-toplevel
```

This will show the location of the repository on your computer.