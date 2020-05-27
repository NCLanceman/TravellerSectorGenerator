import traveller_utilities as t_util
import map_hex

sectorfile = open("New Standard Sector.txt", "r")
sector = sectorfile.read()
planets = sector.split("\n")

for i in planets:
    entry = i.split("\t")
    if (entry[0] != "Hex"):
        location = str(entry[0])
        starport = str(entry[2][0])
        print(("Location: {}, Starport: {}").format(location, starport))

sectorfile.close()
