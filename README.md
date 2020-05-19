

Netspeed is a command line application to calculate your internet speed.


## Prerequisites

Netspeed requires the following:

```
Python 3.5 and above
Tkinter
Click
Pyspeedtest
```
Install Click using:
```
pip3 install click
```

Install pyspeedtest using:
```
pip3 install pyspeedtest
```

### Installing

To install Netspeed, clone the repository. Open the terminal in the directory and run the following command in terminal:
```
pip3 install --editable .
```


## Running the Script:

Open the terminal and enter the command:
```
netspeed run
```
A window will appear. Click the top button and wait for some time (usually 20 sec)
Results will be shown.

## Issue with pyspeedtest

The script will fail to connect to a server beacause of a bug in the pyspeedtest library.
It's easier to correct it in linux than windows.
Enter the command:
```
pip show pyspeedtest
```
Navigate to the location of the package. 
```
vi pyspeedtest.py
```
Change the url in line 186 in the file to "c.speedtest.net" and save.

