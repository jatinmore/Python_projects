import requests
import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


master = Tk()
master.title("Send Sms")
master.geometry("800x600")

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
#response=sendPostRequest(URL, 'WH20O7FIXDMICF6MSYPXZV03OYB15WAP', 'U2U29XAWFPNJSK9Y', 'stage', 'MOB NO', 'EMAIl', 'Hi')


"""
  Note:-
   you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
#print(response.text)



mob=Label(master,text="Mobile No:-").grid(row=1,column=0)
ms=Label(master,text="Message:-").grid(row=2,column=0)
mb=Entry(master,width=18)
mb.grid(row=1,column=1)
w=Text(master,wrap=WORD,width='20',height='10',bd=5)
scr=Scrollbar(master, orient=VERTICAL, command=w.yview)
w.grid(row=3,column=1)
scr.grid(row=3, column=2, rowspan=3, columnspan=1, sticky=NS)
btm=Button(master,text="Send",command=lambda:sendPostRequest(URL, 'WH20O7FIXDMICF6MSYPXZV03OYB15WAP', 'U2U29XAWFPNJSK9Y', 'stage', mb.get(), 'MAIL', w.get(1.0,END )))
btm.grid(row=5,column=1)

master.mainloop()

