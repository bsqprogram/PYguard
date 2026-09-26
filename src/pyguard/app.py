import logger
import random

print("PYguard is running")

logger.initialize_log()

octet_1 = random.randint(0, 255)
octet_2 = random.randint(0, 255)
octet_3 = random.randint(0, 255)
octet_4 = random.randint(0, 255)

ip_address = f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"

username = "admin"

log_attempts = 3


def log_info(ip, user, attempts):
    print(ip, user, attempts)
    


def detect_login_activity(attempts, ip):
    if attempts >= 5:
        return "Suspect Log Detected!"
    elif attempts >= 3 and ip != "192.168.1.1":
        return "Suspect Log Detected!"
    elif attempts == 3 or attempts == 4:
        return "Unusual log activity"
    else:
        return "Login activity looks normal"
    
        
result = detect_login_activity(log_attempts, ip_address)


print(result)


print(ip_address)