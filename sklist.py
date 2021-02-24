'''
    This is program to genrate a effactive world list
'''
import pandas as pd
import random as rd

victim_name = input('Victim Name: ')
victim_surname = input('Victim Surname: ')
victim_nick_name = input('Victim Nick name: ')
victim_DOB1 = int(input('Victim DOB(DDMMYY): '))
victim_DOB = str(victim_DOB1)

partner_name = input('Partner name: ')
partner_surname = input('Partner surname: ')
partner_nick_name = input('Partner Nick name: ')
partner_DOB1 = int(input('Partner DOB(DDMMYY)'))
partner_DOB = str(partner_DOB1)

special_character = input('Do You Want to add Special characcters(Y/N) : ')
random_number = input('Do you want to add random number add the end(Y/N): ')

lst = [victim_name, victim_surname, victim_nick_name, victim_DOB, partner_name, partner_surname, partner_nick_name, partner_DOB]
len_of_lst = len(lst)
lenoflst = len(lst)
lst2 = []
for i in range(len_of_lst):
    for y in range(len_of_lst):
        if i == y:
            pass
        else:
            lst1 = str(lst[i]) + str(lst[y])
            lst2.append(lst2)

new_list = lst + lst2

len_of_lst = len(new_list)
if random_number == 'y' or random_number == 'Y':
    lst3 = []
    for y in range(100):
        nu = str(rd.randint(0, 100))
        for i in range(len_of_lst):
            lst3.append(str(new_list[i]) + str(nu))
    new_list = lst + lst2 + lst3
if special_character == 'y' or special_character == 'Y':
    s_c = ['@', '#', '$', '%', '&', '*']
    len1 = len(s_c)
    slst = []
    for i in s_c:
        for z in range(len1):
            for y in range(len1):
                slst.append(str(s_c[y] + str(s_c[z])))

    slst1 = []
    for i in s_c:
        for z in range(len1):
            for y in range(len1):
                for x in range(len1):
                    slst1.append(str(s_c[z]) + str(s_c[y]) + str(s_c[x]))

    slst2 = []
    for i in s_c:
        for z in range(len1):
            for y in range(len1):
                for x in range(len1):
                    for a in range(len1):
                        slst1.append(str(s_c[z]) + str(s_c[y]) + str(s_c[x]) + str(s_c[a]))

    s_list =s_c +slst +slst1 + slst2
    len_of_lst1 = len(s_list)
    len_of_lst = len(new_list)
    slst3 = []
    for j in range(len_of_lst):
        for i in range(len_of_lst1):
            slst3.append(str(new_list[j]) + str(s_list[i]))

    slst4 = []
    for j in range(len_of_lst):
        for i in range(len_of_lst1):
            slst3.append(str(s_list[j]) + str(new_list[len_of_lst]))
    slst5 = []
    for i in range(lenoflst):
        for y in range(lenoflst):
            for m in range(len_of_lst1):
                if i == y:
                    pass
                else:
                    lst1 = str(lst[i]) + str(s_list[m]) + str(lst[y])
                    lst2.append(slst5)

    new_list = lst + lst2 + lst3 + slst3 + slst4 + slst5
sr = pd.Series(new_list)
sr.to_csv(fr'E:\\IP Project\\Python World List\\{victim_name}.csv', index=None, header= False)

print('Good to go !!')