class StringCount():
    def  __init__(self, filename):
        self.file = open(filename, encoding = "utf-8")

    def countWords(self, *out):
        if out:
            out = str(out).strip("""('",)""")
        else:
            out = "out.txt"
        self.dist = {}
        for i in self.file.read().split():
            i = i.strip("""!@#$%^&*()_+-=~`';:?/.{}[]'".,0123456789""").lower()
            if i not in self.dist:
                self.dist[i] = 0
            self.dist[i] += 1
        with open(out, "w", encoding="utf-8") as file:
            for i in self.dist:
                text = str(i) + " : " + str(self.dist[i]) + "\n"
                file.write(text)