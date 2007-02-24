import wx
import eg
from SizeGrip import SizeGrip

class ButtonRow:
    
    def __init__(self, parent, buttonIds):
        self.parent = parent
        self.numSpecialCtrls = 0
        self.stdbtnsizer = stdbtnsizer = wx.StdDialogButtonSizer()
        default_button = None
        text = eg.text.General
        for ctrl in buttonIds:
            if ctrl not in (wx.ID_OK, wx.ID_CANCEL, wx.ID_HELP):
                stdbtnsizer.Add(ctrl)
                
        if wx.ID_OK in buttonIds:
            okButton = wx.Button(parent, wx.ID_OK, text.ok)
            okButton.Bind(wx.EVT_BUTTON, self.OnOK)
            stdbtnsizer.AddButton(okButton)
            default_button = okButton
            self.okButton = okButton
            
        if wx.ID_CANCEL in buttonIds:
            cancelButton = wx.Button(parent, wx.ID_CANCEL, text.cancel)
            cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
            stdbtnsizer.AddButton(cancelButton)
            if not default_button:
                default_button = cancelButton
            self.cancelButton = cancelButton
        
        if wx.ID_HELP in buttonIds:
            helpButton = wx.Button(parent, wx.ID_HELP, text.help)
            helpButton.Bind(wx.EVT_BUTTON, self.OnHelp)
            stdbtnsizer.AddButton(helpButton)
            if not default_button:
                default_button = helpButton
            self.helpButton = helpButton
        
        stdbtnsizer.Realize()
        default_button.SetDefault()
        
        self.sizer = sizer = wx.BoxSizer(wx.HORIZONTAL)
        if parent.GetWindowStyleFlag() & wx.RESIZE_BORDER:
            self.sizeGrip = SizeGrip(parent)
            sizer.Add(self.sizeGrip.GetSize(), 1)
            sizer.Add(stdbtnsizer, 0, wx.TOP|wx.BOTTOM, 6)
            sizer.Add(self.sizeGrip, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT)
        else:
            sizer.Add((3,3), 1)
            sizer.Add(stdbtnsizer, 0, wx.TOP|wx.BOTTOM, 6)
            sizer.Add((2,2), 0)      

        self.sizer = sizer
        
        
    def Add(
        self, 
        ctrl, 
        proportion=0, 
        flags=wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 
        border=5
    ):
        if self.numSpecialCtrls == 0:
            self.sizer.Insert(0, (5,5))
        self.sizer.Insert(
            self.numSpecialCtrls+1, 
            ctrl, 
            proportion, 
            flags, 
            border
        )
        self.numSpecialCtrls += 1
        
    
    def OnOK(self, event):
        if hasattr(self.parent, "OnOK"):
            self.parent.OnOK(event)
        else:
            event.Skip()
            
            
    def OnCancel(self, event):
        if hasattr(self.parent, "OnCancel"):
            self.parent.OnCancel(event)
        else:
            event.Skip()
            
            
    def OnHelp(self, event):
        if hasattr(self.parent, "OnHelp"):
            self.parent.OnHelp(event)
        else:
            event.Skip()
            
     