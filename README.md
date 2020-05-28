# Simple_CRUD_API_MongoDB
Simple CRUD API  Build With [Tornado](https://www.tornadoweb.org/en/stable/) Framework And  MongoDB   For The Database

------------------------------------

# setup:

<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB </td>
</tr>
<tr>
<td> 2) cd Simple_CRUD_API_MongoDB </td>
</tr>
<tr>
<td> 3) pip install pipenv</td>
</tr>
</tr>
<td> 4) pipenv --python 3.6</td>
</tr>
<tr>
<td> 5) pipenv install - r requirements.txt</td>
</tr>
<tr>
  <td>
    6) run project with <a href="https://pypi.org/project/torn/">torn cli</a> : <b>#command: [ torn run ] </b>  </td>
 </tr>
</table>

-------------------------------

[MongoDB](https://www.mongodb.com/) is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schema

<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/Captures/img.jpg" width="500">

[PyMongo](https://pymongo.readthedocs.io/en/stable/) is a Python distribution containing tools for working with 
[MongoDB](https://www.mongodb.com/), and is the recommended way to work with MongoDB from Python.<h3>

-------------------------------------

## Connecting To A Database and CRUD Life Cycle:

In __init__ the Constructor  of the user class change MongoClient('localhost','27017') to MongoClient('mongodb+srv://USER:Password@cluster0.mongodb.net/ect...') if you are using a MongoDB cloud provider and not working with MongoDB localy on your machine in  
[models/user.py](https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/models/user.py) 

 the next four methods are basically the entire object life in the Database , in NoSql its pure english written to handle an object like the example below.
### ex:


<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/Captures/Capture.PNG">

-----------------------------------------

PS:note that the terminology changes when working with a non relational database:

<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/Captures/img2.png">
