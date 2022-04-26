from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x700")
root.resizable(False,False)

#databases



#create a database or connect to one

conn = sqlite3.connect('sample.db')

#create a cursor

c = conn.cursor()

#Create Table
'''
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''
#create Submit Function For Database

def submit():

    #create a database or connect to one

    conn = sqlite3.connect('sample.db')

    #create a cursor
    c = conn.cursor()

    #Insert Into Table 
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get(),
                
                })


    #commit changes
    conn.commit()

    #close connection
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Query Function 

def query():
    #create a database or connect to one

    conn = sqlite3.connect('sample.db')

    #create a cursor
    c = conn.cursor()

    # Query the database
    #oid is the primary key or unique id for each record
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

        query_label = Label(root,text=print_records)
        query_label.grid(row=12,column=0,columnspan=2)

    #commit changes
    conn.commit()

    #close connection       
    conn.close()

#Delete record function

def delete():
     #create a database or connect to one

    conn = sqlite3.connect('sample.db')

    #create a cursor
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + select_box.get())

    select_box.delete(0, END)

    #commit changes
    conn.commit()

    #close connection       
    conn.close()

#update record 

def update():
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global select_box
    #create a database or connect to one

    conn = sqlite3.connect('sample.db')

    #create a cursor
    c = conn.cursor()

    record_var = select_box.get()

    c.execute("""UPDATE addresses SET 
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",
            {
                'first': f_name_editor.get(),
                'last': l_name_editor.get(),
                'address': address_editor.get(),
                'city':city_editor.get(),
                'state':state_editor.get(),
                'zipcode':zipcode_editor.get(),
                'oid': record_var
            })
                
                
    #commit changes
    conn.commit()

    #close connection       
    conn.close()


    

# Edit Record

def edit():
    global notif

    record_var = select_box.get()
    if record_var == '':
        messagebox.showerror("Error","Please Enter valid ID")
        #notif.config(fg="red",text = "Please Enter valid ID")
    else:
        

        editor = Tk()
        editor.title("Editor")
        editor.geometry("400x400")
        #editor.resizable(False,False)


        #create a database or connect to one

        conn = sqlite3.connect('sample.db')

        #create a cursor
        c = conn.cursor()

        #Insert Into Table 
        c.execute("SELECT * FROM addresses WHERE oid = " + record_var)
        records = c.fetchall()

        #declare global variables

        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor


        #Create Text Boxes
        
        f_name_editor = Entry(editor,width=30)
        f_name_editor.grid(row=0, column=1,padx=20,pady=(10,0))

        l_name_editor = Entry(editor,width=30)
        l_name_editor.grid(row=1, column=1,padx=20)

        address_editor= Entry(editor,width=30)
        address_editor.grid(row=2, column=1,padx=20)

        city_editor= Entry(editor,width=30)
        city_editor.grid(row=3, column=1,padx=20)

        state_editor = Entry(editor,width=30)
        state_editor.grid(row=4, column=1,padx=20)

        zipcode_editor =Entry(editor,width=30)
        zipcode_editor.grid(row=5, column=1,padx=20)


        #Create Text Box lables

        f_name_label = Label(editor,text="First Name")
        f_name_label.grid(row=0, column=0,pady=(10,0))

        l_name_label = Label(editor,text="Last Name")
        l_name_label.grid(row=1,column=0)

        address_label = Label(editor, text="Address")
        address_label.grid(row=2,column=0)

        city_label = Label(editor, text="City")
        city_label.grid(row=3,column=0)

        state_label = Label(editor, text="State")
        state_label.grid(row=4,column=0)

        zip_label = Label(editor, text="Zipcode")
        zip_label.grid(row=5,column=0)

        #loop the results
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        #save button
        
        edit_btn = Button(editor, text="Save Record", command = update)
        edit_btn.grid(row=6,column=0, columnspan=2,pady=10,padx=10,ipadx=137)


#Create Text Boxes
global select_box

    
f_name = Entry(root,width=30)
f_name.grid(row=0, column=1,padx=20,pady=(10,0))

l_name = Entry(root,width=30)
l_name.grid(row=1, column=1,padx=20)

address= Entry(root,width=30)
address.grid(row=2, column=1,padx=20)

city = Entry(root,width=30)
city.grid(row=3, column=1,padx=20)

state = Entry(root,width=30)
state.grid(row=4, column=1,padx=20)

zipcode =Entry(root,width=30)
zipcode.grid(row=5, column=1,padx=20)

select_box = Entry(root,width=30)
select_box.grid(row=8, column=1,padx=10)


#Create Text Box lables

f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0, column=0,pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1,column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2,column=0)

city_label = Label(root, text="City")
city_label.grid(row=3,column=0)

state_label = Label(root, text="State")
state_label.grid(row=4,column=0)

zip_label = Label(root, text="Zipcode")
zip_label.grid(row=5,column=0)

select_label = Label(root, text="Select Id")
select_label.grid(row=8,column=0)

notif = Label(root, font=('calibri,12'))
notif.place(x = 130, y= 400)



#Create Submit Button

submit_btn = Button(root, text="Add Record To Database", command = submit)
submit_btn.grid(row=6,column=0, columnspan=2,pady=10,padx=10,ipadx=100)

#Create Query Button

Query_btn = Button(root, text="Show Records", command = query)
Query_btn.grid(row=7,column=0, columnspan=2,pady=10,padx=10,ipadx=137)


#Delete Button

delete_btn = Button(root, text="Delete Records", command = delete)
delete_btn.grid(row=10,column=0, columnspan=2,pady=10,padx=10,ipadx=110)

#Edit Record Button

Edit_btn = Button(root, text="Edit Record", command = edit)
Edit_btn.grid(row=11,column=0, columnspan=2,pady=10,padx=10,ipadx=100)




#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()
