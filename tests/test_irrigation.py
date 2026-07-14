/*
====================================================
 AgriNova AI v2.0
 Smart Irrigation Tests
====================================================
*/



def test_irrigation_invalid_request(
    client
):


    """
    Test empty irrigation request
    """



    response = client.post(

        "/api/irrigation",

        json={}

    )



    assert response.status_code in [

        400,
        422

    ]







def test_irrigation_required(
    client,
    monkeypatch
):


    """
    Test irrigation recommendation
    """



    def mock_irrigation(
        data
    ):


        return {


            "status":
                "ON",


            "score":
                85,


            "water_amount":
                "25 Liters",


            "duration":
                "40 Minutes",


            "message":
                "Low moisture detected"


        }





    monkeypatch.setattr(

        "services.irrigation_service.IrrigationService.predict",

        mock_irrigation

    )





    payload = {


        "soil_moisture":
            20,


        "temperature":
            32,


        "humidity":
            40


    }





    response = client.post(

        "/api/irrigation",

        json=payload

    )





    result = response.get_json()





    assert response.status_code == 200



    assert result["status"] == "ON"



    assert result["score"] == 85



    assert (
        result["water_amount"]
        ==
        "25 Liters"
    )







def test_irrigation_response_structure(
    client,
    monkeypatch
):


    """
    Verify response keys
    """



    def mock_predict(
        data
    ):


        return {


            "status":
                "OFF",


            "score":
                30,


            "water_amount":
                "0 Liters",


            "duration":
                "0 Minutes",


            "message":
                "Soil moisture is sufficient"


        }





    monkeypatch.setattr(

        "services.irrigation_service.IrrigationService.predict",

        mock_predict

    )





    response = client.post(

        "/api/irrigation",

        json={


            "soil_moisture":
                80,


            "temperature":
                25,


            "humidity":
                70


        }

    )





    result = response.get_json()





    assert "status" in result

    assert "score" in result

    assert "water_amount" in result

    assert "duration" in result

    assert "message" in result