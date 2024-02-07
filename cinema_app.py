


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askyesno
import locale
import datetime
from database import *


today_date = datetime.date.today().strftime("%d-%m-%Y")
tomorrow_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
time_now = datetime.datetime.now()
hour_minute_now = time_now.strftime("%H:%M")


locale.setlocale(locale.LC_ALL, 'id-ID')


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("GROUP 1 MOVIE BOOKING SYSTEM")
root.iconbitmap("images/xx5.ico")
root.state('zoomed')
root.configure(background="#171a30")


center_x_info = (screen_width - 980) * 0.5
center_x_seat = (screen_width - 450) * 0.5
center_x_history = (screen_width - 1147) * 0.5


xx5_img = tk.PhotoImage(file="images/xx5.png")
img_xx5_heading = tk.PhotoImage(file="images/xx5heading.png")

now_img_on = [tk.PhotoImage(file=movie_now[i]["img_on"]) for i in range(4)]
now_img_off = [tk.PhotoImage(file=movie_now[i]['img_off']) for i in range(4)]

upcoming_img_on = [tk.PhotoImage(file=movie_upcoming[i]['img_on']) for i in range(4)]
upcoming_img_off = [tk.PhotoImage(file=movie_upcoming[i]['img_off']) for i in range(4)]

button_logreg_on = tk.PhotoImage(file="images/logreg_on.png")
button_logreg_off = tk.PhotoImage(file="images/logreg_off.png")

button_heading_on = tk.PhotoImage(file="images/heading_on.png")
button_heading_off = tk.PhotoImage(file="images/heading_off.png")

button_time_on = tk.PhotoImage(file="images/time_on.png")
button_time_off = tk.PhotoImage(file="images/time_off.png")

button_price_on = tk.PhotoImage(file="images/price_on.png")
button_price_off = tk.PhotoImage(file="images/price_off.png")

button_method_on = tk.PhotoImage(file="images/method_on.png")
button_method_off = tk.PhotoImage(file="images/method_off.png")

seat_free = tk.PhotoImage(file="images/seat_free.png")
seat_own = tk.PhotoImage(file="images/seat_own.png")
seat_sold = tk.PhotoImage(file="images/seat_sold.png")

screen_img = tk.PhotoImage(file="images/screen.png")

cancelconfirm_off = tk.PhotoImage(file="images/cancelconfirm_off.png")
confirm_on = tk.PhotoImage(file="images/confirm_on.png")
cancel_on = tk.PhotoImage(file="images/cancel_on.png")



def onclick_entry(event, word):
    if event.widget.get() == f"{word}" and (event.widget.get() == "Password" or event.widget.get() == "confirm password" or event.widget.get() == "code invitation"):
        event.widget.delete(0, "end")
        event.widget.config(show="*")
    elif event.widget.get() == f"{word}":
        event.widget.delete(0, "end")

def onleave_entry(event, word):
    if (event.widget.get() == ""):
        event.widget.insert(0, f"{word}")
        event.widget.config(show="")


def onhover_image(event, img):
    event.widget.config(image=img)

def onleave_image(event, img):
    event.widget.config(image=img)


def update_time():
    global today_date, tomorrow_date, time_now, hour_minute_now
    today_date = datetime.date.today().strftime("%d-%m-%Y")
    tomorrow_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
    time_now = datetime.datetime.now()
    hour_minute_now = time_now.strftime("%H:%M")



