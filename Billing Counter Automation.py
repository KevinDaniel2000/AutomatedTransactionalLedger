import time
# INITIATE values
global saved_value_index, value, END_REVENUE, END_no_TRANSACTIONS #, temp_saved_value_index
# List
saved_value_index = [4, 3, 8, 2, 3, 13, 21]
#saved_value_index = [2, 1, 0, 0, 0, 0, 0]
# Tuple
value = (2000, 500, 200, 100, 50, 20, 10)
#temp_saved_value_index = saved_value_index
END_REVENUE = int(0)
END_no_TRANSACTIONS = int(0)

# PIN to TERMINATE program
def pin_function():
    delete_pin = int(1234)
    str_delete_pin_length = str(delete_pin)
    return delete_pin, str_delete_pin_length

# SLEEP function
def sleep():
    print("\n\t Program Has Entered into SLEEP, Programm has been HALTED successfully \n\t press [ctrl+c] to INTERRUPT")
    interrupt = 0
    while interrupt == 0:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            interrupt += 1
            print("\nProgram out of SLEEP")
        if interrupt != 0:
            break

#import os, psutil

def billing_input():
    global total_amount, total_value_of_bank_notes_given, value, billing_value, user_input_split_notes_list
    total_value_of_bank_notes_given = 0
    user_input_split_notes_list = [0,0,0,0,0,0,0]
    
    try:
        #print("Enter bill amount")
        billing_value = int(input(F'Enter Bill Amount | '))
        #billing_value= int(input())        
        assert billing_value > 0
    except AssertionError:
        print("------------------------------------------------------------------------# ERROR #------")
        print("\t MESSAGE: BILLING VALUE CAN'T BE ZERO")
        print("---------------------------------------------------------------------------------------")
    except ValueError:
        print("------------------------------------------------------------------------# ERROR #------")
        print("\t MESSAGE: BILLING VALUE CAN'T BE an CHARACTER")  
        print("---------------------------------------------------------------------------------------")
    else:
        print("Notes before dispense = ", saved_value_index)
        temp_saved_value_index = saved_value_index
    
        for i in range(7):
            try:
                input_value = int(input(F' How many {value[i]} Rs note | '))
                user_input_split_notes_list[i] = input_value
            except ValueError:
                print("------------------------------------------------------------------------# ERROR #------")
                print("UN-EXPECTED INPUT DETECTED | TRY: integer value")
                print("---------------------------------------------------------------------------------------")
                break
    
        for i in range(len(value)):
            temp_container_to_add = 0
            temp_container_to_add = user_input_split_notes_list[i] * value[i]
            total_value_of_bank_notes_given = total_value_of_bank_notes_given + temp_container_to_add
        
        try:
            assert total_value_of_bank_notes_given > 0
        except:
            print("------------------------------------------------------------------------# ERROR #------")
            print("\t MESSAGE: GIVE VALID NUMBER OF BANKNOTES")
            print("---------------------------------------------------------------------------------------")
    
        total_amount_to_dispense = total_value_of_bank_notes_given - billing_value
        total_amount = total_amount_to_dispense 
    
def null_bank_notes():
    global throw
    temp=0
    throw=7
    for j in range(len(saved_value_index)):
        if saved_value_index[temp]==0:
            throw=throw-1
            temp=temp+1
        else:
            pass
    return throw

