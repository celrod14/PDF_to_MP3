import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    
    speaker.save_to_file(clean_text, f'story_page_{page_num}.mp3')
    speaker.runAndWait()

speaker.stop()
