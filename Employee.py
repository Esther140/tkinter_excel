
import tkinter
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
import mysql.connector 
mydb = mysql.connector.connect(host="localhost",username="root",password="xter1171",database="jande")
mycursor =mydb.cursor()


# import pyodbc 
# cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=localhost;Database=Jande;Port=3306;User ID=root;Password=Xter1171')
def enter_data():
    
        Name = Employee_name_entry.get()
        Bags_made =Bags_made_spinbox.get()
        Bags_size =Bags_size_combobox.get()
        Date=Date_entry.get()
        print("Name:",Name,"Bags Made:",Bags_made,"size:",Bags_size,Date)


        sql = "INSERT INTO employee (EmployeeName,Bags_made,date,Bags_size) VALUES (%s, %s,%s,%s)"
        val = (Name,Bags_made,Date,Bags_size)
        mycursor.execute(sql, val)
        mydb.commit ()
        print ( 'Data entered successfully.' )


       




window = tkinter.Tk()

window.title('Employee Records')
frame = tkinter.Frame(window)
frame.pack()     
# frame for users info                                                                                   
user_info_frame = tkinter.LabelFrame(frame,text="Users information ")
user_info_frame.grid(row=0,column=0,padx=25,pady=30)

# #status box
# Status_name = tkinter.Label(user_info_frame,text="Status")
# Status_name.grid(row=0,column=0)
# Status_name_combobox= ttk.Combobox(user_info_frame,values=["","Mr","Mrs","Ms"])
# Status_name_combobox.grid(row=0,column=1,)

# Employee text field
Employee_name = tkinter.Label(user_info_frame,text="Name of employee")
Employee_name.grid(row=0,column=0)
Employee_name_entry=tkinter.Entry(user_info_frame)
Employee_name_entry.grid(row=0,column=1)

#Date text field 
Date = tkinter.Label(user_info_frame,text="Date")
Date.grid(row=1,column=0)
Date_entry=tkinter.Entry(user_info_frame)
Date_entry.grid(row=1,column=1)

#Bags made
Bags_made = tkinter.Label(user_info_frame,text="Amount of bags made")
Bags_made.grid(row=2,column=0)

Bags_made_spinbox=tkinter.Spinbox(user_info_frame,from_=0, to='infinity')
Bags_made_spinbox.grid(row=2,column=1)

#Bags size
Bags_size = tkinter.Label(user_info_frame,text="Bags size")
Bags_size.grid(row=3,column=0)
# size_var = tkinter.StringVar(value="Large size")
# Bags_size_checkbutton=tkinter.Checkbutton(user_info_frame,text="Small",variable=size_var,onvalue= "small size",offvalue="large")
Bags_size_combobox= ttk.Combobox(user_info_frame,values=["Large","small",])
Bags_size_combobox.grid(row=3,column=1)
# Bags_size_checkbutton=tkinter.Checkbutton(user_info_frame,text="Large")
# Bags_size_checkbutton.grid(row=3,column=2)

#button 
button =tkinter.Button(frame,text="Submit",command=enter_data,)
button.grid(row=3,column=0,sticky='news')

#common widget grid  
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)
window.mainloop()