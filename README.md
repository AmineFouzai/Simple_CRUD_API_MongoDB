# Simple_CRUD_API_MongoDB
<p>Simple CRUD API  Build With  <a href="https://www.tornadoweb.org/en/stable/">Tornado</a>  Framework And  MongoDB   For The Database</p>
<hr>
<h1>#setup:</h1>
<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB </td>
</tr>
<tr>
<td> 2) cd Simple_CRUD_API_SQLITE3</td>
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
<hr>
<h3><a href="https://www.mongodb.com/" >MongoDB</a> is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schema</h3>
<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/Captures/img.jpg" width="500">
<h3><a href="https://pymongo.readthedocs.io/en/stable/">PyMongo</a> is a Python distribution containing tools for working with <a href="https://www.mongodb.com/" >MongoDB</a>, and is the recommended way to work with MongoDB from Python.<h3>
<hr>

<h1>#Connecting To A Database and CRUD Life Cycle:</h1> 
<h4>-In __init__ the Constructor  of the user class change MongoClient('localhost','27017') to MongoClient('mongodb+srv://USER:Password@cluster0.mongodb.net/ect...') if you are using a MongoDB cloud provider and not working with MongoDB localy on your machine in  <a href="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/models/user.py" > models/user.py </a>
 </h4> 

 <h4>-the next four methods are basically the entire object life in the Database , in NoSql its pure english written to handle an object like the example below. <h4>
<h3>ex:</h3>
<br>
<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/Captures/Capture.PNG">
  <br>
<hr>
  <h3>#PS:note that the terminology changes when workin with a non relational database:</h3>
<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/Captures/img2.png">
