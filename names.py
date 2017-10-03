students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


for i in students:
    print i["first_name"] + " " + i["last_name"]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students:"
count = 0
for i in users["Students"]:
    string = i["first_name"]+i["last_name"]
    length = str(len(string))
    uh = str(count)
    print uh+" - "+i["first_name"]+" "+i["last_name"]+" - "+length
    count += 1

print "Instructors:
"
count = 0
for i in users["Instructors"]:
    string = i["first_name"]+i["last_name"]
    length = str(len(string))
    uh = str(count)
    print uh+" - "+i["first_name"]+" "+i["last_name"]+" - "+length
    count += 1
# #DICTIONARY > LIST > DICTIONARIES
# for arr in users:
#     print "{}:".format(arr)
    
#     #i represents the key values
#     for i in range(0,len(arr)):
#         print arr[0]
        
        
