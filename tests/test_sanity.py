"""Sanity tests, because a lot can go wrong writing extensions."""

import io
import unittest

import pdftotext
from tests import blank_pdf_file


class BuildTest(unittest.TestCase):
    """See if the build works at all."""

    def test_has_error(self):
        self.assertTrue(hasattr(pdftotext, "Error"))

    def test_has_pdf(self):
        self.assertTrue(hasattr(pdftotext, "PDF"))


class TypeTest(unittest.TestCase):
    """Verify types and method signatures."""

    def setUp(self):
        self.pdf_file = io.BytesIO(blank_pdf_file.getvalue())

    def test_pdf_page_count(self):
        pdf = pdftotext.PDF(self.pdf_file)
        self.assertEqual(type(pdf.page_count), int)
