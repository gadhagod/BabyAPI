# BabyAPI

Translate english to baby from any language with this API!

### Usage
**Base URL**:
[https://babyapi.herokuapp.com/v1](https://babyapi.herokuapp.com/v1)

**Making requests**:
Python request:

    import requests
    requests.get('https://babyapi.herokuapp.com/v1', params={'text': 'Aw shucks! I forgot we had a math test today. I hope the test won\'t be hard. Gotta run!'}).json()

Response:

    {'translated': "aw sucks! i fowgot we had a mad test today. i hope da test won't be hawd. gotta wun!"}

Cool right? Use it for (pretty much) whatever you want, because it's licensed under the MIT License.