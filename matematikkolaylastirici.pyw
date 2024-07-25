import time, pyperclip
import tkinter as tk
from tkinter import ttk
y = 50
by = 17

pencere = tk.Tk()
pencere.geometry("700x640")
pencere.resizable(0,0)

pencere.title("Matematik Kolay İşlem")

sayi_kont = tk.IntVar()

yazi = tk.Text(width=45, heigh = 16, font = ("Consolas",14))
yazi.place(x=15,y=195)

altli_sayi = tk.Checkbutton(text = "Altlı Sayı", variable=sayi_kont,onvalue = 1, offvalue = 0)
altli_sayi.place(x = 525, y = 210)

sayilar = (0,1,2,3,4,5,6,7,8,9)
log_sayilar = ("₀","₁","₂","₃","₄","₅","₆","₇","₈","₉")
uslu_sayilar = ("⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹")

kop_l = tk.Label()
kop_l.place(x = 535, y = 280)
                
tk.Label(text="Bazı Özel Karakterler\n↓",fg = "red", font = ("Consolas",10)).pack()
tk.Label(text="Geliştirici: CAN ÜSTÜN",fg = "red", font = ("Consolas",8)).place(x = 15,y= 605)


def basari_siz():
        kop_l["text"] = ""
        pencere.after(3500,basari_siz)

def kes_f():
        try:
                veri_k = yazi.get("1.0","end")[0:-1]
                pyperclip.copy(veri_k)
                yazi.delete("1.0","end")
                kop_l["text"] = "Kopyalandı."
                kop_l["fg"] = "green"
                
        except Exception as e:
               kop_l["text"] = "Kopyalanamadı!\n"+str(e)
               kop_l["fg"] = "red"
def ek(a):
	yazi.insert("end",a)


#---------------------------------------------------------------------------------------------
tk.Label(text = "İntegral",fg = "Black", font = ("Consolas",10)).place(x = 45, y = 27)
tk.Button(text = "∫", command=lambda:ek("∫"),width = 3,font = ("Consolas",by)).place(x=15,y=50)
tk.Button(text = "∮", command=lambda:ek("∮"),width = 3,font = ("Consolas",by)).place(x=65,y=50)
tk.Button(text = "∯", command=lambda:ek("∯"),width = 3,font = ("Consolas",by)).place(x=115,y=50)
tk.Button(text = "∰", command=lambda:ek("∰"),width = 3,font = ("Consolas",by)).place(x=15,y=97)
tk.Button(text = "⨍", command=lambda:ek("⨍"),width = 3,font = ("Consolas",by)).place(x=65,y=97)
tk.Button(text = "⨏", command=lambda:ek("⨏"),width = 3,font = ("Consolas",by)).place(x=115,y=97)
tk.Button(text = "⨒", command=lambda:ek("⨒"),width = 3,font = ("Consolas",by)).place(x=15,y=144)
tk.Button(text = "∱", command=lambda:ek("∱"),width = 3,font = ("Consolas",by)).place(x=65,y=144)
tk.Button(text = "⨓", command=lambda:ek("⨓"),width = 3,font = ("Consolas",by)).place(x=115,y=144)

#---------------------------------------------------------------------------------------------
tk.Label(text = "Geometrik",fg = "Black", font = ("Consolas",10)).place(x = 225, y = 27)
tk.Button(text = "⌀", command=lambda:ek("⌀"),width = 3,font = ("Consolas",by)).place(x=185,y=50)
tk.Button(text = "⊥", command=lambda:ek("⊥"),width = 3,font = ("Consolas",by)).place(x=235,y=50)
tk.Button(text = "°", command=lambda:ek("°"),width = 3,font = ("Consolas",by)).place(x=285,y=50)
tk.Button(text = "∝", command=lambda:ek("∝"),width = 3,font = ("Consolas",by)).place(x=185,y=97)
tk.Button(text = "⋕", command=lambda:ek("⋕"),width = 3,font = ("Consolas",by)).place(x=235,y=97)
tk.Button(text = "∺", command=lambda:ek("∺"),width = 3,font = ("Consolas",by)).place(x=285,y=97)
tk.Button(text = "∦", command=lambda:ek("∦"),width = 3,font = ("Consolas",by)).place(x=185,y=144)
tk.Button(text = "∥", command=lambda:ek("∥"),width = 3,font = ("Consolas",by)).place(x=235,y=144)
tk.Button(text = "∢", command=lambda:ek("∢"),width = 3,font = ("Consolas",by)).place(x=285,y=144)


