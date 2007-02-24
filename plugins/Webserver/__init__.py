import eg

class PluginInfo(eg.PluginInfo):
    name = "Webserver"
    author = "Bitmonster"
    version = "1.0.0"
    description = (
        "Implements a small webserver, that you can use to generate events "
        "through HTML-pages."
    )
    icon = (
        "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeT"
        "AAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH1gEECzsZ7j1DbAAAAu1JREFUOMul"
        "kztsW3UUxn////Xb1684NXbzsOskA6UiklWCCOmCCiKwsCDBjBShThVCDICYgCIxMHgC"
        "BhYYkbJAhaIoIBCKKvUBhArHGLexaar4/bj2ffjey0CboagTZ/l0jo5+Ovp0PvifJR4c"
        "5F64NOMX7kcoyrppOwmBwOcRHTGZXBk7YuPW5bfrDwWcWv/gdSFlcWEp55mZyxCJhBGA"
        "ruvcqd+lXKpOsMxLpW/ffe8/gNz6h6/FYuFP184VlNO5E8yfTJEKu2QSQbojk51rt7nx"
        "Z4Pr124Sks7HP3918S0ACfDJlz+ueBRZfPaZJ5R3Xinw3HKKx7MRCgtTzCaDRAMKwjJo"
        "N1qcWX6Uu93xm/nn358/Bmzt7r+RX8wG4kGFdm+MGo3h93lojaCnO5RrbZpjQXYmSSrq"
        "Y2EpJ7zC/QLAA1Ctt5568lxeDHULTYaYQtLUwCOh3dX47Osr9EcG0qOgjUzyi1lq1drK"
        "MWBs2ul4LMLiXJxkSHLQNvB5PWiWzfZuid5wjGnZGMMxXr+faFTFmNihY4DANXyK9L28"
        "NkejM6J5NET4VSa2jaqGkIrEtWxsx0EfaAC47r/my3vN3mg4sAcjk0wyTLvR4vL31zls"
        "9FG8Pp5eXWZm9hEmtoMQgn5/iILbPr4AIbaq1b+Xd/ZmQ/WDO5QPWmSmIzQ6A8aWjTY2"
        "SSdVMoVTBFSVq7/XXOHY3wEoAPGl8+VWq3fBDai+W0ea2K8c0hxa5OdPoOAQUCRnl6bZ"
        "eKnASLf49ZdSM51OvvrH7mZXAeiWtweR3FrvqNF7Mb8wh5QSfzjEYVujdtRnYtuczk4x"
        "HQ3gdQwrEZxs39j6fKdSqbSU+5/Y++uHsieateuHg9VYPCpTqSSp6QSJmIqhm+z9VnJu"
        "V6o9Jv2beq++WywWf3IcZ/hgmNKh9JnVk4+d31CCyRXDljEAx9T6zrC+dzYrribCcn9z"
        "c/ObTqdzALjiIQmNArF76gcMYAB0gT7g3l/+ByWIP9hU8ktfAAAAAElFTkSuQmCC"
    )

import wx
import BaseHTTPServer
import SimpleHTTPServer
import os
import posixpath
import urllib
import threading
import httplib
import mimetypes



class MyServer(BaseHTTPServer.HTTPServer):
    pass
    #def handle_error(self, request, client_address):
    #    eg.PrintError("HTTP Error")
            
            
            
class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):	

    def do_GET(self):
        """Serve a GET request."""
        f = None
        try:
            p = self.path.split('?', 1)
            self.path = p[0]
            f = self.send_head()
            if f:
                self.copyfile(f, self.wfile)
                f.close()
                f = None
                if len(p) > 1:
                    a = p[1].split('&')
                    event = a[0]
                    withoutRelease = False
                    payload = None
                    if len(a) > 1:
                        startPos = 1
                        if a[1] == "withoutRelease":
                            withoutRelease = True
                            startPos = 2
                        if len(a) > startPos:
                            payload = []
                            for i in range(startPos, len(a)):
                                payload.append(a[i])
                    if event.strip() == "ButtonReleased":
                        self.EndLastEvent()
                    elif withoutRelease:
                        self.TriggerEnduringEvent(event, payload)
                    else:
                        self.TriggerEvent(event, payload)
        except Exception, ex:
            eg.PrintError("Webserver socket error", self.path)
            eg.PrintError(Exception, ex)
            if f is not None:
                f.close()
            if ex.args[0] == 10053: # Software caused connection abort
                pass
            elif ex.args[0] == 10054: # Connection reset by peer
                pass
            else:
                raise
            
            
    def log_message(self, format, *args):
        # supress all messages
        pass
    

    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax.

        Components that mean special things to the local file system
        (e.g. drive or directory names) are ignored.  (XXX They should
        probably be diagnosed.)

        """
        # stolen from SimpleHTTPServer.SimpleHTTPRequestHandler
        # but changed to handle files from a defined basepath instead
        # of os.getcwd()
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = self.server.basepath
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir): continue
            path = os.path.join(path, word)
        return path

    extensions_map = mimetypes.types_map.copy()
    extensions_map.update(
        {
            '': 'application/octet-stream', # Default
            '.py': 'text/plain',
            '.c': 'text/plain',
            '.h': 'text/plain',
            '.ico': 'image/x-icon',
        }
    )



class Webserver(eg.PluginClass):
    canMultiLoad = True

    class text:
        port = "Use port:"
        documentRoot = "Use document root:"
        eventPrefix = "Use event prefix:"
    
    def __init__(self):
        self.running = False


    def __start__(self, prefix=None, port=80, basepath=None):
        self.info.eventPrefix = prefix
        self.port = port
        self.basepath = basepath
        self.httpd_thread = threading.Thread(target=self.ThreadLoop)
        self.httpd_thread.start()
        self.running = True
        
        
    def __stop__(self):
        if self.running:
            self.abort = True
            conn = httplib.HTTPConnection("localhost:%d" % self.port)
            conn.request("QUIT", "/")
            conn.getresponse()        
            self.httpd_thread = None
            self.running = False
        
        
    def ThreadLoop(self):
        class mySubHandler(MyHTTPRequestHandler):
            TriggerEvent = self.TriggerEvent
            TriggerEnduringEvent = self.TriggerEnduringEvent
            EndLastEvent = self.EndLastEvent
            
        server = MyServer(('', self.port), mySubHandler)
        server.basepath = self.basepath

        # Handle one request at a time until stopped
        self.abort = False
        while not self.abort:
            server.handle_request()


    def Configure(self, prefix="HTTP", port=80, basepath=""):
        dialog = eg.ConfigurationDialog(self)
        
        portCtrl = eg.SpinIntCtrl(dialog, -1, port, min=1, max=65535)

        filepathCtrl = eg.DirBrowseButton(
            dialog, 
            -1, 
            size=(320,-1),
            startDirectory=basepath, 
            labelText="",
            buttonText=eg.text.General.browse
        )
        filepathCtrl.SetValue(basepath)
        
        editCtrl = wx.TextCtrl(dialog, -1, prefix)
        
        dialog.AddLabel(self.text.port)
        dialog.AddCtrl(portCtrl)
        dialog.AddLabel(self.text.documentRoot)
        dialog.AddCtrl(filepathCtrl)
        dialog.AddLabel(self.text.eventPrefix)
        dialog.AddCtrl(editCtrl)
        
        if dialog.AffirmedShowModal():
            return (
                editCtrl.GetValue(), 
                int(portCtrl.GetValue()), 
                filepathCtrl.GetValue()
            )
