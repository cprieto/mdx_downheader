# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from markdown import markdown


class TestDownHeaderExtension(unittest.TestCase):
    def test_it_generates_normal_headers(self):
        """Without the extension we generate normal headers"""
        text_input = "# Header 1"
        expected = "<h1>Header 1</h1>"
        result = markdown(text_input)
        self.assertEqual(expected, result)

    def test_it_downgrade_h1_to_h2(self):
        """With the extension, we downgrade the headers"""
        text_input = "# Header 1"
        expected = "<h2>Header 1</h2>"
        result = markdown(text_input, ['downheader',])
        self.assertEqual(expected, result)

    def test_it_downgrade_all_other_headers(self):
        """With the extension, we downgrade all other headers"""
        data = [('## Header 2', '<h3>Header 2</h3>'),
                ('### Header 3', '<h4>Header 3</h4>'),
                ('#### Header 4', '<h5>Header 4</h5>'),
                ('##### Header 5', '<h6>Header 5</h6>')]
        for text, expected in data:
            result = markdown(text, ['downheader',])
            self.assertEqual(expected, result)

    def test_it_downgrade_several_levels(self):
        """With the extension, we can downgrade the headers several levels"""
        data = [('# Header 1', '<h3>Header 1</h3>'),
                ('## Header 2', '<h4>Header 2</h4>'),
                ('### Header 3', '<h5>Header 3</h5>'),
                ('#### Header 4', '<h6>Header 4</h6>')]
        for text, expected in data:
            result = markdown(text, ['downheader(levels=2)',])
            self.assertEqual(expected, result)

    def test_it_downgrade_negative_levels(self):
        """With the extension, we can upgrade the headers"""
        data = [('## Header 2', '<h1>Header 2</h1>'),
                ('### Header 3', '<h2>Header 3</h2>'),
                ('#### Header 4', '<h3>Header 4</h3>'),
                ('##### Header 5', '<h4>Header 5</h4>'),
                ('###### Header 6', '<h5>Header 6</h5>')]
        for text, expected in data:
            result = markdown(text, ['downheader(levels=-1)',])
            self.assertEqual(expected, result)

    def test_it_downgrade_clip_at_max(self):
        """With the extension, output headings have maximum level 6"""
        data = [('#### Header 4', '<h6>Header 4</h6>'),
                ('##### Header 5', '<h6>Header 5</h6>'),
                ('###### Header 6', '<h6>Header 6</h6>')]
        for text, expected in data:
            result = markdown(text, ['downheader(levels=2)',])
            self.assertEqual(expected, result)

    def test_it_downgrade_clip_at_min(self):
        """With the extension, output headings have minimum level 1"""
        data = [('# Header 1', '<h1>Header 1</h1>'),
                ('## Header 2', '<h1>Header 2</h1>'),
                ('### Header 3', '<h1>Header 3</h1>')]
        for text, expected in data:
            result = markdown(text, ['downheader(levels=-2)',])
            self.assertEqual(expected, result)

    def test_if_it_only_register_extension_once(self):
        text_input = "# Header 1"
        expected = "<h2>Header 1</h2>"
        result = markdown(text_input, ['downheader','downheader'])
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
