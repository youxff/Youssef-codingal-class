class Artwork:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Year: {self.year}")
        print()


class Gallery:
    def __init__(self):
        self.collection = []

    def add_artwork(self, artwork):
        self.collection.append(artwork)

    def show_collection(self):
        print("Art Gallery Collection:")
        print("----------------------")
        for artwork in self.collection:
            artwork.display_info()


# Creating artwork objects
art1 = Artwork("Starry Night", "Vincent van Gogh", 1889)
art2 = Artwork("Mona Lisa", "Leonardo da Vinci", 1503)
art3 = Artwork("The Scream", "Edvard Munch", 1893)

# Creating a gallery object
gallery = Gallery()

# Adding artwork to gallery
gallery.add_artwork(art1)
gallery.add_artwork(art2)
gallery.add_artwork(art3)

# Displaying collection
gallery.show_collection()