# Groupmate: Lam Wing Huen(5520 1870), Lai Tiffany Hoi-Jun(5520 1151), Lo Yan Cho(5520 1022)

# Net Chargable Income calculation:
# Case 1: x < 7100 * 12
#         NCI = salary
# Case 2: (7100*12 <= x <= 30000 * 12)
#         NCI = salary * 0.95
# Case 3: (> 30000 * 12)
#         NCI = salary - 1500

# Progressive tax calculation:
# Case 1: NCI <=50000
# Case 2: 50000 < NCI <= 100000
# Case 3: 100000 < NCI <= 150000
# Case 4: 150000 < NCI <= 200000
# Case 5: NCI >= 200000

def calculate_nci(salary):
    if salary < 7100*12:
        nci = salary
    elif salary >=7100*12 and salary <=30000*12:
        nci = salary*0.95
    else:
        nci = salary - 1500 
    return(nci)

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

status = input("Enter '1' if you are single, '2' if you are married: ")
salary = input('Enter your salary per year: ')
if (str(status) == '2'):
    partner_salary = input("Enter your partner's salary per year: ")
else:
    partner_salary = None


nci = calculate_nci(int(salary))
p_tax = calculate_p_tax(nci)
s_tax = standard_tax(nci)

print()
print("====================================== RESULT ======================================")

if partner_salary is not None:
    partner_nci = calculate_nci(int(partner_salary))
    partner_p_tax = calculate_p_tax(partner_nci)
    partner_s_tax = standard_tax(partner_nci)

    total_seperate_tax = p_tax + partner_p_tax
    total_standard_tax = s_tax + partner_s_tax

    total_nci = nci + partner_nci
    joint_p_tax = calculate_p_tax(total_nci)
    print('Total tax to be paid if paid seperately(progressive tax): ', total_seperate_tax, '(Your tax: ', p_tax, ", your partner's tax: " ,partner_p_tax,')')
    print('Total standard tax: ', total_standard_tax)
    print('Total joint tax: ', joint_p_tax)
    if total_seperate_tax < total_standard_tax and total_seperate_tax < joint_p_tax:
        print('Recommendation: Seperate Progressive Tax')
    elif total_standard_tax <total_seperate_tax and total_standard_tax < joint_p_tax: 
        print ('Recommedation: Standard Tax')
    else:
        print ('Recommendation: Joint Assessment Tax')
else:
    print('progressive tax: ', p_tax)
    print('standard tax: ', s_tax)
    if p_tax > s_tax:
        print('Recommendation: Standard tax')
    else:
        print('Recommendation: Progressive tax')

