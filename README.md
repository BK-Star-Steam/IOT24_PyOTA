# Python Over-The-Air Update

This is a little Python3 project which allows you to update a python program without needing to rerun it. You can take a look at the example folder of this repository in order to understand how this script works.

## Requirements

The only file you need to used this update system for python project is the 'ota-update.py'. Keep in mind that in the directory where this script will be executed, files and folders will be created. I recommend executing this script inside an empty directory which will be used only for your python project.

It requires the [PrintBetter](https://github.com/gruvw/printbetter) python package in order to work.

## File architecture

The typical directory tree of a python project using the 'ota-update.py' script should look like this:

```text
.
├── deposit
├── logs
│   ├── logfile_DD-MM-YY_HH.MM.SS.log
│   └── ...
├── main
│   ├── main.py
│   └── ...
├── ota-update.py
```

* The 'deposit' folder is the place where you can put files from your python project. It can be assets or any type of files or folders. The files inside the 'main' folder will be replaced by the new ones inside the 'deposit' folder once/if the 'ota-update.yp' script is running. The file structure inside the deposit folder will be replicated inside the main folder. You should only place new files inside the deposit folder as opposed to place you whole python project every time: nothing is automatically deleted from the main directory, files that are found inside the 'deposit' folder will be added to the 'main' folder or will replace the old ones.
* The 'main' folder is where your python project is. The 'ota-update.py' script will automatically execute the 'main.py' file inside it.
* The 'logs' folder is the place where you will find the logs generated by the [PrintBetter](https://github.com/gruvw/printbetter) python package used by the 'ota-update.py' script.

### First execution

If there is no 'deposit' or 'main' folders in the same directory of the 'ota-update.py', the first execution of the script will create both of them (along with the 'logs' folder). It will then trow an "No 'main.py' inside the main directory." exception which is totally normal because the main directory didn't existed before. You can now place your python projects files inside the freshly created 'deposit' folder and run the 'ota-update.py' script again.

## How to use

## Why I created this
