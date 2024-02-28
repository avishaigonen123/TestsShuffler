# Mixwer Belender answers of tests in JCT

## Introduction
This project provides Blender answers for tests in JCT.

## Setup Instructions

1. **Clone the project:**
git clone https://github.com/avishaigonen123/TestsShuffler


2. **Navigate to the project directory:**
cd /path/to/TestsShuffler


3. **Install dependencies:**
Activate the setup.py file and install all the necessary packages:
pip install .


4. **Install Tesseract OCR:**
- Download and install Tesseract OCR from [here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe).
- After installation, navigate to `C:\Program Files\Tesseract-OCR\tessdata`.
- Remove the `heb.traineddata` file and replace it with the provided `heb.traineddata` file from the project.

5. **Configure Blender Paths:**
- Navigate to `blender/paths` directory in the project.
- Update Blender paths in the `path` file if necessary. Default paths might suffice.

6. **Install Poppler:**
- Download Poppler from [here](https://github.com/oschwartz10612/poppler-windows/releases/download/v23.11.0-0/Release-23.11.0-0.zip).
- Extract the zip file to a location you can remember.
- Update the `path` file to include the location of Poppler:
  ```python
  poppler_path=r"C:\Program Files (x86)\poppler-23.11.0\Library\bin"
  ```

7. **Run the server:**
python server/server.py


Ensure you follow each step carefully to set up the project correctly.
