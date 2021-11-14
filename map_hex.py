class Map_Hex(): 
    #Derived from https://www.redblobgames.com/grids/hexagons/

        def __init__(self, name): 
            self.name = name
            self.q = 0
            self.r = 0
            self.s = 0
            self.col = int(name[:2])
            self.row = int(name[-2:])
            self.data = ""
            self.axial_to_cube()

        def axial_to_cube(self):
            self.q = self.col
            self.r = int(self.row - (self.col - (self.col % 2))/2)
            self.s = -(self.q)-(self.r)            
        
        def distance(self, ref):
            return max(abs(self.q - ref.q), abs(self.r-ref.r), abs(self.s-ref.s))

        def dist_from(self,location):
            column = int(location[:2])
            row = int(location[-2:])

            q = column 
            r = row - int((column - (column%2))/2)
            s = -q-r

            return max(abs(self.q - q), abs(self.r-r), abs(self.s-s))

