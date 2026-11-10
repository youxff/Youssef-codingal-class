class Instrument:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def play_sound(self):
        print(f"The {self.name} goes '{self.sound}'")


# Create instrument objects
piano = Instrument("Piano", "Plink Plonk")
guitar = Instrument("Guitar", "Strum Strum")
drums = Instrument("Drums", "Boom Boom")
violin = Instrument("Violin", "Screech Screech")

# Menu
print("🎵 Music Instrument Sound Show 🎵")
print("1. Piano")
print("2. Guitar")
print("3. Drums")
print("4. Violin")

choice = input("Choose an instrument (1-4): ")

if choice == "1":
    piano.play_sound()
elif choice == "2":
    guitar.play_sound()
elif choice == "3":
    drums.play_sound()
elif choice == "4":
    violin.play_sound()
else:
    print("Invalid choice!")