def Login():

    def login():
        akun_email = email.get()
        akun_password = pasw.get()
        user_found = False
        for i in range(len(list_user)):
            if akun_email == list_user[i]['email'] and akun_password == list_user[i]['password']:
                user_found = True
                global index_user
                index_user = i
                break
        if user_found:
            showinfo("login done", f"welcome, {akun_email}!")
            LoginToList()
        else:
            showerror("Invalid", "Email and Password doesn't match")
    

    def LoginToRegister():
        login_frame.forget()
        Register()
    

    def LoginToList():
        login_frame.forget()
        ListMovie("nowshowing")
    

    global login_frame
    login_frame = tk.Frame(root, bg="#171a30")
    login_frame.pack()


    label_gambar = tk.Label(login_frame, image=xx5_img, border=0, bg="#171a30").pack()
    heading = tk.Label(login_frame, text="Login", fg="#fc094c", bg="#171a30", font=("Segoe UI", 23, "bold")).pack(pady=10)

 
    email = tk.Entry(login_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Segoe UI", 11), insertbackground="#eaebf1")
    email.pack()
    email_border = tk.Frame(login_frame,width=295,height=2,bg="#eaebf1").pack(pady=(5, 20))
    email.insert(0, "Email")
    email.bind("<FocusIn>", lambda event: onclick_entry(event, "Email"))
    email.bind("<FocusOut>", lambda event: onleave_entry(event, "Email"))


    pasw = tk.Entry(login_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Segoe UI", 11), insertbackground="#eaebf1")
    pasw.pack()
    pasword_border = tk.Frame(login_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))
    pasw.insert(0, "Password")
    pasw.bind("<FocusIn>", lambda event: onclick_entry(event, "Password"))
    pasw.bind("<FocusOut>", lambda event: onleave_entry(event, "Password"))
    

    tombol_login = tk.Button(login_frame, text="Login", command=login, image=button_logreg_off, font=("Segoe UI", 13, "bold"), activebackground="#171a30", activeforeground="#eaebf1", fg="#eaebf1", bg="#171a30", cursor="hand2", borderwidth=0, compound="center")
    tombol_login.pack(pady=(0, 5))
    tombol_login.bind('<Enter>', lambda event, imgs=button_logreg_on: onhover_image(event, imgs))
    tombol_login.bind('<Leave>', lambda event, imgs=button_logreg_off: onleave_image(event, imgs))


    noacc_frame = tk.Frame(login_frame, bg="#171a30")
    label_register = tk.Label(noacc_frame, text="New to us do ", fg="#eaebf1", bg="#171a30", font=("Segoe UI", 11, "bold")).pack(side="left")
    tombol_register = tk.Button(noacc_frame, text="Register", command=LoginToRegister,  font=("Segoe UI", 11, "bold"), borderwidth=0, cursor="hand2", bg="#171a30", fg="#fc094c", activebackground="#171a30", activeforeground="#fc094c").pack()
    noacc_frame.pack()



def Register():
    # TRANSISI REGISTER KE LOGIN
    def RegisterToLogin():
        register_frame.forget()
        Login()
    
    # Callback Function Klik Register
    def klik_register():
        nama_lengkap = nama.get()
        akun_email = email.get()
        akun_password = pasw.get()
        confirm = conf_pasw.get()
        if akun_password == confirm:
            dict = {
                "nama": nama_lengkap,
                "email": akun_email,
                "password": akun_password,
                "saldo": 0,
                "riwayat": []
            }
            read_file = open('database.py', 'r')
            content = read_file.read()
            old_list_user = str(list_user)
            list_user.append(dict)
            new_list_user = str(list_user)

            content = content.replace(old_list_user, new_list_user)
            read_file.close()

            write_file = open('database.py', 'w')
            write_file.write(content)
            write_file.close()

            showinfo("Register", "register done!")
            RegisterToLogin()
        else:
            showerror("Invalid", "Password doesn't match")

 
    global register_frame
    register_frame = tk.Frame(root, bg="#171a30")
    register_frame.pack()

  
    label_gambar = tk.Label(register_frame, image=xx5_img, border=0, bg="#171a30").pack()
    heading = tk.Label(register_frame, text="Register", fg="#fc094c", bg="#171a30", font=("Segoe UI", 23, "bold")).pack(pady=10)

 
    nama = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Segoe UI", 11), insertbackground="#eaebf1")
    nama.pack()
    nama.insert(0, "Name")
    nama.bind("<FocusIn>", lambda event: onclick_entry(event, "Nama Lengkap"))
    nama.bind("<FocusOut>", lambda event: onleave_entry(event, "Nama Lengkap"))
    frame2 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

    # Input email
    email = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Segoe UI", 11), insertbackground="#eaebf1")
    email.pack()
    email.insert(0, "Email")
    email.bind("<FocusIn>", lambda event: onclick_entry(event, "Email"))
    email.bind("<FocusOut>", lambda event: onleave_entry(event, "Email"))
    frame2 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

    # Input Password
    pasw = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Segoe UI", 11), insertbackground="#eaebf1")
    pasw.pack()
    pasw.insert(0, "Password")
    pasw.bind("<FocusIn>", lambda event: onclick_entry(event, "Password"))
    pasw.bind("<FocusOut>", lambda event: onleave_entry(event, "Password"))
    frame3 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))


    conf_pasw = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Segoe UI", 11), insertbackground="#eaebf1")
    conf_pasw.pack()
    conf_pasw.insert(0, "confirm password")
    conf_pasw.bind("<FocusIn>", lambda event: onclick_entry(event, "Konfirmasi Password"))
    conf_pasw.bind("<FocusOut>", lambda event: onleave_entry(event, "Konfirmasi Password"))
    frame3 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

 
    tombol_register = tk.Button(register_frame, text="Register", command=klik_register, image=button_logreg_off, font=("Segoe UI", 13, "bold"), activebackground="#171a30", activeforeground="#eaebf1", fg="#eaebf1", bg="#171a30", cursor="hand2", borderwidth=0, compound="center")
    tombol_register.pack(pady=(0, 5))
    tombol_register.bind('<Enter>', lambda event, imgs=button_logreg_on: onhover_image(event, imgs))
    tombol_register.bind('<Leave>', lambda event, imgs=button_logreg_off: onleave_image(event, imgs))


    sudah_akun = tk.Frame(register_frame, bg="#171a30")
    ada_akun = tk.Label(sudah_akun, text="already have account", fg="#eaebf1", bg="#171a30", font=("Segoe UI", 11, "bold")).pack(side="left")
    tombol_login = tk.Button(sudah_akun, width=6, text="Login", border=0, bg="#171a30", cursor="hand2", fg="#fc094c", activebackground="#171a30", activeforeground="#fc094c", font=("Segoe UI", 11, "bold"), command=RegisterToLogin).pack()
    sudah_akun.pack()



