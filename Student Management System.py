# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:12:10 2023

@author: _NILESH_
"""

import tkinter as tk
import pymysql
import logging

root = tk.Tk()

root.title('My App')
root.geometry('1350x750+0+0')
root.config(bg='black')



# Creating Variable
sid = tk.StringVar()
name = tk.StringVar()
classs =  tk.StringVar()
stream = tk.StringVar()
gmail = tk.StringVar()
mo_no = tk.StringVar()

python = tk.IntVar()
data_science = tk.IntVar()
django = tk.IntVar()
total = tk.IntVar()
percentage = tk.StringVar()
grade = tk.StringVar()


# Creating Frame

top_frame = tk.Frame(root, bg ='red')
top_frame.place(x=5, y=5,width=1340, height=150) 

lft_frame = tk.Frame(root, bg ='red')
lft_frame.place(x=5, y=160,width=667, height=480) 

lft_frame_title = tk.Frame(lft_frame, bg ='red')
lft_frame_title.place(x=5, y=5,width=657, height=50)

lft_frame_content = tk.Frame(lft_frame, bg ='red')
lft_frame_content.place(x=5, y=60,width=657, height=415)

rt_frame = tk.Frame(root, bg ='red')
rt_frame.place(x=678, y=160,width=667, height=480) 

rt_frame_title = tk.Frame(rt_frame, bg ='red')
rt_frame_title.place(x=5, y=5,width=657, height=50)

rt_frame_content = tk.Frame(rt_frame, bg ='red')
rt_frame_content.place(x=5, y=60,width=657, height=415)


btn_frame = tk.Frame(root, bg ='red')
btn_frame.place(x=5, y=645,width=1340, height=100) 


# Creating Heading

logging.basicConfig(filename='GUI_log.log',
                    level= logging.DEBUG,
                    format= '%(asctime)s:%(levelname)s:%(message)s')


main_title = tk.Label(top_frame , text = 'Result 4.0',font=('Baskerville',35,'bold'),
                       fg='black',bg='red')
main_title.pack(pady=40)

lft_title = tk.Label(lft_frame, text = 'Student_information:- ',font=('Baskerville',20,'bold'),
                    fg='black',bg='red')
lft_title.grid(row=0,padx=5,pady=5)


lbl_sd = tk.Label(lft_frame, text = 'SID',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_sd.grid(row=1,padx=5,pady=5)

ent_sd = tk.Entry(lft_frame,textvariable=sid,font=
                    ('Baskerville',20,'bold'),fg='black',bg='red')
ent_sd.grid(row=1,column=1,padx=5,pady=5)


lbl_nm = tk.Label(lft_frame, text = 'Name',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_nm.grid(row=3,column=0,padx=5,pady=5)
ent_nm = tk.Entry(lft_frame,textvariable=name
                    ,font=('Baskerville',20,'bold'),fg='black',bg='red')
ent_nm.grid(row=3,column=1,padx=5,pady=5)


lbl_cl = tk.Label(lft_frame, text = 'Class',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_cl.grid(row=4,column=0,padx=5,pady=5)
ent_cl = tk.Entry(lft_frame,textvariable=classs
                    ,font=('Baskerville',20,'bold'),fg='black',bg='red')
ent_cl.grid(row=4,column=1,padx=5,pady=5)


lbl_sm = tk.Label(lft_frame, text = 'Stream',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_sm.grid(row=5,column=0,padx=5,pady=5)
ent_sm = tk.Entry(lft_frame,textvariable=stream
                    ,font=('Baskerville',20,'bold'),fg='black',bg='red')
ent_sm.grid(row=5,column=1,padx=5,pady=5)


lbl_gm = tk.Label(lft_frame, text = 'G-mail',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_gm.grid(row=6,column=0,padx=5,pady=5)
ent_gm = tk.Entry(lft_frame,textvariable=gmail
                    ,font=('Baskerville',20,'bold'),fg='black',bg='red')
ent_gm.grid(row=6,column=1,padx=5,pady=5)


lbl_mn = tk.Label(lft_frame, text = 'Mo_no',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_mn.grid(row=7,column=0,padx=5,pady=5)
ent_mn = tk.Entry(lft_frame,textvariable=mo_no
                    ,font=('Baskerville',20,'bold'),fg='black',bg='red')
ent_mn.grid(row=7,column=1,padx=5,pady=5)


#### Right hand



lbl_name = tk.Label(rt_frame, text = 'Marks_information:- ',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_name.grid(row=0,padx=5,pady=5)


lbl_py = tk.Label(rt_frame, text = 'Python',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_py.grid(row=1,padx=5,pady=5)
ent_py = tk.Entry(rt_frame, textvariable = python,font=('Baskerville',20,'bold'),
                    fg='black',bg='red')
ent_py.grid(row=1,column=1,padx=5,pady=5)



lbl_ds = tk.Label(rt_frame, text = 'Data_Science',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_ds.grid(row=2,column=0,padx=5,pady=5)
ent_ds = tk.Entry(rt_frame, textvariable = data_science,font=('Baskerville',20,'bold'),
                    fg='black',bg='red')
ent_ds.grid(row=2,column=1,padx=5,pady=5)


lbl_dj = tk.Label(rt_frame, text = 'Django',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_dj.grid(row=3,column=0,padx=5,pady=5)
ent_dj = tk.Entry(rt_frame, textvariable = django,font=('Baskerville',20,'bold'),
                    fg='black',bg='red')
ent_dj.grid(row=3,column=1,padx=5,pady=5)



lbl_tot = tk.Label(rt_frame, text = 'Total',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_tot.grid(row=4,column=0,padx=5,pady=5)
ent_tot = tk.Entry(rt_frame, textvariable = total,state ='disabled',font=('Baskerville',20,'bold'),
                    fg='black',bg='red')
ent_tot.grid(row=4,column=1,padx=5,pady=5)


lbl_pr = tk.Label(rt_frame, text = 'Percentage',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_pr.grid(row=5,column=0,padx=5,pady=5)
ent_pr = tk.Entry(rt_frame, textvariable = percentage,state = 'disabled',font=('Baskerville',20,'bold'),
                    fg='black',bg='red')
ent_pr.grid(row=5,column=1,padx=5,pady=5)


lbl_gr = tk.Label(rt_frame, text = 'Grade',font=('Baskerville',20,'bold'),
                       fg='black',bg='red')
lbl_gr.grid(row=6,column=0,padx=5,pady=5)
ent_gr = tk.Entry(rt_frame, textvariable = grade,state = 'disabled',
                    font=('Baskerville',20,'bold'),fg='black',bg='red')
ent_gr.grid(row=6,column=1,padx=5,pady=5)



# Craeting Function

def connect_db():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='Nilesh123',
                         database ='gui_db' )
    # print(db)
    cursor = pymysql.cursors.Cursor(db)
    return db ,cursor
    


def reset_entry():
    ent_tot['disabledbackground'] = 'white'
    ent_pr['disabledbackground'] = 'white'
    ent_gr['disabledbackground'] = 'white'


def close_window(): 
    ask = tk.messagebox.askyesno('Warning',
                                 'Do you really want to close the window?')
                                 
   
    if ask == True:
       root.destroy()  
       
# logging.warning('Close windows')      

def clr_screen():
    
    sid.set('')
    name.set('') 
    classs.set('')
    stream.set('')
    gmail.set('') 
    mo_no.set('')  

    python.set(0) 
    data_science.set(0) 
    django.set(0) 
    total.set(0) 
    percentage.set(0) 
    grade.set('')     
    
# logging.warning('Clear screen')

def calculate():
    tot = python.get() + data_science.get() + django.get()
    total.set(tot)
    
    # Calculate Percentage
    p = tot/3
    percentage.set(p)
    
    if p >= 75:
        grade.set('A')
    elif p >= 65:
        grade.srt('B')
    elif p >=45:
        grade.set('C')
    else:
        grade.set('Fail')

    
    reset_entry()
        
    # Calculate Total
    
    tot = python.get() + data_science.get() + django.get()
    total.set(tot)
    
    # Calculate Percentage
    
    p = tot/3
    percentage.set(round(p,2))
    
    if p >= 75:
        grade.set('A')
    elif p >= 60:
         grade.set('B')
    elif p >= 45:
          grade.set('C')
    else:
           grade.set('Fail')  
           ent_tot.config(disabledbackground= 'blue')
           ent_pr.config(state='disable',disabledbackground= 'orange') 
           ent_gr.config(state='disable',disabledbackground= 'orange')

# logging.warning('Calculate a Percentage')

# Save the Details

def save():
  
    calculate()
    db,cursor = connect_db()
    query = f'''
    insert into results 
    values('{sid.get()}',
           '{name.get()}',
           '{classs.get()}',
           '{stream.get()}',
           '{gmail.get()}',
           '{mo_no.get()}',
           '{python.get()}',
           '{data_science.get()}',
           '{django.get()}',
           '{total.get()}',
           '{percentage.get()}',
           '{grade.get()}')
    
    '''
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()    

# logging.warning('Save files')

def save_as():
    
      db,cursor = connect_db()
      query = f'select * from results where sid = "{sid.get()}"'
      cursor.execute(query)
      
      res = cursor.fetchone()
      
      if res != None:
          ask = tk.messagebox.askyesno('COMFORM',
                                       'DO you updated the record')
          if ask:
              query1 = f'delete from results where sid = "{sid.get()}"'
              cursor.execute(query1)
              
              db.commit()
              cursor.close()
              db.close()
              save()
              tk.messagebox.showinfo('UPDATED',
                                     'Record updated sucessfully')
          
      else:
          save()
          tk.messagebox.showinfo('SAVED',
                                      'Record Saved sucessfully')
  


def search_file():
    db,cursor = connect_db()
    query =  f'select * from results where sid = "{sid.get()}"'
    cursor.execute(query)
    
    res = cursor.fetchone()   # strore the data
    if res != None:
        name.set(res[1])
        classs.set(res[2])
        stream.set(res[3])
        gmail.set(res[4])
        mo_no.set(res[5])
        python.set(res[6])
        data_science.set(res[7])
        django.set(res[8])
        total.set(res[9])
        percentage.set(res[10])
        grade.set(res[11])
       
    else:
        tk.messagebox.showerror('WARNING',
                                'Record does not exist')
    cursor.close()
    db.close()

# logging.info('search a file')

def delete_file():
    db,cursor = connect_db()
    query = f'select * from results where sid = "{sid.get()}"'
    cursor.execute(query)
    
    res = cursor.fetchone()
    
    if res != None:
        ask = tk.messagebox.askyesno('CONFORM',
                                     'Do you delete the record')
        if ask:
            query1 = f'delete from results where sid = "{sid.get()}"'
            cursor.execute(query1)
            tk.messagebox.showinfo('SUCCESS',
                                   'Record delete sucessfully')
        
            
            db.commit()
            cursor.close()
            db.close()
            save()
           
    else:
        tk.messagebox.showinfo('WARNING',
                               'Record does not exist')
    
        
# logging.warning(f's:%{sid.set},s:%{name.set}Delete file')
        

# Creating Button

search = tk.Button(btn_frame,text='Search',font=('chalkduster',15,'bold'),
                  bg='green',fg='white',height=60, command= search_file)   #<== Function call
search.pack(padx=10,pady=25,side='left')

delete_btn = tk.Button(btn_frame,text='Delete',font=('chalkduster',15,'bold'),
                  bg='green',fg='white',height=60, command= delete_file)   #<== Function call
delete_btn.pack(padx=10,pady=25,side='left')


close = tk.Button(btn_frame,text='Quit',font=('chalkduster',15,'bold'),
                  bg='green',fg='white',height=60, command= close_window)   #<== Function call
close.pack(padx=10,pady=25,side='right')


cal = tk.Button(btn_frame,text='Calculate',font=('chalkduster',15,'bold'),
                  bg='green',fg='white',height=60, command= calculate)   #<== Function call
cal.pack(padx=10,pady=25,side='right')



clear = tk.Button(btn_frame,text='Reset',font=('chalkduster',15,'bold'),
                  bg='green',fg='white',height=40,command=clr_screen)
clear.pack(padx=10,pady=25,side='right')


save_btn = tk.Button(btn_frame,text='SAVE',font=('chalkduster',15,'bold'),
                  bg='green',fg='white',height=40,command=save_as)
save_btn.pack(padx=10,pady=25,side='right')



root.mainloop()







