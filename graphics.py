
import tkinter as tk

class GraphWin(tk.Canvas):

    def __init__ (self, title="Graphics Window", width=200, height=200, autoflush=True):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height)
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.foreground = "black"
        self.items = []
        self.mouse = None
        self.mouseY = None
        self.bind("<Button-1>", self._onClick)
        self.height = height
        self.width = width
        self.autoflush = autoflush
        self._mouseCallback = None
        self.trans = None
        self.closed = False
        master.lift()
        if autoflush: _root.update()

    def __checkOpen(self):
        if self.closed:
            raise GraphicsError("window is closed")

    def setBackground(self, color):
        self.__checkOpen()
        self.config(bg=color)
        self.__autoflush()
    
    def setCoords(self, x1, y1, x2, y2):
        self.trans = Transform(self.width, self.height, x1, y1, x2, y2)

    def close(self):
        if self.closed: return
        self.closed = True
        self.master.destroy()
        self.__autoflush()
        ''' close window '''

    def isClosed(self):
        return not self.closed

    def isOpen(self):
        return not self.closed

    def __autoflush(self):
        if self.autoflush:
            _root.update()

    def plot(self, x, y, color="black"):
        self.__checkOpen()
        xs,ys = self.toScreen(x,y)
        self.create_line(xs,ys,xs+1,ys, fill=color)
        self.autoflush()
        ''' set colors '''

    def plotPixel(self, x, y, color="black"):
        self.__checkOpen()
        self.create_line(x,y,x+1,ys, fill=color)
        self.__autoflush()
        ''' set pixels colors '''

    def flush(self):
        self.__checkOpen()
        self.update_idletasks()
        ''' update the drawing to window '''

    def getMouse(self):
        self.update()
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
            if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1)
        x,y = self.toWorld(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return Point(x,y)
        ''' waiting for mouse click and return object by representing click'''

    def checkMouse(self):
        if self.isClosed():
            raise GraphicsError("checkMouse in closed window")
        self.update()
        if self.mouseX != None and self.mouseY != None:
            x,y = self.toWorld(self.mouseX, self.mouseY)
            self.mouseX = None
            self.mouseY = None
            return Point(x,y)
        else:
            return None
        ''' If nothing has been clicked, this returns last mouse '''

    def getHeight(self):
        return self.height
        '''Reset Height'''

    def getWidth(self):
        return self.width
        '''Reset width'''
            