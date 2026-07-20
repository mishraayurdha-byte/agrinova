/*
====================================================
 AgriNova AI
 Weather Intelligence Module
====================================================
*/

"use strict";

let temperatureChart = null;

document.addEventListener("DOMContentLoaded", function () {

    const searchButton = document.getElementById("weatherSearch");
    const cityInput = document.getElementById("city");

    if (!searchButton || !cityInput) {
        return;
    }
        // Load history table
            loadWeatherHistory();

    // Default city
    cityInput.value = "Delhi";

    loadWeather("Delhi");
    loadForecast("Delhi");

    searchButton.addEventListener("click", async function () {

        const city = cityInput.value.trim();

        if (!city) {

            showToast("Please enter a city name.", "warning");

            return;
        }

        await loadWeather(city);

        await loadForecast(city);

         // Refresh history after search
            loadWeatherHistory();

    });

});


/*==================================================
    Load Current Weather
==================================================*/

async function loadWeather(city) {

    try {

        const response = await fetch(
            `/api/weather?city=${encodeURIComponent(city)}`
        );

        const result = await response.json();

        if (!result.success) {

            showToast(result.message, "danger");

            return;

        }

        updateWeatherUI(result.weather);

        updateAdvice(result.farming_advice);
        console.

        showMessage("Weather updated successfully.", "success");

    }

    catch (error) {

        console.error(error);

        showMessage("Unable to fetch weather.", "danger");

    }

}


/*==================================================
    Load Forecast
==================================================*/

async function loadForecast(city) {

    const container =
        document.getElementById("forecastContainer");

    if (!container) {
        return;
    }

    try {

        const response = await fetch(
            `/api/forecast?city=${encodeURIComponent(city)}`
        );

        const result = await response.json();

        if (!result.success) {
            return;
        }

        container.innerHTML = "";

        const labels = [];

        const temperatures = [];

        const forecast =
            result.forecast.list.filter(
                (item, index) => index % 8 === 0
            );

        forecast.forEach(day => {

            labels.push(
                day.dt_txt.split(" ")[0]
            );

            temperatures.push(
                day.main.temp
            );

            container.innerHTML += `

                <div class="col-lg-2 col-md-4 col-sm-6 mb-3">

                    <div class="card shadow-sm h-100">

                        <div class="card-body text-center">

                            <h6>${day.dt_txt.split(" ")[0]}</h6>

                            <img
                                src="https://openweathermap.org/img/wn/${day.weather[0].icon}@2x.png"
                                width="60"
                                alt="Weather Icon">

                            <h5>${day.main.temp.toFixed(1)} °C</h5>

                            <p class="mb-0">

                                ${day.weather[0].main}

                            </p>

                        </div>

                    </div>

                </div>

            `;

        });

        drawTemperatureChart(
            labels,
            temperatures
        );

    }

    catch (error) {

        console.error(error);

    }

}


/*==================================================
    Update Weather Cards
==================================================*/

function updateWeatherUI(weather) {

    setValue("cityName", weather.city);

    setValue(
        "temperatureValue",
        `${weather.temperature} °C`
    );

    setValue(
        "humidityValue",
        `${weather.humidity} %`
    );

    setValue(
        "pressureValue",
        `${weather.pressure} hPa`
    );

    setValue(
        "windValue",
        `${weather.wind_speed} m/s`
    );

    setValue(
        "conditionValue",
        weather.condition
    );

    setValue(
        "weatherDescription",
        weather.description
    );

}


/*==================================================
    AI Farming Advice
==================================================*/

function updateAdvice(advice) {

    const list =
        document.getElementById("adviceList");

    if (!list) {
        return;
    }

    list.innerHTML = "";

    advice.forEach(item => {

        list.innerHTML += `

            <li class="list-group-item">

                ${item}

            </li>

        `;

    });

}


/*==================================================
    Temperature Chart
==================================================*/

function drawTemperatureChart(labels, data) {

    const canvas =
        document.getElementById(
            "temperatureChart"
        );

    if (!canvas) {
        return;
    }

    if (temperatureChart) {

        temperatureChart.destroy();

    }

    temperatureChart = new Chart(canvas, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "Temperature (°C)",

                    data: data,

                    borderColor: "#198754",

                    backgroundColor:
                        "rgba(25,135,84,0.15)",

                    fill: true,

                    borderWidth: 3,

                    tension: 0.4

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: true

                }

            },

            scales: {

                y: {

                    beginAtZero: false

                }

            }

        }

    });

}


/*==================================================
    Safe DOM Update
==================================================*/

function setValue(id, value) {

    const element =
        document.getElementById(id);

    if (element) {

        element.innerHTML = value;

    }

}


/*==================================================
    Load Weather History
==================================================*/

async function loadWeatherHistory() {
console.log("Loading weather history...");

    try {

        const response = await fetch(
            "/api/weather/history"
        );


        const result = await response.json();


        const table =
            document.getElementById(
                "historyTable"
            );


        if (!table) {

            return;

        }


        table.innerHTML = "";


        if (
            !result.success ||
            result.history.length === 0
        ) {


            table.innerHTML = `

                <tr>

                    <td colspan="6"
                    class="text-center text-muted">

                        No weather history available.

                    </td>

                </tr>

            `;


            return;

        }



        result.history.forEach(item => {


            table.innerHTML += `

                <tr>
                    <td>${item.city}</td>
                    <td>${item.temperature} °C</td>
                    <td>${item.humidity} %</td>
                    <td>${item.wind_speed} m/s</td>
                    <td>${item.weather}</td>
                    <td>${item.created_at}</td>
                </tr>

            `;


        });


    }

    catch(error) {

        console.error(
            "Weather History Error:",
            error
        );

    }

}



/*==================================================
    Toast Helper
==================================================*/

function showToast(message, type) {

    if (window.AgriNova &&
        typeof AgriNova.toast === "function") {

        AgriNova.toast(message, type);

    } else {

        console.error(error);

    }

}