import random
import string
from tkinter import *
from tkinter import ttk
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas Seguras")
        self.root.geometry("400x450")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.password_length = IntVar(value=12)
        self.password_var = StringVar()
        
        # Main Frame
        main_frame = Frame(root, bg='#f0f0f0', pady=20, padx=20)
        main_frame.pack(expand=True, fill='both')
        
        # Length Frame
        length_frame = LabelFrame(main_frame, text="Longitud de la Contraseña", bg='#f0f0f0', pady=10, padx=10)
        length_frame.pack(fill='x', pady=10)
        
        length_scale = Scale(length_frame, from_=8, to=32, orient=HORIZONTAL,
                           variable=self.password_length, bg='#f0f0f0')
        length_scale.pack(fill='x')
        
        # Button Frame
        btn_frame = Frame(main_frame, bg='#f0f0f0')
        btn_frame.pack(pady=10)
        
        generate_btn = ttk.Button(btn_frame, text="Generar Contraseña",
                                command=self.generate_password)
        generate_btn.pack(pady=5)
        
        # Password Display Frame
        display_frame = LabelFrame(main_frame, text="Contraseña Generada", bg='#f0f0f0', pady=10, padx=10)
        display_frame.pack(fill='x', pady=10)
        
        self.password_label = Entry(display_frame, textvariable=self.password_var,
                                  font=('Courier', 12), justify='center', state='readonly')
        self.password_label.pack(fill='x', pady=5)
        
        copy_btn = ttk.Button(display_frame, text="Copiar al Portapapeles",
                            command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)
        
        # Strength Indicator
        self.strength_var = StringVar(value="Fuerza: N/A")
        self.strength_label = Label(main_frame, textvariable=self.strength_var,
                                  bg='#f0f0f0', font=('Arial', 10))
        self.strength_label.pack(pady=5)
        
    def generate_password(self):
        length = self.password_length.get()
        
        # Ensure at least one of each character type
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice(string.punctuation)
        
        # Generate remaining characters
        remaining_length = length - 4
        all_chars = string.ascii_letters + string.digits + string.punctuation
        remaining_chars = ''.join(random.choice(all_chars) for _ in range(remaining_length))
        
        # Combine and shuffle
        password_list = list(lowercase + uppercase + digit + symbol + remaining_chars)
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        self.password_var.set(password)
        self.update_strength_indicator(password)
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
    
    def update_strength_indicator(self, password):
        score = 0
        feedback = []
        
        if len(password) >= 12:
            score += 1
            feedback.append("Longitud buena")
        if any(c.isupper() for c in password):
            score += 1
            feedback.append("Mayúsculas")
        if any(c.islower() for c in password):
            score += 1
            feedback.append("Minúsculas")
        if any(c.isdigit() for c in password):
            score += 1
            feedback.append("Números")
        if any(c in string.punctuation for c in password):
            score += 1
            feedback.append("Símbolos")
            
        strength = {
            0: ("Muy Débil", "red"),
            1: ("Débil", "red"),
            2: ("Moderada", "orange"),
            3: ("Fuerte", "light green"),
            4: ("Muy Fuerte", "green"),
            5: ("Excelente", "dark green")
        }
        
        strength_text, _ = strength[score]
        self.strength_var.set(f"Fuerza: {strength_text} ({', '.join(feedback)})")

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()