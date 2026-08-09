# Build an online exam access checker

# take inputs from the user
import subprocess
registered = input("Is registered? (Yes/No): ")
fee_paid = input("Is fee paid? (Yes/No): ")
identity_verified = input("Is identity verified? (Yes/No): ")
system_check = input("Is system check passed? (Pass/Fail): ")

# Check whether the student can access the online exam 
if registered == "No" or registered == "no" :
    print("Access Denied: Registration Incomplete") 
elif fee_paid == "No" or fee_paid == "no":
    print("Access Denied: Fee Payment Pending") 

elif identity_verified == "No" or identity_verified == "no":
    print("Access Denied: Identity Verification Pending") 
elif system_check == "Fail" or system_check == "fail":
    print("Access Denied: System Check Failed") 
else:
    print("Access Granted")