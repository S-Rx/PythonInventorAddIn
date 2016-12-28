#-*- coding: utf-8 -*-
#!/usr/bin/env python

# -------------------------------------------------------------------------------
# Name:        AddInServer
# Purpose:
#
# Author:      S.Hanin
#
# Created:     15.12.2016
# Copyright:   (c) S.Hanin 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import win32com.client.gencache as gencache

import win32con
import win32com
import win32gui
import logging

module = gencache.GetModuleForTypelib("{D98A091D-3A0F-4C3E-B36E-61F62068D488}", 0, 1, 0)

__author__ = 'Ханин'

logger = logging.getLogger("AddInServer")
logger.setLevel(logging.WARNING)
logger.addHandler(logging.StreamHandler)


class AddInServer(module.ApplicationAddInServer):
    _public_methods_ = ['Activate', 'Deactivate', 'ExecuteCommand']
    _public_attrs_ = ['Automation']
    _reg_desc_ = "Simple Python AddIn sample that demonstrates basic API functionality"
    _reg_progid_ = "Python.InventorAddIn"
    _reg_clsid_ = "{0445899D-ED0A-4966-82B3-BF2E960BC6E4}"  # This guid should be unique
    _reg_catids_ = ["{39AD2B5C-7A29-11D6-8E0A-0010B541CAA8}", ]
    _reg_options_ = {"Settings": ""}
    _settings_ = {"Hidden": "1", "UserUnloadable": "0", "LoadOnStartUp": "1"}
    m_inventorApplication = None

    def __init__(self):
        win32gui.MessageBox(None, u"__init__ call", u"OK", 0)  # change it to pass

    def Activate(self, AddInSiteObject, firstTime):
        """

        :param AddInSiteObject: Inventor.ApplicationAddInSite
        :param firstTime: bool
        :return: Void

        the Activate method is called by Inventor when it loads the addin
        the AddInSiteObject provides access to the Inventor Application object
        the FirstTime flag indicates if the addin is loaded for the first time
        """

        try:
            AddInSiteObject = win32com.client.Dispatch(AddInSiteObject)
            AddInServer.m_inventorApplication = AddInSiteObject.Application
            win32gui.MessageBox(None, u"LOAD OK", u"OK", 0)
        except Exception as err:
            win32gui.MessageBox(None, u"Error while loading Python.InventorAddIn", u"ERROR", 0)

    def Deactivate(self):
        self.m_inventorApplication = None

    def ExecuteCommand(self, CommandID):
        """
        this method was used to notify when an AddIn command was executed
        the CommandID parameter identifies the command that was executed

        Note:this method is now obsolete, you should use the new
        ControlDefinition objects to implement commands, they have
        their own event sinks to notify when the command is executed
        :param CommandID: int
        :return: Void
        """
        pass

    @property
    def Automation(self):
        """
        //if you want to return an interface to another client of this addin,
        //implement that interface in a class and return that class object
        //through this property
        """
        return None


def main():
    import sys
    import win32com.server.register
    win32com.server.register.UseCommandLine(AddInServer)
    if "--register" in sys.argv:
        import win32api
        base = win32con.HKEY_CLASSES_ROOT
        key = "CLSID\\%s\\Settings" % AddInServer._reg_clsid_
        hkey = win32api.RegCreateKey(base, key)

        win32api.RegSetValueEx(hkey, "AddInType", None, win32con.REG_SZ, "Standard")
        win32api.RegSetValueEx(hkey, "LoadOnStartUp", None, win32con.REG_SZ, "1")
        win32api.RegSetValueEx(hkey, "Hidden", None, win32con.REG_SZ, "0")
        win32api.RegSetValueEx(hkey, "UserUnloadable", None, win32con.REG_SZ, "1")
        win32api.RegSetValueEx(hkey, "Version", None, win32con.REG_SZ, "0")

        key = "CLSID\\%s\\Required Categories" % AddInServer._reg_clsid_
        win32api.RegCreateKey(base, key)
        subkey = "{0}\\{1}".format(key, "{E357129B-DB40-11D2-B783-0060B0F159EF}")
        win32api.RegCreateKey(base, subkey)


if __name__ == "__main__":
    main()
