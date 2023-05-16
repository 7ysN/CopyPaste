# CopyPaste.py

**Sometimes we work in hardened environments. For example, the simple copy and paste operation is cancelled.** 
**In cases where it is not possible to copy and paste using `CTRL+V`, you can use this program instead.**
**This program gets a text from the end user and automatically types it on the keyboard.**


## Usage:
**1. In the large upper window, paste the `Text` to transfer.**

**2. In the small window below, you can set the `Timer` for the copy operation.**

**3. Then, press `Paste` click on the second screen and wait for the text to be copied.**


![2023-03-18 19_26_02-dist](https://user-images.githubusercontent.com/62604022/226123201-55c54ce7-3506-4a8b-ba96-d2a367d95797.png)

## Building Standalone Executable (~10MB):
```
pip install -r requirements.txt
pyinstaller -F .\CopyPaste.py -w
```

## Enjoy !
