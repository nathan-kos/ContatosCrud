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
        #checking if phone has 11 digits
        if(len(phone) != 11):
            raise ValueError("Telefone inválido");

        self.phone = phone;

    def setEmail(self, email):
        #checking if email has @
        if("@" not in email):
            raise ValueError("Email inválido");
    
        self.email = email;