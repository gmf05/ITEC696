# ITEC696: Python Programming for Business Analytics

##

# Setting Up (Locally)

## 1. Download [Cygwin](https://cygwin.com/install.html) (Windows users): 
Run the setup file and choose a mirror. Then find and double click the following additional Cygwin packages to install them:

* openssh

* git (optional for cloning, below)

* python3-ipython (optional)


## 2. Download Miniconda / Anaconda / [Spyder](https://pythonhosted.org/spyder/installation.html).

## 3. Install / configure pip

## 4. Get the course repo:

### Clone:

#### Cygwin Terminal (Windows)
```
cd /cygdrive/c/Users/$USER/Documents/ITEC621
git clone https://github.com/gmf05/ITEC696.git repo
```

#### Unix Terminal (Mac/Linux)
```
cd ~/Documents/ITEC621
git clone https://github.com/gmf05/ITEC696.git repo
```

### Download:

Download the repo as a `.zip` file and unpack it into your working directory.


#### Cygwin Terminal (Windows)
```
cd /cygdrive/c/Users/$USER/Documents/ITEC621
unzip /cygdrive/c/Users/$USER/Downloads/ITEC621-master.zip
mv ITC621-master repo
rm /cygdrive/c/Users/$USER/Downloads/ITEC621-master.zip
```

#### Unix Terminal (Mac/Linux)
```
cd ~/Documents/ITEC621
unzip ~/Downloads/ITEC621-master.zip
mv ITC621-master repo
rm ~/Downloads/ITEC621-master.zip
```

## 5. Create virtual environment and install packages

Windows
```

# create virtual environment
# TODO: FIX
python3 -m venv env/python/<YOUR ENVIRONMENT NAME>

# activate virtual environment
# TODO: FIX
source env/python/<YOUR ENVIRONMENT NAME>/bin/activate

# install packages from list
pip install -r repo/requirements.txt

```

Mac/Linux
```

# see where Python 3 lives before (optional)
which python3  

# create virtual environment
python3 -m venv env/python/<YOUR ENVIRONMENT NAME>

# activate virtual environment
source env/python/<YOUR ENVIRONMENT NAME>/bin/activate

# verify where Python 3 and pip are called now (optional)
which python3
which pip 

# install packages from list
pip install -r repo/requirements.txt

```

##

# Setting Up (Remotely)

## 1. Download and move key

Start a Terminal (Mac/Linux) or Cygwin Terminal (Windows)

#### Cygwin Terminal (Windows)
```
mkdir ~/.ssh # if it doesn't exist already
mv /cygdrive/c/Users/$USER/Downloads/MYKEY.pem ~/.ssh/
```

#### Unix Terminal (Mac/Linux)
```
mkdir ~/.ssh # if it doesn't exist already
mv $HOME/Downloads/<KEY FILE> ~/.ssh/
```

## 2. Login

`ssh -i ~/MYKEY.pem <STUDENT ID>@neurocoding.info`

## 3. Create virtual environment and install packages:

```

# see where Python 3 lives before
which python3 

# create virtual environment
python3 -m venv env/python/<YOUR ENVIRONMENT NAME>

# activate virtual environment
source env/python/<YOUR ENVIRONMENT NAME>/bin/activate

# notice the tag with <YOUR ENVIRONMENT NAME> that's now
# displayed in the shell

# verify where Python 3 and pip are called now 
which python3
which pip 

# install packages
pip install ipython
pip install jupyter
which ipython

# install packages from list
pip install -r repo/requirements.txt

```

## 4. Make virtual environment start automatically from now on

```
echo "source env/python/<YOUR ENVIRONMENT NAME>/bin/activate" >> ~/.profile
source ~/.profile
```

## 5. Start Jupyter Notebook behind screen:
	
```
screen
jupyter notebook
```

Then hit `CTRL+A` followed by `CTRL+D` to detach from the screen session and type `exit` to leave the SSH connection.


## 6. Start an SSH tunnel

`ssh -i ~/.ssh/<KEY NAME> -f -N -L 8888:localhost:8888 <STUDENT ID>@neurocoding.info`

## 7. Connect to Jupyter Notebook

Open a web browser and navigate to `localhost:8888`



