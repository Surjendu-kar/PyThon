###
prg = {'JS':['Atom','VS'],'CS':'VS','Python':['Pycharm','Subline'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prg)
print(prg['JS'][1])
print(prg['Python'][0])
print(prg['Java']['JEE'])

# Nested a list in a dictionary
travel_log = {
    "france" : ["paris","Lille","Dijon"],
    "Germany" : ["Berlin","Hamburg","Stuttgart"]
}
print(travel_log)

# Nesting dictionary in a dictionary
travel_log = {
    "france" : {"cities_visited":["paris","Lille","Dijon"],"total_visits":12},
    "Germany" : {"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":9}
}
print("\n",travel_log)
print(travel_log["france"]["cities_visited"])
print(travel_log["france"]["total_visits"])
print(travel_log["Germany"]["cities_visited"][2])

# Nesting dictionary in a list
travel_log = [
    {
        "country":"france",
        "cities_visited":["paris","Lille","Dijon"],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":9}
]
print(travel_log[0])