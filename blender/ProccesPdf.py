import os

from blender.Logicalscripts import *
from blender.FunctionalScripts import *
from blender.constants import output_directory

successPdf = []
athOfPdf = ""
answersId = []
pageCode = True
detailsBetweenQ = False


# input_directory = "C:\\Users\\izeik\\Pictures\\אוטומטים לא מעורבל\\"
# output_directory = "blender\\images\\"


def blend_pdf(path_original_pdf: str) -> str:
    # Convert test .pdf to page.png
    path_originial_pages_png = functionalFiles.pdf_to_png(path_original_pdf, output_directory)

    # TODO dont merge the pages because the ocr is less good, see what to do that it will be splited pages
    # Merge the pages
    pathOfMerge = functionalFiles.combineFiles(path_originial_pages_png, output_directory + 'result')

    # Find how much q and a there are
    # make each q to .png
    arrayOfQuestions, numQ = exportPng.export_questions(path_originial_pages_png, output_directory)
    print("Success export Q\n")
    # make each a to .png
    for pathQ in arrayOfQuestions:
        global answersId
        answersId = logicalList.findNumAnswers(pathQ)
        exportPng.export_answers(pathQ, answersId, output_directory)
        print("Success export A in Q {}\n".format(pathQ))

    # crop each a
    logicalPng.reCrop()
    print("Success Croping\n")

    # Mix the order of the answer
    mixAnswers = logicalList.mixfiles()
    print("Success Mixing\n")
    # Make answers and questions to pages .png
    paths_of_pages = logicalPng.combineFilestoPages(mixAnswers, output_directory)
    print("Success final pages\n")

    # Add answers page
    answer_page_path, path_answers = logicalPng.createAnswersPage(mixAnswers)
    paths_of_pages = paths_of_pages + answer_page_path
    print("Success answer page\n")
    # Make .png to .pdf
    paths_of_pages_pdf = []
    for current_page in paths_of_pages:
        paths_of_pages_pdf.append(functionalFiles.png_to_pdf(current_page))
    print("Success convert pages to.pdf\n")

    output_pdf_path = os.path.join("blender", "final_pdfs",
                                   path_original_pdf[path_original_pdf.rfind("/") + 1:-4] + "scramble")
    functionalFiles.merge_pdf(paths_of_pages_pdf,
                              output_pdf_path)
    print("Success merge pages\n")

    functionalFiles.delete_files(tuple(
        functionalFiles.getFilesPaths()[0] + B for B in functionalFiles.getFilesPaths()[1]))

    return output_pdf_path


def process_pdfs(array_paths):
    '''
    First conver the PDF to PNG files and combine and delete them.
    The answers and questions are exported to PNG files.
    We mix the answers and export to PDF
    '''
    global successPdf
    successPdf = []
    failPdf = []
    for pdf_file_path in array_paths:
        global path_original_pdf
        path_original_pdf = pdf_file_path
        file_name = os.path.basename(path_original_pdf)
        fileNameEnd = path_original_pdf[path_original_pdf.rfind("\\") + 1:-4] + "scramble" + path_original_pdf[-4:]
        try:
            # zip all the successPdf
            successPdf.append(blend_pdf(path_original_pdf=path_original_pdf) + ".pdf")

            print("SUCCESS {}".format(fileNameEnd))
        except Exception as e:
            print("NOT  SUCCESS {}".format(fileNameEnd) + " ERROR: ", e)
            failPdf.append(pdf_file_path)
    return successPdf, successPdf != []


def get_output_directory():
    return output_directory


if __name__ == "__ProccessPdf__":
    process_pdfs()
