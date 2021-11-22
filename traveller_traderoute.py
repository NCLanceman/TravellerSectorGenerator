import random
import map_hex as m


def generateTradeRoutes(UPPData, bias):
    tradeRoutes = []

    sectorfile = open(UPPData, 'r')
    sector = sectorfile.read()
    planets = sector.split("\n")

    populated = generateBoard(planets)
    sectorfile.close()

    #Use Populated to create a list of all possible Connections
    connections = generateConnections(populated)
    tradeRoutes = trade_bias(connections,bias)
    tradeRoutes = verifyConnections(tradeRoutes)
    
    return traderoute_printer(tradeRoutes)

def generateBoard(planets):
    board = []

    for i in planets:
        if i:
            entry = i.split("\t")
            if (entry[0] != "Hex") and (entry[0][0:6] != "Origin") and (entry[1] != "Blank"):
                location = str(entry[0])
                newHex = m.Map_Hex(location)
                newHex.data = i
                board.append(newHex)
    
    return board

def generateConnections(data):

    connections = []

    for x in data:
        for y in data:
            x_data = x.data.split("\t")
            y_data = y.data.split("\t")
            distance = x.distance(y)

            if ((distance <= 4) and (distance > 0)):
                if((x_data[2][0] != "X") and (y_data[2][0] != "X")):
                    #determine dominant starport
                    dom_starport = min(x_data[2][0], y_data[2][0])
                    sec_starport = max(x_data[2][0], y_data[2][0])
                    #record entry as [x_location, y_location, dom_port, sec_port, distance]
                    connections.append([x.name, y.name, dom_starport, sec_starport, distance])


    print(("Connections: {} Entries").format(len(connections)))

    print("Removing redundant entries.")

    for x in connections:
        for y in connections:
            if(x[0]==y[1]) and (x[1]==y[0]):
                connections.remove(y)

    print(("Connections: {} Entries").format(len(connections)))

    return connections

def verifyConnections(data):
    verified = []
    
    for x in data:
        if(Connection_Eval(x) == True):
            verified.append(x)

    print(("Verified Connections: {} Entries").format(len(verified)))

    print("Removing duplicate paths")
    for x in verified:
        for y in verified:
            for z in verified:
                if(x[1]==y[0]) and (y[1] == z[1]) and (z[0]==x[0]):
                    #print(("Comparing {},{},{}").format(x,y,z))
                    if(y[2] > z[2]):
                        print(("Removing {}").format(y))
                        verified.remove(y)
                    else:
                        print(("Removing {}").format(z))
                        verified.remove(z)

    print(("Verified Connections: {} Entries").format(len(verified)))

    return verified

def single_throw():
    return random.randint(1,6)

def d100_throw():
    return random.randint(1,100)

