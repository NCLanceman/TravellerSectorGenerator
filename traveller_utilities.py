import random
import map_hex as m
import traveller_charts as t_charts

def single_throw():
    return random.randint(1,6)

def throw():
    return single_throw() + single_throw()

def half_throw():
    return random.randint(1,3)

def jump_sector_hex(radius):
    #origin = [radius+1, radius+1]
    edge = (radius*2)+1

    board = []
    count = 0
    for i in range(1,edge+1):
        for j in range(1, edge+1):
            hexlocation = (str(i)).zfill(2) + (str(j)).zfill(2)
            board.append(m.Map_Hex(hexlocation))
            count = count + 1
    
    return board

def subsector_hex():
    board =[]
    count = 0

    for x in range(1,9):
        for y in range (1,11):
            hexlocation = (str(x)).zfill(2) + (str(y)).zfill(2)
            board.append(m.Map_Hex(hexlocation))
            count = count + 1
    
    return board



def systemcontent():
    syscontent = {
        2: "ANNY",
        3: "ANNY",
        4: "ANNY",
        5: "BNNY",
        6: "BNNY",
        7: "CNYY",
        8: "CYYY",
        9: "DYYY",
        10: "EYYN",
        11: "EYYN",
        12: "XYYN"
    }
    #Starbase Roll
    roll1 = throw()
    #Naval Base Roll
    roll2 = throw()
    #Scout Base Roll
    roll3 = throw()
    #Gas Giant Roll
    roll4 = throw()

    starport = (syscontent.get(roll1))[0]
        
    if starport == "A" or starport == "B":
        navalbase = (syscontent.get(roll2))[1]
    else: 
        navalbase = "N"
    
    if starport == "A":
        scoutbase = (syscontent.get(roll3-3,"ANNY"))[2]
    elif starport == "B":
        scoutbase = (syscontent.get(roll3-2, "ANNY"))[2]
    elif starport == "C":
        scoutbase = (syscontent.get(roll3-1, "ANNY"))[2]
    else: 
        scoutbase = "N"

    gasgiant = (syscontent.get(roll4))[3]
    
    result = starport + navalbase + scoutbase + gasgiant

    return result

def techlevel(port, size, atm, hyd, pop, govt):
    dieMod = 0

    if port == "A":
        dieMod = dieMod + 6
    elif port == "B":
        dieMod = dieMod + 4
    elif port == "C":
        dieMod = dieMod + 2
    elif port == "X":
        dieMod = dieMod - 4

    if size <= 1:
        dieMod = dieMod + 2
    elif size > 1 and size <= 4: 
        dieMod = dieMod + 1
    
    if atm <= 3 or atm >= 10:
        dieMod = dieMod + 1
    
    if hyd == 9:
        dieMod = dieMod + 1
    elif hyd == 10:
        dieMod = dieMod + 2
    
    if pop > 0 and pop <= 5:
        dieMod = dieMod + 1
    elif pop == 9:
        dieMod = dieMod + 2
    elif pop == 10:
        dieMod = dieMod + 4

    if govt == 0 or govt == 5:
        dieMod = dieMod + 1
    elif govt == 13: 
        dieMod = dieMod - 1

    return single_throw() + dieMod

#A full Traveller UWP:
#Location: XXYY
#Name: String
#UWP: 
#Bases: NS
#Remarks: Trade Codes
#PBG: Population Multiplier, Belts, Gas Giants
#Allegince: Two-Character code
#Stars: Stellar Classification, Space Seprated
def uwp_gen(base, size, atmo, hydro, pop, govt, law, tech, content, remarks):
    start_list = [size, atmo, hydro, pop, govt, law, tech]
    uwp_list = []
    
    if remarks == "Unknown":
        uwp = "???????-?"
    else: 
        for x in start_list:
            uwp_list.append(t_charts.hex_translate(x))
        
        uwp_list.insert(0, base)
        uwp_list.insert((len(uwp_list)-1),"-")
        uwp = "".join(uwp_list)

    if remarks == "Capital":
        tradecodes = tradecode_generate(uwp, True)
    elif remarks == "Known":
        tradecodes = tradecode_generate(uwp, False)
    elif remarks == "Unknown":
        tradecodes = ""
        content = "\t"*7 + "???" +"\t"*3 

    uwp = uwp + "\t" + tradecodes + content
    
    sysdetail = ""

    #if (content[1:])[0] == "Y" and remarks != "Unknown":
    #    sysdetail += "N"
    #if (content[1:])[1] == "Y" and remarks != "Unknown":
    #    sysdetail += "S"
    #if (content[1:])[2] == "Y" and remarks != "Unknown":
    #    sysdetail += "G"

    #uwp = uwp + "\t" + sysdetail

    return uwp 

