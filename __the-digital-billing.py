#importng reequired libraries
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import os.path

# creating tkinter window 
root =tk.Tk() 

# root window title and dimension 
root.title("THE DIGITAL BILLING")
root.configure(bg='#BDCBF8')
root.geometry('1600x750')

# Creating a photoimage object to use image 
photo = PhotoImage(file = r"the digital billing.png")

# set image on label
l = Label(image = photo).pack(side="top")


#list for customer and its payable amount .we are declaring these list here not in invoice becausewe have to save both data previous and new one .which was not happening in function
cus_pay=[]
cus_date=[]

#invoice
def invoice():
   print("-------------------------------------------------\n")
   shop=input("Enter name of shop :")

   #taking data from product details file
   f=pd.read_csv("PRODUCTS_DETAILS.csv")        #creating datframe of products details
   p_list = f['Product'].tolist()      #retrieving products list from csv file
   sp_list=f['Selling price'].tolist() #retrieving selling price from csv 
   gst_list=f['Gst'].tolist()          #retrieving gst from csv file
 
   c = open("invoice#.txt","a")          #making txt file
   c = open("invoice#.txt","r")             #opening file in read only format
   x = c.read()                             #reading file
   c.close()
   c = open("invoice#.txt","w")
   
   if len(x) == 0:                       #len(x)=0 means file is empty that means its first invoice
       c.write("1")            #as it is first invoice so we assign it 1 and it is named as counter and it is written 1 in file.
       counter = 1              #counter is a variable which denotes position of invoice like first invoice or second invoice
   else:
                counter = int(x)            #else condition is for when file is not empty it means its not the first invoice.
                counter = counter + 1        #this increase number of counter
                c.write(str(counter))        #this changes counter i.e,number of invoice indicating a new invoice is generated. 
   c.close()
   from datetime import datetime
   time = datetime.now()
   date1 = datetime.date(time)                    # time and date for printing in invoice
   datee=str(date1)
	
   namep = shop                     #shop,defined in first line of function invoice, is input we have taken for shop name
   print(f)                    #dataframe of product details will be printed.
   ly = []                      #ly is an empty list which will serve as a list containg name of products o be invoiced.
   ny=[]                          #ny is an empty list which will be used to store quantity of each products sold .
   cus=[]                           #cus is an empty list
   p1 = []                              #empty list which will serve as a list of product names.p_list is also product list but it will be changed to a list of selected items to be invoiced
   for i in p_list:                   #copying products names from list p_list to pl.
       p1.append(i)
   a = 1

   while a ==1:                                               #This while loop is for selecting  products sold and their quantities  whose invoice is to be generated.
       print("Enter Product name:")
       p = input()                                 #p is name of product to be invoiced.
		
       if p not in p1:
           print ("No Such Product Found!" + " Please Try Again")
           continue
       ly.append(p)                            #adding name of products to be invoiced to list ly.                        
		
       print("Quantity:")
       while True:                   #taking quantity input.this is done to prevent getting error if entered number is not integer.we were getting error found solution at stackoverflow.
           try:
               c = float((input()))
               ny.append(c)
               break
           except:
               print("Quantity can only be Integer or Float! Please Add Again")

       print ("Enter 1 to Stop adding product or press any other key to add more.CAUTION :dont repeat any product.")
       if input() == "1":
              print ("Enter Discount(in %)")
              dis = float(input())
              break
                    
   #for adding data to csv file "sales.csv" for analysis
   cust_name=input("enter customer name :")
   customer=[]
   p_list = []                               #making p_list null .earlier it was having list of products
   prod_sold=[]
   quant=[]
   dtime=[]
   for i in range (len(ly)):                    #ly is list of products to be invoiced.len(ly denotes number of products to be invoiced .
       p_list.append(ly[i])           #adding name of products to be sold to list p_list .
       customer.append(cust_name)      #making a list customer having customer name.
       dtime.append(date1)              #storing date and time in list dtime
       quant.append(ny[i])              #storing quantity of products 
   prod_sold = ly                                 #copying ly list to a new list prod_sold for making datframe.
   solddict={"Products":prod_sold,"Quantity":quant,"Date time":dtime,"Customer":customer}      #making dictionary with details of products sold, quantity, time and date and customer name.
   sold_df=pd.DataFrame(solddict)                                  #creating datframe 
   sold_df.set_index('Products',inplace=True)                          #setting index 
   
   if counter==1:                        #when this is first invoice ,datframe sold_df will be added to a csv named 'SALES.CSV'.
        sold_df.to_csv('SALES.csv')    #adding dataframe data to csv

 

   if counter>1:                                            #this is for time when this invoice is not first one.   
        soldor_df=pd.read_csv('SALES.CSV')                #in this we first read data of sales.csv filw which contains data of previous sales.
        hu=soldor_df['Products'].tolist()                 #and then copy them to a list and then add this old data with current one to make a new list.
        prne=prod_sold + hu                               #this new list is made for each attribute product name,quantity,customer,date and time
        ds=soldor_df['Quantity'].tolist()
        quane=quant + ds
        vd=soldor_df['Date time'].tolist()
        dt=dtime+vd
        jk=soldor_df['Customer'].tolist()
        cusnew=customer+ jk
        soldordict={"Products":prne,"Quantity":quane,"Date time":dt,"Customer":cusnew}
        soldornew=pd.DataFrame(soldordict)
        soldornew.to_csv('SALES.csv')       #updating csv file 'sales.csv' 

   #making invoice file in which invoice will be saved.
   x = open("invoice.txt","w+")                     
   l = " " + "S.no" + " "*2+ "Product Name" + " "*2 + "Price" + " "*4 + "GST(%)" + " "*2 +"Quantity" + "  "+ "Total"+" "
	
	
	
	
   x.write('-----------------------------------------------------------------------------------'+"\n")
   x.write ("                                             "+ namep + "\n")
   x.write('-----------------------------------------------------------------------------------'+"\n")
   x.write("                        "+"Date and Time: " + str(time) + "\n"*1)
   x.write("                                  " + "Invoice#" + " " + str(counter)+"\n"*1)
   x.write("                              " + "Customer name:"+ cust_name +"\n"*2)
	
	
   x.write(("S.no" + "   "+ " Product Name  " + "      " + "Price" + "        " + "GST(%)" + "        " +"Quantity" + "            "+ "Total"+"     ")+"\n")
   t = 0
   disc = 0
	
   for i in range(len(p_list)):                           #this is done to get products and their details to be ivoiced from list we have made earlier.
       s_no = i+1
       name=p_list[i]
       price =sp_list[i]
       gst = gst_list[i]
       qt = (ny[i])
       x.write((" " + str(s_no) + ")." + "                " + name + "              " + str(price) + "                "  + str(gst) + "         " + str(qt) + "           " + str(round((price*float(qt)+price*gst*int(qt)/100),2)) + "\n"))
       dc = price*float(qt)+price*gst*float(qt)/100
       disc = disc + dc
   d = disc*dis*0.01
   x.write("\n")
   x.write(" " +" "+ "Discount:" + " " + str(round(d,2))+"\n")
   x.write(" " +" "+ "Net Payable:" + " " + str(round(disc-d,2))+"\n"*4)
	
   x.write("\n"+"Thanks for shopping with us")
	
   x.close()
   print ("Invoice generated and  Saved Successfully in Invoice.txt .")
   print("Net Payable : ",round((disc-d),2))
   #making data for net payable by customer 
   cus_pay.append(disc-d)                                                 
   cus_date.append(datee)
   dict_cus_net={"customer":cust_name,"total" :cus_pay,"date":cus_date}
   cus_netpay=pd.DataFrame(dict_cus_net)
   if os.path.exists("customer_total.csv")==True:  #means if this file exists or not
      old_cus_netpay=pd.read_csv("customer_total.csv")
      fv=pd.concat([old_cus_netpay,cus_netpay],axis=0)   #adding dataframes
      
      fv.to_csv("customer_total.csv")
      
   else:
      cus_netpay.to_csv("customer_total.csv")           # for having total sales by a customer on a date  we mae a csv cutomer_total.csv
      
   input()


