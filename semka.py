class sparseVector(dict):

    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)

    def __len__(self):
        return int(max(self.keys())) + 1



    def __getitem__(self, item):
        if item in self.keys():
            return self.get(item)
        else:
            return 0.0

    def __iter__(self):       
        for i in range(0, max(self.keys()) + 1):
            if i in self.keys():
                yield self[i]
            else:
                yield 0.0

    def __mul__(self, other):
        E = 0
        if isinstance(other, sparseVector):
            for key, value in other.items():
                E += value * self[key]
            return E
        elif isinstance(other, list):
            for i, num in enumerate(other):
                E += num * self[i]
            return E
        else:
            print("WTF")
                
        

x = sparseVector()
x[0] = 1.0
x[3] = 2.0
x[5] = 3.0
print (len(x))
print([v for v in x])
y = sparseVector()
y[0] = 30.0
y[4] = 10.0
print (x*y)

print(x*[30, 0, 0, 0, 10])
