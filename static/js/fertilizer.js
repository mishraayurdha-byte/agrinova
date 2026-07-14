document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("fertilizerForm");
    const resultCard = document.getElementById("resultCard");

    form.addEventListener("submit", async function (e) {

        e.preventDefault();

        const payload = {

            crop: document.getElementById("crop").value,

            soil_type: document.getElementById("soil_type").value,

            nitrogen: document.getElementById("nitrogen").value,

            phosphorus: document.getElementById("phosphorus").value,

            potassium: document.getElementById("potassium").value

        };

        resultCard.innerHTML = `

            <div class="text-center py-5">

                <div class="spinner-border text-success"></div>

                <p class="mt-3">

                    Generating recommendation...

                </p>

            </div>

        `;

        try {

            const response = await fetch("/fertilizer/recommend", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(payload)

            });

            const data = await response.json();

            if (!data.success) {

                resultCard.innerHTML = `

                    <div class="alert alert-danger">

                        ${data.message}

                    </div>

                `;

                return;

            }

            const result = data.result;

            resultCard.innerHTML = `

                <h4 class="text-success mb-3">

                    🌱 Recommendation Result

                </h4>

                <table class="table table-bordered">

                    <tr>

                        <th width="35%">Crop</th>

                        <td>${result.crop}</td>

                    </tr>

                    <tr>

                        <th>Soil Type</th>

                        <td>${result.soil_type}</td>

                    </tr>

                    <tr>

                        <th>Soil Health</th>

                        <td>

                            <span class="badge bg-success">

                                ${result.soil_health}

                            </span>

                        </td>

                    </tr>

                    <tr>

                        <th>Nitrogen</th>

                        <td>${result.nitrogen_status}</td>

                    </tr>

                    <tr>

                        <th>Phosphorus</th>

                        <td>${result.phosphorus_status}</td>

                    </tr>

                    <tr>

                        <th>Potassium</th>

                        <td>${result.potassium_status}</td>

                    </tr>

                </table>

                <hr>

                <h5>

                    💊 Recommended Fertilizers

                </h5>

                <ul>

                    ${result.recommended_fertilizer.map(f =>
                        `<li>${f}</li>`
                    ).join("")}

                </ul>

                <hr>

                <h5>

                    📋 Advice

                </h5>

                <ul>

                    ${result.advice.map(a =>
                        `<li>${a}</li>`
                    ).join("")}

                </ul>

                <hr>

                <h5>

                    🌾 General Tips

                </h5>

                <ul>

                    ${result.general_tips.map(t =>
                        `<li>${t}</li>`
                    ).join("")}

                </ul>

            `;

        }

        catch (error) {

            console.error(error);

            resultCard.innerHTML = `

                <div class="alert alert-danger">

                    Unable to connect to the server.

                </div>

            `;

        }

    });

});