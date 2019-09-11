import traveller_utilities as t_util
#Starter Traveller Planet Generation

program_running = True

current_uwp = ""

while(program_running):
    print("Traveller System Generator!")
    print("Make a selection: ")
    print("1. Create a New System.")
    print("2. Save Previous System.")
    print("3. Create Jump Subsector.")
    print("4. Exit Program.")

    try:
        select = int(input("\nSelection: "))    
    except ValueError:
        print("Invalid Selection!")
    else:
        if select == 1:
            current_uwp = t_util.create_system()
        elif select == 2:
            saveFile = open("Saved UWPs.txt", 'a')
            saveFile.write(current_uwp)
            saveFile.write("\n"+t_util.print_description(current_uwp)+"\n\n")
            saveFile.close()
            print("\n\nFile Saved!\n\n")
        elif select == 3:
            try:
                j_range = int(input("\nJump Range: "))
            except ValueError:
                print("Invalid Selection!")
            else:
                try:
                    known = int(input("\nKnown System Radius: "))
                except ValueError:
                    print("Invalid Selection!")
                else:
                    saveFile = open("New Sector.txt", 'a')
                    saveFile.write(t_util.create_j_subsector(j_range,known))
                    saveFile.close()
                    print("\n\nSystem Saved!\n\n")
        elif select == 4:
            program_running = False
