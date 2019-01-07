#!/usr/bin/env python

import pcbnew
import wx

def positon_from_file(filename):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()
    positions = {}
    for line in content:
        name, x, y = line.split()
        x, y = float(x), float(y)
        positions[name] = (x, y)
    return positions


def move_module_ref2gridori(x,y,ref, brd = None):
    if not brd:
        brd = pcbnew.GetBoard()
    m = brd.FindModuleByReference(ref)
    if m:
        grid_origin = brd.GetGridOrigin()
        m.SetPosition(grid_origin + pcbnew.wxPointMils(x,y))
        #  m.SetPosition(pcbnew.wxPointMils(x,y))
        #  m.Move(grid_origin + pcbnew.wxPointMils(x,y))

class keyboard_auto_layout( pcbnew.ActionPlugin ):
    """
    gen_mf_doc: A plugin used to generate BOM and position file
    How to use:
    - just call the plugin
    - the BOM and Position file will generate under the PCB file folder
      BOM file name is <pcb file name>_BOM.csv
      Position file name is <pcb file name>_POS.csv
    - the Gerber and drill file will generate under gerber folder
    """

    def defaults( self ):
        """
        Method defaults must be redefined
        self.name should be the menu label to use
        self.category should be the category (not yet used)
        self.description should be a comprehensive description
          of the plugin
        """
        self.name = "Keyboard Auto Layout"
        #self.category = "Modify PCB"
        self.description = "Keyboard Auto Layout tool"

    def Run( self ):
        with wx.FileDialog(None, "Open position file", wildcard="position file (*.txt)|*.txt",
                       style=wx.FD_OPEN) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathname = fileDialog.GetPath()
            positions = positon_from_file(pathname)
            for name in positions:
                x, y = positions[name]
                move_module_ref2gridori(x , y ,name)
            pcbnew.Refresh()



keyboard_auto_layout().register()





