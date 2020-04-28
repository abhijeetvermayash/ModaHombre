import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql
class windowone:
    def __init__(self, root):
        self.root=root
        self.root.title("MODA HOMBRE")
        self.root.geometry("500x500+0+0")

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Manage_Frame.place(x=0,y=0,width=500,height=560)


        button_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="white")
        button_Frame.place(x=0,y=50,width=250)

        shirtsbtn=Button(button_Frame,text='SHIRTS_STOCK',width=15,command=self.loadwindowtwo).grid(row=0,column=0,padx=10,pady=10)
        salesbtn=Button(button_Frame,text='SALES',width=10,command=self.loadwindowsales).grid(row=1,column=0,padx=10,pady=10)
      

    def loadwindowtwo(self):
        self.newwindow=tk.Toplevel(self.root)
        self.newwindow.geometry("1500x750+0+0")
        self.app=windowtwo(self.newwindow)

    def loadwindowsales(self):
        self.newwindow1=tk.Toplevel(self.root)
        self.newwindow1.geometry("1500x750+0+0")
        self.app=windowsales(self.newwindow1)

    def loadwindowreturn(self):
        self.newwindow2=tk.Toplevel(self.root)
        self.newwindow2.geometry("1500x750+0+0")
        self.app=windowreturn(self.newwindow2)