def dispense(total):
    global denomination_variable, out, loop_went_through_note, bug
    
    bug = 0
    loop_went_through_note = [0, 0, 0, 0, 0, 0, 0]
    
    out = int(0)
    i=0
    denomination_variable = [0, 0, 0, 0, 0, 0, 0]    

    while out<=total:
        if out <= total:
            if saved_value_index[0] != 0 and out+2000 <= total:
                out = out+2000
                saved_value_index[0]=saved_value_index[0]-1
                denomination_variable[0] = denomination_variable[0]+1
                loop_went_through_note[0] = loop_went_through_note[0]+1
                
            elif saved_value_index[1] != 0 and out+500 <= total:
                out = out+500
                saved_value_index[1]=saved_value_index[1]-1
                denomination_variable[1] = denomination_variable[1]+1
                loop_went_through_note[1] = loop_went_through_note[1]+1
                
            elif saved_value_index[2] != 0 and out+200 <= total:
                out = out+200
                saved_value_index[2]=saved_value_index[2]-1
                denomination_variable[2] = denomination_variable[2]+1
                loop_went_through_note[2] = loop_went_through_note[2]+1
                
            elif saved_value_index[3] != 0 and out+100 <= total:
                out = out+100
                saved_value_index[3]=saved_value_index[3]-1
                denomination_variable[3] = denomination_variable[3]+1
                loop_went_through_note[3] = loop_went_through_note[3]+1
                
            elif saved_value_index[4] != 0 and out+50 <= total:
                out = out+50
                saved_value_index[4]=saved_value_index[4]-1
                denomination_variable[4] = denomination_variable[4]+1
                loop_went_through_note[4] = loop_went_through_note[4]+1

            elif saved_value_index[5] != 0 and out+20 <= total:
                out = out+20
                saved_value_index[5]=saved_value_index[5]-1
                denomination_variable[5] = denomination_variable[5]+1
                loop_went_through_note[5] = loop_went_through_note[5]+1
                
            elif saved_value_index[6] != 0 and out+10 <= total:
                out = out+10
                saved_value_index[6]=saved_value_index[6]-1
                denomination_variable[6] = denomination_variable[6]+1
                loop_went_through_note[6] = loop_went_through_note[6]+1
                
            else:
                bug = bug+1
                out = 0
                
                if bug == 1:
                    increment_variable=0
                    for i in range(len(saved_value_index)):
                        saved_value_index[increment_variable] = saved_value_index[increment_variable] + loop_went_through_note[increment_variable]
                        denomination_variable[increment_variable] = denomination_variable[increment_variable] - loop_went_through_note[increment_variable]
                        increment_variable = increment_variable+1
                    if (total_value_of_bank_notes_given == billing_value):
                        print(" ")
                        print("Exact value has given")                    
                    elif (bug == 1):
                        print("------------------------------------------------------------------------# ERROR #------")
                        print("\t MESSAGE: Dispense combination error | TRY: give lower amount")
                        print("---------------------------------------------------------------------------------------")

                else:
                    pass
                break
                
        elif out == total:
            pass
        
        null_bank_notes() #function call
        
        if (out==total) or (throw==0):
            if out < total:
                print("------------------------------------------------------------------------# ERROR #------")
                print("\t MESSAGE: Not enough cash to dispense")
                print("---------------------------------------------------------------------------------------")
            break
    return out, bug
    
def input_denomination_throw(user_input_split_notes_list):
    print("_______________________________________________________________________________________________")
    print("|INPUT DENOMINATION", user_input_split_notes_list)
    print("\t |Number of 2000 rs note given x ", user_input_split_notes_list[0] , " = ", user_input_split_notes_list[0]*2000)
    print("\t |Number of 500  rs note given x ", user_input_split_notes_list[1] , " = ", user_input_split_notes_list[1]*500)
    print("\t |Number of 200  rs note given x ", user_input_split_notes_list[2] , " = ", user_input_split_notes_list[2]*200)
    print("\t |Number of 100  rs note given x ", user_input_split_notes_list[3] , " = ", user_input_split_notes_list[3]*100)
    print("\t |Number of 50   rs note given x ", user_input_split_notes_list[4] , " = ", user_input_split_notes_list[4]*50)
    print("\t |Number of 20   rs note given x ", user_input_split_notes_list[5] , " = ", user_input_split_notes_list[5]*20)
    print("\t |Number of 10   rs note given x ", user_input_split_notes_list[6] , " = ", user_input_split_notes_list[6]*10)
    print("\n Total value of bank notes recieved",total_value_of_bank_notes_given)
    print("_______________________________________________________________________________________________")
    
