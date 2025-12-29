a = {'name': 'Thor Odinson',
    'age': 1500,
    'weapon': ['mjonir', 'stormbreaker'],
    'strongest': True}


# for i in a:
#     print(f"{i} --> {a[i]}")

# # for i in a:
# #     print(i,":",a[i])


'''
city_wise_data = {
    "Delhi": {
        "population_lakh": 450,
        "avg_temp_c": 30,
        "metro": True
    },
    "Mumbai": {
        "population_lakh": 400,
        "avg_temp_c": 32,
        "metro": True
    },
    "Bengaluru": {
        "population_lakh": 325,
        "avg_temp_c": 26,
        "metro": True
    }
}


# print(city_wise_data["Bengaluru"]["population_lakh"])

a=city_wise_data.get("Mumbai").get("avg_temp_c")
print(a)

'''

a.update({"eng": 99})
print(a)

a["sst"] = 50
print(a)