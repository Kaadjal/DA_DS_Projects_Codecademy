# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 2. Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity,\
# the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, \
# you want to look at data about the most powerful hurricanes that have occurred.
# Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region.\
# For some of the hurricanes, damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (1000000000) and M stands for millions (1000000).
# Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
# Test your function with the data stored in damages.

# Write your update damages function here:
def damage_conversion(n):
  conversion = {"M": 1000000, "B": 1000000000}
  damage = []
  for item in n:
    if item == 'Damages not recorded':
      damage.append('Damages not recorded')
    elif item[-1] == 'M':
      num = float(item[:-1])
      value = num*conversion["M"]
      damage.append(value)
    elif item[-1] == 'B':
      num = float(item[:-1])
      value = num*conversion["B"]     
      damage.append(value)
  return damage

new_damages = damage_conversion(damages)
#print(new_damages)

# 3. Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data includes:
#    names: names of the hurricanes
#    months: months in which the hurricanes occurred
#    years: years in which the hurricanes occurred
#    max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
#    areas_affected: list of different areas affected by each of the hurricanes
#    deaths: total number of deaths caused by each of the hurricanes
# The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane. For example, names[0] yields the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).
# Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
# Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}.
# Test your function on the lists of data provided.
# Write your construct hurricane dictionary function here:
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths):
  dict = {}
  ranges = range(len(names))
  for i in ranges:
    dict[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage" : new_damages[i], "Death": deaths[i]}
  return dict

hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
#print(hurricanes)

# 4. In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
# Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
# For example, the key 1932 would yield the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], \
# 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', \
# 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}].
# Test your function on your hurricane dictionary.
# write your construct hurricane by year dictionary function here:
def year_cane(d):
  dict = {}
  val = d.items()
  year_key = []
  for k,v in val:
    if v['Year'] not in year_key:
      year_key.append(v['Year'])
      dict[v['Year']] = [v]
    elif v['Year'] in year_key:
      dict[v['Year']].append(v)
  return dict

hur_year = year_cane(hurricanes)
#print(hur_year[1932])

# 5. You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.
# Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are \
# counts of how many times the areas were affected.
# Test your function on your hurricane dictionary.
# write your count affected areas function here:
def damage_count(d):
  val = d.items()
  count = []
  areas = []
  affected = []
  for k, v in val:
    area = v["Areas Affected"]
    #print(area)
    if len(area) > 1:
      for i in range(len(area)):
        a = area[i]
        areas.append(a)
      #print(areas)
    elif len(area) == 1:
      areas.append(area[0])
    #print(areas)
  for item in areas:
    num = areas.count(item)
    count.append(num)
    if item not in affected:
      affected.append(item)
  area_count = {k:v for k, v in zip(affected, count)}
  return area_count

area_count = damage_count(hurricanes) 
#print(area_count)

# 6. You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.
# Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are 
# \counts of how many times the areas were affected.
# Test your function on your hurricane dictionary.
# write your find most affected area function here:
def max_count(d):
  area_max = ''
  count_max = 0
  for area in d:  
    hits = d[area]
    if hits > count_max:
      count_max = hits
      area_max = area
  print("{} is the most affect area, with {} hits".format(area_max, count_max))
  ##the code above counts for only 1 area, for multiple areas:  
  areas = d.items()
  #print(areas)
  most_hit = []
  for k,v in areas:
    if v == count_max:
      most_hit.append(k)
  print("{} are the most affected areas with {} hits".format(most_hit, count_max))

print(max_count(area_count))

# 7. Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
# Test your function on your hurricane dictionary.
# write your greatest number of deaths function here:
def most_deadly(d):
  dead_max = 0
  dead_hur = ''
  hurrs = hurricanes.items()
  for key, val in hurrs:
    dead = val['Death']
    if dead > dead_max:
      dead_max = dead
      dead_hur = key
  print("Hurricane {} is the deadliest with {} deaths.".format(dead_hur, dead_max))

deadliest = most_deadly(hurricanes)
#print(deadliest)

# 8. Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.
# Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.
# mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
# For example, a hurricane with a 1 mortality rating would have resulted in greater than 0 but less than or equal to 100 deaths. A hurricane with a 5 mortality rating\
# would have resulted in greater than 10000 deaths.
# Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
# Test your function on your hurricane dictionary.
# Write your catgeorize by mortality function here:
def mortality(d):
  #mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  mortality_scale = {}
  zero = []
  one = []
  two = []
  three = []
  four = []
  five = []
  val = d.items()
  #print(val)
  for k, v in val:
    dead = v["Death"]
    name = k
    if dead == 0:
      zero.append(name)
      mortality_scale[0] = zero
    elif dead <= 100:
      one.append(name)
      mortality_scale[1] = one
    elif dead <= 500:
      two.append(name)
      mortality_scale[2] = two
    elif dead <= 1000:
      three.append(name)
      mortality_scale[3] = three
    elif dead <= 10000:
      four.append(name)
      mortality_scale[4] = four
    else:
      five.append(name)
      mortality_scale[5] = five
  return mortality_scale

mort = mortality(hurricanes)
print(mort)


# 9. Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
# Test your function on your hurricane dictionary.
# write your greatest damage function here:
def great_damage(d):
  max_dam = 0
  dam_hur = ''
  hurrs = hurricanes.items()
  for key, val in hurrs:
    damage = val['Damage']
    if type(damage) == float:
      if damage > max_dam:
        max_dam = damage
        dam_hur = key
    elif damage == 'Damage not recorded':
      continue
  print("Hurricane {} is the one with the most damage, costs: ${}.".format(dam_hur, max_dam))

costly = great_damage(hurricanes)
#print(costly)


#10. Lastly, you want to rate hurricanes according to how much damage they cause.
# Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
# damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
# For example, a hurricane with a 1 damage rating would have resulted in damages greater than 0 USD but less than or equal to 100000000 USD. A hurricane with a 5 damage rating\
#  would have resulted in damages greater than 50000000000 USD (talk about a lot of money).
# Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
# Test your function on your hurricane dictionary.
# Write your catgeorize by damage function here:
def damage_cost(d):
  #damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  damage_scale = {}
  zero = []
  one = []
  two = []
  three = []
  four = []
  five = []
  val = d.items()
  for k, v in val:
    damage = v["Damage"]
    name = k
    if type(damage) == float:
      if damage == 0.0:
        zero.append(name)
        damage_scale[0] = zero
      elif damage <= 100000000.0:
        one.append(name)
        damage_scale[1] = one
      elif damage <= 1000000000.0:
        two.append(name)
        damage_scale[2] = two
      elif damage <= 10000000000.0:
        three.append(name)
        damage_scale[3] = three
      elif damage <= 50000000000.0:
        four.append(name)
        damage_scale[4] = four
      else:
        five.append(name)
        damage_scale[5] = five
    elif damage == 'Damage not recorded':
      continue    
  return damage_scale

high_cost = damage_cost(hurricanes)
print(high_cost)
