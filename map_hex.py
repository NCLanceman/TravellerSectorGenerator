class Map_Hex(): 
    #Derived from https://www.redblobgames.com/grids/hexagons/

        def __init__(self, name): 
            self.name = name
            self.x = 0
            self.y = 0
            self.z = 0
            self.col = int(name[:2])
            self.row = int(name[-2:])
            self.data = ""
            self.axial_to_cube()

        def axial_to_cube(self):
            self.x = self.col
            self.z = int(self.row - (self.col - (self.col % 2))/2)
            self.y = -(self.x)-(self.z)            
        
        def distance(self, ref):
            return max(abs(self.x - ref.x), abs(self.y-ref.y), abs(self.z-ref.z))

        def dist_from(self,location):
            column = int(location[:2])
            row = int(location[-2:])

            x = column 
            z = row - int((column - (column%2))/2)
            y = -x-z

            return max(abs(self.x - x), abs(self.y-y), abs(self.z-z))

