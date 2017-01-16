#-*- coding: utf-8 -*-
#!/usr/bin/env python

# -------------------------------------------------------------------------------
# Name:        AddIn
# Purpose:
#
# Author:      S.Hanin
#
# Created:     09.01.2017
# Copyright:   (c) S.Hanin 2017
# Licence:     <your licence>
# -------------------------------------------------------------------------------

from win32com.client import Dispatch, DispatchWithEvents

from EventHandlers.PyApplicationEvents import ApplicationEvents


class AddIn(object):
    def __init__(self, AddInSiteObject):
        self._app = Dispatch(AddInSiteObject).Application
        self._ApplicationEvents = DispatchWithEvents(self._app.ApplicationEvents, ApplicationEvents)

    def create_ui(self):
        pass
