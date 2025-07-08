import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        result = f"Your BMI is: {bmi:.2f}\n"

        if bmi < 18.5:
            result += "You are underweight."
        elif 18.5 <= bmi < 24.9:
            result += "You have a normal weight."
        elif 25 <= bmi < 29.9:
            result += "You are overweight."
        else:
            result += "You are obese."

        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
    except ZeroDivisionError:
        messagebox.showerror("Enter valid Input","other value than 0")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
root.resizable(False, False)

label_weight = tk.Label(root, text="Enter weight (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()


label_height = tk.Label(root, text="Enter height (m):")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

btn_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
btn_calculate.pack(pady=10)


root.mainloop()
