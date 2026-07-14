/*
====================================================
 AgriNova AI v2.0
 Disease Detection Tests
====================================================
*/


import io



from PIL import Image






def create_test_image():


    """
    Create dummy crop image
    for API testing
    """


    image = Image.new(
        "RGB",
        (100,100),
        color="green"
    )


    image_bytes = io.BytesIO()


    image.save(
        image_bytes,
        format="JPEG"
    )


    image_bytes.seek(
        0
    )


    return image_bytes






def test_disease_api_without_image(
    client
):


    """
    Test invalid request
    """


    response = client.post(
        "/api/disease/detect"
    )



    assert response.status_code in [
        400,
        422
    ]







def test_disease_api_with_image(
    client,
    monkeypatch
):


    """
    Test disease prediction API
    """



    def mock_prediction(
        image
    ):


        return {


            "disease":
                "Healthy Leaf",


            "confidence":
                98.5,


            "recommendation":
                "No treatment required"


        }





    monkeypatch.setattr(

        "services.disease_service.DiseaseService.predict",

        mock_prediction

    )





    image = create_test_image()





    response = client.post(

        "/api/disease/detect",

        data={

            "image":
                (
                    image,
                    "leaf.jpg"
                )

        },

        content_type=
            "multipart/form-data"

    )





    data = response.get_json()





    assert response.status_code == 200



    assert data["success"] is True



    assert (
        data["disease"]
        ==
        "Healthy Leaf"
    )



    assert (
        data["confidence"]
        ==
        98.5
    )







def test_disease_response_structure(
    client,
    monkeypatch
):


    """
    Verify response keys
    """



    def mock_prediction(
        image
    ):


        return {


            "disease":
                "Leaf Blight",


            "confidence":
                95,


            "recommendation":
                "Apply fungicide"


        }




    monkeypatch.setattr(

        "services.disease_service.DiseaseService.predict",

        mock_prediction

    )





    image =
        create_test_image()





    response = client.post(

        "/api/disease/detect",

        data={

            "image":
                (
                    image,
                    "test.jpg"
                )

        },

        content_type=
        "multipart/form-data"

    )




    result =
        response.get_json()





    assert "success" in result

    assert "disease" in result

    assert "confidence" in result

    assert "recommendation" in result