#generate invoice

def generate_invoice():
   if os.path.exists("PRODUCTS_DETAILS.csv")==True:
      invoice()
   else:
      messagebox.showerror("error", "No data found.")
      
      
   
#add products

def add():
  n=int(input("How many products you want to add:"))
  yn=input("is this your first time entering products,enter y or n,y stands for yes and n stands for no::")
  if yn=="n" or yn=="y":
     pass 
  else:
    yn=input("enter y or n only,y stands for yes and n stands for no:")
    

  pr=[]                                  # empty lists for products ,selling price,gst
  sp=[]
  gst=[]

  for a in range(n):
            prname = input("Enter name of Product: ")
            sprice = (input("Enter Selling Price(Excluding GST): "))
            gsprice = (input("Enter GST (in %): "))                           #getting products and its details
            pr.append(prname)                                          
            sp.append(sprice)                     #adding data to list
            gst.append(gsprice)
            
  prodict={"Product":pr,"Selling price":sp,"Gst":gst}  #making dictionary of products and its details          
  proser=pd.Series(pr)
  gstser=pd.Series(gst)
  spser=pd.Series(sp)
  product_df=pd.DataFrame(prodict)           #making datframe using prodict dictionary
  product_df.set_index('Product',inplace=True)
                                               #this is done to protect old data of csv file being vanished on adding new data 
  if yn== 'n': 
        pre_df=pd.read_csv('PRODUCTS_DETAILS.CSV')
        hii=pre_df['Product'].tolist()
        prad=pr + hii
        dsss=pre_df['Selling price'].tolist()
        apad= sp+ dsss
        vddd=pre_df['Gst'].tolist()
        gsadd=gst+vddd
        
        
        predordict={"Product":prad,"Selling price":apad,"Gst":gsadd}
        preornew=pd.DataFrame(predordict)
        preornew.set_index("Product",inplace=True)
        preornew.to_csv('PRODUCTS_DETAILS.CSV')
  if yn== "y" :
        product_df.to_csv('PRODUCTS_DETAILS.CSV')
  #data to csv

        
  fi=pd.read_csv('PRODUCTS_DETAILS.CSV')
  print(fi)    
    

