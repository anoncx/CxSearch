import os
import threading
import time

import customtkinter as ctk

# System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# App Settings
app = ctk.CTk()
app.title("CxSearch")
app.geometry("700x500")
app.resizable(height=False, width=False)
app.font = ctk.CTkFont(size=20)

delete = ctk.StringVar(value="0")

MainAFrame = ctk.CTkFrame(app, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1, height=30,
                          fg_color='transparent')
MainAFrame.pack(pady=10)

# MainMenu Text
MainText = ctk.CTkLabel(MainAFrame, text="CxSearch", font=("Trebuchet MS", 30))
MainText.pack(pady=10, padx=10)

tabview = ctk.CTkTabview(app, width=700, height=600, border_color="#00876e", border_width=2,
                         segmented_button_selected_color="#00876e")
tabview.pack(padx=20, pady=20)

tabview.add("Info")
tabview.add("Settings")
tabview.add("Start Search")

Info = tabview.tab("Info")
Settings = tabview.tab("Settings")
StartS = tabview.tab("Start Search")

tabview.set("Info")

# //////////////////////////////////////////////////// Info Tab ///////////////////////////////////////////////////////////////////////////////////////////////

InfoFrame = ctk.CTkFrame(Info, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30)
InfoFrame.pack(pady=10)

# MainInfoMenu Text
MainInfoText = ctk.CTkLabel(InfoFrame, text="[ Info ]", font=("Trebuchet MS", 15))
MainInfoText.pack(pady=10, padx=10)

# Credits
InfoCredits = ctk.CTkLabel(Info, text="[ Made By AnonCx ]",
                           font=("Trebuchet MS", 20))
InfoCredits.pack(pady=10, padx=10)


# //////////////////////////////////////////////////// Search Function ///////////////////////////////////////////////////////////////////////////////////////////////


def Search(sRoot, sKeyWord):
    Scanned = 0
    Found = 0
    rootDir = sRoot
    with open('Found.txt', 'w') as f:
        for subdir, dirs, files in os.walk(rootDir):
            for file in files:
                try:
                    if sKeyWord in file:
                        try:
                            Found = Found + 1
                            f.write("\nFound File With Name: " + file + "   At: " + subdir)
                            FoundL.configure(text=f"Found KeyWord {sKeyWord} in {Found} Files", text_color="green")
                            if delete.get() == "1":
                                try:
                                    os.remove(f"{subdir}/{file}")
                                    print("Removed")
                                except:
                                    print("Error Deleting")
                            else:
                                print("LOL HOW")
                        except:
                            Logs.configure(text="Unknown Error", text_color="red")
                    else:
                        Scanned = Scanned + 1
                        Logs.configure(text=f"Scanned {Scanned} Files", text_color="orange")
                except:
                    Logs.configure(text=f"No Access To That Folder", text_color="yellow")


# //////////////////////////////////////////////////// Search Function ///////////////////////////////////////////////////////////////////////////////////////////////


InfoFrame = ctk.CTkFrame(Settings, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30)
InfoFrame.pack(pady=10)

# MainInfoMenu Text
MainInfoText = ctk.CTkLabel(InfoFrame, text="[ Settings ]", font=("Trebuchet MS", 15))
MainInfoText.pack(pady=10, padx=10)

# rootDir Input
sPathE = ctk.CTkEntry(Settings, placeholder_text="Enter Path Of Where To Start Searching", height=38, font=app.font,
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
sPathE.pack(padx=20, pady=(0, 20))

# search Input
sWhatE = ctk.CTkEntry(Settings, placeholder_text="What To Search For", height=38, font=app.font,
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
sWhatE.pack(padx=20, pady=(0, 20))

deleteS = ctk.CTkSwitch(Settings, text="Delete Found Files", variable=delete, onvalue="1", offvalue="0",
                        progress_color="#960325")
deleteS.pack(padx=20, pady=5)

# //////////////////////////////////////////////////// Search Function ///////////////////////////////////////////////////////////////////////////////////////////////


InfoFrame = ctk.CTkFrame(StartS, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30)
InfoFrame.pack(pady=10)

# MainInfoMenu Text
MainInfoText = ctk.CTkLabel(InfoFrame, text="[ Start The Search ]", font=("Trebuchet MS", 15))
MainInfoText.pack(pady=10, padx=10)


def runThread2():
    SNButton.configure(text="Starting..")
    time.sleep(1)
    SNButton.configure(text="Start")


def runThread():
    threading.Thread(target=lambda: Search(sPathE.get(), sWhatE.get())).start()
    threading.Thread(target=runThread2).start()


# Start Button
SNButton = ctk.CTkButton(StartS, text="Start", command=runThread, border_width=1,
                         border_color=("#00ffd0", "#00876e"), fg_color='transparent', hover_color="#00876e")
SNButton.pack(padx=20, pady=10)

# MainInfoMenu Text
Logs = ctk.CTkLabel(StartS, text="", font=("Trebuchet MS", 15), text_color="grey")
Logs.pack(pady=10, padx=10)

# MainInfoMenu Text
FoundL = ctk.CTkLabel(StartS, text="", font=("Trebuchet MS", 15), text_color="grey")
FoundL.pack(pady=10, padx=10)

app.mainloop()
