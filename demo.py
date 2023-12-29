class Artist:
    all = []

    def __init__(self, name):
        self.name = name
        Artist.all.append(self)

    def __repr__(self):
        return f"Artist: {self.name}"


class Painting:
    all = []

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        Painting.all.append(self)

    def __repr__(self):
        return f"Painting: {self.title}, {self.genre}"


vangogh = Artist("Vincent van Gogh")
starry_night = Painting("Starry Night", "post-impressionism")
print(vangogh)
print(starry_night)
