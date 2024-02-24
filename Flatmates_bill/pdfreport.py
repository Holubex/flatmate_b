import webbrowser
import os
from fpdf import FPDF
from filestack import Client

class PdfReport:
    '''
    Creates a Odf file that contains data about the
    flatmates such as their names, their due amount and
    the period of the bill.
    '''

    def __init__(self, filename):
        self.filename = filename


    def generate(self, flatmate1, flatmate2, bill):
        flatmate1pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name='files/house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', border=0, ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flat mate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1pay, border=0, ln=1)

        # Insert name and due amount of the first flat mate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2pay, border=0, ln=1)

        os.chdir('files')

        pdf.output(self.filename)

        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self, filepath, api_key="INSERT YOUR API KEY"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

