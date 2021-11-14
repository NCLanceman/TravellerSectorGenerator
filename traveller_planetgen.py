import os
import traveller_utilities as t_util
import traveller_traderoute as t_trade

def getSectorName():
    name = str(input("Enter Sector Name: "))
    return name

#Set up file paths for Result Folder
path = os.getcwd()
if((os.path.isdir('Results')) == False):
        os.mkdir('Results')

workingFilePath = os.path.join(path,'Results')

current_uwp = ""
result = ""

#Main Menu Loop
program_running = True
while(program_running):
    print("Traveller System Generator!")
    print("\nMake a selection: ")
    print("1. Create a New System.")
    print("2. Save Previous System.")
    print("3. Create Jump Subsector.")
    print("4. Create Standard Subsector.")
    print("5. Add or Replace Trade Route to Existing Subsector Chart")
    print("6. Create Booklet from UWP Chart.")
    print("7. Exit Program.")

    try:
        select = int(input("\nSelection: "))    
    except ValueError:
        print("Invalid Selection!")
    else:
        #Create New System
        if select == 1:
            location = input("\nLocation: ")
            current_uwp = t_util.create_system("Known")
            result += location +"\tKnown\t"+ current_uwp +"\n"
            print(result)
        #Save Previous System
        elif select == 2:
            fileName = os.path.join(workingFilePath, "Saved UWPs.txt")
            saveFile = open(fileName, 'a')
            saveFile.write("\n"+t_util.print_description(current_uwp)+"\n\n")
            saveFile.close()
            print("\n\nFile Saved!\n\n")
        #Create Jump Subsector
        elif select == 3:
            sectorName = getSectorName()
            tradeRoutes = sectorName + " Trade Routes"
            sectorFileName = os.path.join(workingFilePath, sectorName +".txt")
            tradeFileName = os.path.join(workingFilePath, tradeRoutes + ".txt")
            bias = int(input("Enter Trade Route Bias (1-100%): "))
            try:
                j_range = int(input("Jump Range: "))
            except ValueError:
                print("Invalid Selection!")
            else:
                origin = ((str(j_range+1)).zfill(2))*2
                try:
                    known = int(input("Known System Radius: "))
                except ValueError:
                    print("Invalid Selection!")
                else:
                    board = t_util.jump_sector_hex(j_range)
                    board = t_util.create_j_sector(board, known,origin)
                    saveFile = open(sectorFileName, 'w')
                    saveFile.write("Origin: " + origin + "\n")
                    saveFile.write(t_util.board_printer(board))
                    saveFile.close()

                    tradeFile = open(tradeFileName,'w')
                    tradeFile.write(t_trade.generateTradeRoutes(sectorFileName,bias))
                    tradeFile.close()
                    print("\n\nSystem Saved!\n\n")
        #Create Standard Subsector
        elif select == 4:
            sectorName = getSectorName()
            tradeRoutes = sectorName + " Trade Routes"
            sectorFileName = os.path.join(workingFilePath, sectorName +".txt")
            tradeFileName = os.path.join(workingFilePath, tradeRoutes + ".txt")

            bias = int(input("Enter Trade Route Bias (1-100%): "))

            board = t_util.create_sector()
            
            sectorFile = open(sectorFileName, 'w')
            sectorFile.write(t_util.board_printer(board))
            sectorFile.close()

            tradeFile= open(tradeFileName,'w')
            tradeFile.write(t_trade.generateTradeRoutes(sectorFileName,bias))
            tradeFile.close()
            print("\n\nSystem Saved!\n\n")
        #Create or Reroll Trade Route
        elif select == 5:
            list = os.listdir(workingFilePath)

            for i in list:
                if (i[-16:] == "Trade Routes.txt"):
                    list.remove(i)
                elif (i[-11:] == "Booklet.txt"):
                    list.remove(i)
            for j in range(len(list)):
                print(("{}. {}").format(j+1, list[j]))
            
            try:
                selection = int(input("Select Chart To Re-Roll or Press 'N' to Escape: "))
            except: 
                print("Returning to Menu.\n")
            else:
                if (selection not in range(1,len(list)+1)):
                    print("Selection Out Of Range")
                elif (selection in range(1,len(list)+1)):
                    print("Generating New Trade Routes...")
                    tradeRoutes = (list[selection-1])[:-4] + " Trade Routes"
                    sectorFileName = os.path.join(workingFilePath, list[selection-1])
                    tradeFileName = os.path.join(workingFilePath, tradeRoutes + ".txt")
                    bias = int(input("Enter Trade Route Bias (1-100%): "))
                    
                    tradeFile= open(tradeFileName,'w')
                    tradeFile.write(t_trade.generateTradeRoutes(sectorFileName,bias))
                    tradeFile.close()
                    print("\n\nSystem Saved!\n\n")
        #Create Booklet from UWP Chart
        elif select == 6:
            list = os.listdir(workingFilePath)

            for i in list:
                if (i[-16:] == "Trade Routes.txt"):
                    list.remove(i)
                elif (i[-11:] == "Booklet.txt"):
                    list.remove(i)

            for j in range(len(list)):
                print(("{}. {}").format(j+1, list[j]))
            
            try:
                selection = int(input("Select Booklet to Create or Press 'N' to Escape: "))
            except: 
                print("Returning to Menu.\n")
            else:
                if (selection not in range(1,len(list)+1)):
                    print("Selection Out Of Range")
                elif (selection in range(1,len(list)+1)):
                    print("Generating Booklet...")
                    booklet = (list[selection-1])[:-4] + " Booklet"
                    sectorFileName = os.path.join(workingFilePath, list[selection-1])
                    bookletFileName = os.path.join(workingFilePath, booklet + ".txt")
                    
                    bookletFile= open(bookletFileName,'w')
                    sectorFile = open(sectorFileName,'r')
                    sector = (sectorFile.read()).split("\n")

                    for i in sector:
                        if i:
                            entry = i.split("\t")
                            #current_uwp = entry[2:]
                            #print(("Current UWP: {}").format(current_uwp))
                            if (entry[0] != "Hex") and (entry[0][0:6] != "Origin"):
                                bookletFile.write(("{}\t{}").format(entry[0],entry[1]))
                                bookletFile.write("\n"+t_util.print_description(i)+"\n\n")                         

                    bookletFile.close()
                    sectorFile.close()
                    print("\n\nSystem Saved!\n\n")
        elif select == 7:
            program_running = False
