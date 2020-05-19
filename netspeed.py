import tkinter as tk
from tkinter import *
from tkinter import font as tkFont
import pyspeedtest
import click


st=pyspeedtest.SpeedTest()

window = tk.Tk()
window.title("SPEEDTEST")

framea=tk.Frame(master=window,
 relief=RAISED,
 height=10,
 borderwidth=5
)

but=tk.Button(text="CHECK SPEED",
 font = ("Helvetica", 30),
 bg="red",
 fg="white",
 master=framea,
 activebackground='green',
 activeforeground='white',
)

load_lbl=tk.Label(text="Press the button and please wait for some time",
 bg="#fa00d9",
 fg="white",
 font = ("Helvetica", 15),
 height=1
)

ping_lbl=tk.Label(text="Ping",
 height=2,
 width=40,
 bg="#622eff",
 font = ("Helvetica", 20),
 fg="white"
)

down_lbl=tk.Label(text="Download speed",
 height=2,
 width=40,
 bg="#622eff",
 font = ("Helvetica", 20),
 fg="white"
)

up_lbl=tk.Label(text="Upload speed",
 height=2,
 width=40,
 bg="#622eff",
 font = ("Helvetica", 20),
 fg="white"
)


@click.group()
def cli():
    pass


@cli.command()
def run():

    framea.pack(fill=tk.X)
    load_lbl.pack(fill=tk.X)
    but.bind("<Button-1>",speed)
    but.pack(fill=tk.X)
    ping_lbl.pack(fill=tk.X)
    down_lbl.pack(fill=tk.X)
    up_lbl.pack(fill=tk.X)

    window.mainloop()


def speed(event):
    ping=st.ping()
    downs=st.download()
    ups=st.upload()
    but["bg"]="green"
    ping_lbl["text"]=str(ping)+" ms"
    down_lbl["text"]=str(float(downs/1024/1024))+" Mbps"
    up_lbl["text"]=str(float(ups/1024))+" Kbps"
    load_lbl["text"]="DONE"