#view products


def view():
  dff=pd.read_csv("PRODUCTS_DETAILS.CSV")
  row,column=dff.shape
  #total number of product entries
  print("total no of products:",row)

  if row == 0:
    print("Product list empty!")
    print("press any key to continue")
    input()
  if row != 0 :
    print(dff)
    
#delete products
def delete():
    fd=pd.read_csv("PRODUCTS_DETAILS.CSV")
    print(fd)
    row,column=fd.shape
    fd.set_index('Product',inplace=True)                 #making products index

    u=int(input("Enter how many products you want to delete:"))
    while u > row:                                         #this is for user,enters number of products ore than they are present
        print("Enter correct number =,entered number exceeds the number of total products")
        u=int(input("Enter how many products you want to delete:"))
    
    for i in range(u):
      an=(input("Enter name of product to be deleted:"))
      fd=fd.drop([an],axis=0)       #it will delte products we want by taking input of product name
    
    print("Products deleted successfully!")
    print(fd)
    fd.to_csv('PRODUCTS_DETAILS.CSV')

def main_products(p):                  #defining a function for asking user what he want to do add ,view or delete acc to input 1,2 and respectively.
    if p==1:
        add()                            #if p=1 then add function is called
    if p==2:                                 #if p=2 then view function is called
        view()        
    if p==3 :                        #if p=3 then delete  function is called
        delete()
#manage_products
def manage_products():            #for showing user options under manage products
    print("enter 1 to add products")
    print("Enter 2 to view products")
    print("Enter 3 to delete products")
    a=(input("Enter 1,2 or 3 according to ur need:"))
    p=int(a)
    main_products(p)


#graph of sales date wise
def date_sales_graph():
        df_analy=pd.read_csv("customer_total.csv")
        sales_Grap=pd.pivot_table(df_analy,index=['date'],values=['total'],aggfunc=['sum']) #pivoting dataframe with inde date 
        sales_Grap=sales_Grap.head(12)
        date_list=sales_Grap.index.values.tolist()       #making date to list
        sales_list=sales_Grap['sum']
        plt.plot(date_list,sales_list,label='Date Wise Sales')
        plt.xlabel('date')
        plt.ylabel('sales')
        plt.xticks(date_list)
        plt.title("date wise sales")
        plt.show()


