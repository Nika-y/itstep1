import tkinter as tk
from tkinter import ttk


class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертор валют")
        self.root.geometry("300x250")

        self.rates = {
            "UAH": 0.027,
            "EUR": 1.1,
            "GBP": 1.25,
            "CNY": 0.14,
            "JPY": 0.007
        }

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Конвертор валют у USD", font=("Arial", 14)).pack(pady=10)

        ttk.Label(self.root, text="Оберіть валюту:", font=("Arial", 10)).pack()
        self.currency_combobox = ttk.Combobox(self.root, values=list(self.rates.keys()), state="readonly")
        self.currency_combobox.pack(pady=5)
        self.currency_combobox.current(0)

        ttk.Label(self.root, text="Введіть суму:", font=("Arial", 10)).pack()
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        ttk.Button(self.root, text="Конвертувати", command=self.convert_currency).pack(pady=10)
        self.result_label = ttk.Label(self.root, text="", font=("Arial", 12), foreground="green")
        self.result_label.pack()

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            if amount < 0:
                self.result_label.config(text="Сума має бути додатною!", foreground="red")
                return

            selected_currency = self.currency_combobox.get()
            rate_to_usd = self.rates[selected_currency]
            usd_amount = amount * rate_to_usd
            self.result_label.config(
                text=f"{amount} {selected_currency} = {usd_amount:.2f} USD", foreground="green"
            )
        except ValueError:
            self.result_label.config(text="Введіть коректну суму!", foreground="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
