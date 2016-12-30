# PythonInventorAddIn

Autodesk Inventor 2010 COM AddIn writen in python 2.7 with pywin32.

How to make it work:

Use "C:\Python27\Lib\site-packages\win32com\client\makepy.py" to generate python file for Autodesk Inventor Object Library.

First, run script for com registration, then run inventor.

It does nothing, just registers itself in windows registry.
Inventor loads it at start and call Activate method
