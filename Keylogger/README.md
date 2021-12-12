
**GETTING STARTED – PYTHON, PYCHARM AND MODULES**

Ensure you have Python installed as well as the proper modules.

**Step One:** Go to https://www.python.org, navigate to the downloads section and download the latest version of python.
**Step Two:** Go through the setup wizard and make sure to install pip as well as add python to the path 

![image](https://user-images.githubusercontent.com/37224519/145714855-d524af9f-0454-4cc1-9c0e-1077e603e7ab.png)

**Step Three:** Go to https://www.jetbrains.com/pycharm/download/#section=windows, under Community, choose the free download option. Go through the setup wizard using default options.
**Step Four:** Open PyCharm once downloaded and select Create Open  

**Step 5:** Now you will download all packages / modules / dependencies for the project. There are multiple methods to do this, including using the pip tool, or directly importing through PyCharm. We will be directly importing all packages in Python (because often permission and file paths can get messed up when using the pip tool).

To install a package through PyCharm, navigate to File --> Settings (CTRL + ALT + S).
Under settings, navigate to Project: Project Name, and select Project Interpreter.
In the Project Interpreter, click the + icon to add a new module.

![image](https://user-images.githubusercontent.com/37224519/145714956-da19592d-4d06-4aec-a073-5073705ae780.png)

When you have clicked on the + icon, a new window will pop open named Available Packages. We can search for each module / package and install directly into our project. For
example, to install the cryptography module, simply search “cryptography”, click the package which says cryptography, then click Install Package and wait for it to install.

![image](https://user-images.githubusercontent.com/37224519/145714987-82184fde-f998-4c7f-a874-e6ab44e4f6c5.png)

Once package has been successfully installed, we can move onto the next module to install.
For this project, install all of the following modules (name is exactly the name of the package)
- pywin32 (To get the clipboard information)
- pynput (To log keys using python)
- scipy (To writing to a .wav file) 
- cryptography (To encrypt files)
- requests (To Manage requests)
- pillow (To take a screenshot)
- sounddevice (To record with microphone)

Once you have imported all modules, exit out all of settings windows and wait a few minutes for each package to install.

Once all packages are installed you can just run your code