def print_description(data):
    content = data.split('\t')
    print(content)
    uwp = ""

    if(data[0] not in ["A","B","C","D","E","X","?"]):
        #print("Adjusting Entry...")
        uwp = "\t".join(content[2:])
        content = content[2:]
        #print(("UWP: {}").format(uwp))
        #print(("Content: {}").format(content))

    description = ""
    if uwp[0] == "?":
        description = "An Unexplored System is here."
    else:
        description += ("WORLD DETAILS: " + uwp)
        description +=("\nTrade Codes: " + tradecode_translate(uwp))
        description +=("\nStarbase: " + t_charts.uwp1_translate(uwp[0]))
        description +=("\nSize: " + t_charts.uwp2_translate(uwp[1]))
        description +=("\nAtmosphere: " + t_charts.uwp3_translate(uwp[2]))
        description +=("\nHydrographic: " + t_charts.uwp4_translate(uwp[3]))
        description +=("\nPopulation: " + t_charts.uwp5_translate(uwp[4]))
        description +=("\nGovernment: " + t_charts.uwp6_translate(uwp[5]))
        description +=("\nLaw Level: " + t_charts.uwp7_translate(uwp[6]))
        description +=("\nTech Level: " + t_charts.uwp8_translate(uwp[8]))

        if content:
            if (content[6] == "N"):
                description +=("\nNaval Base? Y")
                description +=("\nScout Base? N")
            elif (content[6] == "S"):
                description +=("\nNaval Base? N")
                description +=("\nScout Base? S")
            elif (content[6]== "NS"):
                description +=("\nNaval Base? Y")
                description +=("\nScout Base? Y")
            elif (content[6]==""):
                description +=("\nNaval Base? N")
                description +=("\nScout Base? N")
            
            if (int(content[8][2]) > 0):
                description +=("\nGas Giant? Y\n\n")
            else:
                description +=("\nGas Giant? N\n\n")
        else:
            description +=("\nNaval Base? N")
            description +=("\nScout Base? N")
            description +=("\nGas Giant? N\n\n")

    return description

def tradecode_generate(uwp, cap):
    #UWP
    size = t_charts.int_translate(uwp[1])
    atmo = t_charts.int_translate(uwp[2])
    hydro = t_charts.int_translate(uwp[3])
    pop = t_charts.int_translate(uwp[4])
    gov = t_charts.int_translate(uwp[5])
    law = t_charts.int_translate(uwp[6])

    
    tc_list = []
    remarks = ""
    
    #Agricultural (Ag)
    if atmo in [4,5,6,7,8,9] and hydro in [4,5,6,7,8] and pop in [5,6,7]:
        tc_list.append("Ag")
    
    #Non-Agricultural (Na)
    if atmo <= 3 and hydro <= 3 and pop >= 6:
        tc_list.append("Na")
    
    #Industrial (In)
    if atmo in [0,1,2,4,7,9] and pop >= 9:
        tc_list.append("In")
    
    #Non-Industrual(Ni)
    if pop <= 6:
        tc_list.append("Ni")
    
    #Rich (Ri)
    if atmo in [6, 7, 8] and pop in [6, 7, 8] and gov >=4 and gov <= 9:
        tc_list.append("Ri")
    
    #Poor (Po)
    if atmo in [2,3,4,5] and hydro <= 3:
        tc_list.append("Po")
    
    #Water World (Wa)
    if hydro == 10:
        tc_list.append("Wa")

    #Desert World (De)
    if hydro == 0 and atmo > 2:
        tc_list.append("De")
    
    #Vacuum World (Va)
    if atmo == 0:
        tc_list.append("Va")
    
    #Asteroid Belt (As)
    if size == 0:
        tc_list.append("As")
    
    #Ice-Capped (Ic)
    if atmo <= 1 and hydro > 1:
        tc_list.append("Ic")

    #Capital (Ca)
    if cap == True:
        tc_list.append("Ca")
    
    for x in tc_list:
        remarks += x + " "

    return remarks

