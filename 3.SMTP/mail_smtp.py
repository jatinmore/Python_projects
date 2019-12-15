import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('SENDER ID','PASSWORD')
server.sendmail('SENDER ID','RECIEVER ID','Subject: \n\n MSG')
server.quit()
