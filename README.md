# ITEC696: Python Programming for Business Analytics

Welcome to the course home page!

The steps below describe how to install Python on your machine, including an IDE (Spyder) and the course repo.

## Viewing Options

* **Option 1**: If you are viewing this on Github, you should be able to start viewing the book by clicking on [`contents.ipynb`](https://github.com/gmf05/ITEC696/blob/master/contents.ipynb).
* **Option 2**: Once you download the course repo, you can read these notes as a browser-based book by opening [`contents.html`](https://github.com/gmf05/ITEC696/blob/master/contents.html). In that event you can navigate forward and back using your browser.
* **Option 3**: If you also have Jupyter Notebook, you can read the `.ipynb` files and try running their content.




## Installing Python and Spyder

Install [**Miniconda**](https://conda.io/miniconda.html) (preferred) or [**Anaconda**](https://www.anaconda.com/download/). Anaconda comes with many packages already installed, while Miniconda is a more lightweight version allowing you to install only the packages you want. Here we prefer Miniconda since we'll soon install our own packages.

To install packages we'll use the Python package manager **pip** (short for "pip installs packages"), which runs on the command line. We will use both Anaconda and pip via the command prompt. While the integrated development environment (IDE) **Spyder** offers a way to install packages, using the command line will allow us more flexibility to manage **virtual environments**, self-contained versions of Python. It also practices skills used in **remote computing**, i.e. doing computations on machines that are far away (often more powerful machines like desktops or supercomputing clusters).

Install [Spyder](https://pythonhosted.org/spyder) by opening a command prompt (*Windows*: Anaconda command prompt; *Mac/Linux*: Terminal) and running

```bash
conda install -c anaconda spyder
```

Spyder is an Integrated Development Environment (IDE) named so because it brings together several software tools that are useful when programming in Python. The two main tools are

* Text Editor (default left pane)
* Python / IPython Console (default bottom right pane)

There are other helpful tools, too, like a Code Profiler, a Help Viewer, and a Plot Viewer. You can find them under `View -> Panes`.

## Virtual environments

One of the key benefits to Anaconda is that it manages virtual environments for us. A **virtual environment** is a self-contained copy of Python with its own unique packages installed. Virtual environments are useful for managing multiple projects and making it much easier to reproduce code across different machines.

To make a new virtual environment using Anaconda, open a terminal and run the following:

```bash
conda create -n itec696 python=3.6

```
This will make a new directory called `itec696` (or whatever name you use) and copy the base Python 3.6 installation within Anaconda there.

---

Now we'll run a quick experiment to see where the virtual environment lives and test whether it works. Try running the lines below in the terminal.

```bash
source activate itec696

```

You should see your command prompt change

```bash
    user@machine-name$ |
```

has now become

```bash
    (itec696) user@machine-name$ |
```

The extra `(itec696)` signifies the virtual environment is active and commands like `python` and `pip` refer to the copy located in the virtual environment.

If you have Windows and your command prompt is slightly different, don't worry. We'll standardize our terminal next. This will give us practice working with a Unix-style command prompt, common to virtually all computers.


## Download [Cygwin Terminal](https://cygwin.com/install.html) (Windows users)

Run the setup file and choose a mirror. When you get to the package selection prompt, use the search bar at the top to type in the following package names. For each package, search for the matching name, description, and category, then click the package to select it.

* *git: Distributed version control system* Category: Devel. For file version control.

* *openssh: The OpenSSH server and client programs*. Category: Net. For remote computing. (Optional)

* *vim: Vi IMproved Text Editor.* Category: Editors (Optional)

## Terminal Walkthrough

We'll work in the terminal (aka command line) frequently through this course. While many new programmers find the terminal daunting, it's extremely useful, and the simple operations will be familiar to anyone who has used a graphical file explorer.

Like the file explorer, the terminal has a current directory where it's operating. From the current directory, one can navigate to other directories, make new folders, copy or move files, delete items, and so on.

To start, try typing these lines, which use some of the common commands. A description appears next to each command as a **comment**, a segment of code that is ignored. In both terminal and in Python, comments begin with a hashtag `#` and can be an entire line or a partial line.

```bash
pwd # show the Present Working Directory (PWD)
ls # LiSt the contents of pwd
echo "This is a test" # print text
cd ~/Code # Change Directory to ~/Code
mkdir test # MaKe DIRectory
cd test
ls
cd .. # Change Directory to go up one level
rmdir test # ReMove DIRectory
```

Some commands above overlap with the usual Windows command prompt, while others have synonymous functions (e.g. `ls` on Unix is `dir` on Windows).

Where do these commands live? Use the `which` command to probe each one. Underneath your input, the terminal will print the directory (i.e. folder) where the command lives. 

```bash
which ls
which echo
which cd
which rm
which cp
which mv
which mkdir
which rmdir
which git # should work if git is installed
which ssh # optional, if you installed openssh
which vim # optional, if you installed vim
```

What do the paths have in common?

Finally, let's make a couple symbolic links (i.e. shortcuts) with command `ln`. These will save us from typing out long Windows paths like `/cygdrive/c/Users/$USER/` all the time.

```bash
ln -s /cygdrive/c/Users/$USER/Code ~/Code
```

You can consider adding other folders like `Documents`, too.

## Installing libraries#

In addition to `python`, Anaconda also comes with a file called `pip`. Pip - short for "Pip installs packages" - is a package manager that handles downloading and setting up packages hosted on the [Python Package Index (PyPi)](https://pypi.org). 

Pip can handle installing packages one-by-one (e.g. `pip install numpy`) or from a text list (e.g. `pip install -r requirements.txt`). Typically we'll use the latter option when setting up a virtual environment. To install the requirements included in the course repo, try running the sequence below.

```bash
pip install -r ~/Code/ITEC696/requirements.txt

```
You should begin to see lots of output printing to the terminal as Pip downloads each package then installs it. This may take several minutes to finish, depending on your internet connection and processor speed. 

The command `pip freeze` will print the list of currently installed packages. So, if you happen to install a new package and want to generate a revised list of requirements, you can export the output of `pip freeze` to a file like so:

```bash
pip freeze > requirements_v2.txt
```

## Testing Python#

Let's now ensure our libraries load correctly. You can run the test script in Python from the command line:

```bash
python ~/Code/ITEC696/test.py
```

It should generate some output:
```bash
Starting imports...
Done!
< DATE AND TIME >
```	

## Setting PYTHONPATH (Optional)

If you skip this step altogether, you can still write Python code. You'll just need to comment out any of the Table of Contents cells when running `notebook.ipynb` files.

We can always add more folders to the `PYTHONPATH` later by appending them to the variable we just assigned, so long as we separate the folders with a colon `:`, similar to the system `PATH` variable.


---

### Windows

* Option 1: Open Spyder. From the user menu, navigate `Tools -> Current user environment variables`. Add key `PYTHONPATH` with value `C:\...\Code\ITEC696\`. 

* Option 2: Press the Windows key and search "environment variables". Click `Set user environment variables`. Then add key `PYTHONPATH` with value `C:\...\Code\ITEC696\`.

Additionally, we'll need to add this folder to `PYTHONPATH` through the Spyder GUI under `Tools`.

---


### Mac/Linux

On Unix systems you can run the following, substituting `...` for the written out path on your system. Note the usual home folder shortcut `~` may not work here.


```bash
echo 'export PATH="/.../Code/ITEC696/unit5:$PATH"' >> ~/.bashrc
echo 'export PYTHONPATH="/.../Code/ITEC696"' >> ~/.bashrc
source ~/.bashrc
```

## Testing Jupyter Notebook

Now that our Python environment setup is complete, we will test one other tool we'll use in this course: Jupyter Notebook. **Jupyter Notebook** is an interactive, browser-based Python interpreter and is *extremely* useful for exporting documents.

In your terminal run

```bash
source activate itec696 # may be optional, depending on system
cd ~/Code/ITEC696 
jupyter notebook
```

And watch as a browser window opens, beginning in the same folder where you launched. You can now both

* Start a new notebook `Untitled.ipynb` by clicking `New -> Python 3` from the dropdown menu in the upper right corner.
* Open any of the course notebooks, e.g. `example.ipynb` or `unit0/lab.ipynb`.

