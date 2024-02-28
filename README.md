TestsShuffler
Description
TestsShuffler is a project designed to shuffle and process answers for tests using Blender, Tesseract OCR, and Poppler.

Setup Instructions
Clone the Project
bash
Copy code
git clone https://github.com/avishaigonen123/TestsShuffler
cd TestsShuffler
Install Dependencies
Activate the setup.py file to install all necessary Python packages:

bash
Copy code
pip install .
Installing Tesseract
Download Tesseract OCR from here.
Install Tesseract OCR and remember the installation directory (default: C:\Program Files\Tesseract-OCR\).
Replace the Hebrew trained data:
Remove heb.traineddata from C:\Program Files\Tesseract-OCR\tessdata\.
Copy the provided heb.traineddata to the same directory.
Configuring Blender Paths
Navigate to blender/paths directory in the project.
Update Blender paths in the path file if necessary. (Default paths might suffice)
Installing Poppler
Download Poppler from here.
Extract the zip file and remember the location.
Update the path file to point to the Poppler binary location:
python
Copy code
poppler_path=r"C:\Program Files (x86)\poppler-23.11.0\Library\bin"
Running the Server
Launch the server:

bash
Copy code
python server/server.py
Make sure to follow each step carefully to ensure that the project is set up correctly.

License
This project is licensed under the MIT License.
