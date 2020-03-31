import string 
import random

def random_password(): #Function to generate random text as password
	random_passcode = first_name[0:2] + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + last_name[-2:]
	return random_passcode
	
def password_check(real_passcode): #Check if password length is lesser than 7
		if len(real_passcode) < 7:
			print('Password length should be equal to or greater than 7.')
			real_passcode = input('Enter password: ')
			password_check(real_passcode)
		return real_passcode
		
		
def password(): #Password function
	real_password = random_password()
	response = input(f'Password is {real_password}.\n Are you satisfied with it? Enter "Yes" to continue and "No" to change: ')
	if response.lower() == "yes":
		print(f'User details: \n\tFirst Name: {first_name}\n\t Last Name {last_name}\n\t Email: {email}\n\t Password: {real_password} ')
		return real_password
	elif response.lower() == 'no':
		real_password = input('Enter password: ')
		return password_check(real_password)
	else:
		password()

def save_details(fname, lname, mail, pword): #Save details to a dictionary
	user_info = {}			
	user_info['First Name'] = fname
	user_info['Last Name'] = lname
	user_info['Email'] = mail
	user_info['Password'] = pword
	user_data.append(user_info)
	
def is_user(): #Check if there is any user available
	any_user = input('Are there any user? Enter "Yes" or "No": ')
	if any_user.lower() == 'yes':
		user()
	elif any_user.lower() == 'no':
		pass
	else:
		is_user()
			
def user(): #Inout first name, last name, email, etc
	global first_name, last_name, email, user_password
	first_name = input('Enter first name: ')
	last_name = input('Enter last name: ')
	email = input('Enter email address: ')
	user_password = password()
	
	save_details(first_name, last_name, email, user_password)
	is_user()
	
def user_details(): 
	global user_data
	user_data = []#Empty list to store each user dictionary
	user()
	for i in user_data: #Loop through list and display info
		print('Details for user :')
		print('\t First Name: ', i['First Name'])
		print('\t Last Name: ', i['Last Name'])
		print('\t Email: ', i['Email'])
		print('\t Pasword: ', i['Password'])

user_details()
