class Data:
    def get_size(self):
        pass

class File(Data):
    def __init__(self, i):
        self.size = i

    def get_size(self):
        return self.size

class Folder(Data):
    def __init__(self):
        self.dataList = []

    def add(self, file):
        self.dataList.append(file)

    def remove(self,file):
        self.dataList.remove(file)

    def get_size(self):
        s = 0
        for x in self.dataList:
            s += x.get_size()

        return s

if __name__ == '__main__':
    f1 = File(5)
    f2 = File(10)

    folder1 = Folder()
    folder1.add(f1)
    folder1.add(f2)

    folder2 = Folder()
    f3 = File(5)
    folder2.add(f3)

    folder1.add(folder2)

    folder3 = Folder()
    f4 = File(10)
    folder3.add(f4)

    print("Folder 1 size: ", folder1.get_size())
    print("Folder 2 size: ", folder2.get_size())
    print("File 2 size: ", f2.get_size())
    folder1.remove(folder2)
    folder1.remove(f2)
    print("\nRemoving Folder2 & File2 from Folder1...\n")
    print("Folder 1 size: ", folder1.get_size())
    print("Folder 3 size: ", folder3.get_size())