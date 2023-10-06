class Procedure:
    
    def __init__ (self,name,date,practitioner,charges,id):
        self.proc_name = name
        self.proc_date = date
        self.proc_practitioner = practitioner
        self.proc_charges = charges
        self.patient_id = id


    def get_proc_name(self):
        return self.proc_name
    
    def get_proc_date(self):
        return self.proc_date
    
    def get_proc_practitioner(self):
        return self.proc_practitioner
    
    def get_proc_charges(self):
        return self.proc_charges
    
    def get_patient_id(self):
        return self.patient_id