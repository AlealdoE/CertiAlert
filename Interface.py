import pandas as pd
import win32com.client as win32
from openpyxl import Workbook, load_workbook
import datetime
def play():
   # wb = load_workbook(r'Vencimentos.xlsx')
    df = pd.read_excel(r'..\Dataframe\BD VENCIMENTOS.xlsx',sheet_name='Planilha1', dtype = str)

    #wb.save('Vencimentos.xlsx')
    for index, dado in df.iterrows():
        data = datetime.datetime.now()
        data_string = data.strftime('%d/%m/%Y')

    
        if data_string == dado['Data Vencimento'] :
            
            outlook =win32.Dispatch('outlook.application')
            email = outlook.CreateItem(0)
            email.To = f'{dado["EMAIL"]}'
            email.Subject ='Importante - Vencimento de Certificado'
            email.HTMLBody = """
            <p>TEXTO PERSONALIZADO  
            <p>
            <p> Mensagem enviada por robô
            """
            email.Send()
            
        else:
            continue

if __name__ == '__main__':
    play() 
