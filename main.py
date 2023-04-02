import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from ftplib import FTP

passwd = []

def write(ctx):
    global passwd
    ctx = ctx.decode("utf-8")
    ctx = ctx.split(";")
    passwd = ctx.copy()


ftp = FTP("<host>", "<user>", "<passwd>")
ftp.retrbinary("RETR passwords.txt", write)
ftp.close()

labels = []

for i in passwd:
    labels.append(Label(text=f"{i.split('-')[0].strip()}\n{i.split('-')[1].strip()}"))
print(labels)

class Main(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        for i in labels:
            box.add_widget(i)
        return box

app = Main()
app.run()
