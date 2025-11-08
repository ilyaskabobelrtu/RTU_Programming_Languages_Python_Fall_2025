"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [10, 100, 33, 30, 27, 24, 21]
city_population = {
    "Riga": 3410000,
    "Los Angeles": 4980000,
    "Atyrau": 2716000,
    "Seatle": 2328000,
    "Phoenix": 1690000
}

# TODO: Compute aggregates
temp_sum = sum(temperatures)
average_temperature = temp_sum / len(temperatures)
largest_population = 0
largest_city = ""
for city, pop in city_population.items():
    if pop > largest_population:
        largest_population = pop
        largest_city = city
total_population = 0
for pop in city_population.values():
    total_population += pop

# TODO: Print results
print("Average temperature:", round(average_temperature, 1))
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
