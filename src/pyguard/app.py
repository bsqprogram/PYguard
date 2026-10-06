import logger
import random
import datetime

print("-------------------------------------------------------------------------------")
print("PYguard is running")

logger.initialize_log()

octet_1 = random.randint(0, 255)
octet_2 = random.randint(0, 255)
octet_3 = random.randint(0, 255)
octet_4 = random.randint(0, 255)

ip_address = f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"

username = "admin"

log_attempts = 5

login_results = []

failed_attempts = 0


def detect_login_activity(failed_attempts):
    if failed_attempts >= 3:
        return "Suspect Log Detected!"
    else:
        return "Login activity looks normal"    



for i in range(1, log_attempts + 1):
    
    log_result = random.choice(["successful", "failed"])

    login_event = {
        "timestamp": datetime.datetime.now(),
        "attempt": i,  
        "ip": ip_address, 
        "username": username, 
        "result": log_result
    }
    
    login_results.append(login_event)

    if log_result == "successful":
        print("Login attempt:", i," | ", ip_address, " | ", "successful")
        break
    else:
        print("Login attempt:", i," | ", ip_address, " | ", "failed")
        failed_attempts += 1

    
    
result = detect_login_activity(failed_attempts)
print("failed attempts: ", failed_attempts)
print(result)
print(login_results)