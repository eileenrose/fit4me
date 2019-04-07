'''Dictionary of maximum number of nutrients per day {nutrient:{age range: grams or calories of nutrient}} --- nutrients with no upper limit are stored as v. large #'s'''

ul = {
    "Biotin":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Calcium":{(0, 0.5):1000, (0.5, 1):1500, (1, 3):2500, (4, 8):2500, (9, 13):3000, (14, 18):3000, (19, 150):2500},
    "Choline":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000, (4, 8):1500, (9, 13):2000, (14, 18):3000, (19, 150):3500},
    "Copper":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000, (4, 8):3000, (9, 13):5000, (14, 18):8000, (19, 150):10000},
    "Fluoride":{(0, 0.5):0.7, (0.5, 1):0.9, (1, 3):1.3, (4, 8):2.2, (9, 13):10, (14, 18):10, (19, 150):10},
    "Folate":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):300, (4, 8):400, (9, 13):600, (14, 18):800, (19, 150):1000},
    "Iodine":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):200, (4, 8):300, (9, 13):500, (14, 18):900, (19, 150):1100},
    "Iron":{(0, 0.5):40, (0.5, 1):40, (1, 3):40, (4, 8):40, (9, 13):40, (14, 18):45, (19, 150):45},
    "Magnesium":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):65, (4, 8):110, (9, 13):350, (14, 18):350, (19, 150):350},
    "Manganese":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):2, (4, 8):3, (9, 13):6, (14, 18):9, (19, 150):11},
    "Niacin":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):10, (4, 8):15, (9, 13):20, (14, 18):30, (19, 150):35},
    "Pantothenic acid":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Phosphorus":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):3000, (4, 8):3000, (9, 13):4000, (14, 18):4000, (19, 150):4000},
    "Potassium":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Riboflavin":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Selenium":{(0, 0.5):45, (0.5, 1):60, (1, 3):90, (4, 8):150, (9, 13):280, (14, 18):400, (19, 150):400},
    "Thiamin":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Vitamin A":{(0, 0.5):600, (0.5, 1):600, (1, 3):600, (4, 8):900, (9, 13):1700, (14, 18):2800, (19, 150):3000},
    "Vitamin B-12":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Vitamin B-6":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):30, (4, 8):40, (9, 13):60, (14, 18):80, (19, 150):100},
    "Vitamin C":{(0, 0.5):50, (0.5, 1):15, (1, 3):25, (4, 8):45, (9, 13):70, (14, 18):82, (19, 150):2000},
    "Vitamin D (IU)":{(0, 0.5):1000, (0.5, 1):1520, (1, 3):2520, (4, 8):3000, (9, 13):4000, (14, 18):4000, (19, 150):4000},
    "Vitamin E":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):200, (4, 8):300, (9, 13):600, (14, 18):800, (19, 150):1000},
    "Vitamin K (phylloquin)":{(0, 0.5):1000000, (0.5, 1):1000000, (1, 3):1000000, (4, 8):1000000, (9, 13):1000000, (14, 18):1000000, (19, 150):1000000},
    "Zinc":{(0, 0.5):4, (0.5, 1):5, (1, 3):7, (4, 8):12, (9, 13):23, (14, 18):34, (19, 150):40},
    "Protein":{(0, 0.5):40, (0.5, 1):40, (1, 3):40, (4, 8):45, (9, 13):50, (14, 18):56, (19, 150):56},
    "Total lipid(fat)":{(0, 0.5):80, (0.5, 1):80, (1, 3):80, (4, 8):78, (9, 13):78, (14, 18):78, (19, 150):70},
    "Fiber":{(0, 0.5):15, (0.5, 1):15, (1, 3):15, (4, 8):18, (9, 13):18, (14, 18):18, (19, 150):25},
    "Water":{(0, 0.5):1000, (0.5, 1):2000, (1, 3):2000, (4, 8):2500, (9, 13):2500, (14, 18):2500, (19, 150):2500},
    "Carbohydrate":{(0, 0.5):400, (0.5, 1):400, (1, 3):400, (4, 8):350, (9, 13):350, (14, 18):350, (19, 150):300},
    "Calories":{(0, 0.5):1000, (0.5, 1):1400, (1, 3):1500, (4, 8):1700, (9, 13):2000, (14, 18):2000, (19, 150):2000}
}
