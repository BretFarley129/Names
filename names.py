students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(arr):
    count = 1
    for i in arr:
        length = len(i["first_name"] + i["last_name"])
        print count,"-", i["first_name"] + " " + i["last_name"],"-",length
        count += 1
names(students)

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
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I could not get this function to work the way I wanted it to, so I've commented
it out but left to revisit at a later time. In the meantime, I got the desired 
result by using my names() function in a global scope.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def betterNames(d):
    for i in d.iterkeys():
        print i+":"
        for j in d.itervalues():
            names(j)

betterNames(users)
"""

print "Students:"
names(users["Students"])

print "Instructors:"
names(users["Instructors"])

