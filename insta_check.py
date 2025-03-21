import time
import instaloader

# Instaloader object with a user-agent
Insta = instaloader.Instaloader()

# Login session
username = input("Enter your username: ")
password = input("Enter your password: ")

# Login to Instagram account
# Consider how to handle user credentials here
# Also think about Instagram's two-factor authentication
try:
    Insta.load_session_from_file(username)
    print("Session loaded successfully")
except:
    print("No session found, attempting login...")
    try:
        time.sleep(3)
        Insta.login(username, password)
    except instaloader.exceptions.BadCredentialsException as e:
        print(f"Log in failed: Bad credentials - {e}")
    except instaloader.exceptions.TwoFactorAuthRequiredException as e:
        print(f"2FA required: {e}")
        two_factor_code = input("Enter 2FA code: ")
        Insta.two_factor_login(username, password, two_factor_code)
    except Exception as e:
        print(f"Log in failed: Unknown error - {e}")
    else:
        print(f"Logged in as {Insta.context.username}")
        Insta.save_session_to_file()  # Save session for next time

# fetch following list

# fetch followers list

# Compare the two lists to find non-followers

# display results