#pie chart for most sold product
def piechart_product():
        prod_df=pd.read_csv("SALES.csv")
        jj=pd.pivot_table(prod_df,index=['Products'],values=['Quantity'])
        jj=jj.sort_values(by='Quantity',ascending=0)# ascending =0 signifies descending order
        row,column=jj.shape
        if row==1:
           gh=jj.head(1)#getting first first row of datframe jj

           products_piechart=gh.index.values.tolist()#making list of first most sold  products
           quantities_sold_piechart=gh['Quantity'].tolist()#making list of first most sold  products quantities

           explode=(0.1)#explode first slice
           colors=['red']
           ''' plotting '''
           plt.pie(quantities_sold_piechart,explode=explode,labels=products_piechart,colors=colors,shadow=True)
           plt.title("pie chart of most sold product")
           plt.show()
    
    
        elif row==2:
           gh=jj.head(2)#getting first two rows of datframe jj

           products_piechart=gh.index.values.tolist()#making list of first two most sold  products
           quantities_sold_piechart=gh['Quantity'].tolist()#making list of first two most sold  products quantities

           explode=(0.1,0)#explode first slice
           colors=['red','gold']
           ''' plotting '''
           plt.pie(quantities_sold_piechart,explode=explode,labels=products_piechart,colors=colors,shadow=True)
           plt.title("pie chart of most sold product")
           plt.show()
        elif row==3:    
            gh=jj.head(3)#getting first three rows of datframe jj

            products_piechart=gh.index.values.tolist()#making list of first three most sold  products
            quantities_sold_piechart=gh['Quantity'].tolist()#making list of first three most sold  products quantities

            explode=(0.1,0,0)#explode first slice
            colors=['red','gold','yellowgreen']
            ''' plotting '''
            plt.pie(quantities_sold_piechart,explode=explode,labels=products_piechart,colors=colors,shadow=True)
            plt.title("pie chart of most sold product")
            plt.show()

        elif row==4:    
            gh=jj.head(4)#getting first four rows of datframe jj

            products_piechart=gh.index.values.tolist()#making list of first four most sold  products
            quantities_sold_piechart=gh['Quantity'].tolist()#making list of first four most sold  products quantities

            explode=(0.1,0,0,0)#explode first slice
            colors=['red','gold','yellowgreen','blue']
            ''' plotting '''
            plt.pie(quantities_sold_piechart,explode=explode,labels=products_piechart,colors=colors,shadow=True)
            plt.title("pie chart of most sold product")
            plt.show()
   

        else:
   
          gh=jj.head(5)#getting first five rows of datframe jj

          products_piechart=gh.index.values.tolist()#making list of first five most sold  products
          quantities_sold_piechart=gh['Quantity'].tolist()#making list of first five most sold  products quantities

          explode=(0.1,0,0,0,0)#explode first slice
          colors=['red','gold','yellowgreen','blue','lightcoral']
          ''' plotting '''
          plt.pie(quantities_sold_piechart,explode=explode,labels=products_piechart,colors=colors,shadow=True)
          plt.title("pie chart of most sold product")
          plt.show()

def customer_vs_their_sales_on_a_date():
    df_analy=pd.read_csv("customer_total.csv")
    print("-------------DATES---------------")
    print(df_analy.date.unique())

    dat_in=input("enter date of whose analysis you want to see.enter same as in above format:")
    dat_in_anl=df_analy.loc[df_analy['date']==dat_in]
    df_ana=dat_in_anl
    bhj=pd.pivot_table(df_ana,index=['customer'],values=['total'])# customers data on that date
    row,column=bhj.shape
   
    cust_list=bhj.index.values.tolist()
    sales_list=bhj['total']
    plt.bar(cust_list,sales_list,width=.5,color='lightskyblue')#plotting  bar chart
    plt.xlabel("customers")
    plt.ylabel("sales")
    hjb="Customers and their sales on"+dat_in
    plt.title(hjb)
    plt.show()


#bar chart for most sold product
def barchart_product():
        prod_df=pd.read_csv("SALES.csv")
        jj=pd.pivot_table(prod_df,index=['Products'],values=['Quantity'])
        jj=jj.sort_values(by='Quantity',ascending=0)# ascending =0 signifies descending order
        row,column=jj.shape
        if row>=5:
           gh=jj.head(5)#getting first three rows of datframe jj

           products_barchart=gh.index.values.tolist()#making list of first three most sold  products
           quantities_sold_piechart=gh['Quantity'].tolist()#making list of first three most sold  products quantities
           plt.bar(products_barchart,quantities_sold_piechart,align='center',color='lightskyblue')
           plt.title("pie chart of most sold product")
           plt.show()
        else :
                print("Not enough products sold to show chart. Bar chart for most sold products will be displayed for more than 5 products sold.")

                               

