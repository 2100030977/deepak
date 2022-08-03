class parent:
    def __init__(self, txt):
        self.message = txt

    def print(self):
        print(self.message)


class child(parent):
    def __init__(self, txt):
        super().__init__(txt)


x = child("my name is deepak reddy")
x.print()