def denomination_throw(no_of_note_dispense):
    print("_______________________________________________________________________________________________")
    print("|DISPENSE DENOMINATION", denomination_variable)
    print("\t |Number of 2000 rs note dispensed x ", no_of_note_dispense[0] , " = ", no_of_note_dispense[0]*2000)
    print("\t |Number of 500  rs note dispensed x ", no_of_note_dispense[1] , " = ", no_of_note_dispense[1]*500)
    print("\t |Number of 200  rs note dispensed x ", no_of_note_dispense[2] , " = ", no_of_note_dispense[2]*200)
    print("\t |Number of 100  rs note dispensed x ", no_of_note_dispense[3] , " = ", no_of_note_dispense[3]*100)
    print("\t |Number of 50   rs note dispensed x ", no_of_note_dispense[4] , " = ", no_of_note_dispense[4]*50)
    print("\t |Number of 20   rs note dispensed x ", no_of_note_dispense[5] , " = ", no_of_note_dispense[5]*20)
    print("\t |Number of 10   rs note dispensed x ", no_of_note_dispense[6] , " = ", no_of_note_dispense[6]*10)
    print("\n Total amount dispensed = ",out)
    print("_______________________________________________________________________________________________")

def master_initiate(value_of_money, no_of_notes, expected_value, bill_amount, input_value_for_billing):
  # NOTATION  
    #value = value_of_money
    #saved_value_index = no_of_notes
    #total_amount = expected_value
    #billing_value = bill_amount
    #total_value_of_bank_notes_given = input_value_for_billing
    
    user_condition_validation = 0
    while user_condition_validation == 0:
        input_denomination_throw(user_input_split_notes_list)
        confirm_from_user = str(input("CONFIRM THE BANKNOTES | ")[0])
        try:
            assert (confirm_from_user == "y") or (confirm_from_user == "Y") or (confirm_from_user == "n") or (confirm_from_user == "N")
        except AssertionError:
            print("------------------------------------------------------------------------# ERROR #------")
            print("\t MESSAGE: Enter valid condition")
            print("---------------------------------------------------------------------------------------")
        else:
            
            if confirm_from_user == "y" or confirm_from_user == "Y":
            
                j=0
                cross_check_availability = 0
            
                for i in range(len(value_of_money)):
                    temp = value_of_money[j] * no_of_notes[j]
                    cross_check_availability = cross_check_availability + temp
                    j=j+1
        
                if bill_amount > input_value_for_billing:
                    print("------------------------------------------------------------------------# ERROR #------")
                    print("\t MESSAGE: GIVE SUFFICIENT MONEY FOR BILLING")
                    print("---------------------------------------------------------------------------------------")           
                
                elif cross_check_availability >= expected_value:
                    dispense(total_amount)
                    if input_value_for_billing == bill_amount:
                        print("EXACT VALUE HAS GIVEN")
        
                    else:
                        #dispense(total_amount)
                        null_bank_notes()
                        if bug !=1:
                            denomination_throw(denomination_variable)
                        
                    if out > 0 or (total_value_of_bank_notes_given == billing_value):
                        global END_REVENUE, END_no_TRANSACTIONS
                        END_REVENUE = (END_REVENUE + int(billing_value))
                        END_no_TRANSACTIONS = (END_no_TRANSACTIONS + 1)
                        print("_______________________________________________________________________________________________")
                        print("\t MESSAGE: BILLING SUCCESS | HAPPY SHOPPING")
                        print("_______________________________________________________________________________________________")
                        
                        for i in range(7):
                            temp_value_add_container = user_input_split_notes_list[i]
                            saved_value_index[i] = saved_value_index[i] + temp_value_add_container
                        print("---------------Remaining value after iteration", saved_value_index)
                    
                elif cross_check_availability < expected_value:
                    print("Value you're expecting in return to dispense = ", (total_value_of_bank_notes_given - billing_value) )
                    print("------------------------------------------------------------------------# ERROR #------")
                    print("\t MESSAGE: Not sufficient money to dispense")
                    print("---------------------------------------------------------------------------------------")
                    
                    if cross_check_availability != 0:
                        print("Try to give lower amount")
                    elif (cross_check_availability == 0) or (cross_check_availability < expected_value):
                        print("\n_______________________________________________________________________________________________")
                        print("\t MESSAGE: SORRY FOR INCONVENIENCE")
                        print("_______________________________________________________________________________________________") 
                        
                user_condition_validation+=1
            
            elif confirm_from_user == "n" or confirm_from_user == "N":
                print("\n \t USER DECLINED")
                user_condition_validation += 1
                
            if user_condition_validation > 0:
                break
                
                    
