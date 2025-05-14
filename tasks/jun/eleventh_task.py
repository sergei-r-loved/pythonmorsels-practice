# Below 60 is F
# From 60 to below 70 is D
# From 70 to below 80 is C
# From 80 to below 90 is B
# 90 and above is A



def percent_to_grade(percent):
    if percent < 60.0:
        return "F"
    elif percent >= 60.0 and percent < 70.0:
        return "D"
    elif percent >= 70.0 and percent < 80.0:
        return "C"
    elif percent >= 80.0 and percent < 90.0:
        return "B"
    elif percent >= 90.0:
        return "A"