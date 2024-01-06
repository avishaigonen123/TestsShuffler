import os

from blender.ProccesPdf import process_pdfs, blend_pdf

test_root_dir = os.path.dirname(os.path.realpath(__file__))
test_data_dir = test_root_dir + "data"


def test_processpdfs():
    array_path, sucess_flag = process_pdfs(os.path.join(test_data_dir, "test_example.pdf"))


def test_blend_pdf():
    pdf_path = os.path.join(test_data_dir, "test_example.pdf")
    path = blend_pdf(path_original_pdf=pdf_path)
