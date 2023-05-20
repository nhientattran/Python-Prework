# Question 1:
def hello_name(user_name):
    print("\nHello, " + user_name.title() + "! Have a great day!")

# Question 2:
def first_odd():
    number = 0
    while number < 100:
        number += 1
        if number % 2 == 0:
            continue    
        print(number)

# Question 3:
def max_num_in_list(a_list):
        output = max(a_list)
        print("\nMaximum number in a list is " + str(output) + ".")

# Question 4:
def is_leap_year(a_year):
     if a_year % 4 == 0:
          if a_year % 100 == 0:
               if a_year % 400 == 0:
                    return True
               else:
                    return False
          else:
               return True
     else:
          return False

# Question 5:
def is_consecutive(a_list):
     b_list = list(range((a_list[0]),(a_list[-1]),1))
     b_list.append(a_list[-1])
     if a_list == b_list:
          return True
     else:
          return False

     
