document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("cropForm");
    const predictBtn = document.getElementById("predictBtn");

    const resultCard = document.getElementById("resultCard");
    const cropResult = document.getElementById("cropResult");
    const confidenceText = document.getElementById("confidenceText");
    const confidenceBar = document.getElementById("confidenceBar");

    form.addEventListener("submit", async function (e) {

        e.preventDefault();

        // Read values
        const nitrogen = parseFloat(document.getElementById("nitrogen").value);
        const phosphorus = parseFloat(document.getElementById("phosphorus").value);
        const potassium = parseFloat(document.getElementById("potassium").value);
        const temperature = parseFloat(document.getElementById("temperature").value);
        const humidity = parseFloat(document.getElementById("humidity").value);
        const ph = parseFloat(document.getElementById("ph").value);
        const rainfall = parseFloat(document.getElementById("rainfall").value);

        // Validation
        if (
            isNaN(nitrogen) ||
            isNaN(phosphorus) ||
            isNaN(potassium) ||
            isNaN(temperature) ||
            isNaN(humidity) ||
            isNaN(ph) ||
            isNaN(rainfall)
        ) {

            alert("Please fill all fields.");

            return;
        }

        if (
            nitrogen < 0 ||
            phosphorus < 0 ||
            potassium < 0 ||
            humidity < 0 ||
            humidity > 100 ||
            ph < 0 ||
            ph > 14 ||
            rainfall < 0
        ) {

            alert("Please enter valid values.");

            return;
        }

        // Loading State
        predictBtn.disabled = true;

        predictBtn.innerHTML = `
            <span class="spinner-border spinner-border-sm"></span>
            Predicting...
        `;

        resultCard.style.display = "none";

        try {

            const response = await fetch("/crop/predict", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    nitrogen: nitrogen,
                    phosphorus: phosphorus,
                    potassium: potassium,
                    temperature: temperature,
                    humidity: humidity,
                    ph: ph,
                    rainfall: rainfall

                })

            });

            const result = await response.json();

            console.log(result);

            if (!response.ok) {

                throw new Error(result.message || "Prediction failed.");

            }

            if (result.status !== "success") {

                throw new Error(result.message);

            }

            // Show Result
            resultCard.style.display = "block";

            cropResult.innerHTML = "🌾 " + result.crop;

            confidenceText.innerHTML =
                result.confidence.toFixed(2) + "%";

            confidenceBar.style.width =
                result.confidence + "%";

            confidenceBar.innerHTML =
                result.confidence.toFixed(2) + "%";

            // Change Progress Color
            confidenceBar.classList.remove(
                "bg-success",
                "bg-warning",
                "bg-danger"
            );

            if (result.confidence >= 90) {

                confidenceBar.classList.add("bg-success");

            }
            else if (result.confidence >= 70) {

                confidenceBar.classList.add("bg-warning");

            }
            else {

                confidenceBar.classList.add("bg-danger");

            }

        }
        catch (error) {

            console.error("Crop Prediction Error:", error);

            alert(error.message);

        }
        finally {

            predictBtn.disabled = false;

            predictBtn.innerHTML = `
                🌱 Recommend Crop
            `;

        }

    });

});