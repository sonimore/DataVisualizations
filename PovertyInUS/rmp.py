# Get data from the morph.io api
import requests

# We're always asking for json because it's the easiest to deal with
morph_api_url = "https://api.morph.io/chrisguags/ratemyprofessors/data.json"

# Keep this key secret!
morph_api_key = "KqfZoD2VKYSXfMffhdOM"

r = requests.get(morph_api_url, params={
  'key': morph_api_key,
  'query': "select * from "data" limit 10"
})

print r.json()