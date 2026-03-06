from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 16)
        self.cell(0, 10, 'Main Prompts for Python Scripts', border=True, ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', '', 12)

    # Prompt 1: Grade Calculator
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, '1. Grade Calculator (grade_calculator.py)', ln=True)
    pdf.set_font('helvetica', '', 12)
    prompts_grade = [
        "● Asks for a student's name",
        "● Asks for 3 subject marks",
        "● Calculates the average",
        "● Displays Pass if average >= 40, otherwise Fail",
        "● Assign Grade A for average >= 75",
        "● Grade B for 60-74",
        "● Grade C for 40-59",
        "● Fail below 40",
        "● Run repeatedly until the user types 'Exit'",
        "● Print a clean formatted output with separators"
    ]
    for p in prompts_grade:
        pdf.multi_cell(0, 7, p)
    
    pdf.ln(10)

    # Prompt 2: Budget Tracker
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, '2. Monthly Budget Tracker (monthly_budget.py)', ln=True)
    pdf.set_font('helvetica', '', 12)
    prompts_budget = [
        "● Asks the user for total monthly budget",
        "● Asks for expenses multiple times",
        "● Stop entering when they type 'done'",
        "● Subtracts total expenses from total budget",
        "● Displays remaining balance",
        "● Warning: Low Funds if balance < 500 LKR"
    ]
    for p in prompts_budget:
        pdf.multi_cell(0, 7, p)

    pdf.output("main_prompts.pdf")
    print("PDF 'main_prompts.pdf' created successfully.")

if __name__ == "__main__":
    create_pdf()
