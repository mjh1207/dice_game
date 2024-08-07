from tkinter import BOTH, Tk, Canvas, Button, Label, Frame

class GameWindow:
    def __init__(self, width=800, height=800):
        self._primary_color = "#f0e399"
        
        # Game window
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Dice!")
        self.root.configure(bg="#f0e399")
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        # Canvas and header
        self.canvas = Canvas(self.root, bg=self._primary_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.header = Label(self.canvas, text="Welcome to Dice!", width=width, font=("Arial", 24), bg=self._primary_color)
        self.header.pack()

        # How to play and new game buttons
        self.footer_frame = Frame(self.canvas, bg="#f0e399")
        self.footer_frame.pack(side="bottom")
        self.help_button = Button(self.footer_frame, text="How to play",font=("Arial", 16), bg="white",)
        self.new_game_button = Button(self.footer_frame, text="New Game", font=("Arial", 16), bg="white")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.help_button.grid(row=0, column=0, padx=5, pady=10)
        self.new_game_button.grid(row=0, column=1, padx=5, pady=10)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Closing Game...")
    
    def close(self):
        self.running = False

