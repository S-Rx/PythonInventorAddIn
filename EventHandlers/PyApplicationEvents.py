#-*- coding: utf-8 -*-
#!/usr/bin/env python

# -------------------------------------------------------------------------------
# Name:        PyApplicationEvents
# Purpose:
#
# Author:      S.Hanin
#
# Created:     30.12.2016
# Copyright:   (c) S.Hanin 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------


class ApplicationEvents(object):

    def OnActivateDocument(self, DocumentObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnActivateView(self, ViewObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnActiveProjectChanged(self, ProjectObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnApplicationOptionChange(self, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnCloseDocument(self, DocumentObject, FullDocumentName, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnCloseView(self, ViewObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnDeactivateDocument(self, DocumentObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnDeactivateView(self, ViewObject, BeforeOrAfter, Context, ):
        pass

    def OnDisplayModeChange(self, ViewObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnDocumentChange(self, DocumentObject, BeforeOrAfter, ReasonsForChange, Context, HandlingCode):
        pass

    def OnInitializeDocument(self, DocumentObject, FullDocumentName, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnMigrateDocument(self, DocumentObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnNewDocument(self, DocumentObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnNewEditObject(self, EditObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnNewView(self, ViewObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnOpenDocument(self, DocumentObject, FullDocumentName, BeforeOrAfter, Context, HandlingCode):
        pass
        # win32gui.MessageBox(None, u"OnOpenDocument call", u"OK", 0)

    def  OnQuit(self, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnReady(self, BeforeOrAfter, Context, HandlingCode):
        pass
        #win32gui.MessageBox(None, u"OnReady call", u"OK", 0)

    def OnRestart32BitHost(self, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnSaveDocument(self, DocumentObject, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnTerminateDocumen(self, DocumentObject, FullDocumentName, BeforeOrAfter, Context, HandlingCode):
        pass

    def OnTranslateDocument(self, TranslatingIn, DocumentObject, FullFileName, BeforeOrAfter, Context, HandlingCode):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
