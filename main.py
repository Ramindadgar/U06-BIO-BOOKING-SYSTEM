from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3
from database import DatabaseHandler


#============================================= user Window Class =================================================
class User:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    #========================================= Draw Widgets (GUI) ==================================================
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        #===================================== Login Frame And Widgets (GUI) ======================================
        self.login_frame = Frame(self.master, padx=10, pady=10)
        Label(self.login_frame, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.login_frame, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.login_frame, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.login_frame, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5,
               command=self.create_account).grid(row=2,
                                                 column=1)
        self.login_frame.pack()

        #============================= Create Account Frame And Widgets (GUI) =======================================
        self.create_account_frame = Frame(self.master, padx=10, pady=10)
        Label(self.create_account_frame, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_account_frame, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.create_account_frame, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_account_frame, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1,
                                                                                                           column=1)
        Button(self.create_account_frame, text='Create Account', bd=3, font=('', 15), padx=5, pady=5,
               command=self.new_user).grid()
        Button(self.create_account_frame, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5,
               command=self.log).grid(row=2, column=1)

        # ====================================Login Function===================================================

    def login(self):
        result = db.check_user_exist(username=self.username.get(), password=self.password.get())
        if result:
            self.login_frame.pack_forget()
            self.head['text'] = "Welcome, " + self.username.get()
            self.head.configure(fg="green")
            self.head.pack(fill=X)
            application = Cinema(root)
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        result = db.check_user_exist_by_username(username=self.username.get())
        if result:
            ms.showerror('Error!', 'Username Already Taken!')
        else:
            ms.showinfo('Success!', 'Account Created!')

            # Create New Account
            db.insert_new_user(username=self.n_username.get(), password=self.n_password.get())
            self.log()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.create_account_frame.pack_forget()
        self.head['text'] = 'LOGIN'
        self.login_frame.pack()

    def create_account(self):
        self.n_username.set('')
        self.n_password.set('')
        self.login_frame.pack_forget()
        self.head['text'] = 'Create Account'
        self.create_account_frame.pack()


# =============================================Cinema window class==================================================
class Cinema:

    def __init__(self, root):
        self.root = root
        self.root.title("Cinema Booking System Stockholm")
        self.root.geometry(geometry)
        self.root.configure(background='black')

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref = StringVar()
        CinemaTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        cocacola_variable = IntVar()
        popcorn_variable = IntVar()

        salon_variable = StringVar()
        movie_name_variable = StringVar()

        Firstname = StringVar()
        Lastname = StringVar()
        Mobile = StringVar()
        Email = StringVar()

        CocaCola = StringVar()
        PopCorn = StringVar()

        Receipt = StringVar()

        CocaCola.set("0")
        PopCorn.set("0")

        # ==========================================Define Function==================================================

        def iExit():
            iExit = ms.askyesno("Prompt!", "Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            CocaCola.set("0")
            PopCorn.set("0")

            Firstname.set("")
            Lastname.set("")
            Mobile.set("")
            Email.set("")

            CinemaTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)

            cocacola_variable.set(0)
            popcorn_variable.set(0)

            salon_variable.set("0")
            movie_name_variable.set("0")

            self.txtCocaCola.configure(state=DISABLED)
            self.txtPopCorn.configure(state=DISABLED)
