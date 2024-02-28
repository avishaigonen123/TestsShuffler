tsShuffler

## Introduction
TestsShuffler is a Python project designed to shuffle and process answers for tests using Blender, Tesseract OCR, and Poppler.

## Setup Instructions
### Clone the Project:
git clone https://github.com/avishaigonen123/TestsShuffler
cd TestsShuffler

### Install Dependencies:
Activate the setup.py file to install all necessary Python packages:
pip install .

### Installing Tesseract:
1. Download and install Tesseract OCR from here.
2. Replace the Hebrew trained data:
    - Remove heb.traineddata from C:\Program Files\Tesseract-OCR\tessdata\.
    - Copy the provided heb.traineddata to the same directory.

### Configuring Blender Paths:
1. Navigate to blender/paths directory in the project.
2. Update Blender paths in the path file if necessary. (Default paths might suffice)

### Installing Poppler:
1. Download Poppler from here.
2. Extract the zip file and remember the location.
3. Update the path file to point to the Poppler binary location:
    poppler_path=r"C:\Program Files (x86)\poppler-23.11.0\Library\bin"

## Running the Server
Launch the server:
python server/server.py

Ensure you follow each step carefully to set up the project correctly.

## License
This project is licensed under the MIT License.

