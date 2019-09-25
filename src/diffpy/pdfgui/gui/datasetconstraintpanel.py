#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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

# generated by wxGlade 0.9.3 on Fri Jul 19 16:01:02 2019

import wx
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui import tooltips
from diffpy.pdfgui.control.constraint import Constraint
from diffpy.pdfgui.gui.wxextensions.textctrlutils import textCtrlAsGridCell

class DataSetConstraintPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: DataSetConstraintPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.panelNameLabel = wx.StaticText(self, wx.ID_ANY, "Data Set Constraints")
        self.labelScaleFactor = wx.StaticText(self, wx.ID_ANY, "Scale Factor")
        self.textCtrlScaleFactor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.labelQdamp = wx.StaticText(self, wx.ID_ANY, "Qdamp")
        self.textCtrlQdamp = wx.TextCtrl(self, wx.ID_ANY, "")
        self.labelQbroad = wx.StaticText(self, wx.ID_ANY, "Qbroad")
        self.textCtrlQbroad = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: DataSetConstraintPanel.__set_properties
        self.panelNameLabel.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DataSetConstraintPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 5, 10)
        sizer_panelname = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_panelname.Add(self.panelNameLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)
        sizer_1.Add(sizer_panelname, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_1.Add(self.labelScaleFactor, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 5)
        grid_sizer_1.Add(self.textCtrlScaleFactor, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)
        grid_sizer_1.Add(self.labelQdamp, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 5)
        grid_sizer_1.Add(self.textCtrlQdamp, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)
        grid_sizer_1.Add(self.labelQbroad, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 5)
        grid_sizer_1.Add(self.textCtrlQbroad, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    # USER CONFIGURATION CODE #################################################

    def __customProperties(self):
        self._focusedText = None
        self.constraints = {}
        self.ctrlMap = {
                        'dscale'        :   'textCtrlScaleFactor',
                        'qdamp'         :   'textCtrlQdamp',
                        'qbroad'        :   'textCtrlQbroad',
                        }

        # Give each textCtrl a name that can be referenced
        for (key, value) in self.ctrlMap.items():
            textCtrl = getattr(self, value)
            textCtrl.SetName(key)

        # Setup the event code.
        for ctrlName in self.ctrlMap.values():
            textCtrl = getattr(self, ctrlName)
            textCtrl.Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
            textCtrl.Bind(wx.EVT_KILL_FOCUS, self.onLoseFocus)
            textCtrl.Bind(wx.EVT_KEY_DOWN, self.onTextCtrlKey)

        # Define tooltips.
        self.setToolTips(tooltips.datasetconstraintpanel)
        return

    # Create the onTextCtrlKey event handler from textCtrlAsGridCell from
    # wxextensions.textctrlutils
    onTextCtrlKey = textCtrlAsGridCell

    def setConstraintsData(self):
        """Set the values in the constraints panel.

        The values come from the constraints member dictionary.
        dscale
        qdamp
        qbroad
        """
        for (par, ctrlName) in self.ctrlMap.items():
            textCtrl = getattr(self, ctrlName)
            if par in self.constraints:
                val = self.constraints[par].formula
                textCtrl.SetValue(val)
            else:
                textCtrl.SetValue('')
        return

    def processFormula(self, value, parname):
        """Process a formula that was entered into a textCtrl."""
        formula = value.strip()
        oldconst = self.constraints.get(parname)
        oldformula = ""
        if oldconst:
            oldformula = oldconst.formula
        if formula == "":
            self.constraints.pop(parname, None)
        elif oldformula != formula:
            # Let the PDFGui error handler take care of this
            self.constraints[parname] = Constraint(formula)
            self.mainFrame.needsSave()

        return

    # EVENT CODE #############################################################
    def onSetFocus(self, event):
        """Saves a TextCtrl value, to be compared in onKillFocus later."""
        self._focusedText = event.GetEventObject().GetValue()
        event.Skip()
        return

    def onLoseFocus(self, event):
        """Record the user's selection for the text ctrl data."""
        textCtrl = event.GetEventObject()
        value = textCtrl.GetValue()
        par = textCtrl.GetName()
        self.processFormula(value, par)
        if par in self.constraints:
            val = self.constraints[par].formula
            textCtrl.SetValue(val)
        else:
            textCtrl.SetValue('')
        event.Skip()
        return

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Refresh the panel."""
        # Set the constraints data
        self.setConstraintsData()
        return

# end of class DataSetConstraintPanel
