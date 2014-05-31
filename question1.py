class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        '''
        initializing the coordinates
        '''
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.left = min(x1, x2)
        self.top = min(y1, y2)
        self.right = max(x1, x2)
        self.bottom = max(y1, y2)

#rectangle1 = Rectangle(12,23,13,24)
#rectangle2 = Rectangle(23,24,35,13)
def rectangle_overlap(rectangle1, rectangle2):
        if rectangle1.right > rectangle2.left and rectangle1.left < rectangle2.right and rectangle1.top < rectangle2.bottom and rectangle1.bottom > rectangle2.top:
            return True
        else:
            return False


