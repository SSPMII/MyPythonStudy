def city_format(city, country, population=0):
	"生成格式化的城市国家名字"
	city_country_population = city + ', ' + country + ' - population ' + str(population)
	return city_country_population.title()

print(city_format('shanghai', 'china', 2.4e7))