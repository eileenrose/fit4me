'''Dictionary of minimum number of nutrients per day {nutrient:{age range: grams or calories of nutrient}}'''

dv = {
    "Biotin":{(0, 0.5):6, (0.5, 1):6, (1, 3):8, (4, 8):30, (9, 13):30, (14, 18):30, (19, 150):30},
    "Calcium":{(0, 0.5):260, (0.5, 1):260, (1, 3):700, (4, 8):1300, (9, 13):1300, (14, 18):1300, (19, 150):1300},
    "Choline":{(0, 0.5):150, (0.5, 1):150, (1, 3):200, (4, 8):550, (9, 13):550, (14, 18):550, (19, 150):550},
    "Copper":{(0, 0.5):200, (0.5, 1):220, (1, 3):300, (4, 8):900, (9, 13):900, (14, 18):900, (19, 150):900},
    "Fluoride":{(0, 0.5):0, (0.5, 1):0, (1, 3):0, (4, 8):0, (9, 13):0, (14, 18):0, (19, 150):0},
    "Folate":{(0, 0.5):80, (0.5, 1):80, (1, 3):150, (4, 8):400, (9, 13):400, (14, 18):400, (19, 150):400},
    "Iodine":{(0, 0.5):130, (0.5, 1):130, (1, 3):90, (4, 8):150, (9, 13):150, (14, 18):150, (19, 150):150},
    "Iron":{(0, 0.5):11, (0.5, 1):11, (1, 3):7, (4, 8):18, (9, 13):18, (14, 18):18, (19, 150):18},
    "Magnesium":{(0, 0.5):75, (0.5, 1):75, (1, 3):80, (4, 8):420, (9, 13):420, (14, 18):420, (19, 150):420},
    "Manganese":{(0, 0.5):0.6, (0.5, 1):0.6, (1, 3):1.2, (4, 8):2.3, (9, 13):2.3, (14, 18):2.3, (19, 150):2.3},
    "Niacin":{(0, 0.5):4, (0.5, 1):4, (1, 3):6, (4, 8):16, (9, 13):16, (14, 18):16, (19, 150):16},
    "Pantothenic acid":{(0, 0.5):1.8, (0.5, 1):1.8, (1, 3):2, (4, 8):5, (9, 13):5, (14, 18):5, (19, 150):5},
    "Phosphorus":{(0, 0.5):3, (0.5, 1):275, (1, 3):460, (4, 8):1250, (9, 13):1250, (14, 18):1250, (19, 150):1250},
    "Potassium":{(0, 0.5):700, (0.5, 1):700, (1, 3):3000, (4, 8):4700, (9, 13):4700, (14, 18):4700, (19, 150):4700},
    "Riboflavin":{(0, 0.5):0.4, (0.5, 1):0.4, (1, 3):1.3, (4, 8):1.3, (9, 13):1.3, (14, 18):1.3, (19, 150):1.3},
    "Selenium":{(0, 0.5):20, (0.5, 1):20, (1, 3):20, (4, 8):55, (9, 13):55, (14, 18):55, (19, 150):55},
    "Thiamin":{(0, 0.5):0.3, (0.5, 1):0.3, (1, 3):0.5, (4, 8):1.2, (9, 13):1.2, (14, 18):1.2, (19, 150):1.2},
    "Vitamin A":{(0, 0.5):500, (0.5, 1):500, (1, 3):300, (4, 8):900, (9, 13):900, (14, 18):900, (19, 150):900},
    "Vitamin B-12":{(0, 0.5):0.5, (0.5, 1):0.5, (1, 3):0.9, (4, 8):2.4, (9, 13):2.4, (14, 18):2.4, (19, 150):2.4},
    "Vitamin B-6":{(0, 0.5):0.3, (0.5, 1):0.3, (1, 3):0.5, (4, 8):1.7, (9, 13):1.7, (14, 18):1.7, (19, 150):1.7},
    "Vitamin C":{(0, 0.5):0, (0.5, 1):0, (1, 3):400, (4, 8):650, (9, 13):1200, (14, 18):1800, (19, 150):2000},
    "Vitamin D (IU)":{(0, 0.5):400, (0.5, 1):400, (1, 3):15, (4, 8):20, (9, 13):20, (14, 18):20, (19, 150):20},
    "Vitamin E":{(0, 0.5):5, (0.5, 1):5, (1, 3):6, (4, 8):15, (9, 13):15, (14, 18):15, (19, 150):15},
    "Vitamin K (phylloquin)":{(0, 0.5):2.5, (0.5, 1):2.5, (1, 3):30, (4, 8):120, (9, 13):120, (14, 18):120, (19, 150):120},
    "Zinc":{(0, 0.5):3, (0.5, 1):3, (1, 3):3, (4, 8):11, (9, 13):11, (14, 18):11, (19, 150):11},
    "Protein":{(0, 0.5):10, (0.5, 1):14, (1, 3):14, (4, 8):20, (9, 13):33, (14, 18):55, (19, 150):70},
    "Total lipid(fat)":{(0, 0.5):31, (0.5, 1):30, (1, 3):40, (4, 8):55, (9, 13):70, (14, 18):100, (19, 150):130},
    "Fiber":{(0, 0.5):0, (0.5, 1):0, (1, 3):14, (4, 8):18, (9, 13):22, (14, 18):25, (19, 150):28},
    "Water":{(0, 0.5):800, (0.5, 1):800, (1, 3):1000, (4, 8):1500, (9, 13):1500, (14, 18):1500, (19, 150):1500},
    "Carbohydrate":{(0, 0.5):200, (0.5, 1):200, (1, 3):400, (4, 8):350, (9, 13):350, (14, 18):350, (19, 150):300},
    "Calories":{(0, 0.5):1000, (0.5, 1):1200, (1, 3):1200, (4, 8):1500, (9, 13):1800, (14, 18):1700, (19, 150):1500}
}
