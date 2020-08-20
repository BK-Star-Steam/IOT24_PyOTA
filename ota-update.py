import os
import printbetter as pb
import shutil
from functools import reduce
import subprocess as sp
import time


def depositFiles():
    files = []
    for file in os.listdir("./deposit"):
        if not file.startswith("."):
            files.append(file)
    return files


def directoryTree(rootdir):
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
    for name in directoryTree:
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


def moveToMain(names):
    # if "main.py" in names:
    tree = directoryTree("deposit")
    moveDir(tree["deposit"], "")
    pb.info("Main has been updated with new deposit files.")
    # else:
    #     raise Exception("No 'main.py' inside deposit.")


def startMain():
    files = []
    for file in os.listdir("./main"):
        if not file.startswith("."):
            files.append(file)
    if "main.py" in files:
        pb.info("Starting main program.")
        extProc = sp.Popen(['python3', 'main.py'], cwd="./main")
        return extProc
    else:
        raise Exception("No 'main.py' inside main.")


def endMain(mainProc):
    status = sp.Popen.poll(mainProc)
    if status is None:
        sp.Popen.terminate(mainProc)
        pb.info("Main program terminated.")


pb.init()

# checking if OTA architecture OK and update it if needed
neededDirectories = ("deposit", "main")

for directory in neededDirectories:
    if not os.path.isdir(f'./{directory}'):
        pb.warn(f"No '{directory}' directory found: creating one...")
        os.mkdir(f'./{directory}')
        pb.info(f"Directory '{directory}' created.")

pb.info("OTA architecture is set up.")

# checking if deposit is not empty, if yes: update main
if depositFiles():
    pb.info("New files in deposit detected.")
    moveToMain(depositFiles())

# start main
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
        time.sleep(10)
        pb.info("Interupting main program.")
        endMain(mainProc)
        moveToMain(depositFiles())

pb.exit()
