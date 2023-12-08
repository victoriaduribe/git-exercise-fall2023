class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
 
    def get_area(self):
        return (1/2) * self.base * self.height
 
    def set_base(self, base):
        self.base = base
 
    def set_height(self, height):
        self.height = height
