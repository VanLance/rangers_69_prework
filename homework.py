#question 1
#greet user
def hello_name(user_name):
    """Greeting to User"""
    print('hello_' + user_name.upper() + '!')
hello_name('dylan')

#question 2
#print odd numbers
def odd_numbers():
    for value in range(1, 201, 2):
        print(value)
odd_numbers()

#question 3
#finding max number
def max_num_list(a_list):
    """Max number in a list"""
    a_list.sort()
    print(a_list[-1])
num_list = [1, 6, 10, 2, 8]
max_num_list(num_list)

#question 4
#leap year
def is_leap_year(a_year):
    """is number a leap year"""
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
answer = is_leap_year(2024)
print(answer)

#question 5
def is_consecutive(a_list):
    x = a_list[0] - 1
    for number in a_list:
        if number == x + 1:
            number = x
            return True
            
        else:
            return False
alist = [1, 2, 3, 4, 5]
correct = is_consecutive(alist)
print(correct)    
        