def analysis_menu():
    print("-------------------------------------------------\n")
    print(" 1 to see overview of total sales per day  ")
    print(" 2 to see analysis of a particular date ")
    print(" 3 for graphical analysis ")
    print("-------------------------------------------------\n")
    
    io=(input("Enter 1 ,2 OR 3 according to your choice"))

    if int(io)==1:
            overview_analysis()
    elif int(io)==2:
            analysis_particular_Date()
    elif int(io)==3:
            graphical_analysis()            
    

def overview_analysis():
    df_analy=pd.read_csv("customer_total.csv")
    
    print("-----DATE WISE TOTAL SALES AND MEAN SALES-----")
    print(pd.pivot_table(df_analy,index=['date'],values=['total'],aggfunc=['sum','mean']))#complete overview analysis by date
    print("-------------------------------------------------\n")
    print("press any key to go to main menu:")
    fbs=input()
    analysis_menu()
    

def analysis_particular_Date():
    df_analy=pd.read_csv("customer_total.csv")
    print("---------------DATES------------------")
    print(df_analy.date.unique())    #show dates on which sales happened
    dat_in=input("enter date of whose analysis you want to see.enter same as in above format:")
    dat_in_anl=df_analy.loc[df_analy['date']==dat_in]   #dates
    df_ana=dat_in_anl
    print("--------CUSTOMERS DATA ON ",dat_in,"---------")
    print(pd.pivot_table(df_ana,index=['customer'],values=['total']))# customers data on that date

    print("Total number of ",df_ana[['customer']].count())    #count no of customers

    print("-----TOTAL SALES OF ",dat_in,"------") #total sales
    Total = df_ana['total'].sum()
    print (Total)
    maxsales=df_ana[['total']].max()    #maximum sales
    print("Highest sales :",maxsales)
    avgsales=df_ana[['total']].mean()   #average sales
    print("average sales:",avgsales)

    print("most frequent customer:",df_analy['customer'].mode())    #frequentcustomer
    print("-------------------------------------------------\n")

    print("press any key to go to main menu:")
    fbs=input()
    analysis_menu()

    
def graphical_analysis():
    print("-------------------------------------------------\n")
    print("Pie chart for most sold product : 1")
    print("Graph of last 12 day total sales : 2")
    print("Customer and their sales graph on a date:3")
    print("Bar chart for most sold product: 4")
    print("to go back to main menu : 5")
    print("-------------------------------------------------\n")
    print("Enter 1, 2 ,3 ,4 or 5 according to ur choice:")
    ad=(input())

    if int(ad)==1:
        piechart_product()
        pass
    elif int(ad)==2:
        date_sales_graph()
        pass
    elif int(ad)==3:
        customer_vs_their_sales_on_a_date()
        pass
    elif int(ad)==4:
        barchart_product()
        pass
    elif int(ad)==5:
        analysis()
        pass
    print("press any key to go to main menu:")
    fbs=input()
    analysis_menu()
    
def analysis():
   if os.path.exists("customer_total.csv")==True and os.path.exists("SALES.csv")==True:# to ensure file exists
    analysis_menu()
   else:
      messagebox.showerror("error", "No data found.")


#section of menu .making frame
menu_frame=Frame(root, bg='#4EC0CB', width=350, height=600, pady=3).place(x=10,y=25)
#label of menu
menu_label = tk.Label(root, text="   MENU   ",fg = "#50F5DA",bg = "#2E86C1",font = "Helvetica 45 bold italic").place(x=45,y=60) 
# button 1 
manpro = Button(root, text = 'MANAGE PRODUCTS', font =('calibri', 18, 'bold'),borderwidth = '4',bg='#A3E4D7',activebackground='#1ABC9C', command = manage_products).place(x=75,y=200)
#button 2
geninvoi = Button(root, text = ' GENERATE INVOICE ', font =('calibri', 18, 'bold'),borderwidth = '4', bg='#A3E4D7',activebackground='#1ABC9C',command = generate_invoice).place(x=75,y=300)
#BUTTON 3
analy= Button(root, text = '           ANALYSIS          ', font =('calibri', 18, 'bold'),borderwidth = '4',bg='#A3E4D7',activebackground='#1ABC9C', command =analysis).place(x=75,y=400)

