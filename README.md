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

In __init__ the Constructor  of the user class change 

```python
MongoClient('localhost','27017')
````
to

```python
MongoClient('mongodb+srv://USER:Password@cluster0.mongodb.net/ect...') 
```
if you are using a MongoDB cloud provider and not working with MongoDB localy on your machine
in [models/user.py](https://github.com/MedAmineFouzai/Simple_CRUD_API_MongoDB/blob/master/models/user.py) 

the next four methods are basically the entire object life in the Database , in NoSql its pure english written to handle an object like the example below.

### ex:

```python
class user(object):
    def __init__(self,first_name=None,last_name=None,date=None):
        client=MongoClient('localhost', 27017)# or  uri from MongoDB Atlas 
        self.db=client.user
        self.first_name=first_name
        self.last_name=last_name
        self.date=date
        
    def add(self):
    
        return self.db.users.insert_one({
         "first_name":self.first_name,
         "last_name":self.last_name,
         "date":self.date
         })
        
    def delete(self,_id):
        self.db.users.find_one_and_delete({
        "_id":ObjectId(_id)
        })

    def update(self,_id):
        self.db.users.find_one_and_replace({
          "_id":ObjectId(_id)
        },
        { 
          "first_name":self.first_name,
          "last_name":self.last_name,
          "date":self.date
          })
        

    def get(self):
        
        documents=self.db.users.find_raw_batches()
        return [ str(decode_all(document)) for document in documents]
```

-----------------------------------------

### PS:

note that the terminology changes when working with a non relational database:

| RDBMS   |      MongoDB      |
|----------|:-------------:|
| Table|  Collection |
| Row |   JSON Document  |
