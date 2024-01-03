import sys

# adding TestsShuffler to the system path
sys.path.insert(0, r'C:\Users\avish\git\TestsShuffler')  # here you should change to project dir

import zipfile

from flask import Flask, request, jsonify, send_file, render_template
import os
from zipfile import ZipFile

from blender.ProccesPdf import main as pdfProccessing

app = Flask(__name__)


def change_to_project_dir():
    # make sure i'm in the right directory.
    current_directory = os.getcwd()

    if os.path.basename(current_directory) == "server":
        # Move one directory up
        parent_directory = os.path.dirname(current_directory)
        os.chdir(parent_directory)
        print(f"Moved to parent directory: {parent_directory}")
    else:
        print("Not in a directory named 'server'.")


# func i added in order to clean the directories
def clear_dir(dir_path, except_endswith="."):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        if os.path.isfile(file_path) and not filename.endswith(except_endswith):
            os.remove(file_path)
            print(f"Deleted: {file_path}")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_pdf():
    change_to_project_dir()
   
    os.makedirs('server', exist_ok=True)
    os.makedirs('server/pdf', exist_ok=True)
    clear_dir('server/pdf')

    pdf_files = request.files.getlist('pdfFiles')
    print(pdf_files)
    pdf_paths = []  # List to store the full paths of processed PDF files
    for pdf_file in pdf_files:
        # Save each uploaded PDF file
        pdf_file_path = os.path.join('server/pdf', pdf_file.filename)
        pdf_file.save(pdf_file_path)
        # Append the full path to the list
        pdf_paths.append(pdf_file_path)

    print(pdf_paths)
    array_paths, success_flag = pdfProccessing(pdf_paths)

    print(array_paths)

    if success_flag:
        with ZipFile('server/pdf/generated.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in array_paths:
                # Add the file to the ZIP
                zipf.write(file, os.path.basename(file))
                os.remove(file)
            clear_dir('server/pdf', '.zip')
            return jsonify({'success': True, 'message': 'Process success!'})
    else:
        print('Error processing PDF:')

        return jsonify({'success': False, 'message': 'Error processing PDF'}), 500


@app.route('/download-zip', methods=['POST'])
def download_zip():
    try:
        # Take the temporary ZIP file
        zip_filename = 'pdf\\generated.zip'
        return send_file(zip_filename, as_attachment=True)

    except Exception as e:
        print(f"Error generating ZIP file: {e}")
        return {'success': False, 'message': 'Error generating ZIP file.'}


if __name__ == '__main__':
    app.run(debug=True)
