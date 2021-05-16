import pyttsx3
import PyPDF2
book = open('PreventionandManagementofCOVID19FLWEnglish.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)#total no. of pages in book

speaker = pyttsx3.init()
for num in range(0, pages):#from the page to be read and  stop
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()