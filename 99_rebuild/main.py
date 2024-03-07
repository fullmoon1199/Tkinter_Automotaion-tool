import tkinter as tk
import gui


if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    window.title("V920 SADK Verification Program")
    # window size
    window.geometry("1650x900+30+30")

    # Create the instances of the class
    Window_Tilte = gui.Window_Title(window)


    window.mainloop()