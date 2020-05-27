import traveller_utilities as t_util
import map_hex
#Starter Traveller Planet Generation

program_running = True

current_uwp = ""
result = ""

while(program_running):
    print("Traveller System Generator!")
    print("Make a selection: ")
    print("1. Create a New System.")
    print("2. Save Previous System.")
    print("3. Create Jump Subsector.")
    print("4. Create Standard Subsector.")
    print("5. Exit Program.")

    try:
        select = int(input("\nSelection: "))    
    except ValueError:
        print("Invalid Selection!")
    else:
        if select == 1:
            location = input("\nLocation: ")
            current_uwp = t_util.create_system("Known")
            result += location +"\tKnown\t"+ current_uwp +"\n"
            print(result)
        elif select == 2:
            saveFile = open("Saved UWPs.txt", 'a')
            saveFile.write("\n"+t_util.print_description(current_uwp)+"\n\n")
            saveFile.close()
            print("\n\nFile Saved!\n\n")
        elif select == 3:
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
                    board = t_util.grid_generate(j_range)
                    saveFile = open("New Jump Sector.txt", 'a')
                    saveFile.write("Origin: " + origin + "\n")
                    saveFile.write(t_util.create_j_sector(board,known))
                    saveFile.close()
                    print("\n\nSystem Saved!\n\n")
        elif select == 4:
            sector_list = []
            
            for x in range(1,9):
                for y in range (1,11):
                    hexlocation = (str(x)).zfill(2) + (str(y)).zfill(2)
                    sector_list.append(hexlocation)
            board = t_util.create_sector(sector_list)

            saveFile = open("New Standard Sector.txt", 'a')
            saveFile.write(board)
            saveFile.close()
            print("\n\nSystem Saved!\n\n")
        elif select == 5:
            program_running = False
