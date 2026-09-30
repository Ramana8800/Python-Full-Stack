
'''
import smtplib
#first we need to connect to gmail server
server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
#starting the connection
server.starttls()
server.login('ramanakomati52@gmail.com','gcgp nrtd trfb byvr')#give your app pwd
#give your desired message
message = "Hello I have created email automation..."
server.sendmail("ramanakomati52@gmail.com","ramanakomati88@gmail.com",message)
server.quit()
print("Mail Sent...")

import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
while True:
    msg = MIMEMultipart()
    print(msg)
    #now add from,to,subject
    From = "ramanakomati52@gmail.com"
    To = "ramanakomati88@gmail.com"
    subject = "Email Automation project using python"
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = subject
    body = "Prepare well and make sure to present well"

    otp = random.randint(1000, 9999)

    print("Your OTP is:", otp)

    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("OTP is correct.")
    else:
        print("Invalid OTP.")
        
    msg.attach(MIMEText(body))
    #finally we will convert above as string
    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)
    #starting the connection
    server.starttls()
    server.login('ramanakomati52@gmail.com','gcgp nrtd trfb byvr')#give your app pwd
    server.sendmail(From,To,text)
    server.quit()
    print("Mail Sent...")
'''

import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math,random
#as we want will generate a random number
digits = "0123456789"
OTP =""
#now we will create OTP using math and random
for i in range(4):
    OTP +=digits[math.floor(random.random()*10)]
    print(OTP)
#print(OTP)
body = f'Your OTP is {OTP}'

From = "ramanakomati52@gmail.com"
To = "ramanakomati88@gmail.com"
subject = "You have received an order"
msg['From'] = From
msg['To'] = To
msg['Subject'] = subject
        
msg.attach(MIMEText(body))
#finally we will convert above as string
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
#starting the connection
server.starttls()
server.login('ramanakomati52@gmail.com','gcgp nrtd trfb byvr')#give your app pwd
server.sendmail(From,To,text)
user = input("Enter the OTP")
if user == OTP:
    print("Authorization Successs")
else:
    print("Check the OTP again")
























