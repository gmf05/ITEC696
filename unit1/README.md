# Setting Up (Locally)

## Download [Cygwin](https://cygwin.com/install.html) (Windows users only)

Run the setup file and choose a mirror. Then find and double click the following additional Cygwin packages to install them:

* openssh

* git (optional for cloning, see below)

* python3-ipython (optional)

## Get the course repo:

### Clone (Option A):

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

### Download (Option B):

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

## Install [Miniconda](https://conda.io/miniconda.html) or  [Anaconda](https://www.anaconda.com/download/)

## Create virtual environment and install packages

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

## Install [Spyder](https://pythonhosted.org/spyder/installation.html)

```bash
conda install -c anaconda spyder
```
##



