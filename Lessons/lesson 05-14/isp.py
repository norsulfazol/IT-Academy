# class Drawer:

#     def drawLine():
#         pass

#     def drawCircle():
#         pass

#     def drawSquare():
#         pass

#     def drawTriangle():
#         pass

#     def drawStar():
#         pass

#     def drawCylinder():
#         pass

class LineDrawer:

    def drawLine():
        pass

class CircleDrawer:

    def drawCircle():
        pass

class ShapeDrawer:

    def drawShape():
        pass

class RectangleDrawer(LineDrawer):

    def drawRectangle(self):
        LineDrawer.drawLine()
        LineDrawer.drawLine()
        LineDrawer.drawLine()
        LineDrawer.drawLine()

class CylinderDrawer(LineDrawer, CircleDrawer):

    def drawCylinder(self):
        self.drawLine()
        self.drawLine()
        drawCircle()
        drawCircle()

class Drawer(RectangleDrawer, CylinderDrawer): pass