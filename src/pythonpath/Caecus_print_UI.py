# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Wed Dec 12 22:20:01 2018
#      by: unodit 0.7.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
import serial
import serial.tools.list_ports

from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor

class Caecus_print_UI(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...
    """
    def __init__(self):
        ports = serial.tools.list_ports.comports()
        available_ports = [port.device for port in ports]
    
        self.LocalContext = uno.getComponentContext()
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)
        self.DialogModel.Height = 122
        self.DialogModel.PositionY = "29"
        self.DialogModel.Closeable = True
        self.DialogModel.Name = "Imprimir com CAECUS"
        self.DialogModel.PositionX = "85"
        self.DialogModel.Width = 166
        self.DialogModel.Moveable = True


        # --------- create an instance of ComboBox control, set properties ---
        self.PortaSerial = self.DialogModel.createInstance("com.sun.star.awt.UnoControlComboBoxModel")

        self.PortaSerial.Dropdown = True
        self.PortaSerial.Height = 11
        self.PortaSerial.PositionY = "100"
        self.PortaSerial.Name = "PortaSerial"
        self.PortaSerial.PositionX = "8"
        self.PortaSerial.TabIndex = 0
        self.PortaSerial.Width = 70
        self.PortaSerial.StringItemList = available_ports

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("PortaSerial", self.PortaSerial)

        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        fonte_label1 = uno.createUnoStruct("com.sun.star.awt.FontDescriptor", Name="Segoe UI", Height=12)
        self.Label1.Height = 38
        self.Label1.PositionY = "60"
        self.Label1.Name = "Label1"
        self.Label1.PositionX = "8"
        self.Label1.Label = "Selecione a porta em que está conectada a impressora:"
        self.Label1.TabIndex = 3
        self.Label1.Width = 78
        self.Label1.MultiLine = True
        self.Label1.Align = 1
        self.Label1.FontDescriptor = fonte_label1

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

        # --------- create an instance of FixedText control, set properties ---
        self.Titulo = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        fonte_titulo = uno.createUnoStruct("com.sun.star.awt.FontDescriptor", Name="Segoe UI", Height=16)
        self.Titulo.Height = 50
        self.Titulo.Name = "Titulo"
        self.Titulo.PositionY = "5"
        self.Titulo.PositionX = "5"
        self.Titulo.Label = "Imprimir em Braille com a impressora CAECUS"
        self.Titulo.Width = 156
        self.Titulo.TabIndex = 1
        self.Titulo.MultiLine = True
        self.Titulo.Align = 1
        self.Titulo.FontDescriptor = fonte_titulo

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Titulo", self.Titulo)

        # --------- create an instance of Button control, set properties ---
        self.BotaoImprimir = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        fonte_botao = uno.createUnoStruct("com.sun.star.awt.FontDescriptor", Name="Segoe UI", Height=13)
        self.BotaoImprimir.Height = 32
        self.BotaoImprimir.PositionY = "80"
        self.BotaoImprimir.Name = "BotaoImprimir"
        self.BotaoImprimir.PositionX = "93"
        self.BotaoImprimir.Label = "Imprimir"
        self.BotaoImprimir.TabIndex = 2
        self.BotaoImprimir.Width = 66
        self.BotaoImprimir.FontDescriptor = fonte_botao

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("BotaoImprimir", self.BotaoImprimir)

        # add the action listener
        self.DialogContainer.getControl('BotaoImprimir').addActionListener(self)
        self.DialogContainer.getControl('BotaoImprimir').setActionCommand('BotaoImprimir_OnClick')

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        
        if oActionEvent.ActionCommand == 'BotaoImprimir_OnClick':
            self.BotaoImprimir_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------