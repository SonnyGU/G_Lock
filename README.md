<h1>"G-Lock: Password Manager"</h1>
<br />
</br>

<h2>Overview</h2>

G-Lock is a user-friendly desktop application designed to manage and store your passwords securely. 
Built with Python and Tkinter, users can generate random strong passwords, save them alongside the corresponding website and email/username details, and retrieve them easily. 
The application also features a search function to find stored credentials quickly.
<br />


<h2>Features</h2>

1. **Random Password Generation:** Generates a strong, random password combining letters, numbers, and symbols.
2. **Secure Password Storage:** Saves passwords and associated website and email/username information in a JSON file.
3. **Search Functionality:** Quickly retrieve passwords by searching for the associated website.
4. **User-Friendly Interface:** A simple and intuitive GUI built with Tkinter, making it easy for anyone to use.
5. **Clipboard Integration:** Automatically copies generated passwords to the clipboard for easy use.


<h2>Prerequisites </h2>
<h3>To run this project, you will need:</h3>

+ **Python:** The application is written in Python(3.6 and above), a recent version of [Python](https://www.python.org/downloads/).
+ **Pip:** Python's package installer, pip, should be installed for managing Python packages. It usually comes with Python installation.
+ **Tkinter installed** (usually comes with Python).
+ **pyperclip library installed** (pip install pyperclip).

<h2>Installation</h2>

- **Clone the Repository:** git clone https://github.com/SonnyGU/G_Lock.git
- **Install the Pyperclip library using pip:** pip install pyperclip
- **Run the Application:** python main.py 
<h2>Usage</h2>

- **Interact with the GUI:** Use the interface to generate passwords, save credentials, and search for stored information.
<h2>Data Storage</h2>

- Credentials are stored in myFile.json in the same directory as the script. Ensure this file exists or allow the application to create it upon adding the first set of credentials.


<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/CfcV2Rv.png" height="80%" width="80%" alt="G-Lock Steps"/>
<br />
<br />
Type in a website and hit the search function:  <br/>
<img src="https://i.imgur.com/ZlKovsL.png" height="50%" width="50%" alt="G-Lock Steps"/>
<br />
<br /> 
It Will Return Username and Password:    <br/>
<img src="https://i.imgur.com/QTBKLsj.png" height="50%" width="50%" alt="G-Lock Steps"/>
<br />
<br />
Hit generate Password   <br/>:
<img src="https://i.imgur.com/84wBAvR.png" height="50%" width="50%" alt="G-Lock Steps"/>
<br />
<br />
When a Password is generated, It Is Immediately Copied onto your Clipboard for Use:    <br/>
<img src="https://i.imgur.com/P4u5oNR.png" height="50%" width="50%" alt="G-Lock Steps"/>
<br />
<br />
Hit Add to Save the information, input fields will clear:   <br/>
<img src="https://i.imgur.com/0PbLr56.png" height="50%" width="50%" alt="G-Lock Steps"/>


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
