# Python OTA update example

This folder exists in order for you to try the _ota-update.py_ script and understand how it works.

## Try it out

1. Run the _ota-update.py_ script
   * This will execute the _main.py_ script inside the main directory
     * This script is just printing the content of the _info.txt_ file every 3 seconds
   * The output will be displayed
2. Move or copy the content from the *to_deposit* folder to the _deposit_ directory
   * The _ota-update.py_ script will notice that change
   * It will kill the currently running _main.py_ script
   * It will update the files inside the _main_ directory with the new ones from the _deposit_ directory
   * After that, the updated _main.py_ script will start
     * This update is adding a new file (_text.txt_)
     * The updated _main.py_ file will now print the _text.txt_ and the _info.txt_ content
3. Press <kbd>ctrl</kbd> + <kbd>c</kbd>, to kill the _ota-update.py_ script

## Be careful

You need to run the _ota-update.py_ script directly from its parent directory!

For example:

```bash
cd users/gruvw/python-ota-update/example
python ota-update.py
```

## Issues

Fill free to open an issue if anything is not working for you.
