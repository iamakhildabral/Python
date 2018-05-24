

import smtplib
from email.mime.text import MIMEText
file_obj = open("NEWS.txt",'rb')
msg = MIMEText(file_obj.read())
file_obj.close()

msg['Subject'] =  'The contents of NEWS.tx'
msg['From'] = akhildabral02@gmail.com
msg['To'] = akhildabral02@gmail.com

s = smtplib.SMTP('smtp.gmail.com')
s.sendmail(akhildabral02@gmail.com,[akhildabral02@gmail.com],msg.as_string())
s.quit()



