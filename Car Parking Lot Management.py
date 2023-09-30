import tkinter as tk
from tkinter import *
from tkinter import messagebox


class ParkingLotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Parking Lot Management")
        self.root.maxsize(width=500, height=600)
        self.root.minsize(width=500, height=600)
        self.root.configure(bg="#cc99ff")

        self.login_frame = None
        self.home_frame = None
        self.add_vehicle_frame = None
        self.display_vehicles_frame = None
        self.remove_vehicle_frame = None

        self.vehicles = []

        self.create_login_page()

    def create_login_page(self):
        self.hide_frames()

        self.login_frame = tk.Frame(self.root, bg="#cc99ff")
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        login_label = tk.Label(self.login_frame, text="Login", bg='#cc99ff', fg="#000000", font=("Arial", 25))
        login_label.pack(pady=(50, 10))

        username_label = tk.Label(self.login_frame, text="Username:", bg='#cc99ff', fg="#000000", font=("Arial", 16))
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=10)

        password_label = tk.Label(self.login_frame, text="Password:", bg='#cc99ff', fg="#000000", font=("Arial", 16))
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.pack(pady=10)

        self.login_frame.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check username and password (dummy validation)
        if username == "admin" and password == "1234":
            self.create_home_page()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

        # Hide the login page
        self.hide_frame(self.login_frame)

    def create_home_page(self):
        self.hide_frames()

        self.home_frame = tk.Frame(self.root, bg="#cc99ff")

        home_label = tk.Label(self.home_frame, text="Welcome to Parking Lot Management")
        home_label.pack(pady=10)

        add_vehicle_button = tk.Button(self.home_frame, text="Add Vehicle", command=self.create_add_vehicle_page)
        add_vehicle_button.pack(pady=10)

        display_vehicles_button = tk.Button(self.home_frame, text="Display Vehicles",
                                            command=self.create_display_vehicles_page)
        display_vehicles_button.pack(pady=10)

        remove_vehicle_button = tk.Button(self.home_frame, text="Remove Vehicle", command=self.create_remove_vehicle_page)
        remove_vehicle_button.pack(pady=10)

        logout_button = tk.Button(self.home_frame, text="Logout", command=self.logout)
        logout_button.pack(pady=10)

        self.home_frame.pack()

    def logout(self):
        self.create_login_page()

    def create_add_vehicle_page(self):
        self.hide_frames()

        self.add_vehicle_frame = tk.Frame(self.root,bg='')

        add_vehicle_label = tk.Label(self.add_vehicle_frame, text="Add New Vehicle")
        add_vehicle_label.pack(pady=10)

        vehicle_number_label = tk.Label(self.add_vehicle_frame, text="Vehicle Number:")
        vehicle_number_label.pack()
        self.vehicle_number_entry = tk.Entry(self.add_vehicle_frame)
        self.vehicle_number_entry.pack()

        add_button = tk.Button(self.add_vehicle_frame, text="Add", command=self.add_vehicle)
        add_button.pack(pady=10)

        back_button = tk.Button(self.add_vehicle_frame, text="Back", command=self.back_to_home)
        back_button.pack()

        self.add_vehicle_frame.pack()

    def add_vehicle(self):
        vehicle_number = self.vehicle_number_entry.get()

        # Perform validation and add the vehicle to the list
        if vehicle_number:
            self.vehicles.append(vehicle_number)
            messagebox.showinfo("Success", f"Vehicle {vehicle_number} has been added.")
            self.vehicle_number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter the vehicle number.")

    def create_display_vehicles_page(self):
        self.hide_frames()

        self.display_vehicles_frame = tk.Frame(self.root,bg='')

        display_vehicles_label = tk.Label(self.display_vehicles_frame, text="Display Vehicles")
        display_vehicles_label.pack(pady=10)

        # Display the vehicles in the parking lot
        if self.vehicles:
            for index, vehicle in enumerate(self.vehicles, start=1):
                vehicle_label = tk.Label(self.display_vehicles_frame, text=vehicle)
                vehicle_label.pack()
        else:
            no_vehicles_label = tk.Label(self.display_vehicles_frame, text="No vehicles found.")
            no_vehicles_label.pack()

        back_button = tk.Button(self.display_vehicles_frame, text="Back", command=self.back_to_home)
        back_button.pack()

        self.display_vehicles_frame.pack()

    def create_remove_vehicle_page(self):
        self.hide_frames()

        self.remove_vehicle_frame = tk.Frame(self.root,bg='')

        remove_vehicle_label = tk.Label(self.remove_vehicle_frame, text="Remove Vehicle")
        remove_vehicle_label.pack(pady=10)

        vehicle_number_label = tk.Label(self.remove_vehicle_frame, text="Vehicle Number:")
        vehicle_number_label.pack()
        self.remove_vehicle_entry = tk.Entry(self.remove_vehicle_frame)
        self.remove_vehicle_entry.pack()

        remove_button = tk.Button(self.remove_vehicle_frame, text="Remove", command=self.remove_vehicle)
        remove_button.pack(pady=10)

        back_button = tk.Button(self.remove_vehicle_frame, text="Back", command=self.back_to_home)
        back_button.pack()

        self.remove_vehicle_frame.pack()

    def remove_vehicle(self):
        vehicle_number = self.remove_vehicle_entry.get()

        # Perform validation and remove the vehicle from the list
        if vehicle_number:
            if vehicle_number in self.vehicles:
                self.vehicles.remove(vehicle_number)
                messagebox.showinfo("Success", f"Vehicle {vehicle_number} has been removed.")
                self.remove_vehicle_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"Vehicle {vehicle_number} not found.")
        else:
            messagebox.showerror("Error", "Please enter the vehicle number.")

    def back_to_home(self):
        self.create_home_page()

    def hide_frame(self, frame):
        if frame is not None:
            frame.pack_forget()

    def hide_frames(self):
        self.hide_frame(self.login_frame)
        self.hide_frame(self.home_frame)
        self.hide_frame(self.add_vehicle_frame)
        self.hide_frame(self.display_vehicles_frame)
        self.hide_frame(self.remove_vehicle_frame)

    def run(self):
        self.root.mainloop()


def main():
    parking_lot_gui = ParkingLotGUI()
    parking_lot_gui.run()


if __name__ == "__main__":
    main()