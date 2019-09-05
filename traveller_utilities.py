import random
import traveller_charts as t_charts

def __init__():
    self.Charts = Traveller_Charts()

def throw():
    return single_throw() + single_throw()

def single_throw():
    return random.randint(1,6)

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

def uwp_gen(base, size, atmo, hydro, pop, govt, law, tech, content):
    start_list = [size, atmo, hydro, pop, govt, law, tech]
    uwp_list = []
    
    for x in start_list:
        uwp_list.append(t_charts.hex_translate(x))
    
    uwp_list.insert(0, base)
    uwp_list.insert((len(uwp_list)-1),"-")
    uwp = "".join(uwp_list)
    tradecodes = tradecode_generate(uwp)
    uwp = uwp + "\t"
    for x in tradecodes:
        uwp = uwp + " " + x
    
    sysdetail = ""

    if (content[1:])[0] == "Y":
        sysdetail += "N"
    if (content[1:])[1] == "Y":
        sysdetail += "S"
    if (content[1:])[2] == "Y":
        sysdetail += "G"

    uwp = uwp + "\t" + sysdetail

    return uwp 

def print_description(uwp):
    content = (((uwp.split('\t'))[2]).split(" "))[0]
    
    description = ""

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
        if "N" in content: 
            description +=("\nNaval Base? Y")
        else:
            description +=("\nNaval Base? N")
        
        if "S" in content:
            description +=("\nScout Base? Y")
        else:
            description +=("\nScout Base? Y")
        
        if "G" in content:
            description +=("\nGas Giant? Y\n\n")
        else:
            description +=("\nGas Giant? N\n\n")
    else:
        description +=("\nNaval Base? N")
        description +=("\nScout Base? N")
        description +=("\nGas Giant? N\n\n")

    return description

def tradecode_generate(uwp):
    #UWP
    size = t_charts.int_translate(uwp[1])
    atmo = t_charts.int_translate(uwp[2])
    hydro = t_charts.int_translate(uwp[3])
    pop = t_charts.int_translate(uwp[4])
    gov = t_charts.int_translate(uwp[5])
    law = t_charts.int_translate(uwp[6])

    
    tc_list = []
    
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
    
    return tc_list

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
        "Ic":"Ice Capped"
    }
    tradecodes = ((uwp.split('\t'))[1]).split(" ")
    tradecodes.pop(0)
    if tradecodes:
        for x in tradecodes:
            result = result + " " + trade_chart.get(x) + " "
    else:
        result = "None"

    return result

def create_system():    
    #System Content
    #[0] = Starbase
    #[1] = Naval Base
    #[2] = Scout Base
    #[3] = Gas Giant
    pcontent = systemcontent()

    #Planet Size
    psize = throw()-2
    #Atmosphere
    patmo = (throw()-7) + psize

    if patmo >= 12:
        patmo = 12
    elif patmo <= 0:
        patmo = 0

    #Hydrographic
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

    ptech = techlevel(pcontent[0], psize, patmo, phydro, ppop, pgov)
    uwp = uwp_gen(pcontent[0], psize, patmo, phydro, ppop, pgov, plaw, ptech, pcontent)
    print(print_description(uwp))

    return uwp
