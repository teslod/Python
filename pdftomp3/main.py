
#gtts to make sound of our file
from gtts import gTTS
#art to decorate cmd
from art import tprint
#to read pdf
import pdfplumber
#to get path of pdf file 
from pathlib import Path


def Pdf_To_Mp3(file_Path="",language="en"):
    if Path(file_Path).is_file() and Path(file_Path).suffix =='.pdf':#check if file exists and if it is pdf
        print(f'[+] Original file:{Path(file_Path).name} ')
        print('[+] Processing....')
        # return 'File exists' was used for checkin if it ex
        with pdfplumber.PDF(open(file=file_Path,mode='rb')) as pdf:#reading pfd.....
            pages =[page.extract_text()  for page in pdf.pages]#extracting pages from pdf...


        text=''.join(pages)
        text=text.replace("\n",'')

        #..................................
        my_Audio=gTTS(text=text,lang=language)
        file_Name=Path(file_Path).stem
        my_Audio.save(f'{file_Name}.mp3')
        #getting text and making mp3 file
        return f'[+]{file_Name}.mp3 saved'
    else:
        return "File not exists"#returns it if file name,path wrong or it not exists



def main():
    tprint('PDF>>TO>>MP3',font='bulbhead')#decorating cmd 
    file_Path=input("Enter file path: ")
    language=input("en or ru: ")
    print(Pdf_To_Mp3(file_Path=file_Path,language=language))#staring fc
if __name__ =='__main__':
    main()#starting app