area = [['*','*','*'],['*','*','*'],['*','*','*']]
##area[0][0] = 'x'
##area[0][1] = 'x'
##area[0][2] = '0'
##area[1][0] = 'x'
##area[1][1] = '0'
##area[1][2] = '0'
##area[2][0] = 'x'
##area[2][1] = '0'
##area[2][2] = 'x
def check_winer():
    if area[0][0] == "x" and area[0][1] == "x" and area[0][2] == "x":
        return "x"
    if area[1][0] == "x" and area[1][1] == "x" and area[1][2] == "x":
        return "x"
    if area[2][0] == "x" and area[2][1] == "x" and area[2][2] == "x":
        return "x"
    if area[0][0] == "x" and area[1][0] == "x" and area[2][0] == "x":
        return "x"


    if area[0][1] == "x" and area[1][1] == "x" and area[2][1] == "x": 
        return "x"
    if area[0][2] == "x" and area[1][2] == "x" and area[2][2] == "x":


        return "x" 
    if area[0][0] == "x" and area[1][1] == "x" and area[2][2] == "x":


        return "x"
    if area[0][2] == "x" and area[1][1] == "x" and area[2][0] == "x":


        return "x" 
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":


        return "0"


    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":


        return "0"


    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":


        return "0"


    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":


        return "0"


    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":


        return "0"


    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":


        return "0"


    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":


        return "0"


    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":


        return "0"


    return "*" 




for i in range(1,10):
    row = input("Which row you want to put mark ")
    row = int(row)
    column = input("Which coulumn you want to put mark ")
    column = int(column)
    if area[row][column] != "*":
        print("You skip your turn!")
        continue
    if (i%2) == 0:
        area[row][column] = '0'
    else:    
        area[row][column] = 'x'
    for j in area:
        print(j)
    if check_winer() == "x":
        print("The x take the win")
        break
    elif check_winer() == "0":
        print("The 0 take the win")
        break
    elif i == 9 and check_winer() == "*":
        print("Its a draw!") 



##Move the code for printing the field into a separate "print_area" function and call this function in the main program.

##Figure out how to solve the awkward entry of row and column numbers so that the user can enter not 0,1, and 2, but 1, 2, and 3.
