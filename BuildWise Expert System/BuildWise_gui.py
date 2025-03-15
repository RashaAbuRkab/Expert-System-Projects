import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Import your fuzzy logic system functions
from expert_system_code import define_variables, define_rules, build_control_system, simulate_control_system

class FuzzyLogicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuzzy Logic Damage Assessment System")
        self.root.geometry("800x600")  # Adjusted width to fit inputs and outputs side by side
        self.root.configure(bg="#f0f0f0")  # Background color of the window

        # Define variables and rules
        self.variables = define_variables()
        self.rules = define_rules(*self.variables)
        self.control_simulation = build_control_system(self.rules)

        # Create input fields (left side of the window)
        self.create_input_fields()

        # Create output fields (right side of the window)
        self.create_output_fields()

        # Create buttons (below the output fields)
        self.create_buttons()

    def create_input_fields(self):
        """Create input fields on the left side of the window."""
        input_frame = ttk.LabelFrame(self.root, text="Input Parameters", padding="20")
        input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.input_entries = {}
        inputs = [
            ('Foundation', 0.8),
            ('Earth_Stability', 0.7),
            ('Basic_Facilities', 0.6),
            ('Number_of_Floors', 5),
            ('Building_Age', 20),
            ('Material_Type', 0.8),
            ('Exposure_to_Bombing', 0.4),
            ('Wall_Stability', 0.9),
            ('Roof_Condition', 0.75),
            ('Material_Strength', 0.6),
            ('Load_Distribution', 0.8),
            ('Cracks_Deformation', 0.4)
        ]

        for i, (label, default_value) in enumerate(inputs):
            ttk.Label(input_frame, text=label, font=("Arial", 10)).grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(input_frame, font=("Arial", 10))
            entry.insert(0, str(default_value))
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.input_entries[label] = entry

        # Add black borders to input fields
        for child in input_frame.winfo_children():
            if isinstance(child, ttk.Entry):
                child.configure(style="Black.TEntry")

    def create_output_fields(self):
        """Create output fields on the right side of the window."""
        output_frame = ttk.LabelFrame(self.root, text="Output Results", padding="20")
        output_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.output_labels = {}
        outputs = [
            ('Damage Percentage', 'damage_percentage'),
            ('Damage Classification', 'damage_classification'),
            ('Recommendation', 'recommendation')
        ]

        for i, (label, key) in enumerate(outputs):
            ttk.Label(output_frame, text=label, font=("Arial", 10)).grid(row=i, column=0, padx=5, pady=5, sticky="w")
            output_label = ttk.Label(output_frame, text="", font=("Arial", 10, "bold"), foreground="blue")
            output_label.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.output_labels[key] = output_label

    def create_buttons(self):
        """Create buttons at the bottom of the window."""
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Apply a custom style to buttons
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=5, background="#4CAF50", foreground="black")  # Text color set to black
        style.configure("Black.TEntry", bordercolor="black", borderwidth=2)  # Black border for input fields

        ttk.Button(button_frame, text="Run Simulation", command=self.run_simulation, style="TButton").grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_fields, style="TButton").grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit, style="TButton").grid(row=0, column=2, padx=5, pady=5)

    def run_simulation(self):
        """Run the simulation and display results."""
        try:
            inputs = {}
            for label, entry in self.input_entries.items():
                value = float(entry.get())
                inputs[label] = value

            results = simulate_control_system(self.control_simulation, inputs)

            self.output_labels['damage_percentage'].config(text=f"{results['damage_percentage']:.2f}%")
            self.output_labels['damage_classification'].config(text=results['damage_classification'])
            self.output_labels['recommendation'].config(text=results['recommendation'])

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def reset_fields(self):
        """Reset all input and output fields."""
        for entry in self.input_entries.values():
            entry.delete(0, tk.END)
            entry.insert(0, "0.0")

        for label in self.output_labels.values():
            label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FuzzyLogicApp(root)
    root.mainloop()