#quit button
def close_window():
    root.destroy()
quitbutt= Button(root, text = '               QUIT                ', font =('calibri', 18, 'bold'),borderwidth = '4', bg='#A3E4D7',activebackground='#1ABC9C',command =close_window).place(x=75,y=500) 

#function for about
def about():
   p1='This project is about creating an application using python that will be used for billing and invoice generation. Our project aim is to completely digitize the old manual billing system. Small scale businesses like grocery shops, garments shop etc. uses manual billing for bill and payment. Manual billing have many loopholes and problems like mistakes in calculation, difficult to find a particular bill book, maintain records of old bill books etc. Our software will be helpful to these small scale businesses by providing flexibility and ease in billing and digitizing invoices,also we will provide analysis of their business like no .of customers visited ,profirs etc. It would also make us independent as we would be using a software developed by our own country “India” for the development of India . #vocalforlocal #atamnirbharbaniye'
   messagebox.showinfo("ABOUT THIS SOFTWARE ", p1)


#function for help
def help_1():
    p2='For maintaing list and details of product we have a button MANAGE BUTTON under section MENU .In MANAGE PRODUCTS user can perform three tasks adding details of products available to be sols,view for viewing list of products available and delete for deleting product and its details.In INVOICE button under section MENU we can generate invoice.In ANALYSIS button we can analyse user business through charts and graph showing which product is sold more , frequency of customers etc.'
    messagebox.showinfo("HELP ", p2)
#section for help
help_frame=Frame(root, bg='#4EC0CB', width=350, height=350, pady=3).place(x=1000,y=30)
help_button = Button(root, text = '    FOR HELP   ', font =('calibri', 18, 'bold'),borderwidth = '4',bg='#A3E4D7',activebackground='#1ABC9C', command =help_1).place(x=1095,y=275)
about_button = Button(root, text = 'ABOUT THIS SOFTWARE', font =('calibri', 18, 'bold'),borderwidth = '4',bg='#A3E4D7',activebackground='#1ABC9C', command = about).place(x=1040,y=175)
help_label = tk.Label(root, text=" HELP DESK ",fg = "#50F5DA",bg = "#2E86C1",font = "Helvetica 35 bold italic").place(x=1027,y=75)

#function for giving feedback
fed_dictionary={}             #a dictionary for storing feedbacks with name who have given feedback.

def feedback():
    feed_name=input("enter your name:")
    quo='Bill gates said " WE ALL NEED PEOPLE WHO GIVE US FEEDBACK. THATS HOW WE IMPROVE ". So here enter your customer valuable feedback!'
    print(quo)
    fedinp=input()
    fed_dictionary[feed_name]=fedinp
    print("Thank you for ur valuable feedback.")
    
#function for seeing feedback
def feedback_see():
        print(fed_dictionary)
    
#section for feedback
feedback_frame=Frame(root, bg='#4EC0CB', width=360, height=250, pady=3).place(x=1000,y=410)
feedback_entry = Button(root, text = 'FEEDBACK OF \n CUSTOMERS ', font =('calibri', 18, 'bold'),borderwidth = '4',bg='#A3E4D7',activebackground='#1ABC9C', command = feedback).place(x=1100,y=500)
feedback_see = Button(root, text = 'SEE FEEDBACKS  ', font =('calibri', 18, 'bold'),borderwidth = '4',bg='#A3E4D7',activebackground='#1ABC9C', command = feedback_see).place(x=1090,y=600)
feedback_label = tk.Label(root, text=" FEEDBACK DESK",fg = "#50F5DA",bg = "#2E86C1",font = "Helvetica 27 bold italic").place(x=1015,y=430)

#welcome message
welcome_message = "      WELCOME TO THE DIGITAL BILLING                            A small business tool for big business success  "
msg = tk.Message(root, text =welcome_message,bg='#FF8728', font=('times', 20, 'italic'),width=600).place(x=405,y=575)

root.mainloop() 
  

