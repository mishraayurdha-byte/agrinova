/*
====================================================
 AgriNova AI v2.0
 Yield Prediction Tests
====================================================
*/



def test_yield_api_invalid_request(
    client
):


    """
    Test empty request validation
    """



    response = client.post(

        "/api/yield/predict",

        json={}

    )



    assert response.status_code in [

        400,
        422

    ]







def test_yield_prediction_success(
    client,
    monkeypatch
):


    """
    Test successful yield prediction
    """



    def mock_predict(
        data
    ):


        return {


            "crop":
                "Rice",


            "predicted_yield":
                6.2,


            "accuracy":
                "95%",


            "recommendation":
                "Maintain soil nutrients"


        }





    monkeypatch.setattr(

        "services.yield_service.YieldService.predict",

        mock_predict

    )





    payload = {


        "crop":
            "Rice",



        "area":
            2,



        "rainfall":
            120,



        "temperature":
            28,



        "humidity":
            70,



        "soil":
            "Loamy"


    }





    response = client.post(

        "/api/yield/predict",

        json=payload

    )





    result = response.get_json()





    assert response.status_code == 200



    assert result["success"] is True



    assert (
        result["crop"]
        ==
        "Rice"
    )



    assert (
        result["predicted_yield"]
        ==
        6.2
    )







def test_yield_response_structure(
    client,
    monkeypatch
):


    """
    Validate API response keys
    """



    def mock_predict(
        data
    ):


        return {


            "crop":
                "Wheat",


            "predicted_yield":
                5.5,


            "accuracy":
                "93%",


            "recommendation":
                "Optimize irrigation"


        }





    monkeypatch.setattr(

        "services.yield_service.YieldService.predict",

        mock_predict

    )





    response = client.post(

        "/api/yield/predict",

        json={


            "crop":
                "Wheat",


            "area":
                3,


            "rainfall":
                100,


            "temperature":
                25,


            "humidity":
                65,


            "soil":
                "Clay"

        }

    )





    result = response.get_json()





    assert "success" in result

    assert "crop" in result

    assert "predicted_yield" in result

    assert "recommendation" in result