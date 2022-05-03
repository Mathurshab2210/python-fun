travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country():
    new={}
    new["country"]=input("enter name of city")
    new["visits"]=int(input("enter number of visits"))
    list=[]
    new["cities"]= list
    for i in range(0,5):
        list.append(input(f"enter name of city {i}"))
        
    travel_log.append(new)


add_new_country()


print(travel_log)
