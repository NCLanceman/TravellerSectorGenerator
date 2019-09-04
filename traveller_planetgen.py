import random

#Starter Traveller Planet Generation

def throw():
    return single_throw() + single_throw()

def single_throw():
    return random.randint(1,6)

def hex_translate(num):
    if num <= -1:
        return "0"
    else:
        hex_chart= {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F",
            16: "G"
        }
        return hex_chart.get(num, "Invalid Num")

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

def uwp_gen(base, size, atmo, hydro, pop, govt, law, tech, tradecodes):
    start_list = [size, atmo, hydro, pop, govt, law, tech]
    uwp_list = []
    
    for x in start_list:
        uwp_list.append(hex_translate(x))
    
    uwp_list.insert(0, base)
    uwp_list.insert((len(uwp_list)-1),"-")
    uwp = "".join(uwp_list)
    uwp = uwp + "\t"
    for x in tradecodes:
        uwp = uwp + " " + x

    return uwp 

def uwp1_translate(base):
    starport = {
        "A": "Excellent quality installation. \nRefined Fuel Available. " +
        "Annual maintainence overhaul available. Shipyard capable of constructing starships and " +
        "non-starships present.",
        "B": "Good quality installation. \nRefined fuel available. Annual maintainence overhaul available." +
        "Shipyard capable of constructing non-starships present.",
        "C": "Routine quality installation. \nOnly unrefined fuel available. Reasonable repair facilities present.",
        "D": "Poor quality installaition. \nOnly unrefined fuel available. No repair or shipyard facilities present.",
        "E": "Frontier installation. \nEssentially a marked spot of bedrock with no fuel, facilities, or bases present.",
        "X": "No starport. \nNo provision is made for any ship landings."
    }
    return starport.get(base)

def uwp2_translate(size):
    size_chart = {
        "0": "Asteroid/Planetoid Belt",
        "1": "1,000 miles (1,600 km)",
        "2": "2,000 miles (3,200 km)",
        "3": "3,000 miles (4,800 km)",
        "4": "4,000 miles (6,400 km)",
        "5": "5,000 miles (8,000 km)",
        "6": "6,000 miles (9,600 km)",
        "7": "7,000 miles (11,200 km)",
        "8": "8,000 miles (12,800 km)",
        "9": "9,000 miles (14,400 km)",
        "A": "10,000 miles (16,000 km)"
    }
    return size_chart.get(size)

def uwp3_translate(atmo):
    atmo_chart = {
        "0": "No Atmosphere",
        "1": "Trace",
        "2": "Very thin, tainted",
        "3": "Very thin",
        "4": "Thin, tainted",
        "5": "Thin",
        "6": "Standard",
        "7": "Standard, tainted",
        "8": "Dense",
        "9": "Dense, tainted",
        "A": "Exotic",
        "B": "Corrosive",
        "C": "Insidious"
    }
    return atmo_chart.get(atmo)

def uwp4_translate(hydro):
    hydro_chart = {
        "0": "No free standing water",
        "1": "10% water",
        "2": "20% water",
        "3": "30% water",
        "4": "40% water",
        "5": "50% water",
        "6": "60% water",
        "7": "70% water",
        "8": "80% water",
        "9": "90% water",
        "A": "No landmasses"
    }
    return hydro_chart.get(hydro)

def uwp5_translate(population):
    pop_chart = {
        "0": "No inhabitants",
        "1": "Tens of inhabitants",
        "2": "Hundreds of inhabitants",
        "3": "Thousands of inhabitants",
        "4": "Ten of Thousands of inhabitants",
        "5": "Hundreds of Thousands of inhabitants",
        "6": "Millions of inhabitants",
        "7": "Tens of Millions of inhabitants",
        "8": "Hundreds of Millions of inhabitants",
        "9": "Billions of inhabitants",
        "A": "Tens of Billions of inhabitants"
    }
    return pop_chart.get(population)

def uwp6_translate(govnt):
    gov_chart = {
        "0": "No government structure." +
        "\nIn many cases, family bonds predominate.",
        "1": "Company/Corporation. \nGovernment by company managerial elite;" + 
        " citizens are company employees.",
        "2": "Participating Democracy." + 
        "\nGovernment by advice and concent of the citizen.",
        "3": "Self-Perpetuating Oligarchy." + 
        "\nGovernment by a restricted minority, with little or no input from the masses.",
        "4": "Representative Democracy." +
        "\nGovernment by elected representatives.",
        "5": "Feudal Technocracy." + 
        "\nGovernment by specific individuals for those who agree to be ruled. Relationships are based\n" 
        + "on the performance of techincal activities which are mutually beneficial.",
        "6": "Captive Government."+ 
        "\nGovernment by leadership answerable to an outside group; a colony or conquered area.",
        "7": "Balkanization." +
        "\nNo central ruling authority exists; rival governments compete for control.",
        "8": "Civil Service Bureaucracy." + 
        "\nGovernment by agencies employing individuals selected for their expertise.",
        "9": "Impersonal Bureaucracy." + 
        "\nGovernment by agencies which are insulated from the governed.",
        "A": "Charismatic Dictator." +
        "\nGovernment by a single leader enjoying the confidence of the citizens.",
        "B": "Non-charismatic Dictator."+
        "\nA previous charismatic dictator has been replaced by a leader through normal channels.",
        "C": "Charismatic Oligarchy"+
        "\nGovernment by a select group, orginzation, or class enjoying the overwhelming "+ 
        "\nconfidence of the citizenry.",
        "D": "Religious Dictatorship"+
        "\nGovernment by a religious organization without regard to the needs of the citizenry."
    }
    return gov_chart.get(govnt)

