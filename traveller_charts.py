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

def int_translate(hexnum):
        int_chart={
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
            "G": 16
        }
        return int_chart.get(hexnum, "Invalid Hex")

def uwp1_translate(base):
    starport = {
        "A": "A. Excellent quality installation. \nRefined Fuel Available. " +
        "Annual maintainence overhaul available. Shipyard capable of constructing starships and " +
        "non-starships present.",
        "B": "B. Good quality installation. \nRefined fuel available. Annual maintainence overhaul available. " +
        "Shipyard capable of constructing non-starships present.",
        "C": "C. Routine quality installation. \nOnly unrefined fuel available. Reasonable repair facilities present.",
        "D": "D. Poor quality installaition. \nOnly unrefined fuel available. No repair or shipyard facilities present.",
        "E": "E. Frontier installation. \nEssentially a marked spot of bedrock with no fuel, facilities, or bases present.",
        "X": "X. No starport. \nNo provision is made for any ship landings."
    }
    return starport.get(base)

def uwp2_translate(size):
    size_chart = {
        "0": "0. Asteroid/Planetoid Belt",
        "1": "1. 1,000 miles (1,600 km)",
        "2": "2. 2,000 miles (3,200 km)",
        "3": "3. 3,000 miles (4,800 km)",
        "4": "4. 4,000 miles (6,400 km)",
        "5": "5. 5,000 miles (8,000 km)",
        "6": "6. 6,000 miles (9,600 km)",
        "7": "7. 7,000 miles (11,200 km)",
        "8": "8. 8,000 miles (12,800 km)",
        "9": "9. 9,000 miles (14,400 km)",
        "A": "A. 10,000 miles (16,000 km)"
    }
    return size_chart.get(size)

def uwp3_translate(atmo):
    atmo_chart = {
        "0": "0. No Atmosphere",
        "1": "1. Trace",
        "2": "2. Very thin, tainted",
        "3": "3. Very thin",
        "4": "4. Thin, tainted",
        "5": "5. Thin",
        "6": "6. Standard",
        "7": "7. Standard, tainted",
        "8": "8. Dense",
        "9": "9. Dense, tainted",
        "A": "A. Exotic",
        "B": "B. Corrosive",
        "C": "C. Insidious"
    }
    return atmo_chart.get(atmo)

def uwp4_translate(hydro):
    hydro_chart = {
        "0": "0. No free standing water",
        "1": "1. 10% water",
        "2": "2. 20% water",
        "3": "3. 30% water",
        "4": "4. 40% water",
        "5": "5. 50% water",
        "6": "6. 60% water",
        "7": "7. 70% water",
        "8": "8. 80% water",
        "9": "9. 90% water",
        "A": "A. No landmasses"
    }
    return hydro_chart.get(hydro)

def uwp5_translate(population):
    pop_chart = {
        "0": "0. No inhabitants",
        "1": "1. Tens of inhabitants",
        "2": "2. Hundreds of inhabitants",
        "3": "3. Thousands of inhabitants",
        "4": "4. Ten of Thousands of inhabitants",
        "5": "5. Hundreds of Thousands of inhabitants",
        "6": "6. Millions of inhabitants",
        "7": "7. Tens of Millions of inhabitants",
        "8": "8. Hundreds of Millions of inhabitants",
        "9": "9. Billions of inhabitants",
        "A": "A. Tens of Billions of inhabitants"
    }
    return pop_chart.get(population)

def uwp6_translate(govnt):
    gov_chart = {
        "0": "0. No government structure." +
        "\nIn many cases, family bonds predominate.",
        "1": "1. Company/Corporation. \nGovernment by company managerial elite;" + 
        " citizens are company employees.",
        "2": "2. Participating Democracy." + 
        "\nGovernment by advice and concent of the citizen.",
        "3": "3. Self-Perpetuating Oligarchy." + 
        "\nGovernment by a restricted minority, with little or no input from the masses.",
        "4": "4. Representative Democracy." +
        "\nGovernment by elected representatives.",
        "5": "5. Feudal Technocracy." + 
        "\nGovernment by specific individuals for those who agree to be ruled. Relationships are based\n" 
        + "on the performance of techincal activities which are mutually beneficial.",
        "6": "6. Captive Government."+ 
        "\nGovernment by leadership answerable to an outside group; a colony or conquered area.",
        "7": "7. Balkanization." +
        "\nNo central ruling authority exists; rival governments compete for control.",
        "8": "8. Civil Service Bureaucracy." + 
        "\nGovernment by agencies employing individuals selected for their expertise.",
        "9": "9. Impersonal Bureaucracy." + 
        "\nGovernment by agencies which are insulated from the governed.",
        "A": "A. Charismatic Dictator." +
        "\nGovernment by a single leader enjoying the confidence of the citizens.",
        "B": "B. Non-charismatic Dictator."+
        "\nA previous charismatic dictator has been replaced by a leader through normal channels.",
        "C": "C. Charismatic Oligarchy"+
        "\nGovernment by a select group, orginzation, or class enjoying the overwhelming "+ 
        "\nconfidence of the citizenry.",
        "D": "D. Religious Dictatorship"+
        "\nGovernment by a religious organization without regard to the needs of the citizenry."
    }
    return gov_chart.get(govnt)

def uwp7_translate(law):
    law_chart = {
        "0": "0. No prohibitions",
        "1": "1. Body pistols undedectable by standard scanners, explosives (bombs, grenades)"+
        "\nand poison gas prohibited.",
        "2": "2. Portable energy weapons (laser carbine, laser rifle) prohibited. Ships gunnery not affected.",
        "3": "3. Weapons of a strict military nature (machine guns, automatic rifles) prohibited.",
        "4": "4. Light assault weapons (submachine guns) prohibited.",
        "5": "5. Personal concealable firearms (pistols and revolvers) prohibited.",
        "6": "6. Most firearms (except shotguns) prohibited. The carrying of any type of"+
        "\nweapon openly is discouraged.",
        "7": "7. Shotguns are prohibited.",
        "8": "8. Long bladed weapons (all but daggers) are controlled, and open possesion is prohibited.",
        "9": "9. Possession of any weapon outside one's residence is prohibited.",
        "A": "A. Possession of any weapon is prohibited."
    }
    return law_chart.get(law)

def uwp8_translate(tech):
    tech_chart = {
        "0": "0. Stone Age. Primitive",
        "1": "1. Bronze Age to Middle Ages",
        "2": "2. circa 1400 to 1700",
        "3": "3. circa 1700 to 1860",
        "4": "4. circa 1860 to 1900",
        "5": "5. circa 1900 to 1939",
        "6": "6. circa 1940 to 1969",
        "7": "7. circa 1970 to 1979",
        "8": "8. circa 1980 to 1989",
        "9": "9. circa 1990 to 2000",
        "A": "A. Interstellar community",
        "B": "B. Average Imperial",
        "C": "C. Average Imperial",
        "D": "D. Above Average Imperial",
        "E": "E. Above Average Imperial",
        "F": "F. Technical Maximum Imperial",
        "G": "G. Occasional non-Imperial"
    }
    return tech_chart.get(tech)
