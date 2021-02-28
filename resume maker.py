# declare variable and accept user input
name = input('Enter your Name:')
mail = input('Enter your Email Id:')
num  = input('Enter your Contact No.:')
l    = input('Enter your Location:')
edu  = input('Enter Latest Education:')
p    = input('Enter Percentage:')
y    = input('Enter passing year:')
c    = input('Enter College:')
e    = input('Enter Latest Experience:')
org  = input('Enter Name of Company:')
# list to store multiple number of projects
pj   = []
pro  = int(input('Enter Number of projects you want to add:'))
for i in range(pro):
    pj.append(input("Enter projects:"))
# empty list to store multiple number of skills
sk   = []
s    = int(input('Enter Number of skills you want to add:'))
for i in range(s):
    sk.append(input("Enter skills:"))
a    = input('Enter your Achievements')
# empty list to store multiple number of hobbies
ho   = []
hob  = int(input('Enter Number of hobbies you want to add:'))
for i in range(hob):
    ho.append(input("Enter hobbies:"))
# empty list to store multiple number of languages known
lang = []
lan  = int(input('Enter Number of languages you know:'))
for i in range(lan):
    lang.append(input("Enter language:"))
    
# print resume format
print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\t{}'.format(name))
print('\t\t{}\t\t{}\t\t{}'.format(mail,num,l))

print('-------------------------------------------------------------------------------------------------')

print('\t\t\t\t\tEducation')
print('\t\t{}\t\t{}\t\t{}\t\t{}'.format(edu,p,y,c))

print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\tExperience')
print('\t\t\t{}\t\t{}'.format(e,org))

print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\tSkills')
for i in sk:
    print('\t\t\t\t{}'.format(i))
    
print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\tProjects')
for i in pj:
    print('\t\t\t\t{}'.format(i))
    
print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\tAchievements')
print('\t\t\t\t{}'.format(a))

print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\tHobbies')
for i in ho:
    print('\t\t\t\t{}'.format(i))

print('-------------------------------------------------------------------------------------------------')
print('\t\t\t\t\tLanguages')
for i in lang:
    print('\t\t\t\t{}'.format(i))
