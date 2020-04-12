from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
root = Tk()
root.title("Email Details")
Email_Sent_Number = 0
Username_Label = Label(root,text = "Email Id: ")
Username_Label.grid(row=2,column=1)
Username_Entry = ttk.Entry(root,width = 50)
Username_Entry.grid(row=2,column=2,pady=5,padx=5)
Password_Label = Label(root,text = "Password: ")
Password_Label.grid(row=3,column=1)
Password_Entry = ttk.Entry(root,width = 50,show="*")
Password_Entry.grid(row=3,column=2,padx=5)

Receiver_Email_Label = Label(root,text = "Receiver email: ")
Receiver_Email_Label.grid(row = 4,column = 1)
Receiver_Email_Entry = ttk.Entry(root,width = 50)
Receiver_Email_Entry.grid(row=4,column=2,pady=5,padx=5)


Mail_Subject_Label = Label(root,text = "Subject:")
Mail_Subject_Label.grid(row=5,column = 1)
Mail_Subject_Entry = ttk.Entry(root,width = 50)
Mail_Subject_Entry.grid(row=5,column = 2,padx=5)

scrollbar = Scrollbar(orient="horizontal")
Mail_Message_Label = Label(root,text = "Message:")
Mail_Message_Label.grid(row=6,column = 1)
Mail_Message_Entry = ttk.Entry(root,width = 50,xscrollcommand=scrollbar.set)
Mail_Message_Entry.grid(row=6,column = 2,pady=5,padx=5)
scrollbar.grid(row=6,column=4)
scrollbar.config(command=Mail_Message_Entry.xview)


def Done():
    a = messagebox.askyesno(title = "Submit",message = "Are you sure to send the email")
    if(a==True):
        Done_Yes()

def Done_Yes():
    User_Email,User_Password,Receiver_Email=Username_Entry.get(), Password_Entry.get(), Receiver_Email_Entry.get()
    message = ("Subject: {}\n\n{}".format(Mail_Subject_Entry.get(),Mail_Message_Entry.get()))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(User_Email, User_Password)
        server.sendmail(User_Email, Receiver_Email, message)
        server.quit()
        root.quit()
    except:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 25)
            server.connect("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(User_Email, User_Password)
            server.sendmail(User_Email, Receiver_Email, message)
            server.quit()
            root.quit()
        except:
            error = messagebox.showwarning(title="Error",message="""            1.There is no internet connection. 
            2.The details are incorrect.
            3.Permissions in the account are not granted.""")

Submit = ttk.Button(root,text = "Submit",command = Done)
Submit.grid(row=7,column=1,columnspan=2)
root.mainloop()