class Patient:

    def __init__(self,idno,name,address,num,status):
        self.id = idno
        self.name = name
        self.address = address
        self.phone = num 
        self.veteran_status = status

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_phone(self):
        return str(self.phone)
    
    def get_veteran_status(self):
        return self.veteran_status.lower()
    
    