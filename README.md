# auto_formfill

### Motivation
I came across a company called Carta Healthcare (www.carta.healthcare) that works with clinicians to support data abstraction for registeries, QI projects, and research. I wanted to try to replicate this task of automating the process of filling up registeries with the same data over and over again.

### How to run the script
To run this script, open up the terminal window, change the directory to the directory containing the python3 script using the command `cd`, and type in the following command : -
```
python3 <script_filename> <pdfform_filename>'
```

where, 
 <br/><script_filename> : refers to the name of the file in which this pythonscript is saved as. In my case it is "main.py"
 <br/><pdfform_filename> : refers to the name of the file in which the pdf form is saved as. You may use an absolute path or a relative path.
  
### About the script

This project aims to be able to write a Python script to be able to parse a pdf form file(AcroForm), read the data entered into the respective fields in the pdf, generate JavaScript code to be used to automatically fill up a web form.

I use the following libraries in this script : -
1. PyPDF2 (version 1.26.0)
2. sys
3. pyperclip (version 1.8.0)
4. webbrowser

This script accounts for the following field types in a pdf form : -
  1. Text fields
  2. Checkboxes/Radio buttons
  3. Drop down menu
  
### References

Castiglione, C., 2021. How to Automate Filling In Web Forms with Python - Learn to code in 30 Days. [online] Learn to code in 30 Days. Available at: <https://learn.onemonth.com/automate-web-forms-with-python/>.

Fossies.org. n.d. openslides: PyPDF2 Namespace Reference - doxygen documentation | Fossies Dox. [online] Available at: <https://fossies.org/dox/openslides-2.3-portable/namespacePyPDF2.html> [Accessed 15 March 2021].

Garg, A., 2020. How to Extract Data from PDF Forms Using Python. [online] Medium. Available at: <https://towardsdatascience.com/how-to-extract-data-from-pdf-forms-using-python-10b5e5f26f70> [Accessed 15 March 2021].

Juviler, J., 2020. What is UTF-8 Encoding? A Guide for Non-Programmers. [online] Blog.hubspot.com. Available at: <https://blog.hubspot.com/website/what-is-utf-8#:~:text=UTF%2D8%20is%20an%20encoding,or%20%E2%80%9CUnicode%20Transformation%20Format.%E2%80%9D> [Accessed 15 March 2021].

Sweigart, A., 2020. Automate the boring stuff with Python. 2nd ed. San Francisco: No Starch Press.
