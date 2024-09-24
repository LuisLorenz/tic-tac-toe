num_list = [0,1,2,3,4,5,6,7,8]

user_input = int(input('Choose your number: '))

def get_valid_num(user_input):
    if user_input in num_list: 
        return True 
    else:
        return False 
    
print(get_valid_num(user_input)) 
# it is working ,yeah 