class Country:

    def __init__(
                self, position_in_file, country_name,
                happines, continent
                ):

        self.position_in_file = position_in_file
        self.country_name = country_name
        self.happines = happines
        self.continent = continent


def find_happiest(filename):
    countries = list()
    happines_by_continent = dict()
    the_happiest_country_by_continent = dict()

    with open(filename, "r") as data_countries:
        for line in data_countries:
            country_data = line.split(",")
            countries.append(
                Country(
                    country_data[0],
                    country_data[1],
                    country_data[2],
                    country_data[3].rstrip()
                )
            )

        for country in countries:
            if country.continent in happines_by_continent:
                if(happines_by_continent[country.continent] <
                        country.happines):
                    happines_by_continent[country.continent] = \
                        country.happines
                    the_happiest_country_by_continent[country.continent] = \
                        country.country_name
            else:
                happines_by_continent[country.continent] = \
                    country.happines
                the_happiest_country_by_continent[country.continent] = \
                    country.country_name

    return the_happiest_country_by_continent

# find_happiest("C:/Users/MacPavel/Desktop/pythonLabs/lab10/happiness_2018.txt")
