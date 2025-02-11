


def restaurants():
    rest_list = []
    filtered_rests = []
    filtered_ratings = []
    rest_count = int(input("Enter the number of restorants:" ))
    for i in range(rest_count):
        rest_name = input("Restorant name: ")
        rest_rating = float(input("Restorant rating "))
        rest_list.append({"name": rest_name, "rating": rest_rating}) 
    min_search_rating = input("Enter the minimum rating: ")
    if min_search_rating != int or float:
        min_search_rating = 4
    for dict in rest_list:
        for key,value in dict.items():
            if key == 'rating' and value >=4:
                filtered_ratings.append(dict["rating"])
                filtered_rests.append(dict["name"])
    print(sorted(filtered_rests))
    print(filtered_ratings)

restaurants()
    

       # if value[1] >=min_search_rating:
        #     print(value)
#             filtered_list.append(name)
# print(filtered_list)
    #     print(restuarants.keys())

#  sukuriam tuscia listą su restoranais: restaurants = []
# leidziam useriui ivesti kiek restoranu sukurti? (skaicius int)
# iteruojam per tą skaičių ir:
#     prasom name + rating
#     sukuriam iš jų diciotnary
#     restaurants.append(new_restaurant)

# restaurants = [{"name": "Vytautas", "rating": 3.0}, {"name": "Mindaugas", "rating": 10.0}, {"name": "Another_one", "rating": 9.0}]


# minimum_threshold = input("enter minimum threshold: ")
# check if user entered anything at all?:
#    set minimum_therhsold and convert to float
# else:  use default  4.0


# iterate through restaurants:
#    check if restaurant["rating"] >= minimum_therhsold

# restaurants = [{"name": "Mindaugas", "rating": 10.0}, {"name": "Another_one", "rating": 9.0}]

# sort the restaurants by name

# print the result