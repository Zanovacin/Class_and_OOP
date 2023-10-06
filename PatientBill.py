import PatientClass as pc
import ProcedureClass as _pc

patient1 = pc.Patient('1','Matt Jones','123 Main st, Waco TX 76706','254-555-7415','True')

procedure_list = [
_pc.Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1),
_pc.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500,1),
_pc.Procedure('CT Scan','2/17/2022','Dr. Drey',1200,2)
]

print('***  Patient Bill    ***')
print(f"Name:   {patient1.get_name()}")
print(f"Address:    {patient1.get_address()}")
print(f"Phone:  {patient1.get_phone()} ")
print()

total = 0

for procedure in procedure_list:
    if procedure.get_patient_id() == int(patient1.get_id()):
        print(f"Procedure:  {procedure.get_proc_name()}")
        print(f"Date:  {procedure.get_proc_date()}")
        print(f"Practitioner:  {procedure.get_proc_practitioner()}")
        print(f"Charge:  ${procedure.get_proc_charges():,.2f}")
        print()
        total += procedure.get_proc_charges()

if patient1.get_veteran_status():
      total *= .6

print(f"Total Charges: ${total:,.2f}")

    

