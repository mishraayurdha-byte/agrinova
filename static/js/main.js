/*
==========================================================
AgriNova AI v2.0
Main JavaScript

Handles:
- API communication
- Loader
- Toast notifications
- AI interactions

==========================================================
*/


// ======================================================
// Loader Control
// ======================================================


function showLoader(){


    const loader = document.getElementById(
        "agrinovaLoader"
    );


    if(loader){

        loader.style.display = "flex";

    }

}





function hideLoader(){


    const loader = document.getElementById(
        "agrinovaLoader"
    );


    if(loader){

        loader.style.display = "none";

    }

}





// Hide loader on page load

window.addEventListener(
    "load",
    () => {

        hideLoader();

    }
);







// ======================================================
// Toast System
// ======================================================


function showToast(
    type,
    message
){


    let toastElement;



    if(type === "success"){


        document.getElementById(
            "successMessage"
        ).innerHTML = message;


        toastElement =
            document.getElementById(
                "successToast"
            );


    }



    else if(type === "warning"){


        document.getElementById(
            "warningMessage"
        ).innerHTML = message;


        toastElement =
            document.getElementById(
                "warningToast"
            );


    }



    else{


        document.getElementById(
            "errorMessage"
        ).innerHTML = message;


        toastElement =
            document.getElementById(
                "errorToast"
            );

    }




    if(toastElement){


        const toast =
            new bootstrap.Toast(
                toastElement
            );


        toast.show();

    }


}







// ======================================================
// API Helper
// ======================================================


async function apiRequest(
    url,
    options={}
){


    try{


        showLoader();



        const response =
            await fetch(
                url,
                options
            );



        const data =
            await response.json();



        hideLoader();



        return data;



    }


    catch(error){


        hideLoader();



        showToast(
            "error",
            "Server connection failed."
        );



        console.error(
            error
        );


        return null;


    }


}







// ======================================================
// Load Dashboard Statistics
// ======================================================


async function loadDashboard(){


    const result =
        await apiRequest(
            "/api/analytics/dashboard"
        );



    if(
        result &&
        result.success
    ){


        console.log(
            "Dashboard:",
            result.data
        );


    }


}







// ======================================================
// AI Chatbot
// ======================================================


async function askAgriNovaAI(question){


    return await apiRequest(

        "/chatbot/ask",

        {


            method:"POST",


            headers:{


                "Content-Type":
                    "application/json"


            },


            body:

                JSON.stringify({

                    question:
                        question

                })


        }

    );


}







// ======================================================
// Disease Detection Upload
// ======================================================


async function detectDisease(
    imageFile
){


    const formData =
        new FormData();



    formData.append(

        "image",

        imageFile

    );



    return await apiRequest(

        "/disease/predict",

        {


            method:"POST",


            body:
                formData


        }

    );


}







// ======================================================
// Irrigation Recommendation
// ======================================================


async function getIrrigationRecommendation(
    farmData
){


    return await apiRequest(

        "/irrigation/recommend",

        {


            method:"POST",


            headers:{


                "Content-Type":
                    "application/json"


            },


            body:

                JSON.stringify(
                    farmData
                )


        }

    );


}







// ======================================================
// Weather Data
// ======================================================


async function getWeather(
    city
){


    return await apiRequest(

        `/weather/current?city=${city}`

    );


}







// ======================================================
// Initialize
// ======================================================


document.addEventListener(

    "DOMContentLoaded",

    ()=>{


        loadDashboard();


    }

);