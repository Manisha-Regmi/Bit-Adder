def byteadder():
    sucess=False
    while sucess==False:
        try:#Performing exceptional handling
            print("\n                   Input section     ")
            print ("********************************************************************************                       ")
            A= None # initilizing our input as none at first
            while A is None:#loops the progarm every time we haven not enetered eiither 0 or 1
                try:
                    A= int(input("\nEnter either 1 0r 0      : "))
                except ValueError:
                    print("Invalid input.Please enter  1 or 0 as input")
            print(str(A))#prints the number that we have typed
            B= None
            while B is None:
                try:
                    B= int(input("Enter either 1 0r 0 again: "))
                except ValueError:
                    print("Invalid input.Please enter  1 or 0 as input")
            print(str(B))

            print("--------------------------------------------------------------------------------")
            print("\n                      Passing through different gates \n       ")
            C_in=None
            while C_in is None:
                try:
                    C_in=0
                except ValueError:
                     print("input is 0,No stored value found.")
            

            C_out=None
            while C_out is None:
                try:
                    C_out=0
                except ValueError:
                     print("input is 0,No stored value found.")
            

            AND_1=None # it depends upon the input input A AND B
            if A==1 and B==1:
                AND_1=1
                print("The value after passing through AND gate is : " ,AND_1)
            else:
                AND_1=0
                print("The value after passing through AND gate is : " ,AND_1)
                


            XOR= None # it depends upon the input input A AND B
            if A == 0 and B == 0: 
                XOR = 0
                print("The value after passing through XOR gate is : " ,XOR)
            elif A == 1 and B == 0:
                XOR = 1
                print("The value after passing through XOR gate is : " ,XOR)
            elif A == 0 and B == 1: 
                XOR = 1
                print("The value after passing through XOR gate is : " ,XOR)
            elif A == 1 and B == 1:
                XOR = 0
                print("The value after passing through XOR gate is : " ,XOR)
            else:
                print("Are you sure you stored input of 1 or 0?")

            AND_2=None # it depends upon the input input A AND B
            if XOR==1 and C_in==1:
                AND_2=1
                
            else:
                AND_2=0
                    

            NOR= None # it depends upon the input input A AND B
            if A == 0 and B == 0: 
                NOR = 1
                print("The value after passing through NOR gate is : " ,NOR)
            elif A == 1 and B == 0:
                NOR = 0
                print("The value after passing through NOR gate is : " ,NOR)
            elif A == 0 and B == 1: 
                NOR = 0
                print("The value after passing through NOR gate is : " ,NOR)
            elif A == 1 and B == 1:
                NOR = 0
                print("The value after passing through NOR gate is : " ,NOR)
            else:
                print("Are you sure you stored input of 1 or 0?")
                
            OR= None # it depends upon the input input A AND B
            if A == 0 and B == 0: 
                OR = 0
                print("The value after passing through OR gate is  : " ,OR)
            elif A == 1 and B == 0:
                OR = 1
                print("The value after passing through OR gate is  : " ,OR)
            elif A == 0 and B == 1: 
                OR = 1
                print("The value after passing through OR gate is  : " ,OR)
            elif A == 1 and B == 1:
                OR = 1
                print("The value after passing through OR gate is  : " ,OR)
            else:
                print("Are you sure you stored input of 1 or 0?")
                
            NAND= None # it depends upon the input input A AND B
            if A == 0 and B == 0: 
                NAND = 1
                print("The value after passing through NAND gate is: " ,NAND)
            elif A == 1 and B == 0:
                NAND = 1
                print("The value after passing through NAND gate is: " ,NAND)
            elif A == 0 and B == 1: 
                NAND = 1
                print("The value after passing through NAND gate is: " ,NAND)
            elif A == 1 and B == 1:
                NAND = 0
                print("The value after passing through NAND gate is: " ,NAND)
            else:
                print("Are you sure you stored input of 1 or 0?")
                
            print("--------------------------------------------------------------------------------")
            print("\n                      Passing through byte adder        ")
            print("  ")

            def first_AND(A,B): # Works on the principle of AND gate
                if A==1 and B==1:
                    AND_1 = 1
                    print("\nPassing value through first AND gate     : ",A ," AND " ,B ," = " ,AND_1)
                else:
                     AND_1 = 0
                     print("Passing value through first AND gate      : ",A ," AND " ,B ," = " ,AND_1)

            def XOR_(A,B):# Works on the principle of XOR gate
                if (A==0 and B==0)or( A==1 and B==1):
                    XOR=0
                    print("Passing value through XOR gate           : ",A ," XOR ",B," = ",XOR)
                else:
                    XOR=1
                    print("Passing value through XOR gate           : ",A ," XOR ",B," = ",XOR)

            def second_AND(XOR,C_in):# Works on the principle of AND gate
                if XOR==1 and C_in==1:
                    AND_2=1
                    print("Passing value through Second AND gate     : ",XOR ," AND ",C_in ," = ",AND_2)
                else:
                     AND_2=0
                     print("Passing value through Second AND gate    : ",XOR ," AND ",C_in ," = ",AND_2)

            def NOR_(AND_1,AND_2):# Works on the principle of NOR gate
                if AND_1==0 and AND_2==0:
                    NOR=1
                    print("Passing value through NOR gate           : ",AND_1 ," NOR ",AND_2 ," = ",NOR)
                else:
                    NOR=0
                    print("Passing value through NOR gate           : ",AND_1 ," NOR ",AND_2," = ",NOR)
                   
            def NOT_(AND_1,AND_2):# Works on the principle of NOT gate
                if AND_1==0 and AND_2==0:
                    NOT=0
                    print("Passing value through NOT gate           : ",AND_1 ," NOT " ,AND_2 ," = ",NOT)
                else:
                    NOT=1
                    print("Passing value through NOT gate           : ",AND_1 ," NOT " ,AND_2 ," = ",NOT)

            def OR_(C_out,XOR):# Works on the principle of OR gate
                if C_out==0 and  XOR==0:
                    OR=0
                    print("Passing value through OR gate            : ",C_out ," OR  " ,XOR," = " ,OR)
                else:
                    OR=1
                    print("Passing value through OR gate            : ",C_out ," OR  " ,XOR," = ",OR)

            def NAND_(C_out,XOR):# Works on the principle of NAND gate
                if C_out==1 and XOR==1:
                    NAND=0
                    print("Passing value through NAND gate          : ",C_out ," NAND",XOR," = ",NAND)
                else:
                    NAND=1
                    print("Passing value through NAND gate          : ",C_out ," NAND",XOR ," = ",NAND)

            def third_AND(OR,NAND):# Works on the principle of AND gate
                if OR==1 and NAND==1:
                    SUM=1
                    print("Passing value through Third AND gate     : ",OR ," AND ",NAND," = ",SUM)
                else:
                    SUM=0
                    print("Passing value through Third AND gate     : ",OR ," AND ",NAND," = ",SUM)
            first_AND(A,B)
            XOR_(A,B)        
            second_AND(XOR,C_in)
            NOR_(AND_1,AND_2)
            NOT_(AND_1,AND_2)
            OR_(C_out,XOR)
            NAND_(C_out,XOR)   
            third_AND(OR,NAND)
            
            continuos=input("\nDo you still want to use this application?. Type for yes to continue: ")
            if continuos.upper()=="YES":
                continue
            else:
                print ("\n-------------------------------------------------------------------------------")
                print("                     Thankyou for using this application.")
                print ("--------------------------------------------------------------------------------")
                break

            
        except:
            print("\nplease enter valid input only")
             
            
byteadder()
