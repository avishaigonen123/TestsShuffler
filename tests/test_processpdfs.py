import os

from blender.ProccesPdf import process_pdfs, blend_pdf


def test_processpdfs(tests_data_dir):
    array_path, sucess_flag = process_pdfs(os.path.join(tests_data_dir, "test_example.pdf"))


def test_blend_pdf(tests_data_dir):
    pdf_path = os.path.join(tests_data_dir, "test_example.pdf")
    path = blend_pdf(path_original_pdf=pdf_path)
