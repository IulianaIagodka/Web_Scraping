import requests
import json

def test_post_headers_body_json():
  url = "https://www.python.org"

  payload = {'key1': 1, 'key2': 'value2'}
  headers = {'Content-Type': 'application/json' }

  response = requests.request("HEAD", url, data = json.dumps(payload,indent=4))

  # Validate response headers and body contents, e.g. status code.
  assert response.status_code == 200
  resp_body = response.json()
  assert resp_body['url'] == url

  print(response.text.encode('utf8'))
