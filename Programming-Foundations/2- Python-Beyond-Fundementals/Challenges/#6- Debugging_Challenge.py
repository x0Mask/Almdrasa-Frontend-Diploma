def plant_recommendation(care_level):
    if care_level == 'low':
        return 'Sabar'
    elif care_level == 'medium':
        return 'Liblab'
    elif care_level == 'high':
        return 'Orcade'

print(plant_recommendation('low'))
print(plant_recommendation('medium'))
print(plant_recommendation('high'))