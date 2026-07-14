document.addEventListener("DOMContentLoaded", () => {

    const imageInput = document.getElementById("image");

    const preview = document.getElementById("preview");

    const predictBtn = document.getElementById("predictBtn");

    const loading = document.getElementById("loading");

    const result = document.getElementById("result");

    const topPredictions = document.getElementById("topPredictions");


    // ============================================
    // Image Preview
    // ============================================

    imageInput.addEventListener("change", function () {

        if (!this.files.length) return;

        const reader = new FileReader();

        reader.onload = function (e) {

            preview.src = e.target.result;

            preview.style.display = "block";

        };

        reader.readAsDataURL(this.files[0]);

    });


    // ============================================
    // Predict
    // ============================================

    predictBtn.addEventListener("click", async () => {

        if (!imageInput.files.length) {

            alert("Please select an image.");

            return;

        }

        loading.style.display = "block";

        result.style.display = "none";

        topPredictions.innerHTML = "";

        const formData = new FormData();

        formData.append(

            "image",

            imageInput.files[0]

        );

        try {

            const response = await fetch(

                "/disease/predict",

                {

                    method: "POST",

                    body: formData

                }

            );

            const data = await response.json();

            loading.style.display = "none";

            if (!data.success) {

                alert(data.message);

                return;

            }

            result.style.display = "block";

            document.getElementById("crop").innerText =
                data.crop;

            document.getElementById("disease").innerText =
                data.disease;

            document.getElementById("confidence").innerText =
                data.confidence + "%";

            document.getElementById("severity").innerText =
                data.severity;

            document.getElementById("treatment").innerText =
                data.treatment;

            document.getElementById("prevention").innerText =
                data.prevention;


            // =====================================
            // Top 3 Predictions
            // =====================================

            if (Array.isArray(data.top_predictions)) {

                data.top_predictions.forEach(item => {

                    topPredictions.innerHTML += `

                        <tr>

                            <td>${item.rank}</td>

                            <td>${item.crop}</td>

                            <td>${item.disease}</td>

                            <td>${item.confidence}%</td>

                        </tr>

                    `;

                });

            }

        }

        catch (error) {

            loading.style.display = "none";

            console.error(error);

            alert("Prediction failed.");

        }

    });

});