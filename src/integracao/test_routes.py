# import pytest
# import requests

# BASE_URL = "http://localhost:5000"

# @pytest.mark.parametrize("endpoint,data,expected_status,expected_response", [
#     ("/circle", {"radius": 5}, 200, "The Area of Circle is 78.5"),
#     ("/square", {"side": 5}, 200,"The Area of Square is 25"),
#     ("/triangle", {"base":5,"height":4}, 200, "The Area of Triangle is 10"),
# ])
# def test_api_integration(endpoint, data, expected_status, expected_response):
#     url = BASE_URL + endpoint
#     response = requests.post(url, json=data)

#     assert response.status_code == expected_status
#     if expected_response:
#         assert response.json() == expected_response