def MenuHeader(frame, name):
    # HEADING NOW PLAYING
    def ToNowPlaying(frame):
        frame.forget()
        ListMovie("nowshowing")


    def ToUpcoming(frame):
        frame.forget()
        ListMovie("upcoming")

 
    def ToSaldo(frame):
        frame.forget()
        TopUp()

   
    def ToRiwayat(frame):
        frame.forget()
        Riwayat()


    def ClickLogOut(frame):
        confirmation = askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if confirmation:
            frame.forget()
            Login()
    
    def now_playing_img(name):
        if name == "movielist_nowshowing":
            return button_heading_on
        else:
            return button_heading_off
    
    def upcoming_img(name):
        if name == "movielist_upcoming":
            return button_heading_on
        else:
            return button_heading_off

    def topup_img(name):
        if name == "saldo":
            return button_heading_on
        else:
            return button_heading_off
    
    def riwayat_img(name):
        if name == "riwayat":
            return button_heading_on
        else:
            return button_heading_off         
    

    header_frame = tk.Frame(frame, bg="#171a30")
    header_frame.pack(pady=(10, 0))

    left_frame = tk.Frame(header_frame, bg="#171a30")
    left_frame.pack(side="left", padx=(0, 45))
    label_gambar = tk.Label(left_frame, image=img_xx5_heading, bg="#171a30").pack(side="left", padx=10)

    now_playing = tk.Button(left_frame, text="Now Playing", command=lambda frame=frame: ToNowPlaying(frame), image=now_playing_img(name), font=("Segoe UI", 14, "bold"), bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", cursor="hand2", borderwidth=0, compound="center")
    now_playing.pack(side="left", anchor="center", padx=10)
    if name != "movielist_nowshowing":
        now_playing.bind('<Enter>', lambda event, imgs=button_heading_on: onhover_image(event, imgs))
        now_playing.bind('<Leave>', lambda event, imgs=button_heading_off: onleave_image(event, imgs))
    
    # Upcoming
    up_coming = tk.Button(left_frame, text="Upcoming", command=lambda frame=frame: ToUpcoming(frame), image=upcoming_img(name), font=("Segoe UI", 14, "bold"), bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", cursor="hand2", borderwidth=0, compound="center")
    up_coming.pack(side="left", anchor="center", padx=10)
    if name != "movielist_upcoming":
        up_coming.bind('<Enter>', lambda event, imgs=button_heading_on: onhover_image(event, imgs))
        up_coming.bind('<Leave>', lambda event, imgs=button_heading_off: onleave_image(event, imgs))


    right_frame = tk.Frame(header_frame, bg="#171a30")
    right_frame.pack(side="right", padx=(45, 0))
    # Topup
    topup = tk.Button(right_frame, text="Top Up", command=lambda frame=frame: ToSaldo(frame), image=topup_img(name), font=("Segoe UI", 14, "bold"), bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", cursor="hand2", borderwidth=0, compound="center")
    topup.pack(side="left", padx=10)
    if name != "saldo":
        topup.bind('<Enter>', lambda event, imgs=button_heading_on: onhover_image(event, imgs))
        topup.bind('<Leave>', lambda event, imgs=button_heading_off: onleave_image(event, imgs))
    

    riwayat = tk.Button(right_frame, text="History", command=lambda frame=frame: ToRiwayat(frame), image=riwayat_img(name), font=("Segoe UI", 14, "bold"), bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", cursor="hand2", borderwidth=0, compound="center")
    riwayat.pack(side="left", padx=10)
    if name != "riwayat":
        riwayat.bind('<Enter>', lambda event, imgs=button_heading_on: onhover_image(event, imgs))
        riwayat.bind('<Leave>', lambda event, imgs=button_heading_off: onleave_image(event, imgs))
    

    logout = tk.Button(right_frame, text="Log Out", command=lambda frame=frame: ClickLogOut(frame), image=button_heading_off, font=("Segoe UI", 14, "bold"), bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", cursor="hand2", borderwidth=0, compound="center")
    logout.pack(side="left", padx=10)
    logout.bind('<Enter>', lambda event, imgs=button_heading_on: onhover_image(event, imgs))
    logout.bind('<Leave>', lambda event, imgs=button_heading_off: onleave_image(event, imgs))


# FRAME Top Up
def TopUp():   

    def isValid():
        method = selected_method.get()
        price = selected_price.get()
        if method == "N/A" or price == 0:
            showerror("Select Balance/Method!", f"Select the correct balance or payment method!")
        else:
            if kode_valid.get() == list_validasi[price][method]:
                read_file = open('database.py', 'r')
                content = read_file.read()
                old_dict_user = str(list_user[index_user])
                list_user[index_user]['saldo'] += price
                new_dict_user = str(list_user[index_user])
                content = content.replace(old_dict_user, new_dict_user)
                read_file.close()

                write_file = open('database.py', 'w')
                write_file.write(content)
                write_file.close()

                sisa_saldo.set(locale.currency(list_user[index_user]['saldo'], grouping=True))
                showinfo("Successful Top Up!", f"Your top up is equal to {locale.currency(price, grouping=True)} done!")
                root.focus_set()
                kode_valid.set("")
                selected_price.set(0)
                selected_method.set("N/A")
            else:
                showerror("Top Up Gagal!", f"Top up Anda gagal! Coba masukkan kode yang benar!")


    global saldo_frame
    saldo_frame = tk.Frame(root, bg="#171a30")
    saldo_frame.pack()


    MenuHeader(saldo_frame, "saldo")


    kode_valid = tk.StringVar()
    sisa_saldo = tk.StringVar()
    sisa_saldo.set(locale.currency(list_user[index_user]['saldo'], grouping=True))


    saldo_title = tk.Label(saldo_frame, text="Top Up", font=("Segoe UI", "30", "bold"), background="#171a30", fg="#fc094c").pack(pady=15)


    frame_pilih_nominal = tk.Frame(saldo_frame, background="#171a30")
    frame_pilih_nominal.pack(pady=15)
    selected_price = tk.IntVar(value=0)
    label_nominal_topup = tk.Label(frame_pilih_nominal, text="select amount", font=("Segoe UI", 16, "bold"), fg="#fc094c", bg="#171a30").pack(pady=5)

    tombol_50ribu = tk.Radiobutton(frame_pilih_nominal, text="Rs50.000,00", value=50000, variable=selected_price, font=("Segoe UI", 14, "bold"), image=button_price_off, selectimage=button_price_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_50ribu.pack(side="left", padx=20)
    tombol_50ribu.bind('<Enter>', lambda event, imgs=button_price_on: onhover_image(event, imgs))
    tombol_50ribu.bind('<Leave>', lambda event, imgs=button_price_off: onleave_image(event, imgs))
   
    tombol_100ribu = tk.Radiobutton(frame_pilih_nominal, text="Rs100.000,00", value=100000, variable=selected_price, font=("Segoe UI", 14, "bold"), image=button_price_off, selectimage=button_price_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_100ribu.pack(side="left", padx=20)
    tombol_100ribu.bind('<Enter>', lambda event, imgs=button_price_on: onhover_image(event, imgs))
    tombol_100ribu.bind('<Leave>', lambda event, imgs=button_price_off: onleave_image(event, imgs))

    tombol_150ribu = tk.Radiobutton(frame_pilih_nominal, text="Rs150.000,00", value=150000, variable=selected_price, font=("Segoe UI", 14, "bold"), image=button_price_off, selectimage=button_price_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_150ribu.pack(side="left", padx=20)
    tombol_150ribu.bind('<Enter>', lambda event, imgs=button_price_on: onhover_image(event, imgs))
    tombol_150ribu.bind('<Leave>', lambda event, imgs=button_price_off: onleave_image(event, imgs))

    tombol_200ribu = tk.Radiobutton(frame_pilih_nominal, text="Rs200.000,00", value=200000, variable=selected_price, font=("Segoe UI", 14, "bold"), image=button_price_off, selectimage=button_price_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_200ribu.pack(padx=20)
    tombol_200ribu.bind('<Enter>', lambda event, imgs=button_price_on: onhover_image(event, imgs))
    tombol_200ribu.bind('<Leave>', lambda event, imgs=button_price_off: onleave_image(event, imgs))    
    frame_pilih_pembayaran = tk.Frame(saldo_frame, background="#171a30")
    frame_pilih_pembayaran.pack(pady=15)
    selected_method = tk.StringVar(value="N/A")
    label_metode_pembayaran = tk.Label(frame_pilih_pembayaran, text="select the mode", font=("Segoe UI", 16, "bold"), fg="#fc094c", bg="#171a30").pack(pady=5)
  
    tombol_gopay = tk.Radiobutton(frame_pilih_pembayaran, text="GooglePay", value="gopay", variable=selected_method, font=("Segoe UI", 14, "bold"), image=button_method_off, selectimage=button_method_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_gopay.pack(side="left", padx=15)
    tombol_gopay.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_gopay.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))

    tombol_ovo = tk.Radiobutton(frame_pilih_pembayaran, text="paytm", value="ovo", variable=selected_method, font=("Segoe UI", 14, "bold"), image=button_method_off, selectimage=button_method_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_ovo.pack(side="left", padx=15)
    tombol_ovo.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_ovo.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))

    tombol_bca = tk.Radiobutton(frame_pilih_pembayaran, text="phonepay", value="bca", variable=selected_method, font=("Segoe UI", 14, "bold"), image=button_method_off, selectimage=button_method_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_bca.pack(side="left", padx=15)
    tombol_bca.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_bca.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))

    tombol_mandiri = tk.Radiobutton(frame_pilih_pembayaran, text="upi", value="mandiri", variable=selected_method, font=("Segoe UI", 14, "bold"), image=button_method_off, selectimage=button_method_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_mandiri.pack(side="left", padx=15)
    tombol_mandiri.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_mandiri.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))
 
    tombol_bni = tk.Radiobutton(frame_pilih_pembayaran, text="mobik", value="bni", variable=selected_method, font=("Segoe UI", 14, "bold"), image=button_method_off, selectimage=button_method_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_bni.pack(side="left", padx=15)
    tombol_bni.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_bni.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))

    tombol_bri = tk.Radiobutton(frame_pilih_pembayaran, text="phonewallet", value="bri", variable=selected_method, font=("Segoe UI", 14, "bold"), image=button_method_off, selectimage=button_method_on, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", selectcolor="#171a30", cursor="hand2", borderwidth=0, indicatoron=False, compound="center")
    tombol_bri.pack(padx=15)
    tombol_bri.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_bri.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))


    frame_validasi = tk.Frame(saldo_frame, background="#171a30")
    frame_validasi.pack(pady=15)
    label_kode = tk.Label(frame_validasi, text="solve these", font=("Segoe UI", 16, "bold"), fg="#fc094c", bg="#171a30").pack()
    label_kode = tk.Label(frame_validasi, text="2+2", font=("Segoe UI", 16, "bold"), fg="#fc094c", bg="#171a30").pack()
    entry_kode = tk.Entry(frame_validasi, width=26, font=("Segoe UI", 13), textvariable=kode_valid, fg="#eaebf1", border=0, bg="#171a30", insertbackground="#eaebf1")
    entry_kode.pack(pady=5)
    entry_kode.insert(0, "code")
    entry_kode.bind("<FocusIn>", lambda event: onclick_entry(event, "code"))
    entry_kode.bind("<FocusOut>", lambda event: onleave_entry(event, "code"))
    entry_kode_border = tk.Frame(frame_validasi,width=240, height=2, bg="#eaebf1").pack(pady=(0, 15))
    tombol_bayar = tk.Button(frame_validasi, text="Go", command=isValid, font=("Segoe UI", 14, "bold"), image=button_method_off, bg="#171a30", fg="#eaebf1", activeforeground="#eaebf1", activebackground="#171a30", cursor="hand2", borderwidth=0, compound="center")
    tombol_bayar.pack()
    tombol_bayar.bind('<Enter>', lambda event, imgs=button_method_on: onhover_image(event, imgs))
    tombol_bayar.bind('<Leave>', lambda event, imgs=button_method_off: onleave_image(event, imgs))



def Riwayat():

    global riwayat_frame
    riwayat_frame = tk.Frame(root, bg="#171a30")
    riwayat_frame.pack(fill="both", expand=1)

  
    MenuHeader(riwayat_frame, "riwayat")


    my_canvas = tk.Canvas(riwayat_frame, background="#171a30", bd=0, highlightthickness=0)
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(riwayat_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    scrollable_riwayat_frame = tk.Frame(my_canvas, background="#171a30")
    my_canvas.create_window((center_x_history, 0), window=scrollable_riwayat_frame, anchor="nw")
    riwayat_title = tk.Label(scrollable_riwayat_frame, text="history", font=("Segoe UI", "26", "bold"), background="#171a30", fg="#fc094c").pack(pady=20)
    tabel_frame = tk.Frame(scrollable_riwayat_frame, bg="#171a30")
    tabel_frame.pack()


    row_riwayat = len(list_user[index_user]['riwayat'])
    tabel_frame.columnconfigure(6)
    tabel_frame.rowconfigure(row_riwayat+1)
    header = ["buytime", "hall", "movie", "date and time", "Ticket", "Total"]


    for i in range(row_riwayat+1):
        if i == 0:
            for j in range(6):
                label = tk.Label(tabel_frame, text=header[j], font=("Segoe UI", 13, "bold"), bg="#fc094c", fg="#eaebf1", width=17).grid(row=i, column=j, sticky="we", ipady=7, padx=3, pady=3)
        else:
            for j in range(6):
                label = tk.Label(tabel_frame, text=list_user[index_user]['riwayat'][i-1][header[j]], font=("Segoe UI", 13, "bold"), bg="#252c54", fg="#eaebf1", width=17, wraplength=170).grid(row=i, column=j, sticky="nswe", ipady=7, ipadx=5, padx=3, pady=3) 

def ListMovie(show_type):
    def klik_img(index_movie):
        if show_type == "nowshowing":
            movielist_frame.forget()
            MovieInfoNow(index_movie)
        elif show_type == "upcoming":
            movielist_frame.forget()
            MovieInfoUpcoming(index_movie)
    def pilih_image(i, state):
        if state == "on":
            if show_type == "nowshowing":
                return now_img_on[i]
            else:
                return upcoming_img_on[i]
        else:
            if show_type == "nowshowing":
                return now_img_off[i]
            else:
                return upcoming_img_off[i]
    def pilih_title():
        if show_type == "nowshowing":
            return str("Movies Now Showing")
        else:
            return str("upcoming Movies")
    def pilih_movie(i):
        if show_type == "nowshowing":
            return f"\n{movie_now[i]['title']}\n{movie_now[i]['age']}"
        else:
            return f"\n{movie_upcoming[i]['title']}\n{movie_upcoming[i]['age']}"

    global movielist_frame
    movielist_frame = tk.Frame(root, background="#171a30")
    movielist_frame.pack()
    MenuHeader(movielist_frame, f"movielist_{show_type}")


    movielist_title = tk.Label(movielist_frame, text=pilih_title(), font=("Segoe UI", "30", "bold"), background="#171a30", fg="#fc094c").pack(ipadx=10, ipady=10, pady=10)


    fourmovie_frame = tk.Frame(movielist_frame, bg="#171a30")
    fourmovie_frame.pack()       

    for i in range(4):
        movie_frame = tk.Frame(fourmovie_frame, background="#171a30")
        movie_frame.pack(padx=20, pady=10, side="left", anchor="n")

        # Image, Title, and Genre
        movie_img = tk.Button(movie_frame, text=pilih_movie(i), command=lambda i=i: klik_img(i), image=pilih_image(i, "off"), font=("Segoe UI", 14, "bold"), cursor="hand2", bg="#171a30", fg="#eaebf1", activebackground="#171a30", activeforeground="#eaebf1", wraplength=220, bd=0, compound="top")  # type: ignore
        movie_img.pack(ipadx=5, ipady=5, anchor="n")
        movie_img.bind('<Enter>', lambda event, imgs=pilih_image(i, "on"): onhover_image(event, imgs))
        movie_img.bind('<Leave>', lambda event, imgs=pilih_image(i, "off"): onleave_image(event, imgs))
def MovieInfoNow(index_movie):
    def cek_disabled(hour, minute):
        time = time_now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if time_now >= time:
            today_time.unbind('<Enter>')
            today_time.unbind('<Leave>')
            today_time["cursor"] = ""
            today_time["state"] = "disabled"
    def InfoToBooking(index_movie, place, day, time):
        movieinfo_frame.forget()
        SeatBooking(index_movie, place, day, time)
    update_time()
    global movieinfo_frame
    movieinfo_frame = tk.Frame(root, background="#171a30")
    movieinfo_frame.pack(fill="both", expand=1)
    MenuHeader(movieinfo_frame, "movieinfo")
    my_canvas = tk.Canvas(movieinfo_frame, background="#171a30", bd=0, highlightthickness=0)
    my_canvas.pack(side="left", fill="both", expand=1)
    scroll_bar = ttk.Scrollbar(movieinfo_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")
    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    moviedesc_frame = tk.Frame(my_canvas, background="#171a30")
    my_canvas.create_window((center_x_info, 0), window=moviedesc_frame, anchor="nw")
    titlegenre_frame = tk.Frame(moviedesc_frame, background="#171a30")
    titlegenre_frame.pack()
    moviedesc_title = tk.Label(titlegenre_frame, font=("Segoe UI", "18", "bold"), text=movie_now[index_movie]["title"], background="#171a30", fg="#fc094c").pack()
    moviedesc_genre = tk.Label(titlegenre_frame, font=("Segoe UI", "14", "bold"), text=movie_now[index_movie]["genre"], background="#171a30", fg="#eaebf1").pack()
    moviedesc_duration = tk.Label(titlegenre_frame, font=("Segoe UI", "14", "bold"), text=movie_now[index_movie]["duration"], background="#171a30", fg="#eaebf1").pack()
    img_and_buy_frame = tk.Frame(moviedesc_frame, background="#171a30")
    img_and_buy_frame.pack(anchor="w", padx=10, pady=20)
    movie_img = tk.Label(img_and_buy_frame, image=now_img_on[index_movie], relief="flat", bg="#171a30", bd=0).pack(side="left")
    buy_frame = tk.Frame(img_and_buy_frame, background="#171a30")
    buy_frame.pack(side="right", padx=40)
    buy_frame.rowconfigure(9, weight=1)
    buy_frame.columnconfigure(5, weight=1)
    for i in range(3):
        loc_title = tk.Label(buy_frame, text=location[i], background="#171a30", font=("Segoe UI", "12", "bold"), fg="#fc094c").grid(row=0+3*i, column=0, columnspan=5, sticky="w", pady=(10, 0))
        today_label = tk.Label(buy_frame, text=today_date, background="#171a30", font=("Segoe UI", "11", "bold"), fg="#eaebf1").grid(row=1+3*i, column=0, padx=(0, 5))
        for j in range(4):
            today_time = tk.Button(buy_frame, text=time_str[j], image=button_time_off, command=lambda i=i, j=j: InfoToBooking(index_movie, location[i], today_date, time_str[j]), fg="#eaebf1", background="#171a30", activebackground="#171a30", activeforeground="#eaebf1", font=("Segoe UI", "11", "bold"), borderwidth=0, cursor="hand2", compound="center")
            today_time.bind('<Enter>', lambda event, imgs=button_time_on: onhover_image(event, imgs))
            today_time.bind('<Leave>', lambda event, imgs=button_time_off: onleave_image(event, imgs))
            cek_disabled(time_int[j]["hour"], time_int[j]["minute"])
            today_time.grid(row=1+3*i, column=j+1, padx=5, pady= 4)

        tomorrow_label = tk.Label(buy_frame, text=tomorrow_date, background="#171a30", font=("Segoe UI", "11", "bold"), fg="#eaebf1").grid(row=2+3*i, column=0, padx=(0, 5))
        for j in range(4):
            tomorrow_time = tk.Button(buy_frame, text=time_str[j], image=button_time_off, command=lambda i=i, j=j: InfoToBooking(index_movie, location[i], tomorrow_date, time_str[j]), fg="#eaebf1", background="#171a30", activebackground="#171a30", activeforeground="#eaebf1", font=("Segoe UI", "11", "bold"), borderwidth=0, cursor="hand2", compound="center")
            tomorrow_time.bind('<Enter>', lambda event, imgs=button_time_on: onhover_image(event, imgs))
            tomorrow_time.bind('<Leave>', lambda event, imgs=button_time_off: onleave_image(event, imgs))
            tomorrow_time.grid(row=2+3*i, column=j+1, padx=5, pady= 4)
    movie_plot_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_plot = tk.Label(movie_plot_frame, wraplength=980, justify="left", text=movie_now[index_movie]["plot"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_plot_frame.pack(anchor="w", padx=10, pady=10)
    movie_prod_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_prod_title = tk.Label(movie_prod_frame, text="Producer", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_prod = tk.Label(movie_prod_frame, text=movie_now[index_movie]["producer"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_prod_frame.pack(anchor="w", padx=10, pady=10)


    movie_director_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_director = tk.Label(movie_director_frame, text=movie_now[index_movie]["director"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_director_frame.pack(anchor="w", padx=10, pady=10)


    movie_writer_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_writer = tk.Label(movie_writer_frame, text=movie_now[index_movie]["writer"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_writer_frame.pack(anchor="w", padx=10, pady=10)
    movie_cast_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Segoe UI", "13", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_cast = tk.Label(movie_cast_frame, wraplength=980, justify="left",text=movie_now[index_movie]["cast"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_cast_frame.pack(anchor="w", padx=10, pady=10)

def MovieInfoUpcoming(index_movie):

    global movie_upcoming_frame
    movie_upcoming_frame = tk.Frame(root, background="#171a30")
    movie_upcoming_frame.pack(fill="both", expand=1)


    MenuHeader(movie_upcoming_frame, "movie_upcoming")

    my_canvas = tk.Canvas(movie_upcoming_frame, background="#171a30", bd=0, highlightthickness=0)
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(movie_upcoming_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


    moviedesc_frame = tk.Frame(my_canvas, background="#171a30")

    my_canvas.create_window((center_x_info, 0), window=moviedesc_frame, anchor="nw")


    titlegenre_frame = tk.Frame(moviedesc_frame, background="#171a30")
    titlegenre_frame.pack()
    moviedesc_title = tk.Label(titlegenre_frame, font=("Segoe UI", "18", "bold"), text=movie_upcoming[index_movie]["title"], background="#171a30", fg="#fc094c").pack()
    moviedesc_genre = tk.Label(titlegenre_frame, font=("Segoe UI", "14", "bold"), text=movie_upcoming[index_movie]["genre"], background="#171a30", fg="#eaebf1").pack()
    moviedesc_duration = tk.Label(titlegenre_frame, font=("Segoe UI", "14", "bold"), text=movie_upcoming[index_movie]["duration"], background="#171a30", fg="#eaebf1").pack()

  
    img_and_buy_frame = tk.Frame(moviedesc_frame, background="#171a30")
    img_and_buy_frame.pack(padx=10, pady=20)
    movie_img = tk.Label(img_and_buy_frame, image=upcoming_img_on[index_movie], relief="flat", bg="#171a30", bd = 0).pack()

 
    movie_plot_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_plot = tk.Label(movie_plot_frame, wraplength=980, justify="left", text=movie_upcoming[index_movie]["plot"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_plot_frame.pack(anchor="w", padx=10, pady=10)


    movie_prod_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_prod_title = tk.Label(movie_prod_frame, text="Producer", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_prod = tk.Label(movie_prod_frame, text=movie_upcoming[index_movie]["producer"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_prod_frame.pack(anchor="w", padx=10, pady=10)


    movie_director_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_director = tk.Label(movie_director_frame, text=movie_upcoming[index_movie]["director"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_director_frame.pack(anchor="w", padx=10, pady=10)


    movie_writer_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Segoe UI", "12", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_writer = tk.Label(movie_writer_frame, text=movie_upcoming[index_movie]["writer"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_writer_frame.pack(anchor="w", padx=10, pady=10)

    movie_cast_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Segoe UI", "13", "bold"), background="#171a30", fg="#fc094c").pack(anchor=tk.W)
    movie_cast = tk.Label(movie_cast_frame, wraplength=980, justify="left",text=movie_upcoming[index_movie]["cast"], background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    movie_cast_frame.pack(anchor="w", padx=10, pady=10)



def SeatBooking(index_movie, place, day, time):
    # Initialization
    # Jumlah Kursi Dipilih
    global count_seat
    count_seat = 0
    text_var_ticket = tk.StringVar()
    text_var_ticket.set("Tickets: 0")


    nominal_saldo = list_user[index_user]['saldo']
    str_saldo = locale.currency(nominal_saldo, grouping=True)


    global total_payment
    total_payment = 0
    price = movie_now[index_movie]['price']
    str_total = tk.StringVar()
    str_total.set("Total Payment: Rp0")


    list_seat = []
    str_seat = "Seats: -"
    text_var_seat = tk.StringVar()
    text_var_seat.set(str_seat)
    picked_seat_ij = [[0 for j in range(15)] for i in range(9)]
    

    def clicked_seat(par, i, j, x, y):
        # Menambah Count Seat
        global count_seat
        picked_seat = x + y
        if par.get() == 1:
            count_seat += 1
            list_seat.append(picked_seat)
            picked_seat_ij[i][j] = True
        elif par.get() == 0:
            count_seat -= 1
            list_seat.remove(picked_seat)
            picked_seat_ij[i][j] = False
        text_var_ticket.set(f"Tickets: {count_seat}")

  
        global total_payment
        total_payment = count_seat*price
        str_total.set(f"Total Payment: {locale.currency(total_payment, grouping=True)}")


        list_seat.sort()
        str_seat = "Seats: "+str(list_seat).replace("[", "").replace("]", "").replace("'", "")
        text_var_seat.set(str_seat)


        if count_seat > 0:
            confirm_button['state'] =  "normal"
            confirm_button['cursor'] = "hand2"
            confirm_button.bind('<Enter>', lambda event, imgs=confirm_on: onhover_image(event, imgs))
            confirm_button.bind('<Leave>', lambda event, imgs=cancelconfirm_off: onleave_image(event, imgs))
        else:
            confirm_button['state'] = "disabled"
            confirm_button['cursor'] = ""
            confirm_button.unbind('<Enter>')
            confirm_button.unbind('<Leave>')
            str_seat = "Seats: -"
            text_var_seat.set(str_seat)
    

    def click_confirm():
        if nominal_saldo <  total_payment:
            showerror(title="Saldo Tidak Cukup", message="Anda kekurangan saldo! Silahkan toup terlebih dahulu")
        else:
            confirmation = askyesno(title='Confirmation', message='Are you sure of your purchase?')
            if confirmation:
        
                update_time()

             
                read_file = open('database.py', 'r')
                content = read_file.read()
                old_dict_user = str(list_user[index_user])
                dict_riwayat = {
                    'buytime': f"{hour_minute_now} {today_date}",
                    'hall': f"{place}\nStudio {index_movie+1}",
                    'movie': movie_now[index_movie]['title'],
                    'date and time': f"{time} {day}",
                    'Ticket': text_var_seat.get().replace("Seats: ", ""),
                    'Total': locale.currency(total_payment, grouping=True)
                }
                list_user[index_user]['riwayat'].append(dict_riwayat)
                list_user[index_user]['saldo'] -= total_payment
                new_dict_user = str(list_user[index_user])
                content = content.replace(old_dict_user, new_dict_user)
                read_file.close()

                write_file = open('database.py', 'w')
                write_file.write(content)
                write_file.close()

         
                read_file = open('database.py', 'r')
                content = read_file.read()
                old_dict_seat = str(movie_now[index_movie]["sold_seat"])
                for i in range(9):
                    for j in range(15):
                        if picked_seat_ij[i][j] == True:
                            movie_now[index_movie]['sold_seat'][f"{place}_{index_movie}"][day][time][i][j] = True
                new_dict_seat = str(movie_now[index_movie]["sold_seat"])
                content = content.replace(old_dict_seat, new_dict_seat)
                read_file.close()

                write_file = open('database.py', 'w')
                write_file.write(content)
                write_file.close()

      
                booking_frame.forget()
                Riwayat()


    def click_cancel():
        confirmation = askyesno(title='Confirmation', message='Are you sure to cancel booking?')
        if confirmation:
            booking_frame.forget()
            MovieInfoNow(index_movie)


    global booking_frame
    booking_frame = tk.Frame(root, background="#171a30")
    booking_frame.pack(fill="both", expand=1)


    MenuHeader(booking_frame, "booking")  

    my_canvas = tk.Canvas(booking_frame, background="#171a30", bd=0, highlightthickness=0)
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(booking_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")
    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    scrollable_frame = tk.Frame(my_canvas, background="#171a30")
    my_canvas.create_window((center_x_seat, 0), window=scrollable_frame, anchor="nw")
    information_frame = tk.Frame(scrollable_frame, background="#171a30")
    information_frame.pack(anchor="w", fill="x")


    icon_frame = tk.Frame(information_frame, background="#171a30")
    icon_frame.pack(anchor="w")
    seat_free_img = tk.Label(icon_frame, image=seat_free, background="#171a30").pack(side="left")
    seat_fre_label = tk.Label(icon_frame, text="Available", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(side="left", padx=(0, 15))
    seat_own_img = tk.Label(icon_frame, image=seat_own, background="#171a30").pack(side="left")
    seat_own_label = tk.Label(icon_frame, text="Picked Seat", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(side="left", padx=(0, 15))
    seat_sold_img = tk.Label(icon_frame, image=seat_sold, background="#171a30").pack(side="left")
    seat_sold_label = tk.Label(icon_frame, text="Sold", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(padx=(0, 10))


    separator = ttk.Separator(information_frame, orient='horizontal').pack(fill='x', pady=10)


    data_frame = tk.Frame(information_frame, background="#171a30")
    data_frame.pack(anchor=tk.W)
    book_title = tk.Label(data_frame, text=movie_now[index_movie]["title"], background="#171a30", fg="#fc094c", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    seat_list = tk.Label(data_frame, textvariable=text_var_seat, wraplength=510, justify="left", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    num_ticket = tk.Label(data_frame, textvariable=text_var_ticket, background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    location = tk.Label(data_frame, text=place, background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    studio = tk.Label(data_frame, text=f"Studio: {index_movie+1}", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    date = tk.Label(data_frame, text=f"{day}, Time: {time}", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    total = tk.Label(data_frame, textvariable=str_total, background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)
    saldo = tk.Label(data_frame, text=f"Saldo Anda: {str_saldo}", background="#171a30", fg="#eaebf1", font=("Segoe UI", "11", "bold")).pack(anchor=tk.W)


    separator = ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=10)

 
    seat_frame = tk.Frame(scrollable_frame, background="#171a30")
    seat_frame.pack()
    seat_frame.rowconfigure((9), weight=1)
    seat_frame.columnconfigure(15, weight=1)


    try: 
        temp = movie_now[index_movie]["sold_seat"][f"{place}_{index_movie}"][day]
    except:
        read_file = open('database.py', 'r')
        content = read_file.read()
        old_dict_place = str(movie_now[index_movie]["sold_seat"])
        movie_now[index_movie]["sold_seat"][f"{place}_{index_movie}"].update({day: {}})
        movie_now[index_movie]["sold_seat"][f"{place}_{index_movie}"][day].update({time: [[0 for i in range(15)] for j in range(9)]})
        new_dict_place = str(movie_now[index_movie]["sold_seat"])
        content = content.replace(old_dict_place, new_dict_place)
        read_file.close()

        write_file = open('database.py', 'w')
        write_file.write(content)
        write_file.close()
    else:
        try: 
            temp = movie_now[index_movie]["sold_seat"][f"{place}_{index_movie}"][day][time]
        except:
            read_file = open('database.py', 'r')
            content = read_file.read()
            old_dict_place = str(movie_now[index_movie]["sold_seat"])
            movie_now[index_movie]["sold_seat"][f"{place}_{index_movie}"][day].update({time: [[0 for i in range(15)] for j in range(9)]})
            new_dict_place = str(movie_now[index_movie]["sold_seat"])
            content = content.replace(old_dict_place, new_dict_place)
            read_file.close()

            write_file = open('database.py', 'w')
            write_file.write(content)
            write_file.close()


    for i in range(9):
        for j in range(15):
            if i == 0: 
                if j < 7:
                    item = tk.Label(seat_frame, text=f"{j+1}", background="#171a30", fg="#eaebf1", font=("Segoe UI", "12", "bold")).grid(row=i, column=j)
                elif j > 7:
                    item = tk.Label(seat_frame, text=f"{j}", background="#171a30", fg="#eaebf1", font=("Segoe UI", "12", "bold")).grid(row=i, column=j)
            elif j == 7: 
                item = tk.Label(seat_frame, text=f"{chr(ord('A')+i-1)}", background="#171a30", fg="#eaebf1", font=("Segoe UI", "12", "bold")).grid(row=i, column=j)
            else: 
                if movie_now[index_movie]["sold_seat"][f"{place}_{index_movie}"][day][time][i][j]: # Jika Sold
                    item = tk.Label(seat_frame, image=seat_sold, background="#171a30").grid(row=i, column=j)
                else: 
               
                    x_seat = ""
                    if j < 7:
                        x_seat = str(j+1)
                    elif j > 7:
                        x_seat = str(j)
                    y_seat = f"{chr(ord('A')+i-1)}"
                    seat_var = tk.IntVar()
                    
                  
                    item = tk.Checkbutton(seat_frame, variable=seat_var, onvalue=1, offvalue=0, command=lambda num=seat_var, i=i, j=j, y=y_seat, x=x_seat: clicked_seat(num, i, j, y, x), indicatoron=False, image=seat_free, selectimage=seat_own, cursor="hand2", background="#171a30", borderwidth=0, selectcolor="#171a30", activebackground="#171a30")
                    item.bind('<Enter>', lambda event, imgs=seat_own: onhover_image(event, imgs))
                    item.bind('<Leave>', lambda event, imgs=seat_free: onleave_image(event, imgs))
                    item.grid(row=i, column=j, padx=3, pady=3)

   
    screen = tk.Label(seat_frame, image=screen_img, background="#171a30").grid(row=11, column=0, columnspan=15, pady=(8,0))


    separator = ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=10)


    button_frame = tk.Frame(scrollable_frame, background="#171a30")
    button_frame.pack(pady=(10, 25))

    confirm_button = tk.Button(button_frame, text="Confirm Order", command=click_confirm, font=("Segoe UI", "13", "bold"), image=cancelconfirm_off, state="disabled" , fg="#eaebf1", background="#171a30", activebackground="#171a30", activeforeground="#eaebf1", borderwidth=0, compound="center")
    confirm_button.pack(side="left",padx=10)
  
    cancel_button = tk.Button(button_frame, text="Cancel", command= click_cancel, font=("Segoe UI", "13", "bold"), image=cancelconfirm_off, fg="#eaebf1", background="#171a30", activebackground="#171a30", activeforeground="#eaebf1", borderwidth=0, cursor="hand2", compound="center")
    cancel_button.bind('<Enter>', lambda event, imgs=cancel_on: onhover_image(event, imgs))
    cancel_button.bind('<Leave>', lambda event, imgs=cancelconfirm_off: onleave_image(event, imgs))
    cancel_button.pack(side="right", padx=10)
Login()

root.mainloop()
