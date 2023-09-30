import tkinter as tk
from tkinter import messagebox

class CafeBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Billing Application")
              
        # Menu data
        self.menu = {
            "Cappucino                              ₹99": 99,
            "Americano                            ₹129": 129,
            "Expresso                              ₹119": 119,
            "Latte                                      ₹149  ": 149,
            "Cheese Burger                       ₹89": 89,
            "Fried Rice                             ₹109": 109,
            "Hakka Noodles                    ₹139": 139,
            "Spring Rolls                            ₹49  ": 49,
            "Plain Maggi                            ₹39": 39,
            "Tandoori Maggi                     ₹79": 79,
            "Cheese Maggi                       ₹89": 89,
            "Masala Maggi                        ₹59  ": 59,
        }
        
        # Order data
        self.order = {}
    
        
        # Create a frame for menu
        menu_frame = tk.Frame(root)
        menu_frame.pack(side=tk.LEFT, padx=20, pady=20)
        
        # Menu Label
        menu_label = tk.Label(menu_frame, text="Items                            Price", font=("Arial", 14))
        menu_label.pack()
        
        # Menu Listbox
        self.menu_listbox = tk.Listbox(menu_frame, selectmode=tk.SINGLE, height=15, width=25, font=("Arial", 12))
        for item in self.menu:
            self.menu_listbox.insert(tk.END, item)
        self.menu_listbox.pack()

        add_button = tk.Button(menu_frame, text="Add to Order", command=self.add_to_order, font=("Arial", 12))
        add_button.pack()
        
        # Create a frame for order
        order_frame = tk.Frame(root)
        order_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Order Label
        order_label = tk.Label(order_frame, text="Order             Quantity", font=("Arial", 14))
        order_label.pack()
        
        # Order Text
        self.order_text = tk.Text(order_frame, height=10, width=30, font=("Arial", 12))
        self.order_text.pack()
        
        remove_button = tk.Button(order_frame, text="Remove Item", command=self.remove_from_order, font=("Arial", 12))
        remove_button.pack() 

        # Calculate Bill Button
        calculate_button = tk.Button(order_frame, text="Calculate Bill", command=self.calculate_bill, font=("Arial", 16))
        calculate_button.pack()               

        # Total Bill Label
       
        
        # Total Bill Amount
        self.total_text = tk.Label(order_frame, text="", font=("Arial", 16))
        self.total_text.pack()
    
    def add_to_order(self):
        selected_item = self.menu_listbox.get(tk.ACTIVE)
        if selected_item:
            if selected_item in self.order:
                self.order[selected_item] += 1
            else:
                self.order[selected_item] = 1
            self.update_order_text()
            
    def remove_from_order(self):
        selected_item = self.menu_listbox.get(tk.ACTIVE)
        if selected_item and selected_item in self.order:
            if self.order[selected_item] > 1:
                self.order[selected_item] -= 1
            else:
                del self.order[selected_item]
            self.update_order_text()

    def update_order_text(self):
        self.order_text.delete("1.0", tk.END)
        for item, quantity in self.order.items():
            self.order_text.insert(tk.END, f"{item}: {quantity}\n")
    
    def calculate_bill(self):
        total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        self.total_text.config(text=f"Total Bill: ₹{total:.2f}")
        messagebox.showinfo("Bill Summary", f"Total Bill: ₹{total:.2f}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = CafeBillingApp(root)
    root.mainloop()
