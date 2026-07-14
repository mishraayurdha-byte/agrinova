"""
====================================================
 AgriNova AI v2.0
 AI Chatbot Tests
====================================================
"""

import pytest


def test_chatbot_empty_message(client):
    """
    Empty message should be rejected.
    """

    response = client.post(
        "/api/chatbot",
        json={}
    )

    assert response.status_code in (400, 422)


def test_chatbot_success(client, monkeypatch):
    """
    Test successful chatbot response.
    """

    def mock_chat(self, message):
        return {
            "success": True,
            "answer": (
                "Maintain proper irrigation and apply balanced fertilizer."
            )
        }

    monkeypatch.setattr(
        "services.chatbot_service.ChatbotService.chat",
        mock_chat
    )

    response = client.post(
        "/api/chatbot",
        json={
            "message": "How can I improve rice yield?"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    assert "answer" in data


def test_chatbot_response_structure(client, monkeypatch):
    """
    Verify chatbot response fields.
    """

    def mock_chat(self, message):
        return {
            "success": True,
            "answer": "Test response"
        }

    monkeypatch.setattr(
        "services.chatbot_service.ChatbotService.chat",
        mock_chat
    )

    response = client.post(
        "/api/chatbot",
        json={
            "message": "Hello"
        }
    )

    result = response.get_json()

    assert "success" in result
    assert "answer" in result


@pytest.mark.parametrize(
    "question",
    [
        "How much water does wheat need?",
        "Suggest fertilizer for rice.",
        "What is tomato leaf blight?",
        "Best crop for sandy soil?"
    ]
)
def test_chatbot_multiple_queries(
    client,
    monkeypatch,
    question
):
    """
    Test chatbot with different agricultural questions.
    """

    def mock_chat(self, message):
        return {
            "success": True,
            "answer": f"Response for: {message}"
        }

    monkeypatch.setattr(
        "services.chatbot_service.ChatbotService.chat",
        mock_chat
    )

    response = client.post(
        "/api/chatbot",
        json={
            "message": question
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    assert question in data["answer"]