def uwp7_translate(law):
    law_chart = {
        "0": "No prohibitions",
        "1": "Body pistols undedectable by standard scanners, explosives (bombs, grenades)"+
        "\nand poison gas prohibited.",
        "2": "Portable energy weapons (laser carbine, laser rifle) prohibited. Ships gunnery not affected.",
        "3": "Weapons of a strict military nature (machine guns, automatic rifles) prohibited.",
        "4": "Light assault weapons (submachine guns) prohibited.",
        "5": "Personal concealable firearms (pistols and revolvers) prohibited.",
        "6": "Most firearms (except shotguns) prohibited. The carrying of any type of"+
         "\nweapon openly is discouraged.",
        "7": "Shotguns are prohibited.",
        "8": "Long bladed weapons (all but daggers) are controlled, and open possesion is prohibited.",
        "9": "Possession of any weapon outside one's residence is prohibited.",
        "A": "Possession of any weapon is prohibited."
    }
    return law_chart.get(law)

def uwp8_translate(tech):
    tech_chart = {
        "0": "Stone Age. Primitive",
        "1": "Bronze Age to Middle Ages",
        "2": "circa 1400 to 1700",
        "3": "circa 1700 to 1860",
        "4": "circa 1860 to 1900",
        "5": "circa 1900 to 1939",
        "6": "circa 1940 to 1969",
        "7": "circa 1970 to 1979",
        "8": "circa 1980 to 1989",
        "9": "circa 1990 to 2000",
        "A": "Interstellar community",
        "B": "Average Imperial",
        "C": "Average Imperial",
        "D": "Above Average Imperial",
        "E": "Above Average Imperial",
        "F": "Technical Maximum Imperial",
        "G": "Occasional non-Imperial"
    }
    return tech_chart.get(tech)

def print_description(uwp, content, tradecodes): 
    print("WORLD DETAILS: " + uwp)
    print("Trade Codes: " + tradecode_translate(tradecodes))
    print("Starbase: " + uwp[0] + ". "+ uwp1_translate(uwp[0]))
    print("Size: " + uwp[1]+ ". "+ uwp2_translate(uwp[1]))
    print("Atmosphere: " + uwp[2]+ ". " + uwp3_translate(uwp[2]))
    print("Hydrographic: " + uwp[3] + ". " + uwp4_translate(uwp[3]))
    print("Population: " + uwp[4] + ". " + uwp5_translate(uwp[4]))
    print("Government: " + uwp[5] + ". " + uwp6_translate(uwp[5]))
    print("Law Level: " + uwp[6] + ". "+ uwp7_translate(uwp[6]))
    print("Tech Level: " + uwp[8] + ". "+ uwp8_translate(uwp[8]))
    print("Naval Base? " + content[1])
    print("Scout Base? " + content[2])
    print("Gas Giant? " + content[3] + "\n\n")

def tradecode_generate(size, atmo, hydro, pop, gov, law):
    tc_list = []
    
    #Agricultural (Ag)
    if atmo >= 4 and atmo <= 9 and hydro <=4 and hydro >=8 and pop >=5 and pop <=7:
        tc_list.append("Ag")
    
    #Non-Agricultural (Na)
    if atmo < 3 and hydro < 3 and pop > 6:
        tc_list.append("Na")
    
    #Industrial (In)
    if atmo in (0,1,2,4,7,9) and pop > 9:
        tc_list.append("In")
    
    #Non-Industrual(Ni)
    if pop < 6:
        tc_list.append("Ni")
    
    #Rich (Ri)
    if atmo in (6, 8) and pop in (6, 7, 8) and gov >=4 and gov <= 9:
        tc_list.append("Ri")
    
    #Poor (Po)
    if atmo >= 2 and atmo <=5 and hydro < 2:
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

def tradecode_translate(tradecodes):
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
    tradecodes = tradecode_generate(psize, patmo, phydro, ppop, pgov, plaw)
    uwp = uwp_gen(pcontent[0], psize, patmo, phydro, ppop, pgov, plaw, ptech, tradecodes)
    print_description(uwp, pcontent, tradecodes)

program_running = True

while(program_running):
    print("Traveller System Generator!")
    print("Make a selection: ")
    print("1. Create a New System.")
    print("2. Exit Program.")

    try:
        select = int(input("\nSelection: "))    
    except ValueError:
        print("Invalid Selection!")
    else:
        if select == 1:
            create_system()
        elif select == 2:
            program_running = False
