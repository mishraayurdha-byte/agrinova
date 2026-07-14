document.addEventListener("DOMContentLoaded", () => {

    loadStatistics();

    loadDiseaseHistory();

    loadCropHistory();

    loadWeatherHistory();

    loadYieldHistory();

    loadFertilizerHistory();

    loadIrrigationHistory();

    loadChatHistory();

    createCharts();


    // ============================================
    // Refresh
    // ============================================

    document.getElementById(

        "refreshReport"

    ).addEventListener(

        "click",

        () => {

            location.reload();

        }

    );


    // ============================================
    // Export Buttons
    // ============================================

    document.getElementById(

        "exportPdf"

    ).addEventListener(

        "click",

        () => {

            window.print();

        }

    );


    document.getElementById(

        "exportExcel"

    ).addEventListener(

        "click",

        () => {

            alert(

                "Excel Export Coming Soon"

            );

        }

    );

});


// ============================================
// Statistics
// ============================================

async function loadStatistics() {

    const response = await fetch(

        "/api/reports/statistics"

    );

    const data = await response.json();

    document.getElementById(

        "cropCount"

    ).innerText = data.crop_count;

    document.getElementById(

        "diseaseCount"

    ).innerText = data.disease_count;

    document.getElementById(

        "yieldCount"

    ).innerText = data.yield_count;

    document.getElementById(

        "chatCount"

    ).innerText = data.chat_count;

}


// ============================================
// Disease History
// ============================================

async function loadDiseaseHistory() {

    const response = await fetch(

        "/api/reports/diseases"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "diseaseHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.crop}</td>

            <td>${item.disease}</td>

            <td>${item.confidence}%</td>

            <td>${item.severity}</td>

        </tr>

        `;

    });

}


// ============================================
// Crop History
// ============================================

async function loadCropHistory() {

    const response = await fetch(

        "/api/reports/crops"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "cropHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.prediction}</td>

            <td>${item.nitrogen}</td>

            <td>${item.phosphorus}</td>

            <td>${item.potassium}</td>

        </tr>

        `;

    });

}


// ============================================
// Weather History
// ============================================

async function loadWeatherHistory() {

    const response = await fetch(

        "/reports/weather"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "weatherHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.city}</td>

            <td>${item.temperature} °C</td>

            <td>${item.humidity}%</td>

            <td>${item.rainfall ?? "-"} mm</td>

        </tr>

        `;

    });

}


// ============================================
// Yield History
// ============================================

async function loadYieldHistory() {

    const response = await fetch(

        "/reports/yield"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "yieldHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.crop}</td>

            <td>${item.state}</td>

            <td>${item.season}</td>

            <td>${item.predicted_yield}</td>

        </tr>

        `;

    });

}


// ============================================
// Fertilizer History
// ============================================

async function loadFertilizerHistory() {

    const response = await fetch(

        "/reports/fertilizers"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "fertilizerHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.crop}</td>

            <td>${item.recommendation}</td>

        </tr>

        `;

    });

}


// ============================================
// Irrigation History
// ============================================

async function loadIrrigationHistory() {

    const response = await fetch(

        "/reports/irrigation"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "irrigationHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.crop}</td>

            <td>${item.soil_moisture}%</td>

            <td>${item.recommendation}</td>

        </tr>

        `;

    });

}


// ============================================
// Chat History
// ============================================

async function loadChatHistory() {

    const response = await fetch(

        "/reports/chat"

    );

    const data = await response.json();

    const tbody = document.getElementById(

        "chatHistory"

    );

    tbody.innerHTML = "";

    data.forEach(item => {

        tbody.innerHTML += `

        <tr>

            <td>${item.created_at}</td>

            <td>${item.question}</td>

            <td>${item.answer}</td>

        </tr>

        `;

    });

}


// ============================================
// Charts
// ============================================

function createCharts() {

    new Chart(

        document.getElementById(

            "predictionChart"

        ),

        {

            type: "doughnut",

            data: {

                labels: [

                    "Crop",

                    "Disease",

                    "Yield",

                    "Weather",

                    "Fertilizer",

                    "Irrigation"

                ],

                datasets: [

                    {

                        data: [

                            15,

                            12,

                            8,

                            10,

                            6,

                            4

                        ]

                    }

                ]

            }

        }

    );


    new Chart(

        document.getElementById(

            "activityChart"

        ),

        {

            type: "line",

            data: {

                labels: [

                    "Jan",

                    "Feb",

                    "Mar",

                    "Apr",

                    "May",

                    "Jun"

                ],

                datasets: [

                    {

                        label: "Predictions",

                        data: [

                            12,

                            20,

                            15,

                            28,

                            24,

                            36

                        ],

                        fill: false

                    }

                ]

            }

        }

    );

}