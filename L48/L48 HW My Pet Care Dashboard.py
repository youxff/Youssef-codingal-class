import tkinter as tk

class Pet:
    def __init__(self, name):
        self.__name = name  # Encapsulation

    def get_name(self):    # Getter
        return self.__name

    def set_name(self, name):  # Setter
        self.__name = name

    def care(self):
        return "Care for your pet"


class Dog(Pet):
    def care(self):
        return "Walk the dog "


class Cat(Pet):
    def care(self):
        return "Feed the cat "


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Care Dashboard")
        self.root.geometry("400x300")

        tk.Label(root, text="Pet Name").pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        tk.Button(
            root,
            text="Show Care Task",
            command=self.show_task
        ).pack(pady=10)

        self.result = tk.Label(root, text="")
        self.result.pack()

    def show_task(self):
        name = self.entry.get()

        # Polymorphism
        if name.lower().startswith("d"):
            pet = Dog(name)
        else:
            pet = Cat(name)

        pet.set_name(name)  # Using setter

        self.result.config(
            text=f"{pet.get_name()}: {pet.care()}"
        )


root = tk.Tk()
app = Dashboard(root)
root.mainloop()