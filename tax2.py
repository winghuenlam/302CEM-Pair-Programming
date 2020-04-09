# Groupmate: Lam Wing Huen(5520 1870), Lai Tiffany Hoi-Jun(5520 1151), Lo Yan Cho(5520 1022)

# Net Chargable Income calculation:
# Case 1: (x <= 30000 * 12)
#         NCI = salary * 0.95
# Case 2: (> 30000 * 12)
#         NCI = salary - 1500

# Progressive tax calculation:
# Case 1: NCI <=50000
# Case 2: 50000 < NCI <= 100000
# Case 3: 100000 < NCI <= 150000
# Case 4: 150000 < NCI <= 200000
# Case 5: NCI >= 200000

basic_allowance = 132000

def calculate_nci(salary):
    if salary <=30000*12 and salary >= 7100*12:
        mpf = salary*0.05
    elif salary < 7100*12:
        mpf = 0
    else:
        mpf = 1500*12
    nci = salary - mpf
    return(nci, mpf)

def standard_tax(nci):
    tax = nci*0.15
    return(tax)

def calculate_p_tax(nci):
    if nci <= 50000: 
        p_tax = nci*0.02
    elif nci >50000 and nci <=100000:
        p_tax = (nci-50000)*0.06 + 50000*0.02
    elif nci >100000 and nci <= 150000:
        p_tax = (nci -50000*2)*0.1 + 50000*(0.02+0.06)
    elif nci >150000 and nci <=200000:
        p_tax = (nci -50000*3)*0.14 + 50000*(0.02+0.06+0.10)
    else:
        p_tax = (nci - 50000*4)*0.17 + 50000*(0.02+0.06+0.10+0.14)
    return(p_tax)

def tax_calculation():
    status_pass = False
    salary_pass = False
    while status_pass == False:
        status = input("Enter '1' if you are single, '2' if you are married: ")
        if status=='1' or status=='2':
            status_pass = True
    status_text = 'single' if status=='1' else 'married'

    while salary_pass == False:
        try:
            salary = int(input('Enter your salary per year: '))
            if (status == '2'):
                partner_salary = int(input("Enter your partner's salary per year: "))
            else:
                partner_salary = None
            salary_pass = True
        except ValueError:
            print('Please enter a valid salary.')


    nci1, mpf = calculate_nci(salary)
    nci = nci1 - basic_allowance if nci1 > basic_allowance else 0

    p_tax = calculate_p_tax(nci)
    s_tax = standard_tax(nci1)

    values={
        'mpf': [mpf],
        'nci': [nci],
        'individual_tax': p_tax,
        'standard_tax': s_tax,
        'recommend': ''
    }

    print()
    print("====================================== RESULT (",status_text,") ======================================")

    if partner_salary is not None:
        partner_nci1, parnter_mpf = calculate_nci(partner_salary)
        partner_nci = partner_nci1 - basic_allowance if partner_nci1 > basic_allowance else 0

        partner_p_tax = calculate_p_tax(partner_nci)
        partner_s_tax = standard_tax(partner_nci1)

        total_seperate_tax = p_tax + partner_p_tax
        total_standard_tax = s_tax + partner_s_tax

        total_nci = nci1 + partner_nci1 - basic_allowance*2 if nci1 + partner_nci1 >= basic_allowance*2 else 0
        joint_p_tax = calculate_p_tax(total_nci)

        stand_pro_total_a = s_tax + partner_p_tax
        stand_pro_total_b = partner_s_tax + p_tax

        values['mpf'].append(parnter_mpf)
        values['nci'].append(partner_nci)
        values['individual_tax'] = total_seperate_tax
        values['standard_tax'] = total_standard_tax
        values['joint_tax'] = joint_p_tax

        print('Your MPF: ', mpf, ", your parnter's MPF: ", parnter_mpf)
        print('Your Net Chargable Income: ', nci, ", your parnter's Net Chargable Income: ", partner_nci)
        print('Total seperate tax(progressive tax): ', total_seperate_tax, '(Your tax: ', p_tax, ", your partner's tax: " ,partner_p_tax,')')
        if min([stand_pro_total_a,stand_pro_total_b])==stand_pro_total_a:
            print('Total seperate tax(standard + progressive tax): ', stand_pro_total_a, '(Your standard tax: ', s_tax, ", your partner's progressive tax: " ,partner_p_tax,')')
        else:
            print('Total seperate tax(progressive + standard tax): ', stand_pro_total_b, '(Your progressive tax: ', p_tax, ", your partner's standard tax: " ,partner_s_tax,')')

        print('Total standard tax: ', total_standard_tax)
        print('Total joint tax: ', joint_p_tax)
        compare_list = [total_seperate_tax, total_standard_tax, joint_p_tax, stand_pro_total_a, stand_pro_total_b]

        if min(compare_list) == total_seperate_tax:
            values['recommend'] = 'seperate'
            print('Recommendation: Seperate Progressive Tax')
        elif min(compare_list) == total_seperate_tax:
            values['recommend'] = 'standard'
            print ('Recommedation: Standard Tax')
        elif min(compare_list) == joint_p_tax:
            values['recommend'] = 'joint'
            print ('Recommendation: Joint Assessment Tax')
        else:
            values['recommend'] = 'standard and progressive tax'
            print ('Recommendation: Standard and Progressive tax')
    else:
        print('Your MPF: ', mpf)
        print('Your Net Chargable Income: ', nci)
        print('progressive tax: ', p_tax)
        print('standard tax: ', s_tax)
        if p_tax > s_tax:
            values['recommend'] = 'standard'
            print('Recommendation: Standard tax')
        else:
            values['recommend'] = 'seperate'
            print('Recommendation: Progressive tax')

    return(values)

if __name__ == "__main__":
    tax_calculation()