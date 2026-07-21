document.addEventListener("DOMContentLoaded", () => {

    const chatBox = document.getElementById("chat-box");
    const input = document.getElementById("user-message");
    const micBtn = document.getElementById("mic-btn");
    const sendBtn = document.getElementById("send-btn");

let voices = [];

window.speechSynthesis.onvoiceschanged = () => {
    voices = window.speechSynthesis.getVoices();
    console.log("Available Voices:", voices);
};

// ===============================
// Voice Recognition
// ===============================

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

let recognition = null;

if (SpeechRecognition) {

    recognition = new SpeechRecognition();

    recognition.lang = navigator.language || "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    
    recognition.onstart = () => {

        console.log("Listening...");

        micBtn.classList.add("listening");

    };

        recognition.onresult = (event) => {

            const transcript = event.results[0][0].transcript.trim();

            input.value = transcript;

            console.log("You said:", transcript);

            // Wait briefly so the user sees the recognized text
            setTimeout(() => {

                sendMessage();

            }, 300);

        };

    recognition.onerror = (event) => {

        console.error(event.error);

    };

    recognition.onend = () => {

        console.log("Recognition stopped");

        micBtn.classList.remove("listening");

    };

    micBtn.addEventListener("click", () => {

        recognition.start();

    });

} else {

    micBtn.disabled = true;

    console.log("Speech Recognition is not supported.");

}

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
                speak(data.answer);

            }

            else {

                addBotMessage(data.message);
                speak(data.message);

            }

        }

        catch (error) {

            hideTyping();

            // addBotMessage(

            //     "Unable to connect to the server."

            // );
            const errorMessage = "Unable to connect to the server.";

            addBotMessage(errorMessage);

            speak(errorMessage);

            console.error(error);


        }

        sendBtn.disabled = false;

    }

    // ===============================
    // Button Click
    // ===============================

        sendBtn.addEventListener("click", function (e) {
            e.preventDefault();
            console.log("Send button clicked");
            sendMessage();
        });


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



   // ===============================
// Text To Speech
// ===============================

function speak(text) {

    window.speechSynthesis.cancel();

    text = text
        .replace(/\*\*/g, "")
        .replace(/\*/g, "")
        .replace(/#/g, "")
        .replace(/`/g, "")
        .replace(/\n/g, " ");

    const speech = new SpeechSynthesisUtterance(text);
     // ✅ language recognization
    speech.lang = recognition ? recognition.lang : navigator.language;
    speech.rate = 0.95;
    speech.pitch = 1;
    speech.volume = 1;

    // Select the best English voice available
    if (voices.length === 0) { voices = window.speechSynthesis.getVoices();  }

    const preferredVoice =
    voices.find(v => v.lang === speech.lang) ||
    voices.find(v => v.lang.startsWith(speech.lang.split("-")[0])) ||
    voices.find(v => v.default);


    if (preferredVoice) {
        speech.voice = preferredVoice;
    }

    speech.onstart = () => {

        console.log("AI Speaking");

    };

    speech.onend = () => {

         console.log("AI Finished");

    };

    window.speechSynthesis.speak(speech);

}
        // voice recgonization
       window.speechSynthesis.getVoices().forEach(v => {
                console.log(v.name, "-", v.lang);
            });
});