def A_Port_Eval(candidate):
    roll = single_throw()
    dist = candidate[4]
    near_starport = candidate[3]

    if dist == 1:
        if near_starport == "A" or near_starport == "B" or near_starport == "C" or near_starport == "D":
            print(("A Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "E"):
            if(roll >= 2):
                print(("A Port Connection: {}").format(candidate))
                return True
            else:
                return False
    elif  dist == 2:
        if (near_starport == "A") and (roll >= 2):
            print(("A Port Connection: {}").format(candidate))            
            return True
        elif (near_starport == "B") and (roll >= 3):
            print(("A Port Connection: {}").format(candidate))            
            return True
        elif (near_starport == "C") and (roll >= 4):
            print(("A Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "D") and (roll >= 5):
            print(("A Port Connection: {}").format(candidate))
            return True
        else:
            return False
    elif dist == 3:
        if (near_starport == "A") or (near_starport == "B"):
            if (roll >= 4):
                print(("A Port Connection: {}").format(candidate))
                return True
        elif (near_starport == "C") and (roll >= 6):
                print(("A Port Connection: {}").format(candidate))
                return True
        else:
            return False
    elif dist == 4:
        if (near_starport == "A") or (near_starport == "B"):
            if (roll >= 5):
                print(("A Port Connection: {}").format(candidate))
                return True
            else:
                return False
    else:
        return False

def B_Port_Eval(candidate):
    roll = single_throw()
    dist = candidate[4]
    near_starport = candidate[3]

    if (dist == 1):
        if(near_starport == "B"):
            print(("B Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "C") and (roll >= 2):
            print(("B Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "D") and (roll >= 3):
            print(("B Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "E") and (roll >= 4):
            print(("B Port Connection: {}").format(candidate))
            return True
        else:
            return False
    elif (dist == 2):
        if (near_starport == "B") and (roll >= 3):
            print(("B Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "C") and (roll >= 4):
            print(("B Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "D") and (roll >= 6):
            print(("B Port Connection: {}").format(candidate))
            return True
        else:
            return False
    elif (dist == 3):
        if (near_starport == "B") and (roll >= 4):
            print(("B Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "C") and (roll >= 6):
            print(("B Port Connection: {}").format(candidate))
            return True
        else:
            return False
    elif (dist == 4):
        if (near_starport == "B") and (roll >= 6):
            print(("B Port Connection: {}").format(candidate))
            return True
        else:
            return False
    else:
        return False

def C_Port_Eval(candidate):
    roll = single_throw()
    dist = candidate[4]
    near_starport = candidate[3]

    if (dist == 1):
        if(near_starport == "C") and (roll >= 3):
            print(("C Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "D") or (near_starport == "E"): 
            if(roll >= 4):
                print(("C Port Connection: {}").format(candidate))
                return True
            else:
                return False
        else:
            return False
    if (dist == 2):
        if (near_starport == "C") and (roll >= 6):
            print(("C Port Connection: {}").format(candidate))
            return True
        else:
            return False
    else:
        return False

def D_Port_Eval(candidate):
    roll = single_throw()
    dist = candidate[4]
    near_starport = candidate[3]

    if (dist == 1):
        if(near_starport == "D") and (roll >= 4):
            print(("D Port Connection: {}").format(candidate))
            return True
        elif (near_starport == "E") and (roll >= 5):
            print(("D Port Connection: {}").format(candidate))
            return True
        else:
            return False
    else:
        return False

def E_Port_Eval(candidate):
    roll = single_throw()
    dist = candidate[4]
    near_starport = candidate[3]
    
    if (dist == 1):
        if(near_starport == "E") and (roll >= 6):
            print(("E Port Connection: {}").format(candidate))
            return True
        else:
            return False
    else:
        return False

def Connection_Eval(candidate):
    dom_starport = candidate[2]
    if (dom_starport == "A"):
        return (A_Port_Eval(candidate))
    elif(dom_starport == "B"):
        return (B_Port_Eval(candidate))
    elif(dom_starport == "C"): 
        return (C_Port_Eval(candidate))
    elif(dom_starport == "D"):
        return (D_Port_Eval(candidate))
    elif(dom_starport == "E"):
        return (E_Port_Eval(candidate))

def traderoute_printer(connections):
    result = "<?xml version=\"1.0\"?>\n<Sector>\n<Routes>\n"
    
    for x in connections:
        result += ("\t<Route Start = \"{}\" End=\"{}\"/>\n").format(x[0], x[1])
    
    result += "\n</Routes>\n</Sector>"
    return result

def trade_bias(data, percentage):
    #Calculate Expected Number of Removals:
    projectedRemovals = int(len(data) * (percentage / 100))
    actualRemovals = 0

    print("Applying Bias...")    
    while(actualRemovals < projectedRemovals):
        data.pop(random.randrange(len(data)))
        actualRemovals = actualRemovals + 1
        
    print(("Removals Expected: {}, Actual Removals: {}").format(projectedRemovals, actualRemovals))
    print(("Connections after Bias: {} Entries").format(len(data)))

    return data