class windowtwo:
    def __init__(self, root):
        self.root=root
        self.root.title("MODA HOMBRE SHIRT STOCK")


     #========================manageframeofshirts===================================#
        Manage_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Manage_Frame1.place(x=0,y=100,width=500,height=580)

        self.shirt_id_var=StringVar()
        self.size_var=StringVar()
        self.colour_var=StringVar()
        self.type_var=StringVar()
        self.gender_var=StringVar()
        self.mrp_var=StringVar()
        self.sp_var=StringVar()
        self.search_text=StringVar()
        self.search_by=StringVar()
        


    


        lbl_id=Label(Manage_Frame1,text="Shirt_id",font=("comic sans",20,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        textid=Entry(Manage_Frame1,textvariable=self.shirt_id_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textid.grid(row=1,column=1,pady=10,padx=10)

        

        lbl_size=Label(Manage_Frame1,text="SIZE",font=("comic sans",20,"bold"))
        lbl_size.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        textsize=Entry(Manage_Frame1,textvariable=self.size_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textsize.grid(row=2,column=1,pady=10,padx=10)

        lbl_color=Label(Manage_Frame1,text="COLOUR",font=("comic sans",20,"bold"))
        lbl_color.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        textcolor=Entry(Manage_Frame1,textvariable=self.colour_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textcolor.grid(row=3,column=1,pady=10,padx=10)

        lbl_type=Label(Manage_Frame1,text="TYPE",font=("comic sans",20,"bold"))
        lbl_type.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        texttype=Entry(Manage_Frame1,textvariable=self.type_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        texttype.grid(row=4,column=1,pady=10,padx=10)

        
        lbl_gender=Label(Manage_Frame1,text="GENDER",font=("comic sans",20,"bold"))
        lbl_gender.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame1,textvariable=self.gender_var,state='readonly',font=(25))
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=5,column=1,pady=10,padx=20)


        lbl_mrp=Label(Manage_Frame1,text="MRP",font=("comic sans",20,"bold"))
        lbl_mrp.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        textmrp=Entry(Manage_Frame1,textvariable=self.mrp_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textmrp.grid(row=6,column=1,pady=10,padx=10)

        lbl_sp=Label(Manage_Frame1,text="SP",font=("comic sans",20,"bold"))
        lbl_sp.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        textsp=Entry(Manage_Frame1,textvariable=self.sp_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textsp.grid(row=7,column=1,pady=10,padx=10)

        #======================buttonframeofshirts===========================================#

        
        button_Frame1=Frame(Manage_Frame1,bd=4,relief=RIDGE,bg="white")
        button_Frame1.place(x=10,y=500,width=450)

        Addbtn=Button(button_Frame1,text='ADD',width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Delbtn=Button(button_Frame1,text='DEL',width=10,command=self.del_row).grid(row=0,column=1,padx=10,pady=10)
        updatebtn=Button(button_Frame1,text='UPDATE',width=10,command=self.update_data).grid(row=0,column=2,padx=10,pady=10)
        Clrbtn=Button(button_Frame1,text='CLEAR',width=10,command=self.clear_fun).grid(row=0,column=3,padx=10,pady=10)


         #=========detail_frameofshirts=======================#

        Detail_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Detail_Frame1.place(x=550,y=100,width=750,height=560)

        
        lbl_search=Label(Detail_Frame1,text="Search",font=("comic sans",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame1,textvariable=self.search_by,width=10,state='readonly',font=(10))
        combo_search['values']=("shirt_id","size","colour","gender","mrp")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        textsearch=Entry(Detail_Frame1,textvariable=self.search_text,font=("comic sans",10,"bold"),bd=5,relief=GROOVE)
        textsearch.grid(row=0,column=2,pady=10,padx=10)

        searchbtn=Button(Detail_Frame1,text='SEARCH',width=10,command=self.fetch_some).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame1,text='SHOW ALL',width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        #==============table_frameofshirts=============================#

        table_Frame1=Frame(Detail_Frame1,bd=4,relief=RIDGE,bg="white")
        table_Frame1.place(x=0,y=100,width=740,height=450)

        scroll_x=Scrollbar(table_Frame1,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame1,orient=VERTICAL)

        self.shirt_table=ttk.Treeview(table_Frame1,column=("shirt_id","size","colour","type","gender","mrp","sp"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.shirt_table.xview)
        scroll_y.config(command=self.shirt_table.yview)
        
        self.shirt_table.heading("shirt_id",text="shirt_id")
        self.shirt_table.heading("size",text="size")
        self.shirt_table.heading("colour",text="colour")
        self.shirt_table.heading("type",text="type")
        self.shirt_table.heading("gender",text="gender")
        self.shirt_table.heading("mrp",text="mrp")
        self.shirt_table.heading("sp",text="sp")
        self.shirt_table['show']='headings'
        self.shirt_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


        
       

    def add_students(self):
            com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
            cur=com.cursor()
            try:
                cur.execute("insert into shirt values(%s,%s,%s,%s,%s,%s,%s)",(self.shirt_id_var.get(),
                                                                              self.size_var.get(),
                                                                              self.colour_var.get(),
                                                                              self.type_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.mrp_var.get(),
                                                                              self.sp_var.get()
                                                                              ))
                print("ok")
            except Exception as e:
                print("Exception: ",e)
       
            com.commit()
            self.fetch_data()
            self.clear_fun()
            com.close()

    def fetch_data(self):
         com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
         cur=com.cursor()
         try:
             cur.execute("select * from shirt")
             rows=cur.fetchall()
             if (rows!=0):
                 self.shirt_table.delete(*self.shirt_table.get_children())
                 for row in rows:
                     self.shirt_table.insert('',END,values=row)
                 com.commit()
             print("ok")
         except Exception as e:
            print("Exception: ",e)
         self.clear_fun()
         com.close()

    
    def clear_fun(self):
        self.shirt_id_var.set("")
        self.size_var.set("")
        self.colour_var.set("")
        self.gender_var.set("")
        self.type_var.set("")
        self.mrp_var.set("")
        self.sp_var.set("")
        self.search_by.set("")
        self.search_text.set("")
        print("okayyy")

    def del_row(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
        cur=com.cursor()
        try:
            cur.execute("delete from shirt where shirt_id=%s",self.shirt_id_var.get())
            print("ok")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        self.fetch_data()
        self.clear_fun()
        com.close()

    def update_data(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
        cur=com.cursor()
        try:
            cur.execute("update shirt set size=%s,colour=%s,type=%s,gender=%s,mrp=%s,sp=%s where shirt_id=%s",(self.size_var.get(),
                                                                                                             self.colour_var.get(),
                                                                                                             self.type_var.get(),
                                                                                                             self.gender_var.get(),
                                                                                                             self.mrp_var.get(),
                                                                                                             self.sp_var.get(),
                                                                                                             self.shirt_id_var.get()
                                                                                                             ))
            self.clear_fun()
            print("fine")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        self.fetch_data()
        self.clear_fun()
        com.close()

    def fetch_some(self):
         com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
         cur=com.cursor()
         try:
             cur.execute("select * from shirt where " + str(self.search_by.get())+ " LIKE " + "'%"+str(self.search_text.get())+"%'")
             rows=cur.fetchall()
             if (rows!=0):
                 self.shirt_table.delete(*self.shirt_table.get_children())
                 print("if")
                 for row in rows:
                     self.shirt_table.insert('',END,values=row)
                     print("nice")
                 com.commit()
             print("yesss")
         except Exception as e:
            print("Exception: ",e)
         self.clear_fun()
         com.close()

class windowsales:
    def __init__(self, root):
        self.root=root
        self.root.title("MODA HOMBRE SALES")

  #========================manageframeofsales===================================#
        Manage_Frame2=Frame(self.root,bd=4,relief=RIDGE,bg="skyblue")
        Manage_Frame2.place(x=0,y=100,width=640,height=580)


        self.shirt_id_var=StringVar()
        self.size_var=StringVar()
        self.colour_var=StringVar()
        self.purchaser_name_var=StringVar()
        self.sp_var=StringVar()
        self.search_by_var=StringVar()
        self.search_text_var=StringVar()


        
        lbl_id=Label(Manage_Frame2,text="Shirt_id",font=("comic sans",20,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        textid=Entry(Manage_Frame2,textvariable=self.shirt_id_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textid.grid(row=1,column=1,pady=10,padx=10)

        lbl_size=Label(Manage_Frame2,text="SIZE",font=("comic sans",20,"bold"))
        lbl_size.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        textsize=Entry(Manage_Frame2,textvariable=self.size_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textsize.grid(row=2,column=1,pady=10,padx=10)

        lbl_color=Label(Manage_Frame2,text="COLOUR",font=("comic sans",20,"bold"))
        lbl_color.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        textcolor=Entry(Manage_Frame2,textvariable=self.colour_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textcolor.grid(row=3,column=1,pady=10,padx=10)

        lbl_purchase=Label(Manage_Frame2,text="PURCHASER NAME",font=("comic sans",20,"bold"))
        lbl_purchase.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        textpurchase=Entry(Manage_Frame2,textvariable=self.purchaser_name_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textpurchase.grid(row=4,column=1,pady=10,padx=10)

        

        lbl_sp=Label(Manage_Frame2,text="SP",font=("comic sans",20,"bold"))
        lbl_sp.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        textsp=Entry(Manage_Frame2,textvariable=self.sp_var,font=("comic sans",20,"bold"),bd=5,relief=GROOVE)
        textsp.grid(row=5,column=1,pady=10,padx=10)

         #======================buttonframeofshirts===========================================#

        
        button_Frame2=Frame(Manage_Frame2,bd=4,relief=RIDGE,bg="skyblue")
        button_Frame2.place(x=10,y=380,width=380)

        Addbtn=Button(button_Frame2,text='ADD',width=10,command=self.add_sales).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(button_Frame2,text='UPDATE',width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Clrbtn=Button(button_Frame2,text='CLEAR',width=10,command=self.clear_fun).grid(row=0,column=2,padx=10,pady=10)

         #=========detail_frameofsales=======================#

        Detail_Frame2=Frame(self.root,bd=4,relief=RIDGE,bg="skyblue")
        Detail_Frame2.place(x=650,y=100,width=750,height=560)

        
        lbl_search1=Label(Detail_Frame2,text="Search",font=("comic sans",10,"bold"))
        lbl_search1.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search1=ttk.Combobox(Detail_Frame2,textvariable=self.search_by_var,width=10,state='readonly',font=(10))
        combo_search1['values']=("shirt_id","size","colour","purchaser_name","mrp")
        combo_search1.grid(row=0,column=1,pady=10,padx=20)

        textsearch1=Entry(Detail_Frame2,textvariable=self.search_text_var,font=("comic sans",10,"bold"),bd=5,relief=GROOVE)
        textsearch1.grid(row=0,column=2,pady=10,padx=10)

        searchbtn1=Button(Detail_Frame2,text='SEARCH',width=10,command=self.fetch_some).grid(row=0,column=3,padx=10,pady=10)
        showallbtn1=Button(Detail_Frame2,text='SHOW ALL',width=10,command=self.fetch_sales).grid(row=0,column=4,padx=10,pady=10)

        #==============table_frameofsales=============================#

        table_Frame2=Frame(Detail_Frame2,bd=4,relief=RIDGE,bg="skyblue")
        table_Frame2.place(x=0,y=100,width=740,height=450)

        scroll_x=Scrollbar(table_Frame2,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame2,orient=VERTICAL)

        self.sales_table=ttk.Treeview(table_Frame2,column=("shirt_id","size","colour","purchaser_name","sp"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.sales_table.xview)
        scroll_y.config(command=self.sales_table.yview)
        
        self.sales_table.heading("shirt_id",text="shirt_id")
        self.sales_table.heading("size",text="size")
        self.sales_table.heading("colour",text="colour")
        self.sales_table.heading("purchaser_name",text="purchaser_name")
        self.sales_table.heading("sp",text="sp")
        self.sales_table['show']='headings'
        self.sales_table.pack(fill=BOTH,expand=1)
        self.fetch_sales()

    def add_sales(self):
            com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
            cur=com.cursor()
            try:
                cur.execute("insert into sales values(%s,%s,%s,%s,%s)",(self.shirt_id_var.get(),
                                                                              self.size_var.get(),
                                                                              self.colour_var.get(),
                                                                              self.purchaser_name_var.get(),
                                                                              self.sp_var.get()
                                                                              ))
                cur.execute("delete from shirt where shirt_id=%s",self.shirt_id_var.get())
                print("ok")
            except Exception as e:
                print("Exception: ",e)
       
            com.commit()
            self.fetch_sales()
            self.clear_fun()
            com.close()


    def fetch_sales(self):
         com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
         cur=com.cursor()
         try:
             cur.execute("select * from sales")
             rows=cur.fetchall()
             if (rows!=0):
                 self.sales_table.delete(*self.sales_table.get_children())
                 for row in rows:
                     self.sales_table.insert('',END,values=row)
                 com.commit()
             print("ok")
         except Exception as e:
            print("Exception: ",e)
         self.clear_fun()
         com.close()

    def clear_fun(self):
        self.shirt_id_var.set("")
        self.size_var.set("")
        self.colour_var.set("")
        self.purchaser_name_var.set("")
        self.sp_var.set("")
        self.search_by_var.set("")
        self.search_text_var.set("")
        print("okayyy")

    def update_data(self):
        com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
        cur=com.cursor()
        try:
            cur.execute("update sales set size=%s,colour=%s,purchaser_name=%s,sp=%s where shirt_id=%s",(self.size_var.get(),
                                                                                                             self.colour_var.get(),
                                                                                                             self.purchaser_name_var.get(),
                                                                                                             self.sp_var.get(),
                                                                                                             self.shirt_id_var.get()
                                                                                                             ))
            self.clear_fun()
            print("fine")
        except Exception as e:
            print("Exception: ",e)
       
        com.commit()
        self.fetch_sales()
        self.clear_fun()
        com.close()

    def fetch_some(self):
         com=pymysql.connect(host='localhost',user='root',password='8579081636',database='mh')
         cur=com.cursor()
         try:
             cur.execute("select * from sales where " + str(self.search_by_var.get())+ " LIKE " + "'%"+str(self.search_text_var.get())+"%'")
             rows=cur.fetchall()
             if (rows!=0):
                 self.sales_table.delete(*self.sales_table.get_children())
                 print("if")
                 for row in rows:
                     self.sales_table.insert('',END,values=row)
                     print("nice")
                 com.commit()
             print("yesss")
         except Exception as e:
            print("Exception: ",e)
         self.clear_fun()
         com.close()

class windowreturn:
    def __init__(self, root):
        self.root=root
        self.root.title("MODA HOMBRE RETURN DETAILS")


        Manage_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        Manage_Frame1.place(x=0,y=100,width=500,height=580)

        self.shirt_id_var=StringVar()
        self.size_var=StringVar()
        self.colour_var=StringVar()
        self.type_var=StringVar()
        self.gender_var=StringVar()
        self.mrp_var=StringVar()
        self.sp_var=StringVar()
        self.search_text=StringVar()
        self.search_by=StringVar()
        

   

   
      













       



     

root=tk.Tk()
ob=windowone(root)
root.mainloop()

