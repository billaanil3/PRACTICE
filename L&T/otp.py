import math, random, string
digits = "0123456789"
# digits = string.digits
OTP=""
for i in range(4):
    OTP += digits[random.randint(1, 10)]
print OTP