# MASTER WHILE
variable_for_master_while = 0
while variable_for_master_while == 0:
    print(" ")
    print("\n_______________________________________________________________________________________________")
    print("* c or C to Check no of Notes in Machine")
    print("* y or Y to RUN")
    print("* n or N to Temporary Halt")
    print("* END to Terminate Permanently")
    print("_______________________________________________________________________________________________")
    master_condition = str(input("ENTER CONDITION | ")[0])
    
    # EXECUTE
    if (master_condition == "y") or (master_condition == "Y"): 
        billing_input()
        if billing_value !=0 and total_value_of_bank_notes_given != 0:
            master_initiate(value, saved_value_index, total_amount, billing_value, total_value_of_bank_notes_given)
        elif (billing_value == 0) or (total_value_of_bank_notes_given == 0):
            print("------------------------------------------------------------------------# ERROR #------")
            print("\t MESSAGE: PLEASE INPUT PROPER VALUE FOR FURTHER BILLING PROCESS \n \t TRY: above zero")
            print("---------------------------------------------------------------------------------------")
    
    # PASS and LOOP
    elif (master_condition == "n") or (master_condition == "N"):
        #global END_REVENUE, END_no_TRANSACTIONS
        print("_______________________________________________________________________________________________")
        sleep()
        print("_______________________________________________________________________________________________")
        
    # CHECK
    elif (master_condition == "c") or (master_condition == "C"):
        total  = 0
        for i in range(len(saved_value_index)):
            temp = value[i] * saved_value_index[i]
            total = total + temp
        print("\n\t BANK NOTES AVAILABLE IN THE MACHINE = ", saved_value_index)
        print(" ")
        for i in range(len(saved_value_index)):
            print("\t", saved_value_index[i], "note of", value[i])
        print("\n\t Total value available =", total, "Rupees")
    
    # MASTER TERMINATE
    # DELETE all variables to free up memory
    elif master_condition == "E":
        pin, str_pin = pin_function()
        try:
            pin_input = int(input("ENTER 4 digit SECURITY PIN | "))
            pin_input_string = str(pin_input)
            assert len(pin_input_string) == len(str_pin)
        except ValueError:
            print("------------------------------------------------------------------------# ERROR #------")
            print("\t MESSAGE: ERROR DETECTED | expected integer value")
            print("---------------------------------------------------------------------------------------")
            del(pin, str_pin)
            continue
        except AssertionError:
            print("------------------------------------------------------------------------# ERROR #------")
            print("\t MESSAGE: ERROR DETECTED | expected 4 digit")
            print("---------------------------------------------------------------------------------------")
            del(pin, str_pin)
            continue
        else:
            pass
        
        if pin_input == pin:
            print("Confirm once again | type: 'END'")
            confirm_end = input()
        
            if confirm_end == "END":
                print("\n_______________________________________________________________________________________________")
                print("PROGRAM ENDED, ALL VARIABLES ARE DELETED")
                #global END_REVENUE, END_no_TRANSACTIONS
                print("\n\t NUMBER OF SUCCESSFULL TRANSACTIONS DONE |", END_no_TRANSACTIONS, "Transactions")
                print("\t TOTAL REVENUE THROUGHT THE DAY |", END_REVENUE, "Rupees")
                print("_______________________________________________________________________________________________")
                print("\t\tPROGRAM TERMINATED")
                time.sleep(10)
                for name in dir():
                    if not name.startswith('_'):
                        del globals()[name] 
                break
            else:
                print("------------------------------------------------------------------------# ERROR #------")
                print("\t MESSAGE: Condition not entered correctly | Redirected to previous")
                print("---------------------------------------------------------------------------------------")
                continue   
        else:
            print("------------------------------------------------------------------------# ERROR #------")
            print("\t MESSAGE: INCORRECT PIN | Redirected to previous")
            print("---------------------------------------------------------------------------------------")
            continue
        
    else:
        print("------------------------------------------------------------------------# ERROR #------")
        print("\t MESSAGE: Please input valid condition") 
        print("---------------------------------------------------------------------------------------")

# MEMORY usage 
#process = psutil.Process(os.getpid())
#print("Memory used", int(process.memory_info().rss/1e+6),"MB")  # in bytes 