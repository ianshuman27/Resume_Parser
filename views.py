import PyPDF2
import re
from PyPDF2 import PdfReader
import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os
from django.http import HttpResponse
from django.shortcuts import render


df=pd.read_excel('template.xlsx')


user_input = input("Enter the path of your file: ")
def parse(request):
    files = os.listdir(user_input)

    for pdf in files:
         reader = PdfReader(pdf)
         number_of_pages = len(reader.pages)
         str=""

         for i in range(0,number_of_pages):
            page=reader.pages[i]
            str+=page.extract_text()
    

            Names=re.findall(r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+", str)
            print(Names)
            name=""
            for i in Names:
               name+=i 
               break 

            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str)
            email=""
            for i in emails:
                email+=i

            phone_number=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', str)
            mobile=""
            for i in phone_number:
                mobile+=i

            df.loc[len(df.index)] = [name, email, mobile]
    df.to_excel("ExtractedInfo.xlsx")    
    return 0













    




