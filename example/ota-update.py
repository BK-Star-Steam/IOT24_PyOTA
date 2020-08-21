import os
import printbetter as pb
import shutil
from functools import reduce
import subprocess as sp
import time


def depositFiles():
    """
    Scans the deposit directory.

    :return: the name of each file inside the deposit directory
    :rtype: list
    """
    files = []
    for file in os.listdir("./deposit"):
        if not file.startswith("."):
            files.append(file)
    return files


def directoryTree(rootdir):
    """
    Generates a directory tree of the given directory.

    :param rootdir: root directory
    :type rootdir: str
    :return: the directory tree
    :rtype: dict
    """
    directory = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], directory)
        parent[folders[-1]] = subdir
    return directory


def moveDir(directoryTree, branch):
    """
    Recursive function used to move the files from the deposit to the main directory.

    :param directoryTree: the directory tree of the deposit directory
    :type directoryTree: list
    :param branch: the current branch (recursive func.)
    :type branch: str
    """
    for name in directoryTree:
        if ".keep" not in name:
            if "." in name:
                src = "./deposit/" + branch + name
                dest = "./main/" + branch + name
                # print(src, "->", dest)
                if not os.path.isdir("./main/" + branch):
                    os.makedirs("./main/" + branch)
                shutil.move(src, dest)
            else:
                moveDir(directoryTree[name], branch + name + "/")
                os.rmdir("./deposit/" + branch + name)


def moveToMain():
    """
    Moves all the files from the deposit to main directory.
    """
    tree = directoryTree("deposit")
    moveDir(tree["deposit"], "")
    pb.info("Main has been updated with new deposit files.")


def startMain():
    """
    Starts the main.py python script inside the main directory.

    :raises Exception: if no main.py found inside the main directory
    :return: the subprocess
    """
    files = []
    for file in os.listdir("./main"):
        if not file.startswith("."):
            files.append(file)
    if "main.py" in files:
        pb.info("Starting main program.")
        extProc = sp.Popen(['python', 'main.py'], cwd="./main")
        return extProc
    else:
        raise Exception("No 'main.py' inside main.")


def endMain(mainProc):
    """
    Kills the given subprocess.

    :param mainProc: the currently running subprocess
    """
    status = sp.Popen.poll(mainProc)
    if status is None:
        sp.Popen.terminate(mainProc)
        pb.info("Main program terminated.")


pb.init()

# checks if OTA architecture OK and updates it if needed
neededDirectories = ("deposit", "main")

for directory in neededDirectories:
    if not os.path.isdir(f'./{directory}'):
        pb.warn(f"No '{directory}' directory found: creating one...")
        os.mkdir(f'./{directory}')
        pb.info(f"Directory '{directory}' created.")

pb.info("OTA architecture is set up.")

# checks if deposit is not empty, if yes: updates main
if depositFiles():
    pb.info("New files in deposit detected.")
    moveToMain()

# starts main
running = True
while running:
    mainProc = startMain()

    while not depositFiles() and running:
        status = sp.Popen.poll(mainProc)
        if status is not None:
            pb.info("Main program reached its end.")
            running = False

    if running:
        pb.info("New files in deposit detected.")
        endMain(mainProc)
        pb.info("10 seconds before update...")
        time.sleep(10)
        moveToMain()

pb.exit()
