import datetime
import pandas as pd
import pymysql 
import sqlalchemy as eng
import matplotlib.pyplot as plt
e = eng.create_engine(f'mysql+pymysql://root:mks123042@localhost:3306/school_ip_project')
print('--------------------------------------------------------------------------------------------------')
malelist =["m","M","0"]
femalelist = ["f","F","1"]
stu_name_list = []
f_name_list =[]
d_o_b_list =[]
age_list =[]
gender2_list =[]
contact_list =[]
stu_class_list =[]
stu_sec_list =[]
stu_house_list =[]
stu_admission_time =[]
yeslist= ['y','yes','0']
nolist= ['n','no','1']
not_allow_char = ['1','2','3','4','5','6','7','8','9','0','-','=',',','.','/',';','\'[',']','!','@','#','$','%','^','&','*','(',')','_','+','<','>','?',':']





print("\n\nPlease Enter You Name\n\n")
while True:
       
    name= input(':--').upper()
    
    invalid_stu_name_char_count1= 0
    
    for char in not_allow_char:
        if char in name:
            invalid_stu_name_char_count1 += 1
            
    if invalid_stu_name_char_count1> 0:
        print("\n\nPlease Enter A Invalid\n\n ")

    else:
        break



print ("\n\nPlease Enter You Gender\nm,M,0 For Male\nf,F,1 For Female\n\n")
while True:
    gender1 = input (":--")
    if ( gender1 in malelist):
        gen1='Mr.'
        break
    elif (gender1 in femalelist):
        gen1='Ms/Mrs.'
        break
    elif (gender1 != malelist and femalelist):
        print("\n\npls give as correct infomation\n\n")
        
        
print (f"\nWelcome {gen1} {name}\n")

print('--------------------------------------------------------------------------------------------------')

