"""
====================================================
 AgriNova AI v2.0
 Reports Module Tests
====================================================
"""

from pathlib import Path


def test_generate_pdf_report(client, monkeypatch):
    """
    Test PDF report generation.
    """

    def mock_generate(self, report_type, report_format, data):
        return "reports/agrinova_test.pdf"

    monkeypatch.setattr(
        "services.report_service.ReportService.generate",
        mock_generate
    )

    response = client.post(
        "/api/reports/generate",
        json={
            "type": "all",
            "format": "pdf"
        }
    )

    assert response.status_code == 200

    result = response.get_json()

    assert result["success"] is True
    assert result["file"].endswith(".pdf")


def test_generate_excel_report(client, monkeypatch):
    """
    Test Excel report generation.
    """

    def mock_generate(self, report_type, report_format, data):
        return "reports/agrinova_test.xlsx"

    monkeypatch.setattr(
        "services.report_service.ReportService.generate",
        mock_generate
    )

    response = client.post(
        "/api/reports/generate",
        json={
            "type": "yield",
            "format": "xlsx"
        }
    )

    assert response.status_code == 200

    result = response.get_json()

    assert result["success"] is True
    assert result["file"].endswith(".xlsx")


def test_generate_csv_report(client, monkeypatch):
    """
    Test CSV report generation.
    """

    def mock_generate(self, report_type, report_format, data):
        return "reports/agrinova_test.csv"

    monkeypatch.setattr(
        "services.report_service.ReportService.generate",
        mock_generate
    )

    response = client.post(
        "/api/reports/generate",
        json={
            "type": "weather",
            "format": "csv"
        }
    )

    assert response.status_code == 200

    result = response.get_json()

    assert result["success"] is True
    assert result["file"].endswith(".csv")


def test_invalid_report_format(client):
    """
    Unsupported report format should fail.
    """

    response = client.post(
        "/api/reports/generate",
        json={
            "type": "all",
            "format": "zip"
        }
    )

    assert response.status_code in (400, 422)


def test_download_missing_report(client):
    """
    Downloading a non-existent report
    should return 404.
    """

    response = client.get(
        "/api/reports/download/not_found.pdf"
    )

    assert response.status_code == 404