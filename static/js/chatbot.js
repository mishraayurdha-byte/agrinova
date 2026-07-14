document.addEventListener("DOMContentLoaded", () => {

    const chatBox = document.getElementById("chat-box");
    const input = document.getElementById("user-message");
    const sendBtn = document.getElementById("send-btn");

    // ===============================
    // Current Time
    // ===============================

    function currentTime() {

        return new Date().toLocaleTimeString([], {

            hour: "2-digit",
            minute: "2-digit"

        });

    }

    // ===============================
    // User Bubble
    // ===============================

    function addUserMessage(message) {

        chatBox.innerHTML += `

        <div class="d-flex justify-content-end mb-3">

            <div style="max-width:75%;">

                <div class="bg-success text-white rounded p-3">

                    ${message}

                </div>

                <small class="text-muted float-end">

                    ${currentTime()}

                </small>

            </div>

        </div>

        `;

        scrollBottom();

    }

    // ===============================
    // Bot Bubble
    // ===============================

    function addBotMessage(message) {

           // Convert markdown style text to HTML
    message = message
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/\*(.*?)\*/g, "<li>$1</li>")
        .replace(/\n/g, "<br>");

        chatBox.innerHTML += `

    <div class="d-flex justify-content-start mb-3">

        <div style="max-width:80%;">

            <div class="bot-card">

                <div class="bot-header">
                    🌱 AgriNova AI
                </div>

                <div class="bot-content">
                    ${message}
                </div>

            </div>


            <small class="text-muted">

                ${currentTime()}

            </small>

        </div>

    </div>

    `;


    scrollBottom();

}

    // ===============================
    // Typing Indicator
    // ===============================

    function showTyping() {

        chatBox.innerHTML += `

        <div id="typing">

            <div class="d-flex justify-content-start mb-3">

                <div class="bg-light border rounded p-3">

                    🤖 AgriNova AI is typing...

                </div>

            </div>

        </div>

        `;

        scrollBottom();

    }

    function hideTyping() {

        const typing = document.getElementById("typing");

        if (typing) {

            typing.remove();

        }

    }

    // ===============================
    // Scroll
    // ===============================

    function scrollBottom() {

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    // ===============================
    // Send Message
    // ===============================

    async function sendMessage(message = null) {

        const text = message || input.value.trim();

        if (text === "") return;

        addUserMessage(text);

        input.value = "";

        input.focus();

        sendBtn.disabled = true;

        showTyping();

        try {

            const response = await fetch("/api/chat", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    message: text

                })

            });

            const data = await response.json();

            hideTyping();

            if (data.status === "success") {

                addBotMessage(data.answer);

            }

            else {

                addBotMessage(data.message);

            }

        }

        catch (error) {

            hideTyping();

            addBotMessage(

                "Unable to connect to the server."

            );

            console.error(error);

        }

        sendBtn.disabled = false;

    }

    // ===============================
    // Button Click
    // ===============================

    sendBtn.addEventListener(

        "click",

        sendMessage

    );

    // ===============================
    // Enter Key
    // ===============================

    input.addEventListener(

        "keydown",

        function(e){

            if(e.key==="Enter"){

                e.preventDefault();

                sendMessage();

            }

        }

    );

    // ===============================
    // Suggested Questions
    // ===============================

    document.querySelectorAll(".suggestion")

    .forEach(button=>{

        button.addEventListener("click",()=>{

            sendMessage(button.innerText);

        });

    });

    input.focus();

});