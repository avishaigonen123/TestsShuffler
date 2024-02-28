# Mixwer
Belender answers of tests in JCT

first, clone the project
**git clone https://github.com/avishaigonen123/TestsShuffler**

after clonning, navigate to project dir
**cd /path/to/TestsShuffler**

then, activate the setup.py file, install all the neccesary packages
**pip install .**


Now you need to install Tesseract:
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
go with the installer and remember where you installed the project, the defualt is:
C:\Program Files\Tesseract-OCR\

after installing, you need to enter C:\Program Files\Tesseract-OCR\tessdata
remove the heb.traineddata that is found there, and copy the heb.traineddata i gave you in the project, to be there.

Then, enter blender/paths and update the paths accoridingly. (if u hit the default, u won't need to change)

next, you need to download poppler from this link:
https://github.com/oschwartz10612/poppler-windows/releases/download/v23.11.0-0/Release-23.11.0-0.zip

unzip it, and remember where it's located.
u need to modify the path file, to be something like this:
poppler_path=r"C:\Program Files (x86)\poppler-23.11.0\Library\bin"

now, after your path file is looks something like this:
poppler_path=r"C:\Program Files (x86)\poppler-23.11.0\Library\bin"

tesseract_path=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

tessdata_path=r'C:\Program Files\Tesseract-OCR\tessdata'

lastly, run the server
**python server/server.py**
