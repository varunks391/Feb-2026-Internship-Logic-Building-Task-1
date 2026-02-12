Python Tkinter Code for Your Prototype
import tkinter as tk
from tkinter import messagebox

class TravelGuruApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Travel Guru")
        self.geometry("400x600")
        
        # Container for all frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        for F in (SplashScreen, WelcomeScreen, HelpSettingsScreen, DestinationScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(SplashScreen)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Travel Guru", font=("Arial", 24)).pack(pady=50)
        tk.Button(self, text="Get Started", command=lambda: controller.show_frame(WelcomeScreen)).pack()

class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Welcome", font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text="Finds your perfect destination").pack(pady=10)
        
        tk.Entry(self, width=30).pack(pady=10)
        tk.Button(self, text="Search", command=lambda: controller.show_frame(DestinationScreen)).pack(pady=10)
        
        tk.Label(self, text="Example: Hampi Stone Chariot").pack(pady=20)
        tk.Button(self, text="Help & Settings", command=lambda: controller.show_frame(HelpSettingsScreen)).pack(side="bottom", pady=20)

class HelpSettingsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="? Help", font=("Arial", 18)).pack(pady=20)
        tk.Label(self, text="Settings", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(WelcomeScreen)).pack(pady=20)

class DestinationScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Hampi Stone Chariot", font=("Arial", 20)).pack(pady=10)
        description = (
            "Hampi, in the Indian state of Karnataka, is a UNESCO World Heritage site.\n"
            "It was once the thriving capital of the Vijayanagara Empire.\n"
            "Hampi is renowned for its stunning architecture and ancient ruins.\n"
            "Visitors can explore majestic temples, palaces, and intricate carvings."
        )
        tk.Label(self, text=description, wraplength=350, justify="left").pack(pady=20)
        tk.Button(self, text="Book Now", command=lambda: messagebox.showinfo("Booking", "Booking confirmed!")).pack(pady=20)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(WelcomeScreen)).pack(pady=10)

if __name__ == "__main__":
    app = TravelGuruApp()
    app.mainloop()
