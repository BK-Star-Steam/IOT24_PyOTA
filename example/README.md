# Python OTA update example

## Try it out

1. Run the 'ota-update.py' script
   * This will execute the 'main.py' script inside the main directory
     * This script is just printing the content of the 'info.txt' file every 3 seconds
   * The output will be displayed
2. Move or copy the content of the 'to_deposit' directory to the 'deposit' directory
   * The 'ota-update.py' script will notice that change
   * It will kill the currently running 'main.py' script
   * It will update the files inside the 'main' directory with the new ones from the 'deposit' directory
   * After that, the updated 'main.py' script will start
     * This update is adding a new file ('text.txt')
     * The updated 'main.py' file will now print the 'text.txt' and the 'info.txt' content
3. Press <kbd>ctrl</kbd> + <kbd>c</kbd>, to kill the 'ota-update.py' script

## Be careful

You need to run the 'ota-update.py' script directly from its parent directory!

For example:

```bash
cd users/gruvw/python-ota-update/example
python ota-update.py
```

## Issue

Fill free to open an issue if anything is not working for you.
