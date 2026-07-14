/*
====================================================
 AgriNova AI v2.0
 Weather Module Tests
====================================================
*/



def test_weather_without_city(
    client
):


    """
    Test missing city parameter
    """



    response = client.get(

        "/api/weather"

    )



    assert response.status_code in [

        400,
        422

    ]








def test_weather_success(
    client,
    monkeypatch
):


    """
    Test weather API response
    """



    def mock_weather(
        city
    ):


        return {


            "success":
                True,


            "city":
                city,


            "temperature":
                30,


            "humidity":
                60,


            "pressure":
                1012,


            "wind_speed":
                12,


            "condition":
                "Cloudy",


            "description":
                "Partly cloudy"


        }





    monkeypatch.setattr(

        "services.weather_service.WeatherService.get_weather",

        mock_weather

    )





    response = client.get(

        "/api/weather?city=Delhi"

    )





    result = response.get_json()





    assert response.status_code == 200



    assert result["success"] is True



    assert result["city"] == "Delhi"



    assert result["temperature"] == 30



    assert result["humidity"] == 60







def test_weather_response_structure(
    client,
    monkeypatch
):


    """
    Validate weather JSON structure
    """



    def mock_weather(
        city
    ):


        return {


            "success":
                True,


            "city":
                city,


            "temperature":
                28,


            "humidity":
                55,


            "pressure":
                1010,


            "wind_speed":
                10,


            "condition":
                "Sunny",


            "description":
                "Clear sky"


        }





    monkeypatch.setattr(

        "services.weather_service.WeatherService.get_weather",

        mock_weather

    )





    response = client.get(

        "/api/weather?city=Bhubaneswar"

    )





    result = response.get_json()





    assert "success" in result

    assert "city" in result

    assert "temperature" in result

    assert "humidity" in result

    assert "wind_speed" in result

    assert "condition" in result