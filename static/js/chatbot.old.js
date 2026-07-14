document.addEventListener("DOMContentLoaded", () => {

    const chatBody = document.getElementById("chatBody");

    const chatInput = document.getElementById("chatInput");

    const sendBtn = document.getElementById("sendMessage");

    const suggestions = document.querySelectorAll(".chat-suggestion");


    // ============================================
    // Initial Message
    // ============================================

    addBotMessage(

        "👋 Hello! I'm AgriNova AI Assistant.<br><br>" +

        "I can help you with:<br>" +

        "🌱 Crop Recommendation<br>" +

        "🦠 Disease Detection<br>" +

        "💧 Irrigation<br>" +

        "🌦 Weather Advice<br>" +

        "🧪 Fertilizer Recommendation"

    );


    // ============================================
    // Send Button
    // ============================================

    sendBtn.addEventListener(

        "click",

        sendMessage

    );


    // ============================================
    // Enter Key
    // ============================================

    chatInput.addEventListener(

        "keypress",

        function(e){

            if(e.key==="Enter"){

                sendMessage();

            }

        }

    );


    // ============================================
    // Suggestions
    // ============================================

    suggestions.forEach(button=>{

        button.addEventListener(

            "click",

            function(){

                chatInput.value=this.innerText;

                sendMessage();

            }

        );

    });


    // ============================================
    // Load History
    // ============================================

    loadHistory();


    // ============================================
    // Send Message
    // ============================================

    async function sendMessage(){

        const message=chatInput.value.trim();

        if(message==="") return;

        addUserMessage(message);

        chatInput.value="";

        const typing=addTyping();

        try{

            const response=await fetch(

                "/api/chat",

                {

                    method:"POST",

                    headers:{

                        "Content-Type":"application/json"

                    },

                    body:JSON.stringify({

                        message:message

                    })

                }

            );

            const data=await response.json();

            typing.remove();

            if(data.success){

                addBotMessage(

                    data.answer

                );

            }

            else{

                addBotMessage(

                    "❌ "+data.message

                );

            }

        }

        catch(error){

            typing.remove();

            addBotMessage(

                "⚠ Unable to connect to AI server."

            );

        }

    }


    // ============================================
    // Load History
    // ============================================

    async function loadHistory(){

        try{

            const response=await fetch(

                "/api/chat/history"

            );

            const data=await response.json();

            if(!data.success) return;

            chatBody.innerHTML="";

            data.history.reverse().forEach(item=>{

                addUserMessage(

                    item.question

                );

                addBotMessage(

                    item.answer

                );

            });

        }

        catch(error){

            console.log(error);

        }

    }


    // ============================================
    // User Message
    // ============================================

    function addUserMessage(message){

        chatBody.innerHTML+=`

        <div class="text-end mb-3">

            <span class="badge bg-success p-3">

                ${message}

            </span>

        </div>

        `;

        scrollBottom();

    }


    // ============================================
    // Bot Message
    // ============================================

    function addBotMessage(message){

        chatBody.innerHTML+=`

        <div class="mb-3">

            <div class="card border-0 bg-light">

                <div class="card-body">

                    ${message}

                </div>

            </div>

        </div>

        `;

        scrollBottom();

    }


    // ============================================
    // Typing
    // ============================================

    function addTyping(){

        const div=document.createElement("div");

        div.innerHTML=`

        <div class="mb-3">

            <div class="card border-0 bg-light">

                <div class="card-body">

                    <span class="spinner-border spinner-border-sm"></span>

                    AI is typing...

                </div>

            </div>

        </div>

        `;

        chatBody.appendChild(div);

        scrollBottom();

        return div;

    }


    // ============================================
    // Scroll
    // ============================================

    function scrollBottom(){

        chatBody.scrollTop=

        chatBody.scrollHeight;

    }

});