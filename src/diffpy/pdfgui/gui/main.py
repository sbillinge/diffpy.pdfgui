#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.4 on Tue Feb 21 12:00:30 2006

import wx


class PDFGuiApp(wx.App):
    def OnInit(self):
        from diffpy.pdfgui.gui.mainframe import MainFrame

        self.frame = MainFrame(None, -1, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class PDFGuiApp


def main():
    """Kick starter for the PDFgui graphical user interface.

    This function is normally called from a light-weight console starter
    diffpy.pdfgui.applications.pdfgui. Command line options and
    arguments can be passed via cmdopts and cmdargs variables of the
    pdfguiglobals module.
    """
    app = PDFGuiApp(0)
    app.MainLoop()
    return


if __name__ == "__main__":
    main()
