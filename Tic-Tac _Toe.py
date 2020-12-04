board=[
    "-", "-","-",
    "-", "-","-",
    "-", "-","-"
    ]

count=1
winner=None

def displayBoard():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

def availableSpace_X():
    position=int(input("Enter Your Choice from 1-9: "))-1
    if board[position]=="X" or board[position]=="O":
        while(board[position]=="X" or board[position]=="O"):
            print("--Position Already Occupied,Please Select Another--")
            position=int(input("Enter Your Choice from 1-9: "))-1

    if board[position]!="X" or board[position]!="O":
        board[position]="X"


def availableSpace_O():
    position=int(input("Enter Your Choice from 1-9: "))-1
    if board[position]=="X" or board[position]=="O":
        while(board[position]=="X" or board[position]=="O"):
            print("--Position Already Occupied,Please Select Another--")
            position=int(input("Enter Your Choice from 1-9: "))-1

    if board[position]!="X" or board[position]!="O":
        board[position]="O"


def row_check():
    if board[0]==board[1]==board[2]!="-":
        # print(f"{board[0]} won")
        return board[0]

    elif board[3]==board[4]==board[5]!="-":
        # print(f"{board[3]} won")    
        return board[3]

    elif board[6]==board[7]==board[8]!="-":
        # print(f"{board[6]} won")
        return board[6]
    


def col_check():
    if board[0]==board[3]==board[6]!="-":
        return board[0]
        # print(f"{board[0]} won")

    elif board[1]==board[4]==board[7]!="-":    
        return board[3]
        # print(f"{board[1]} won")

    elif board[2]==board[5]==board[8]!="-":
        return board[2]
        # print(f"{board[2]} won")
    

def diag_check():
    if board[0]==board[4]==board[8]!="-":
        return board[0]
        # print(f"{board[0]} won")

    elif board[2]==board[4]==board[6]!="-":    
        return board[2]
        # print(f"{board[2]} won")



while(count<10):
    displayBoard()
    if count%2!=0:
        print("It's Turn Of X")
        availableSpace_X()
        row_check()
        col_check()
        diag_check()
        if row_check()=="X":
            
            print(f"{row_check()} Has Won The Game..")
            break

        elif col_check()=="X":
            
            print(f"{col_check()} Has Won The Game..")
            break
        elif diag_check()=="X":
            
            print(f"{diag_check()} Has Won The Game..")
            break
    else:
        print("It's Turn Of O")
        availableSpace_O()
        row_check()
        col_check()
        diag_check()
        if row_check()=="O":
            print(f"{row_check()} Has Won The Game..")
            break

        elif col_check()=="O":
            print(f"{col_check()} Has Won The Game..")
            break
        elif diag_check()=="O":
            print(f"{diag_check()} Has Won The Game..")
            break

    count+=1
    if count==10:
        print('It a Tie...!!')


