'''
Now a long with subject we will also add attachment
'''

import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#now add attachment
from email.mime.base import MIMEBase#to addup our attachment
from email import encoders
import os
#now let us add attachmemt
attach = "myqr.png"#attachment name
msg = MIMEMultipart()

#now add from,to,subject
From = "ramanakomati52@gmail.com"
To = "ramanakomati88@gmail.com"
subject = "Email Automation project using python"
msg['From'] = From
msg['To'] = To
msg['Subject'] = subject
body = "Prepare well and make sure to present well"
#we will be using MIMEBase and Encoders to use the attachment
msg.attach(MIMEText(body))
part = MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
#Now we will use Encoders to encode the file
encoders.encode_base64(part)
#now to add the header the file
part.add_header('Content-Disposition',
                'attachment ;filename="%s" '%(os.path.basename(attach)))
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,"gcgp nrtd trfb byvr")
server.sendmail(From,To,text)
server.quit()
print("Mal sent..")


