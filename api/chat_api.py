from flask import Blueprint, request, jsonify

from services.chatbot_service import ChatbotService


# ==========================================================
# Blueprint
# ==========================================================

chat_bp = Blueprint(
    "chat",
    __name__,
    url_prefix="/api/chat"
)


@chat_bp.route("", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Invalid request"
            }), 400


        user_message = data.get("message")


        if not user_message:
            return jsonify({
                "status": "error",
                "message": "Message is required"
            }), 400



        reply = ChatbotService.ask(
            user_message
        )


        return jsonify({
            "status": "success",
            "reply": reply
        })


    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500