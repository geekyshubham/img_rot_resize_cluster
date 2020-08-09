#!/usr/bin/env python3

import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table ,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(filename,title,paragraphs):
	styles=getSampleStyleSheet()
	report=SimpleDocTemplate(filename)
	report_title=Paragraph(title,styles["h1"])
	report_info=Paragraph(paragraphs,styles["BodyText"])
	report.build([report_title,report_info])
	return True
