import csv
from io import BytesIO, StringIO

from openpyxl import Workbook

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


class ExportService:

    @staticmethod
    def generate_csv(reports):

        output = StringIO()

        writer = csv.writer(output)

        writer.writerow([
            "Title",
            "Category",
            "Date",
            "Status"
        ])

        for report in reports:

            writer.writerow([
                report["title"],
                report["category"],
                report["date"],
                report["status"]
            ])

        return output.getvalue()

    @staticmethod
    def generate_excel(reports):

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "AgriNova Reports"

        sheet.append([
            "Title",
            "Category",
            "Date",
            "Status"
        ])

        for report in reports:

            sheet.append([
                report["title"],
                report["category"],
                str(report["date"]),
                report["status"]
            ])

        output = BytesIO()

        workbook.save(output)

        output.seek(0)

        return output

    @staticmethod
    def generate_pdf(reports):

        output = BytesIO()

        doc = SimpleDocTemplate(output)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "<b>AgriNova AI v2.0 Report</b>",
                styles["Title"]
            )
        )

        elements.append(
            Paragraph("<br/>", styles["Normal"])
        )

        for report in reports:

            elements.append(

                Paragraph(

                    f"""
                    <b>{report['title']}</b><br/>
                    Category : {report['category']}<br/>
                    Date : {report['date']}<br/>
                    Status : {report['status']}<br/><br/>
                    """,

                    styles["Normal"]

                )

            )

        doc.build(elements)

        output.seek(0)

        return output