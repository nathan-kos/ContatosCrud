class Contact:

    def __init__(self, name, phone, email):
        self.name = name;
        self.phone = phone;
        self.email = email;

    def getName(self):
        return self.name;

    def getPhone(self):
        return self.phone;
    
    def getEmail(self):
        return self.email;
    
    def setName(self, name):
        self.name = name;

    def setPhone(self, phone):
        self.phone = phone;

    def setEmail(self, email):
        self.email = email;