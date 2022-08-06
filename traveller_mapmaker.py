import requests
import os

url = 'https://travellermap.com/api/poster'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
origin = ""

def selectStyle():
    #Select Map Type: Poster(Default), Print, Atlus, Candy, Draft, FASA, Terminal, Mongoose
    print("Poster Types: ")
    print("1. Poster.")
    print("2. Atlus")
    print("3. Candy")
    print("4. Draft")
    print("5. FASA")
    print("6. Terminal")
    print("7. Mongoose")
    
    try:
        selection = int(input("Select Style of Poster: "))
    except ValueError:
        print("Invalid Selection! Defaulting to Poster.")
        return "poster"
    else:
        #Create New System
        if selection == 1:
            return "poster"
        elif selection == 2:
            return "atlas"
        elif selection == 3:
            return "candy"
        elif selection == 4:
            return "draft"
        elif selection == 5:
            return "fasa"
        elif selection == 6:
            return "terminal"
        elif selection == 7:
            return "mongoose"
        else:
            print("Invalid Number! Defaulting to Poster.")
            return "poster"
        

#Select Subsector
def selectSubsector():
    subsectors = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    try:
        selection = str(input("Select Subsector, or Leave Blank for Full Sector. (Default: Subsector A)"))
    except (TypeError):
        print("Invalid Selction! Defaulting to Subsector A.")
    else:
        if selection == "":
            print("Using Full Sector.")
            return "Full Sector"
        elif selection.upper() in subsectors:
            print(("Using Subsector {}").format(selection.upper()))
            return selection.upper()
        else:
            print("Selection not in list. Defaulting to Subsector A.")
            return "A"
            

def payloadGenerator():
    styleElement = selectStyle()
    subsectorElement = selectSubsector()

    if (subsectorElement != "Full Sector"):
        return {'style': styleElement, 'subsector': subsectorElement}
    else:
        return {'style': styleElement}

def mapCreate(path):
    tradeRouteFound = False

    print("Setting up Map Creator: ")
    chartsPath = os.path.join(path,'Charts')
    tradePath = os.path.join(path,'Trade Routes')
    mapPath = os.path.join(path,'Maps')

    chartList = os.listdir(chartsPath)
    tradeList = os.listdir(tradePath)

    for j in range(len(chartList)):
        print(("{}. {}").format(j+1, chartList[j]))

    try:
        selection = int(input("Select Sector Map to Create or Press 'N' to Escape: "))
    except: 
        print("Returning to Menu.\n")
    else:
        if (selection not in range(1,len(chartList)+1)):
            print("Selection Out Of Range")
        elif (selection in range(1,len(chartList)+1)):
            print("Generating Map...")

            chartName = chartList[selection-1][(len(chartsPath)):-4]
            print(("Chart Name: {}").format(chartName))

            for i in tradeList:
                if (i[len(tradePath):-17] == chartName):
                    tradeRouteFound = True
                    tradeName = i


            mapCharted = (chartList[selection-1])[:-4] + " Map"
            mapFileName = os.path.join(mapPath, mapCharted + ".jpg")
            sectorFileName = os.path.join(chartsPath, chartList[selection-1])
            tradeRouteFileName = os.path.join(tradePath, tradeName)

            #Create Sector Data
            sectorFile = open(sectorFileName,'r')
            sector = (sectorFile.read()).split("\n")

            for i in range(0,len(sector)-1):
                entry = sector[i].split("\t")
                if (entry[0] != "Hex") and (entry[0][0:6] == "Origin"):
                    origin = entry[0][8:12]
                    print(("Origin of this sector is: {}").format(origin))
                    sector.pop(i)
            sectorData = "\n".join(sector)

            #Retrieve Trade Route Data
            tradeFile = open(tradeRouteFileName,'r')
            tradeData = tradeFile.read()

            print(("Testing Data: {} Testing Trade: {}\n").format(sectorFileName,tradeRouteFileName))

            payload = payloadGenerator()

            if (tradeRouteFound == True):
                totalData = {"data": sectorData, "metadata": tradeData}
            else:
                 totalData = {"data": sectorData}

            r = requests.post(url, headers=headers, data=totalData, params=payload)
            print(r.status_code)

            file = open(mapFileName,"wb")
            file.write(r.content)
            file.close

            print("\nMap Saved!\n")