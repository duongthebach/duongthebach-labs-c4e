from gmail import GMail, Message
import datetime

mail = GMail("thebachht23@gmail.com", "66dcht22707")
 
msg = Message("hom nay em bi om", to="thebach1997@gmail.com", text="vi ly do suc khoe nen em xin duoc nghi 1 hom a!")
now = datetime.datetime.now()
while True:
    if now.hour == 7:
        mail.send(msg)
        break