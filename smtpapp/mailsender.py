import smtplib as s
from django.http import HttpResponse



def sendmail_view(request):
    ob = s.SMTP("SMTP.GMAIL.COM", 587)

    ob.starttls()

    ob.login("kwindominds@gmail.com", "Kwindominds1995@")

    subject = 'sending email using python'
    body = 'this is code of sending email using script '

    message = "subject:{}/n/n{}".format(subject, body)
    listOfAddress = ["kwindominds@gmail.com", "kuldeepwadhwa1995@gmail.com"]

    ob.sendmail('kwindominds@gmail.com', listOfAddress, message)
    print("send sucessfully")
    ob.quit()
    return HttpResponse('SEND SUCESSFULLY')