#---------------------------------------------------------------------------------------------
tk.Label(text = "      Küme",fg = "Black", font = ("Consolas",10)).place(x = 365, y = 27)
tk.Button(text = "{}", command=lambda:ek("{}"),width = 3,font = ("Consolas",by)).place(x=355,y=50)
tk.Button(text = "⊂", command=lambda:ek("⊂"),width = 3,font = ("Consolas",by)).place(x=406,y=50)
tk.Button(text = "⊃", command=lambda:ek("⊃"),width = 3,font = ("Consolas",by)).place(x=455,y=50)
tk.Button(text = "∋", command=lambda:ek("∋"),width = 3,font = ("Consolas",by)).place(x=355,y=97)
tk.Button(text = "∌", command=lambda:ek("∌"),width = 3,font = ("Consolas",by)).place(x=405,y=97)
tk.Button(text = "⊄", command=lambda:ek("⊄"),width = 3,font = ("Consolas",by)).place(x=455,y=97)
tk.Button(text = "⋳", command=lambda:ek("⋳"),width = 3,font = ("Consolas",by)).place(x=355,y=144)
tk.Button(text = "⋵", command=lambda:ek("⋵"),width = 3,font = ("Consolas",by)).place(x=405,y=144)
tk.Button(text = "⊎", command=lambda:ek("⊎"),width = 3,font = ("Consolas",by)).place(x=455,y=144)


#---------------------------------------------------------------------------------------------
tk.Label(text = "   Karışık",fg = "Black", font = ("Consolas",10)).place(x = 550, y = 27)
tk.Button(text = "∞", command=lambda:ek("∞"),width = 3,font = ("Consolas",by)).place(x=525,y=50)
tk.Button(text = "√", command=lambda:ek("√"),width = 3,font = ("Consolas",by)).place(x=575,y=50)
tk.Button(text = "π", command=lambda:ek("π"),width = 3,font = ("Consolas",by)).place(x=625,y=50)
tk.Button(text = "lne", command=lambda:ek("lne"),width = 3,font = ("Consolas",by)).place(x=525,y=97)
tk.Button(text = "ⁿ", command=lambda:ek("ⁿ"),width = 3,font = ("Consolas",by)).place(x=575,y=97)
tk.Button(text = "≠", command=lambda:ek("≠"),width = 3,font = ("Consolas",by)).place(x=625,y=97)
tk.Button(text = "∿", command=lambda:ek("∿"),width = 3,font = ("Consolas",by)).place(x=525,y=144)
tk.Button(text = "<", command=lambda:ek("<"),width = 3,font = ("Consolas",by)).place(x=575,y=144)
tk.Button(text = ">", command=lambda:ek(">"),width = 3,font = ("Consolas",by)).place(x=625,y=144)

tk.Button(text = "✂ Metni Kes ✂", command = kes_f).place(x = 525, y = 250)


def tikladim():
	
	metin = yazi.get(1.0, "end-1c")
	ekle = ""
	if metin [-1] == "f":
		ekle = "(x) = "
	elif metin[-1] == "l":
		ekle = "og"
	elif metin[-1] == "c":
		ekle = "os( )"
                                
	try:
		uslu_sayi = int(metin[-1])
		
		yazi.delete("1.0","end")
		yazi.insert("end",metin[0:-1])
		sira = 0
		for i in sayilar:
			if uslu_sayi == i:
				if sayi_kont.get():
					ekle = str(log_sayilar[sira])

				else:
					ekle = str(uslu_sayilar[sira])
				break
			sira+=1
	except:pass
	
	yazi.insert("end",ekle)
	
a = tk.Button(text="",command = tikladim, font = ("Consolas",10))
a.place(x=15,y=555)

def kontrol():
                try:
                        metin = yazi.get(1.0, "end-1c")[-1]
                except:
                        metin = ""

                a["font"] = ("Consolas",10)
                if metin != "f" and metin != "l" and metin != "c":
                        a["text"] = "Tahminler Burada Gözükecek"
                else:
                        if metin == "f":
                                a["text"] = "f(x) = "
                        
                        elif metin == "l":
                                a["text"] = 'log'

                        elif metin == "c":
                                a["text"] = "cos( )"
                        
                        
                try:
                        sayi = int(metin)
                        sira = 0
                        for i in sayilar:
                                if sayi == i:
                                        if sayi_kont.get():
                                                a["text"] = str(log_sayilar[sira])
                                        else:
                                                a["text"] = str(uslu_sayilar[sira])
                                        a["font"] = ("Consolas",17)
                                        break
                                        
                                sira+=1
                except:
                	pass
	
                pencere.after(100,kontrol)

kontrol()
basari_siz()
pencere.mainloop()