#===================================================SHOW_Receipt===================================================
        def show_receipt():
            if Firstname.get() != "" and Lastname.get() != "" and Mobile.get() != "" and Email.get() != "":
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                x = random.randint(10853, 500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)
                self.txtReceipt1.insert(END, "Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END, 'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END, 'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END, 'Lastname:\n')
                self.txtReceipt2.insert(END, Lastname.get() + "\n")
                self.txtReceipt1.insert(END, 'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END, 'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END, 'Paid:\n')
                self.txtReceipt2.insert(END, CinemaTax.get() + "\n")
                self.txtReceipt1.insert(END, 'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END, 'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
            else:
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                self.txtReceipt1.insert(END, "\nNo Input")
                ms.showwarning("Error !", "Customer Detail is Empty!!!")

#===========================================Coca_Cola===============================================================

        def Coca_Cola():
            global Item1
            if cocacola_variable.get() == 1:
                self.txtCocaCola.configure(state=NORMAL)
                Item1 = float(15)
                CocaCola.set("Kr " + str(Item1))
            elif cocacola_variable.get() == 0:
                self.txtCocaCola.configure(state=DISABLED)
                CocaCola.set("0")
                Item1 = 0
#===========================================Pop_corn===============================================================
        def Pop_Corn():
            global Item2
            if popcorn_variable.get() == 1:
                self.txtPopCorn.configure(state=NORMAL)
                Item2 = float(10)
                PopCorn.set("Kr " + str(Item2))
            elif popcorn_variable.get() == 0:
                self.txtPopCorn.configure(state=DISABLED)
                PopCorn.set("0")
                Item2 = 0
#===========================================Total_Paid============================================================
        def Total_Paid():
            if salon_variable.get() != "" and movie_name_variable.get() != "":
                result = 0
                if popcorn_variable.get() == 1:
                    result += float(PopCorn.get().split()[1])
                if cocacola_variable.get() == 1:
                    result += float(CocaCola.get().split()[1])
                movie_price = db.get_movie_price(movie_name_variable.get().split()[0])
                result += movie_price

                cinema_tax = "Kr " + str('%.2f' % (result * 0.09))
                sub_total = "Kr " + str('%.2f' % result)
                total = "Kr " + str('%.2f' % (result + (result * 0.09)))

                CinemaTax.set(cinema_tax)
                SubTotal.set(sub_total)
                TotalCost.set(total)
            else:
                ms.showwarning("Error !", "Invalid Input\nPlease try again !!!")

        # ================================================mainframe (GUI)========================================================================

        MainFrame = Frame(self.root)
        MainFrame.pack(fill=BOTH, expand=True)
        Tops = Frame(MainFrame, bd=20, width=1350, relief=RIDGE)
        Tops.pack(side=TOP, fill=BOTH, expand=True)
        self.lblTitle = Label(Tops, font=('arial', 70, 'bold'), text=" Cinema Booking System Stockholm ")
        self.lblTitle.grid()

        # ================================================customerframedetail (GUI) =============================================================
        CustomerDetailsFrame = LabelFrame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        FrameDetails = Frame(CustomerDetailsFrame, width=880, height=400, bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)

        CustomerDetail = LabelFrame(FrameDetails, width=150, height=250, bd=10, font=('arial', 12, 'bold'),
                                    text="Customer Detail", relief=RIDGE)
        CustomerDetail.grid(row=0, column=0)

        CinemaFrame = LabelFrame(FrameDetails, bd=10, width=300, height=250, font=('arial', 12, 'bold'),
                                 text="Booking Detail", relief=RIDGE)
        CinemaFrame.grid(row=0, column=1)

        CostFrame = LabelFrame(FrameDetails, bd=10, width=300, height=250, font=('arial', 12, 'bold'),
                               text="Paid Detail", relief=RIDGE)
        CostFrame.grid(row=0, column=2)

        # ===============================================receipt (GUI)======================================================================
        Receipt_BottonFrame = LabelFrame(CustomerDetailsFrame, bd=10, width=450, height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        ReceiptFrame = LabelFrame(Receipt_BottonFrame, width=350, height=300, font=('arial', 12, 'bold'),
                                  text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0, column=0)

        ButtonFrame = LabelFrame(Receipt_BottonFrame, width=350, height=100, relief=RIDGE)
        ButtonFrame.grid(row=1, column=0)
        # =========================================================CustomerName (GUI)====================================================

        self.lblFirstname = Label(CustomerDetail, font=('arial', 14, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerDetail, font=('arial', 14, 'bold'), textvariable=Firstname, bd=7,
                                  insertwidth=2,
                                  justify=RIGHT)
        self.txtFirstname.grid(row=0, column=1)

        self.lblLastname = Label(CustomerDetail, font=('arial', 14, 'bold'), text="Lastname", bd=7)
        self.lblLastname.grid(row=1, column=0, sticky=W)
        self.txtLastname = Entry(CustomerDetail, font=('arial', 14, 'bold'), textvariable=Lastname, bd=7, insertwidth=2,
                                 justify=RIGHT)
        self.txtLastname.grid(row=1, column=1, sticky=W)

        self.lblMobile = Label(CustomerDetail, font=('arial', 14, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=2, column=0, sticky=W)
        self.txtMobile = Entry(CustomerDetail, font=('arial', 14, 'bold'), textvariable=Mobile, bd=7, insertwidth=2,
                               justify=RIGHT)
        self.txtMobile.grid(row=2, column=1)

        self.lblEmail = Label(CustomerDetail, font=('arial', 14, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=3, column=0, sticky=W)
        self.txtEmail = Entry(CustomerDetail, font=('arial', 14, 'bold'), textvariable=Email, bd=7, insertwidth=2,
                              justify=RIGHT)
        self.txtEmail.grid(row=3, column=1)

        # ===============================================Cinema Information (GUI)==============================================================
        self.lblSalon = Label(CinemaFrame, font=('arial', 14, 'bold'), text="Salon", bd=7)
        self.lblSalon.grid(row=0, column=0, sticky=W)

        self.cboSalon = ttk.Combobox(CinemaFrame, textvariable=salon_variable, state='readonly',
                                     font=('arial', 14, 'bold'),
                                     width=35)
        all_salons = db.get_all_salons()
        result = []
        for salon in all_salons:
            result.append(salon[2])
        self.cboSalon['value'] = tuple(result)
        self.cboSalon.current(0)
        self.cboSalon.grid(row=0, column=1)

        self.lblMovieName = Label(CinemaFrame, font=('arial', 14, 'bold'), text="MovieName", bd=7)
        self.lblMovieName.grid(row=1, column=0, sticky=W)

        self.cboMovieName = ttk.Combobox(CinemaFrame, textvariable=movie_name_variable, state='readonly',
                                         font=('arial', 14, 'bold'),
                                         width=35)
        all_movies = db.get_all_movies()
        result = []
        for item in all_movies:
            movie = item[2:]
            result.append(f'{movie[0]} ({movie[1]} {movie[2]}) {movie[3]} kr')
        self.cboMovieName['value'] = tuple(result)
        self.cboMovieName.current(0)
        self.cboMovieName.grid(row=1, column=1)

        self.chkCocaCola = Checkbutton(CinemaFrame, text="Coca Cola", variable=cocacola_variable, onvalue=1, offvalue=0,
                                       font=('arial', 16, 'bold'), command=Coca_Cola).grid(row=3, column=0, sticky=W)
        self.txtCocaCola = Label(CinemaFrame, font=('arial', 14, 'bold'), textvariable=CocaCola, bd=6, width=18,
                                 bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtCocaCola.grid(row=3, column=1)

        self.chkPopCorn = Checkbutton(CinemaFrame, text="PopCorn", variable=popcorn_variable, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), command=Pop_Corn).grid(row=4, column=0, sticky=W)
        self.txtPopCorn = Label(CinemaFrame, font=('arial', 14, 'bold'), textvariable=PopCorn, bd=6, width=18,
                                bg="white",
                                state=DISABLED, justify=RIGHT, relief=SUNKEN, highlightthickness=0)
        self.txtPopCorn.grid(row=4, column=1)

        # =================================payment information(GUI) ===========================================================================

        self.lblCinemaTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Cinema Tax\t\t", bd=7)
        self.lblCinemaTax.grid(row=0, column=0, sticky=W)
        self.txtCinemaTax = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=CinemaTax, bd=7, width=10,
                                  justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtCinemaTax.grid(row=0, column=1)

        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=7)
        self.lblSubTotal.grid(row=1, column=0, sticky=W)
        self.txtSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, width=10,
                                 justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtSubTotal.grid(row=1, column=1)

        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost", bd=7)
        self.lblTotalCost.grid(row=2, column=0, sticky=W)
        self.txtTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, width=10,
                                  justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtTotalCost.grid(row=2, column=1)

        # =======================================Reciept (GUI)====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt1.grid(row=0, column=0, columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt2.grid(row=0, column=2, columnspan=2)

        # ======================================Button (GUI)========================================================================================

        self.btnTotal = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Total',
                               command=Total_Paid).grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Receipt',
                                 command=show_receipt).grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Reset',
                               command=Reset).grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Exit',
                              command=iExit).grid(row=0, column=3)

    # ====================================================================================================================================


if __name__ == '__main__':
    root = Tk()
    db = DatabaseHandler()

    # =========================================== Getting Screen Width (GUI)==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry = "%dx%d+%d+%d" % (w, h, 0, 0)

    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = User(root)
    #app = Cinema(root)
    root.mainloop()
