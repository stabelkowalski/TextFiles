input_filename = 'country_info.txt'

countries = {}
code_lookup = {}
no_capital = []
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        # countries[code.casefold()] = country_dict


print(countries)
# print(code_lookup)

# while True:
#     chosen_country = input('Please enter the name of a country: ').casefold()
#     if chosen_country in countries:
#         country_data = countries[chosen_country]
#         print(f"The capital of {country_data['name']} is {country_data['capital']}")
#     elif chosen_country == 'quit':
#         break
#     elif chosen_country not in countries:
#         print(f"There is no country in data set as {chosen_country}")

for key, value in countries.items():
    if value['capital'] == '':
        no_capital.append(value['name'])
print(no_capital)




