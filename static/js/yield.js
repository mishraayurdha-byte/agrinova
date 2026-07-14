/*
====================================================
 AgriNova AI v2.0
 Yield Prediction JavaScript
====================================================
*/


"use strict";


document.addEventListener(
    "DOMContentLoaded",
    function(){


        const form =
            document.getElementById(
                "yieldForm"
            );



        if(!form){

            return;

        }




        form.addEventListener(
            "submit",
            async function(event){


                event.preventDefault();




                const payload = {


                    crop:
                    document.getElementById(
                        "crop"
                    ).value,



                    area:
                    Number(
                        document.getElementById(
                            "area"
                        ).value
                    ),



                    rainfall:
                    Number(
                        document.getElementById(
                            "rainfall"
                        ).value
                    ),



                    temperature:
                    Number(
                        document.getElementById(
                            "temperature"
                        ).value
                    ),



                    humidity:
                    Number(
                        document.getElementById(
                            "humidity"
                        ).value
                    ),



                    soil:
                    document.getElementById(
                        "soil"
                    ).value


                };





                try{


                    AgriNova.showLoader();




                    const result =
                        await AgriNova.request(
                            "/yield/predict",
                            {


                                method:
                                    "POST",



                                body:
                                    JSON.stringify(
                                        payload
                                    )


                            }
                        );





                    if(result){


                        displayYieldResult(
                            result
                        );



                        AgriNova.toast(
                            "Yield prediction completed",
                            "success"
                        );


                    }





                }


                catch(error){


                    console.error(
                        error
                    );


                    AgriNova.toast(
                        error.message,
                        "danger"
                    );


                }


                finally{


                    AgriNova.hideLoader();


                }


            }
        );


    }
);





/*
====================================
 Display Yield Result
====================================
*/


function displayYieldResult(
    result
){



    const box =
        document.getElementById(
            "yieldResult"
        );



    if(!box){

        return;

    }




    box.innerHTML = `


        <div class="prediction-result">


            <h3 class="text-success">

                Estimated Yield

            </h3>



            <h1>

                ${result.predicted_yield}

                <small>

                    tons/hectare

                </small>

            </h1>




            <hr>




            <p>

                Crop:

                <strong>

                    ${result.crop}

                </strong>

            </p>




            <p>

                Model Accuracy:

                <strong>

                    ${result.accuracy || "N/A"}

                </strong>

            </p>




            <p>

                Recommendation:

                <br>

                ${result.recommendation ||
                "Follow optimized farming practices."}

            </p>



        </div>


    `;



}