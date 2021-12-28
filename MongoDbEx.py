import pymongo
#need to install pymongo and
#mongodb login link
#https://account.mongodb.com/account/login?signedOut=true

client = pymongo.MongoClient("mongodb+srv://viss_mgdb:OshomgDb@cluster0.hmfem.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
#create a database
database_name ='student'
#student is the database name here
student_database=client[database_name]
#creating collection is like a table in oracle
collection ='student_detail' # is table name
student_detail_collection=student_database[collection]
# data will be created like json format
student_data={
    "name": "Senthilkumar",
    "colleage" : "mohamad sathak",
    "address" : "Chennai"
}

student_detail_collection.delete_many({})
print(student_detail_collection.deleted_count, " documents deleted.")
student_detail_collection.insert_one(student_data)
# to fetch data from mongodb
student_cursor = student_detail_collection.find()
student_cursor.next()
for student_details in student_detail_collection.find():
  print(student_details)

student_data_list=[
    {"name":"Thalir",
      "sex": "Female",
     "age" : 30,
     "address":"Mudachikkadu"},
    {"name":"Aruthra",
      "sex": "Female",
     "age" : 5,
     "address":"trichitampalam"},
    {"name":"Kruthikahashi",
      "sex": "Female",
     "age" : 2,
     "address":"Ramanathapuram"}
]

student_detail_collection.insert_many(student_data_list)

for student_details in student_detail_collection.find():
 print(student_details)

# To apply filter
 query={"name":"Aruthra"}
 print('Find name Aruthra record only')
 for student_details in student_detail_collection.find(query):
     print(student_details)

#update values
myquery = { "address": "Chennai" } #old one
newvalues = { "$set": { "address": "Madras" } } # New one
print('Update address from chennai to Madras')
student_detail_collection.update_one(myquery, newvalues) # this will update
print('Value after update of address')
for student_details in student_detail_collection.find():
    print(student_details)

print('Find documents where the address starts with the letter "M" or higher:')
muquery = {"address":{"$gt":"M"}}
#student_detail_collection.find(muquery)
for student_details in student_detail_collection.find(muquery):
    print(student_details)
print('To find only the documents where the "name" field starts with the letter "S", use the regular expression {"$regex": "^S"}:')
myquery = {"name":{"$regex":"^S"}}

for student_details in student_detail_collection.find(myquery):
    print('Name starts with S are',student_details)

print('The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).')
print('''sort("name", 1) #ascending
        sort("name", -1) #descending''')
for student_details in student_detail_collection.find().sort("name",1):
    print('Name sorted ny ascending order are',student_details)
print('Names sorted By Dscending Orders:-')
for student_details in student_detail_collection.find().sort("name",-1):
    print('Name sorted ny Dscending order are',student_details)
print('''To limit the result in MongoDB, we use the limit() method.
        The limit() method takes one parameter, a number defining how many documents to return.''')
for student_details in student_detail_collection.find().sort("name",-1).limit(2):
    print('Name sorted ny Dscending order are',student_details)
print('You can delete a table, or collection as it is called in MongoDB, by using the drop() method.')

student_detail_collection.drop()
print('Collection has been dropped')