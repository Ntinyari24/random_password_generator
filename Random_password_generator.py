import random
import string

# Define character pools
letters = string.ascii_letters  # a-z, A-Z
digits = string.digits          # 0-9
punctuation = "!@#$%&"        # Specific special characters


total = letters + digits + punctuation


length = 12

# Generate password
password = "".join(random.sample(total, length))

print(password)