while True:
    
    print('\n\nPlease Enter Student Name\n\n')

    while True:
        
        stu_name = input(':--').upper()
        
        invalid_stu_name_char_count= 0
        
        for char in not_allow_char:
            if char in stu_name:
                invalid_stu_name_char_count += 1
                
        if invalid_stu_name_char_count> 0:
            print("\n\nInvalid Student Name\n Please Retry\n\n")

        else:
            break
        



    print('--------------------------------------------------------------------------------------------------')

    print("\n\nPlease Enter Student's Father Name\n\n")
    while True:
        f_name = input(":--").upper()
        
        invalid_f_name_char_count= 0
        
        for char in not_allow_char:
            if char in f_name:
                invalid_f_name_char_count += 1
                
        if invalid_f_name_char_count> 0:
            print("Invalid Student Name\n Please Retry")

        else:
            break


    print('--------------------------------------------------------------------------------------------------')

    d_o_b = input("\n\nPlease Enter Student DOB\nFormat Exampls 14/9/2005\n\n:--")


    print('--------------------------------------------------------------------------------------------------')


    print("\n\nPlease Enter Student Age\n\n")
    while True:
        age = (input(':--')) 
        try:
            age = int(age)
        except ValueError:
            print("\n\nPlease Enter The Student Age Nothing Else\n\n")
            continue
            
        if (2<=age and age<=20):
            break
        
        else:
            print("\n\npls enter a valid age\n\n")
            continue
            

    print('--------------------------------------------------------------------------------------------------')
    
    print("\nPlease Enter Info About Student Gender\nM,m,0 For Male and F,f,1 For Female\n\n")

    while True:
        gender2 = input(':--').upper()
        
        if ( gender2 in malelist):
            gen2='MALE'
            break
        elif (gender2 in femalelist):
            gen2='FEMALE'
            break
        elif (gender2 != malelist and femalelist):
            print("\nPlease Give As Correct Infomation\n\n")
    print('--------------------------------------------------------------------------------------------------')
    
    
    print("\nPlease Enter Student Contact Number\n\n")        
    
    
           
    while True:
        
        contact_half = input(':--')
        try:
            contact_half =int(contact_half)
        except ValueError:
            print("\n\nPlease Enter Contact Number Nothing Else\n\n") 
            continue
        contact_half =str(contact_half)
        x= len(contact_half)
        
        if x==10:
            contact_half = int(contact_half)
            break
        
        else:
            print('\n\nPlease Enter A Valid 10 Digit Contact Number\n\n')
            continue





    contact = (f"+91_{contact_half}")
    print('--------------------------------------------------------------------------------------------------')

    print("\n\nPlease Enter Student Class\nFrom Nur to 12\n\n")

    while True:
        class_half = input (':--')


        if (class_half == 'nur'):
            stu_class = 'NUR'
            break

        elif (class_half == 'lkg'):
            stu_class = 'LKG'
            break

        elif (class_half == 'ukg'):
            stu_class = 'UKG'
            break

        elif (class_half == '1'):
            stu_class = 'I'
            break

        elif (class_half == '2'):
            stu_class = 'II'
            break

        elif (class_half == '3'):
            stu_class = 'III'
            break

        elif (class_half == '4'):
            stu_class = 'IV'
            break

        elif (class_half == '5'):
            stu_class = 'V'
            break

        elif (class_half == '6'):
            stu_class = 'VI'
            break

        elif (class_half == '7'):
            stu_class = 'VII'
            break

        elif (class_half == '8'):
            stu_class = 'VIII'
            break

        elif (class_half == '9'):
            stu_class = 'IX'
            break

        elif (class_half == '10'):
            stu_class = 'X'
            break

        elif (class_half == '11'):
            stu_class = 'XI'
            break

        elif (class_half == '12'):
            stu_class = 'XII'
            break
            
        else:
            print("Please Enter A Valid Class")
            continue


    print('--------------------------------------------------------------------------------------------------')
    sec_list =['A','B','C','D','E']

    print('\n\nPlease Enter Student Section\n\n')

    while True:
        stu_sec = input(':--').upper()
        if stu_sec in sec_list:
            break
        
        else:
            print('\n\nPlease Enter A Valid Section\n\n')
    print('--------------------------------------------------------------------------------------------------')
            
    print("\nPlease Enter Student House\nG,0 For \nY,1 For  \nO,2 For \nB,3 For \n\n")

    green_list = ['g','0','G']
    yellow_list =['y','Y','1']
    orange_list =['o','O','2']
    blue_lsit   =['B','b','3']





    while True:
        stu_house_half= input(':--').lower()

        if (stu_house_half in green_list):
            stu_house ="DAYANAND"
            break
            
        elif (stu_house_half in yellow_list):
            stu_house ="HANSRAJ"
            break
            
        elif (stu_house_half in orange_list):
            stu_house ="SHRADDHANAND"
            break

        elif (stu_house_half in blue_lsit):
            stu_house ="VIVEKANANDA"
            break
            
        else:
            print("Please Enter Correct Sturent House")
            continue
            
            

    print('--------------------------------------------------------------------------------------------------')
    current_time =datetime.date.today()



    stu_name_list.append(stu_name)
    f_name_list.append(f_name) 
    d_o_b_list.append(d_o_b) 
    age_list.append(age) 
    gender2_list.append(gen2)
    contact_list.append(contact) 
    stu_class_list.append(stu_class) 
    stu_sec_list.append(stu_sec) 
    stu_house_list.append(stu_house)
    stu_admission_time.append(current_time) 



    dfdata= {
        "STU_NAME": stu_name_list,
        "F_NAME": f_name_list,
        "D.O.B": d_o_b_list,
        "AGE": age_list,
        "GENDER": gender2_list,
        "CONTACT_DETAIL": contact_list,
        "STU_CLASS": stu_class_list,
        "STU_SEC": stu_sec_list,
        "stu_house": stu_house_list,
        "ADMI_TIME": stu_admission_time} 

    tabledf = pd.DataFrame(dfdata)
    
    tabledf_plot_DATA =tabledf[['STU_NAME','AGE']]
    
    tabledf_plot = tabledf_plot_DATA.set_index('STU_NAME')
    
    
    
    
    print("\n\nDo You Want To Add More Student Info\n\n")
    ask_to_re =input(":--")
    
    


    if ask_to_re in yeslist:
        continue
    
    elif ask_to_re in nolist:
        
        print(tabledf)
        while True:
            print("\n\nDo You Want To Add This Dataframe Into Mysql\n\n")
            ask_sql =input(':--')
            if ask_sql in yeslist:
                tabledf.to_sql('new_stu_admission',e,if_exists='replace',index=False)
                print('Data Successfully Add')
                break
            elif ask_sql in nolist:
                print('OK ')
                break
            else:
                continue
    else:
        continue
            
    print('--------------------------------------------------------------------------------------------------')
    print('\n\nDo You Want To See New Admission Student\nAge Graph  ')
    while True:
        ask_for_plot = input(':--')       
        
        if ask_for_plot in yeslist:
            plot1 =tabledf_plot.plot(kind='bar')
            print(plot1)
            break
        
        elif ask_for_plot in nolist:
            break
        
        else:
            continue
    
    print('--------------------------------------------------------------------------------------------------')
    break    
    
            
            
        
    
            
print('thank you for use our progrma')   
exit=input("press enter to exit") 
                
        
            
        
            
            
            
            
    
    





