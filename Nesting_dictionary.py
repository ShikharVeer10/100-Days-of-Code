#Nesting Dictionaries
capitals={
    "France":"Paris",
    "Germany":"Berlin",
}
print(capitals)

#Nesting a list in dictionary

travel_log={
    "France":["Paris","Lille","Dijon"],
    "India":["Mumbai","Delhi","Hyderabad"]
}
print(travel_log)

#Nesting a dictionary in a dictionary
visit_log={
    "France":{"Paris":5,"Lille":6,"Dijon":2},
    "India":{"Mumbai":3,"Delhi":4,"Hyderabad":8}
}
print(visit_log)

trip_log={
    "France":{"Cities Visited":["Paris","Lille","Dijon"],"total_visits":12},
    "India":{"Cities Visited":["Mumbai","Delhi","Hyderabad"], "total_visits":15},
}
print(trip_log)

#Nesting Dictionary in a list
travel_log= [
    {
     "Country":"France",
     "Cities Visited":["Paris","Lille","Dijon"],
     "total_visits":12
    },
    {
        "Country":"India",
     "Cities Visited":["Mumbai","Delhi","Hyderabad"],
       "total_visits":15
    },
]

print(travel_log)