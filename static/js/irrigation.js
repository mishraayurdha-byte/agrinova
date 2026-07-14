// ======================================================
// AgriNova AI v2.0
// Smart Irrigation JavaScript
// ======================================================


let irrigationChart = null;



// --------------------------------------------
// Toast
// --------------------------------------------

function showToast(message, type = "info") {

    if (
        window.AgriNova &&
        typeof AgriNova.toast === "function"
    ) {

        AgriNova.toast(message, type);

    } else {

        alert(message);

    }

}




// --------------------------------------------
// Reset Form
// --------------------------------------------

function resetForm() {


    document.getElementById(
        "soilMoisture"
    ).value = "";


    document.getElementById(
        "temperature"
    ).value = "";


    document.getElementById(
        "humidity"
    ).value = "";



    document.getElementById(
        "moistureValue"
    ).innerHTML = "-- %";


    document.getElementById(
        "temperatureValue"
    ).innerHTML = "-- °C";


    document.getElementById(
        "humidityValue"
    ).innerHTML = "-- %";


    document.getElementById(
        "statusValue"
    ).innerHTML = "--";


    document.getElementById(
        "waterRequired"
    ).innerHTML = "-- L";


    document.getElementById(
        "recommendation"
    ).innerHTML =
        "Enter field parameters and click Predict.";

}




// --------------------------------------------
// Predict Irrigation
// --------------------------------------------

async function predictIrrigation() {


    const soil =
        parseFloat(
            document.getElementById(
                "soilMoisture"
            ).value
        );


    const temp =
        parseFloat(
            document.getElementById(
                "temperature"
            ).value
        );


    const humidity =
        parseFloat(
            document.getElementById(
                "humidity"
            ).value
        );



    if (
        isNaN(soil) ||
        isNaN(temp) ||
        isNaN(humidity)
    ) {


        showToast(
            "Please fill all fields.",
            "warning"
        );


        return;

    }



    try {


        const response = await fetch(

            "/api/irrigation",

            {

                method:"POST",

                headers:{

                    "Content-Type":
                    "application/json"

                },


                body:JSON.stringify({

                    soil_moisture: soil,

                    temperature: temp,

                    humidity: humidity

                })

            }

        );



        const data =
            await response.json();



        if(!data.success){


            showToast(
                data.message,
                "danger"
            );


            return;

        }



        updateUI(
            data.result
        );


        loadIrrigationHistory();



        showToast(
            "Prediction Successful",
            "success"
        );


    }


    catch(error){


        console.error(error);


        showToast(
            "Server Error",
            "danger"
        );

    }

}





// --------------------------------------------
// Update Result UI
// --------------------------------------------

function updateUI(result){


    document.getElementById(
        "moistureValue"
    ).innerHTML =
        result.soil_moisture + " %";



    document.getElementById(
        "temperatureValue"
    ).innerHTML =
        result.temperature + " °C";



    document.getElementById(
        "humidityValue"
    ).innerHTML =
        result.humidity + " %";



    document.getElementById(
        "statusValue"
    ).innerHTML =
        result.status;



    document.getElementById(
        "waterRequired"
    ).innerHTML =
        result.water_required + " L";



    document.getElementById(
        "recommendation"
    ).innerHTML =
        result.recommendation;



    drawChart(result);

}





// --------------------------------------------
// Chart
// --------------------------------------------

function drawChart(result){


    const ctx =
        document.getElementById(
            "irrigationChart"
        ).getContext("2d");



    if(irrigationChart){

        irrigationChart.destroy();

    }



    irrigationChart =
        new Chart(ctx,{

            type:"bar",


            data:{


                labels:[

                    "Moisture",

                    "Temperature",

                    "Humidity",

                    "Water"

                ],



                datasets:[{

                    label:
                    "Irrigation Analysis",


                    data:[

                        result.soil_moisture,

                        result.temperature,

                        result.humidity,

                        result.water_required

                    ]

                }]


            },


            options:{

                responsive:true

            }


        });


}





// --------------------------------------------
// Load Irrigation History
// --------------------------------------------

async function loadIrrigationHistory(){


    try{


        const response =
            await fetch(
                "/api/irrigation/history"
            );



        const data =
            await response.json();



        const table =
            document.getElementById(
                "irrigationHistoryBody"
            );



        if(!table){

            return;

        }



        table.innerHTML = "";



        if(
            !data.success ||
            data.history.length === 0
        ){


            table.innerHTML = `

            <tr>

            <td colspan="6"
            class="text-center text-muted">

            No irrigation history available.

            </td>

            </tr>

            `;


            return;

        }





        data.history.forEach(record=>{


            table.innerHTML += `

            <tr>

            <td>${record.created_at}</td>

            <td>${record.soil_moisture}%</td>

            <td>${record.temperature}°C</td>

            <td>${record.humidity}%</td>

            <td>${record.water_required} L</td>

            <td>${record.status}</td>


            </tr>

            `;


        });



    }


    catch(error){


        console.error(
            "History Error:",
            error
        );

    }

}






// --------------------------------------------
// Page Load
// --------------------------------------------

document.addEventListener(

    "DOMContentLoaded",

    function(){


        document

        .getElementById(
            "predictIrrigation"
        )

        .addEventListener(
            "click",
            predictIrrigation
        );



        document

        .getElementById(
            "resetBtn"
        )

        .addEventListener(
            "click",
            resetForm
        );



        // Load previous history

        loadIrrigationHistory();


    }

);