def tradecode_translate(uwp):
    result = " "
    trade_chart = {
        "Ag":"Agricultural",
        "Na":"Non-Agricultural",
        "In":"Industrial",
        "Ni":"Non-Industrial",
        "Ri":"Rich",
        "Po":"Poor",
        "Wa":"Water World",
        "De":"Desert World",
        "Va":"Vaccum World",
        "As":"Asteroid Belt",
        "Ic":"Ice Capped",
        "Ca": "Capital"
    }
    tradecodes = ((uwp.split('\t'))[1]).split(" ")

    if tradecodes:
        for x in tradecodes:
            if x:
                result += " " + trade_chart.get(x) + " "
    else:
        result = "None"

    return result

def create_system(remarks):    
    #System Content
    #[0] = Starbase
    #[1] = Naval Base
    #[2] = Scout Base
    #[3] = Gas Giant
    pcontent = systemcontent()

    content = "\t"*5

    #Planet Size
    psize = throw()-2
    #Atmosphere
    if(psize == 0):
        patmo = 0
    else:
        if (psize > 0):
            patmo = (throw()-7) + psize
        elif (psize == 0): 
            patmo = 0

        if patmo >= 12:
            patmo = 12
        elif patmo <= 0:
            patmo = 0

    #Hydrographic
    if (psize == 0) or (psize==1):
        phydro = 0
    else:
        if patmo <= 1 or patmo > 9:
            phydro = (throw()-7) + patmo - 4
        else: 
            phydro = (throw()-7) + patmo

        if phydro >= 10:
            phydro = 10
        elif phydro <= 0:
            phydro = 0
    

    #Population
    ppop = (throw()-2)
    #Government
    pgov = (throw()-7) + ppop

    if pgov >= 13:
        pgov = 13
    elif pgov <= 0:
        pgov = 0

    #Law Level
    plaw = (throw()-7) + pgov

    if plaw >= 10:
        plaw = 10
    elif plaw <= 0:
        plaw = 0   
    
    if (pcontent[1] == "Y"):
        content += "N"
    
    if(pcontent[2]== "Y"):
        content += "S" + "\t"*2
    elif(pcontent[2]=="N"):
        content += "\t"*2
    
    content += str(single_throw()) * 2

    if(pcontent[3]== "Y"):
        content += (str(half_throw())) +"\t"*3
    elif(pcontent[3]=="N"):
        content += ("0") + "\t"*3   


    ptech = techlevel(pcontent[0], psize, patmo, phydro, ppop, pgov)
    uwp = uwp_gen(pcontent[0], psize, patmo, phydro, ppop, pgov, plaw, ptech, content, remarks)
    
    #print(print_description(uwp))

    return uwp
    
def create_j_sector(board, known, origin):
    for x in board:
        roll = single_throw()
        location = x.name
        if x.dist_from(origin) == 0 and x.dist_from(origin) <= known:
            current_sys = create_system("Capital")
            while current_sys[0] != "A":
                current_sys = create_system("Capital")
            fulluwp = x.name + "\tCapital\t" + current_sys
            x.data = fulluwp
        elif x.dist_from(origin) <= known:
            if roll >= 4:
                current_sys = create_system("Known")
                fulluwp = x.name +"\tKnown\t"+ current_sys
                x.data = fulluwp
        elif x.dist_from(origin) > known:
            if roll >= 4:
                current_sys = create_system("Unknown")
                fulluwp = x.name +"\tBlank\t"+ current_sys
                x.data = fulluwp
    return board

def create_sector():
    board = subsector_hex()
    for location in board:
        roll = single_throw()

        if roll >= 4:
            current_sys = create_system("Known")
            fulluwp = location.name +"\tKnown\t"+ current_sys 
            location.data = fulluwp
            print("Hit! " + current_sys)         
    
    #traderoute_evaluate(board)

    return board

def board_printer(board):
    result = ("Hex\tName\tUWP\tRemarks\t{Ix}\t(Ex)\t[Cx]\tN\tB\tZ\tPBG\tW\tA\tStellar\n")

    for x in board:
        if x.data:
            result += x.data + "\n"
    return result



    
