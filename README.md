# Portfolio Builder

>  **🔧Create Your Portfolio Site Within minutes**

![site image](https://lh3.googleusercontent.com/ltHaeziGbC3kvBIZKAhmuS9FVfBb7u1vFnvMPLd5PL1vH-yK7BEA-laSoVT4gdY2V6E=w2400)

 *📃follow given Documentation To create Your Site👇*

---
*To install the library 👇*

```python
pip install portf
```
---
```python
from portf import RunApp,Data

# create object from Data Class
dt = Data("Your Name")

# Edit Variables of Object 
# For Ex
dt.image = "Image Url"

# To The the app
RunApp(port=5000,dt)

```

> *References for Data Class*

| Attribute | Description | Type 
| -----   | ---- | ---- 
| name | Your Name | str 
| resume | Resume download url | str 
| occupation  | your job | str 
|image | image url | str
| insta | Instagram Url | str
| git | github Url | str
| twitter | twitter Url | str
| linkedin | linkedin Ur | str
| about | details about You | str
| age | 0 | int
email | example@gmail.com | email
|phone | +910000000000 | number
address | Your Address | str
language | languages you know | str
Programming | your Skills | str
tools | your Skills | str
internet | Your Skills | str
other | other Skills | str

> Other Attributes

```python 
work = [{"time":"JUNE 2021 - PRESENT",
         "company":"Company Name",
         "post":"Job Post",
         "info":"Info about job"}] # list fo object

projects = [{"time":"JUNE 2021 - PRESENT",
             "name":"Name of Project",
             "info":"Info about project"}] # list fo object

education = [{"time":"2018 - 2020",
             "name":"Name of degree",
             "course":"Course Name",
             "collage":"Collage Name",
             "info":"Info about Course",
             "projects":["Project info",'achievements']}] # list fo object
```
---
` this module uses flask for website generation feel free to contribute`

*More features and themes will be coming soon✅*

> Created By @saigenix , All rights are reserved
