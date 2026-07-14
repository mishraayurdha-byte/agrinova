document.addEventListener("DOMContentLoaded", () => {

    loadStatistics();

    loadRecentActivity();

    loadTopDiseases();

    loadTopCrops();

    createCharts();

    document.getElementById(

        "refreshAnalytics"

    ).addEventListener(

        "click",

        refreshAnalytics

    );

});


// ==========================================
// Refresh
// ==========================================

function refreshAnalytics() {

    loadStatistics();

    loadRecentActivity();

    loadTopDiseases();

    loadTopCrops();

}


// ==========================================
// Statistics
// ==========================================

async function loadStatistics() {

    try {

        const response = await fetch(

            "/reports/statistics"

        );

        const data = await response.json();


        document.getElementById(

            "totalDisease"

        ).innerText = data.disease_count;


        document.getElementById(

            "totalCrop"

        ).innerText = data.crop_count;


        document.getElementById(

            "totalChat"

        ).innerText = data.chat_count;


        document.getElementById(

            "totalPredictions"

        ).innerText =

            data.crop_count +

            data.disease_count +

            data.yield_count +

            data.weather_count +

            data.fertilizer_count +

            data.irrigation_count;

    }

    catch (error) {

        console.error(

            error

        );

    }

}


// ==========================================
// Recent Activity
// ==========================================

async function loadRecentActivity() {

    try {

        const response = await fetch(

            "/reports/activity"

        );

        const result = await response.json();

        const tbody = document.getElementById(

            "activityTable"

        );

        tbody.innerHTML = "";


        const activities = [

            ...result.data.diseases.map(item => ({

                module: "Disease",

                name: item.disease,

                date: item.created_at

            })),

            ...result.data.crops.map(item => ({

                module: "Crop",

                name: item.prediction,

                date: item.created_at

            })),

            ...result.data.weather.map(item => ({

                module: "Weather",

                name: item.city,

                date: item.created_at

            })),

            ...result.data.fertilizers.map(item => ({

                module: "Fertilizer",

                name: item.recommendation,

                date: item.created_at

            }))

        ];


        activities.sort((a, b) =>

            new Date(b.date) -

            new Date(a.date)

        );


        activities.slice(0, 10).forEach(item => {

            tbody.innerHTML += `

            <tr>

                <td>${item.date}</td>

                <td>${item.module}</td>

                <td>${item.name}</td>

                <td>

                    <span class="badge bg-success">

                        Completed

                    </span>

                </td>

            </tr>

            `;

        });

    }

    catch (error) {

        console.error(

            error

        );

    }

}

// ==========================================
// Top Diseases
// ==========================================

async function loadTopDiseases() {

    try {

        const response = await fetch(

            "/reports/diseases"

        );

        const data = await response.json();

        const table = document.getElementById(

            "topDiseaseTable"

        );

        table.innerHTML = "";

        const diseaseMap = {};

        data.forEach(item => {

            if (!diseaseMap[item.disease]) {

                diseaseMap[item.disease] = {

                    count: 0,

                    confidence: 0

                };

            }

            diseaseMap[item.disease].count++;

            diseaseMap[item.disease].confidence +=

                parseFloat(item.confidence);

        });

        const sorted = Object.entries(

            diseaseMap

        ).sort(

            (a, b) =>

            b[1].count - a[1].count

        );

        sorted.slice(0, 10).forEach(

            ([name, value], index) => {

                table.innerHTML += `

                <tr>

                    <td>${index + 1}</td>

                    <td>${name}</td>

                    <td>${value.count}</td>

                    <td>${(

                        value.confidence /

                        value.count

                    ).toFixed(2)}%</td>

                </tr>

                `;

            }

        );

    }

    catch (error) {

        console.error(error);

    }

}


// ==========================================
// Top Crops
// ==========================================

async function loadTopCrops() {

    try {

        const response = await fetch(

            "/reports/crops"

        );

        const data = await response.json();

        const table = document.getElementById(

            "topCropTable"

        );

        table.innerHTML = "";

        const cropMap = {};

        data.forEach(item => {

            if (!cropMap[item.prediction]) {

                cropMap[item.prediction] = 0;

            }

            cropMap[item.prediction]++;

        });

        const sorted = Object.entries(

            cropMap

        ).sort(

            (a, b) =>

            b[1] - a[1]

        );

        sorted.slice(0, 10).forEach(

            ([crop, count], index) => {

                table.innerHTML += `

                <tr>

                    <td>${index + 1}</td>

                    <td>${crop}</td>

                    <td>${count}</td>

                </tr>

                `;

            }

        );

    }

    catch (error) {

        console.error(error);

    }

}


// ==========================================
// Charts
// ==========================================

async function createCharts() {

    try {

        const statsResponse = await fetch(

            "/reports/statistics"

        );

        const stats = await statsResponse.json();

        // Disease/Crop/Yield Distribution

        new Chart(

            document.getElementById(

                "diseaseChart"

            ),

            {

                type: "doughnut",

                data: {

                    labels: [

                        "Disease",

                        "Crop",

                        "Yield",

                        "Weather",

                        "Fertilizer",

                        "Irrigation"

                    ],

                    datasets: [

                        {

                            data: [

                                stats.disease_count,

                                stats.crop_count,

                                stats.yield_count,

                                stats.weather_count,

                                stats.fertilizer_count,

                                stats.irrigation_count

                            ]

                        }

                    ]

                }

            }

        );


        // Crop Distribution

        new Chart(

            document.getElementById(

                "cropChart"

            ),

            {

                type: "bar",

                data: {

                    labels: [

                        "Crop",

                        "Disease",

                        "Yield",

                        "Weather"

                    ],

                    datasets: [

                        {

                            label: "Predictions",

                            data: [

                                stats.crop_count,

                                stats.disease_count,

                                stats.yield_count,

                                stats.weather_count

                            ]

                        }

                    ]

                }

            }

        );


        // Monthly Usage

        new Chart(

            document.getElementById(

                "usageChart"

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

                        "Jun",

                        "Jul"

                    ],

                    datasets: [

                        {

                            label: "AI Requests",

                            data: [

                                10,

                                18,

                                25,

                                30,

                                36,

                                45,

                                stats.chat_count

                            ],

                            fill: false,

                            tension: 0.4

                        }

                    ]

                }

            }

        );


        // Accuracy

        new Chart(

            document.getElementById(

                "accuracyChart"

            ),

            {

                type: "radar",

                data: {

                    labels: [

                        "Disease",

                        "Crop",

                        "Yield",

                        "Weather",

                        "Fertilizer"

                    ],

                    datasets: [

                        {

                            label: "Accuracy",

                            data: [

                                98,

                                97,

                                96,

                                95,

                                98

                            ]

                        }

                    ]

                }

            }

        );

    }

    catch (error) {

        console.error(error);

    }

}


// ==========================================
// Auto Refresh
// ==========================================

setInterval(() => {

    refreshAnalytics();

}, 60000);