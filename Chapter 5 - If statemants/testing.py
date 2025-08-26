age = 19
if age >= 18:
    print("You are old enough to vote!")
    registered = str(input(print("Have you registered to vote yet? (Yes/No)")))
    if registered == 'Yes' or 'No':
        if registered == 'Yes':
            print('Great! You can vote.')
        else:
            print('You need to register your self first, to vote.')
    else:
        print('Please enter a valid response, such as "Yes" or "No".')