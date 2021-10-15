import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#window customize
root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title('Data Managemanet v0.0.1')
root.iconbitmap('icon.ico')

# creating Label
name = ttk.Label(root, text='Your Name: ').grid(row='0',column='0', sticky=tk.W)
age = ttk.Label(root, text='Your Age: ').grid(row='1',column='0',sticky=tk.W)
email = ttk.Label(root, text='Your Email Address : ').grid(row='2', column='0',sticky=tk.W)
Phone_Number = ttk.Label(root, text='Your Contact No. :').grid(row='3', column='0',sticky=tk.W)
gender = ttk.Label(root, text='Sex: ').grid(row='4', column='0', sticky=tk.W)


#Storing Value
name_store = tk.StringVar() 
age_store = tk.StringVar() 
email_store = tk.StringVar() 
number_store = tk.StringVar() 
gender_store = tk.StringVar()
u_type = tk.StringVar()
subscribe = tk.IntVar()

#databse


#creating Text Box
name_e = ttk.Entry(root, width=30, textvariable=name_store)
name_e.grid(row='0', column='1',sticky=tk.W)
name_e.focus()
age_e = ttk.Entry(root, width=30, textvariable=age_store)
age_e.grid(row='1', column='1',sticky=tk.W)
email_e = ttk.Entry(root, width=30, textvariable=email_store)
email_e.grid(row='2', column='1',sticky=tk.W)
number_e = ttk.Entry(root, width=30, textvariable=number_store)
number_e.grid(row='3', column='1',sticky=tk.W)


#creating select box
gender_b = ttk.Combobox(root, width='27', textvariable=gender_store, state='readonly')
gender_b['values'] = ('Male','Female', 'Others' )
gender_b.current(0)
gender_b.grid(row='4' ,column='1', sticky=tk.W)

#Radio Button 
button1  =  ttk.Radiobutton(root, text='Student', value='Student', variable=u_type)
button1.grid(row='6' ,column='0') 
button2=  ttk.Radiobutton(root, text='Teacher', value='Teacher',variable=u_type)
button2.grid(row='6' ,column='1') 

#checkbox
check = ttk.Checkbutton(root, text='Check if you want to subscribe our newsletter', variable=subscribe)
check.grid(row='7' ,columnspan='3')

#printable data
def click(): 
    name = name_store.get()
    age = age_store.get()
    gender = gender_store.get()
    email = email_store.get()
    types = u_type.get()
    if subscribe.get() == 0:
        subscribed = "NO"
    else:
        subscribed = "YES"
    sub = subscribed
    non = " "
    us = (f"User: {name} Has Been Added")
    print(f"NAME : {name}\nAGE: {age}\nEMAIL: {email}\nGENDER {gender}\nUSER TYPE : {types}\nSUBSCRIBED : {sub}\n {non}\n")
    # data = ttk.Label(root, text=name).grid(row='10',column='0')
    with open('Userdata.txt', 'a')as f:
        f.write(f'NAME : {name}\nAGE: {age}\nEMAIL: {email}\nGENDER {gender}\nUSER TYPE : {types}\nSUBSCRIBED : {sub}\n {non} \n')
    messagebox.showwarning(title="Registger", message=us ,)
    

    name_e.delete(0, tk.END)
    age_e.delete(0, tk.END)
    email_e.delete(0, tk.END)
    number_e.delete(0, tk.END)


#Submit Data
send = ttk.Button(root, text='Submit', command=click).grid(row='9',column='0')
quits = ttk.Button(root, text='exit', command=root.quit).grid(row='9',column='1')

root.mainloop()
