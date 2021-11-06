import random
import traveller_utilities as t_util
import map_hex as m

board = t_util.create_sector()
sectorfile = open("New Test Sector.txt", 'w')
sectorfile.write(t_util.board_printout(board))
sectorfile.close()

sectorfile = open("New Test Sector.txt", 'r')
sector = sectorfile.read()
planets = sector.split("\n")



a_ports= []
b_ports = []
c_ports = []
d_ports = []
e_ports = []
populated = []

connections = []

def traderoute_printer(data):
    result = "<?xml version=\"1.0\"?>\n<Sector>\n<Routes>\n"
    
    for x in data:
        #print(x[0])
        result += ("\t<Route Start = \"{}\" End=\"{}\"/>\n").format(x[0], x[1])
    
    result += "\n</Routes>\n</Sector>"
    return result

def single_throw():
    return random.randint(1,6)

for i in planets:
    if i:
        entry = i.split("\t")
        if (entry[0] != "Hex"):
            location = str(entry[0])
            starport = str(entry[2][0])
            #print(("Location: {}, Starport: {}").format(location, starport))
            newHex = m.Map_Hex(location)
            newHex.data = i
            #print (("Converted hex: {}").format(newHex.name))
            populated.append(newHex)

            if (starport == "A"):
                a_ports.append(newHex)
            elif (starport == "B"):
                b_ports.append(newHex)
            elif (starport =="C"):
                c_ports.append(newHex)
            elif (starport == "D"):
                d_ports.append(newHex)
            elif (starport == "E"):
                e_ports.append(newHex)
                

sectorfile.close()

print("Evaluating A Ports.")
for x in a_ports:
    for y in populated:
        roll = single_throw()
        entry = y.data.split("\t")
        near_starport = str(entry[2][0])
        dist = x.distance(y)
        #print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))

        if dist == 1:
            if near_starport == "A" or near_starport == "B" or near_starport == "C" or near_starport == "D":
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "E"):
                if(roll >= 2):
                    print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                    #x.connections.append([y.name,dist])
                    connections.append([x.name,y.name,dist])
                    print(("Adding {} to {} Connections").format(y.name, x.name))
        elif  dist == 2:
            if (near_starport == "A") and (roll >= 2):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "B") and (roll >= 3):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "C") and (roll >= 4):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "D") and (roll >= 5):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
        elif dist == 3:
            if (near_starport == "A") or (near_starport == "B"):
                if (roll >= 4):
                    print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                    #x.connections.append([y.name,dist])
                    connections.append([x.name,y.name,dist])
                    print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "C") and (roll >= 6):
                    print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                    #x.connections.append([y.name,dist])
                    connections.append([x.name,y.name,dist])
                    print(("Adding {} to {} Connections").format(y.name, x.name))
        elif dist == 4:
            if (near_starport == "A") or (near_starport == "B"):
                if (roll >= 5):
                    print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                    #x.connections.append([y.name,dist])
                    connections.append([x.name,y.name,dist])
                    print(("Adding {} to {} Connections").format(y.name, x.name))
    
    #Evaluate all Class B Starports

print("Evaluating B Ports.")
for x in b_ports:
    for y in populated:
        roll = single_throw()
        entry = y.data.split("\t")
        near_starport = str(entry[2][0])
        dist = x.distance(y)
        #print(("Evaluating {}").format(x.name))
        #print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))

        if (dist == 1):
            if(near_starport == "B"):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "C") and (roll >= 2):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "D") and (roll >= 3):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "E") and (roll >= 4):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
        elif (dist == 2):
            if (near_starport == "B") and (roll >= 3):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "C") and (roll >= 4):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "D") and (roll >= 6):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
        elif (dist == 3):
            if (near_starport == "B") and (roll >= 4):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "C") and (roll >= 6):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
        elif (dist == 4):
            if (near_starport == "B") and (roll >= 6):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))

#Evaluate all Class C Starports
print("Evaluating C Ports.")
for x in c_ports:
    for y in populated:
        roll = single_throw()
        entry = y.data.split("\t")
        near_starport = str(entry[2][0])
        dist = x.distance(y)
        #print(("Evaluating {}").format(x.name))
        #print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))

        if (dist == 1):
            if(near_starport == "C") and (roll >= 3):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "D") or (near_starport == "E"): 
                if(roll >= 4):
                    print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                    #x.connections.append([y.name,dist])
                    connections.append([x.name,y.name,dist])
                    print(("Adding {} to {} Connections").format(y.name, x.name))
        if (dist == 2):
            if (near_starport == "C") and (roll >= 6):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))

#Evaluate all Class D Starports
print("Evaluating D Ports.")
for x in d_ports:
    for y in populated:
        roll = single_throw()
        entry = y.data.split("\t")
        near_starport = str(entry[2][0])
        dist = x.distance(y)
        #print(("Evaluating {}").format(x.name))
        #print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))

        if (dist == 1):
            if(near_starport == "D") and (roll >= 4):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))
            elif (near_starport == "E") and (roll >= 5):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))

#Evaluate all Class E Starports
print("Evaluating E Ports.")
for x in e_ports:
    for y in populated:
        roll = single_throw()
        entry = y.data.split("\t")
        near_starport = str(entry[2][0])
        dist = x.distance(y)
        #print(("Evaluating {}").format(x.name))
        #print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))

        if (dist == 1):
            if(near_starport == "E") and (roll >= 6):
                print(("Evaluating {} against {}: Distance {}, Near Starport {}, Roll Of {}").format(x.name, y.name, dist, near_starport, roll))
                #x.connections.append([y.name,dist])
                connections.append([x.name,y.name,dist])
                print(("Adding {} to {} Connections").format(y.name, x.name))


#board = []

#Create a first draft of connections

print(("Connections: {} Entries").format(len(connections)))

print("Removing redundant entries.")

for x in connections:
    for y in connections:
        if(x[0]==y[1]) and (x[1]==y[0]):
            connections.remove(y)

print(("Connections: {} Entries").format(len(connections)))

print("Removing duplicate paths")
for x in connections:
    for y in connections:
        for z in connections:
            if(x[1]==y[0]) and (y[1] == z[1]) and (z[0]==x[0]):
                print(("Comparing {},{},{}").format(x,y,z))
                if(y[2] > z[2]):
                    print(("Removing {}").format(y))
                    connections.remove(y)
                else:
                    print(("Removing {}").format(z))
                    connections.remove(z)

print(("Connections: {} Entries").format(len(connections)))

tradefile = open("New Trade Routes.txt", "w")
tradefile.write(list_printer(connections))
tradefile.close()
