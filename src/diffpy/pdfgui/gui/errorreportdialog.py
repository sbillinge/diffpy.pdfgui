#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Dmitriy Bryndin
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.4.1 on Tue Apr 18 22:38:01 2006

#
# "Bug report" Dialog
#
import wx
import wx.html
import webbrowser
import re

# Constants ------------------------------------------------------------------

ISSUESTRACKER = "https://github.com/diffpy/diffpy.pdfgui/issues"
USERSMAILINGLIST = "https://groups.google.com/d/forum/diffpy-users"

_MSG_TRAILER = """
<p>
You can view current bug reports and feature requests at
<a href="{issues}">{issues}</a>.
</p><p>
Discuss PDFgui and learn about new developments and features at
<a href="{mlist}">{mlist}</a>.
</p>
""".format(issues=ISSUESTRACKER, mlist=USERSMAILINGLIST)

_MSG_FEATURE_REQUEST = """
<p>
Share you thoughts about PDFgui!
</p>
""" + _MSG_TRAILER

_MSG_ERROR_REPORT = """
<p>
PDFgui has encountered a problem.  We are sorry for the inconvenience.
</p><p>
""" + _MSG_TRAILER

# ----------------------------------------------------------------------------

class ErrorReportDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ErrorReportDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_header = wx.html.HtmlWindow(self, wx.ID_ANY)
        self.label_log = wx.StaticText(self, wx.ID_ANY, "Error Log:")
        self.text_ctrl_log = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.button_google = wx.Button(self, wx.ID_ANY, "Google This Error")
        self.button_copyErrorLog = wx.Button(self, wx.ID_ANY, "Copy Error Log")
        self.button_close = wx.Button(self, wx.ID_CANCEL, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onGoogle, self.button_google)
        self.Bind(wx.EVT_BUTTON, self.onCopyErrorLog, self.button_copyErrorLog)
        # end wxGlade
        self.__customProperties()
        return

    def __set_properties(self):
        # begin wxGlade: ErrorReportDialog.__set_properties
        self.SetTitle("Problem Report for PDFgui")
        self.SetSize((540, 600))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ErrorReportDialog.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
        sizer_log = wx.BoxSizer(wx.VERTICAL)
        sizer_label = wx.BoxSizer(wx.HORIZONTAL)
        sizer_label.Add(self.label_header, 1, wx.EXPAND, 5)
        sizer_main.Add(sizer_label, 1, wx.ALL | wx.EXPAND, 5)
        sizer_log.Add(self.label_log, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        sizer_log.Add(self.text_ctrl_log, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        sizer_main.Add(sizer_log, 3, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer_main.Add(self.static_line_1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        sizer_buttons.Add((20, 20), 1, 0, 0)
        sizer_buttons.Add(self.button_google, 0, wx.ALL, 5)
        sizer_buttons.Add(self.button_copyErrorLog, 0, wx.ALL, 5)
        sizer_buttons.Add(self.button_close, 0, wx.ALL, 5)
        sizer_main.Add(sizer_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_main)
        self.Layout()
        # end wxGlade

    def __customProperties(self):
        """Set custom properties."""
        # Events
        self.errorReport = True
        self.label_header.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.onURL)
        return

    def ShowModal(self):
        # there are 2 modes: error report and feature request
        if self.text_ctrl_log.GetValue().strip() == "":
            self.SetTitle("Feature Request / Bug Report")
            self.label_header.SetPage(_MSG_FEATURE_REQUEST)
            self.label_header.SetBackgroundColour('')
            self.label_log.Hide()
            self.text_ctrl_log.Hide()
            self.button_google.Hide()
            self.button_copyErrorLog.Hide()
            self.SetSize((540, 200))
            self.errorReport = False
        else:
            self.SetTitle("Problem Report for PDFgui")
            self.label_header.SetPage(_MSG_ERROR_REPORT)
            self.label_header.SetBackgroundColour('')
            self.text_ctrl_log.Show()
            self.errorReport = True

        wx.Dialog.ShowModal(self)

    def onGoogle(self, event):  # wxGlade: ErrorReportDialog.<event_handler>
        # google the `str_to_search`, path-independent items, in the traceback when click button "google this error"
        traceback = self.text_ctrl_log.GetValue()
        str_to_search = ""
        # find 'errorwrapper.py", line 60, in _f' patterns in error log using regular expression
        pattern = re.compile('\w+\.py\"\,\s+line\s+\d+\,\s+in\s+\S+')
        pattern_found = re.findall(pattern, traceback)
        if len(pattern_found) != 0: # if found, replace '", line 60, in ' in the `pattern_found` with ' ' using regular expression
            str_to_search = ' '.join(pattern_found)
            str_to_search = re.sub('\"\,\s+line\s+\d+\,\s+in\s+',' ',str_to_search)
            str_to_search += " "
        # add the Error line in error log into querydata as well
        for line in traceback.split("\n"):
            if "Error:" in line:
                str_to_search += line.strip() + " "
        if str_to_search != "":
            webbrowser.open("https://www.google.com/search?q=" + str_to_search)
        else: # if no error information is extracted successfully above, just google the whole traceback.
            webbrowser.open("https://www.google.com/search?q=" + traceback)
        event.Skip()
        return

    def onCopyErrorLog(self, event):  # wxGlade: ErrorReportDialog.<event_handler>
        # copy the traceback enclosed in GitHub block quotations so it is easier to paste into GitHub issue.
        traceback = self.text_ctrl_log.GetValue()
        clipdata = wx.TextDataObject()
        clipdata.SetText("```" + "\n" + traceback + "\n" + "```")
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()
        event.Skip()
        return

    def onURL(self, event):  # wxGlade: ErrorReportDialog.<event_handler>
        # click on the URL link in dialog, it will open the URL in web browser.
        link = event.GetLinkInfo()
        webbrowser.open(link.GetHref())

# end of class ErrorReportDialog

##### testing code ############################################################

_EXAMPLE_TRACEBACK = """
Traceback (most recent call last):
  File "C:\DiffPy\Python25\lib\site-packages\diffpy.pdfgui-1.0_r3067_20090410-py2.5.egg\diffpy\pdfgui\gui\errorwrapper.py", line 60, in _f
    return func(*args, **kwargs)
  File "C:\DiffPy\Python25\lib\site-packages\diffpy.pdfgui-1.0_r3067_20090410-py2.5.egg\diffpy\pdfgui\gui\mainframe.py", line 2176, in onSave
    self.control.save(self.fullpath)
  File "C:\DiffPy\Python25\lib\site-packages\diffpy.pdfgui-1.0_r3067_20090410-py2.5.egg\diffpy\pdfgui\control\pdfguicontrol.py", line 507, in save
    self.projfile = projfile.encode('ascii')
UnicodeDecodeError: 'ascii' codec can't decode byte 0xb0 in position 115: ordinal not in range(128)
""".strip()

class MyApp(wx.App):
    def OnInit(self):
        self.dialog = ErrorReportDialog(None, -1, "")
        self.SetTopWindow(self.dialog)
        self.test()
        self.dialog.ShowModal()
        self.dialog.Destroy()
        return 1

    def test(self):
        '''Testing code goes here.'''
        self.dialog.text_ctrl_log.SetValue(_EXAMPLE_TRACEBACK)
        return

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

##### end of testing code #####################################################
