import feedparser
from tkinter import *
import webview

def default_color_button():
    btn_son_dakika.configure(bg="lightblue")
    btn_ekonomi.configure(bg="lightblue")
    btn_dunya.configure(bg="lightblue")
    btn_saglik.configure(bg="lightblue")

def clear_frame():
    for winget in fr_haberler.winfo_children():
        winget.destroy()
def open_url(event):
    webview.create_window(event.widget.cget("text"),event.widget.cget("text"))
    webview.start()
def add_haberler(haberler):
    haber_caunt=0
    for haber in haberler.entries:
        haber_caunt = haber_caunt + 1
        if haber_caunt > 2:
            break
        Label(fr_haberler,text=haber.title,anchor="w",font=("Helveticabold",14)).pack(side=TOP,fill="x")
        lbl_link=Label(fr_haberler,text=haber.link,anchor="w",font=("Helveticabold",14),fg="blue",cursor="hand2")
        lbl_link.pack(side=TOP,fill="x")
        lbl_link.bind("<Button-1>",open_url)
        Label(fr_haberler,text="--",anchor="c",bg="pink").pack(side=TOP,fill="x")

def son_dakika_command():
    clear_frame()
    default_color_button()
    btn_son_dakika.configure(bg="green")
    for url in son_dakika_url:
        haberler=feedparser.parse(url)
        add_haberler(haberler)

def dunya_command():
    clear_frame()
    default_color_button()
    btn_dunya.configure(bg="green")

    for url in son_ekonomi_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)
def ekonomi_command():
    clear_frame()
    default_color_button()
    btn_ekonomi.configure(bg="green")

    for url in son_dunya_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)
def saglik_command():
    clear_frame()
    default_color_button()
    btn_saglik.configure(bg="green")
    for url in son_saglık_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)
def instegram_command():
    for url in inst_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

son_dakika_url=["https://haberglobal.com.tr/rss/son-dakika",
                "https://www.ntv.com.tr/son-dakika.rss",
                "https://www.sozcu.com.tr/feeds-son-dakika"]
son_ekonomi_url=["https://haberglobal.com.tr/rss/ekonomi",
                "https://www.ntv.com.tr/ekonomi.rss",
                "https://www.sozcu.com.tr/feeds-rss-category-ekonomi"]
son_dunya_url=["https://haberglobal.com.tr/rss/dunya",
                "https://www.ntv.com.tr/dunya.rss",
                "https://www.sozcu.com.tr/feeds-rss-category-dunyadan-spor"]
son_saglık_url=["https://haberglobal.com.tr/rss/saglik",
                "https://www.ntv.com.tr/saglik.rss",
                "https://www.sozcu.com.tr/feeds-rss-category-saglik"]
inst_url=["https://www.instagram.com/"]



window=Tk()
window.title("Haber Bot Programı")
window.geometry("1000x600")

fr_haberler=Frame(window,height=600)
fr_buttons=Frame(window,relief=RAISED,bg="pink",bd=2)

btn_son_dakika=Button(fr_buttons,text="Son Dakika",font=("Halveticabold",14),bg="lightblue",command=son_dakika_command)
btn_dunya =Button(fr_buttons,text="Dünya",font=("Halveticabold",14),bg="lightblue",command=dunya_command)
btn_ekonomi=Button(fr_buttons,text="Ekonomi",font=("Halveticabold",14),bg="lightblue",command=ekonomi_command)
btn_saglik=Button(fr_buttons,text="Sağlık",font=("Halveticabold",14),bg="lightblue",command=saglik_command)
btn_inst=Button(fr_buttons,text="İnstegram",font=("Halveticabold",14),bg="lightblue",command=instegram_command)

btn_son_dakika.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_dunya.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
btn_ekonomi.grid(row=2,column=0,sticky="ew",padx=5,pady=5)
btn_saglik.grid(row=3,column=0,sticky="ew",padx=5,pady=5)
btn_inst.grid(row=4,column=0,sticky="ew",padx=5,pady=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
fr_haberler.grid(row=0,column=1,sticky="nsew")


window.mainloop()