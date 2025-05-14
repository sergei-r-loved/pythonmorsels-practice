

# def get_earliest(first_date: str, second_date: str):
#     first_date_month, first_date_day, first_date_year = first_date.split("/")
#     second_date_month, second_date_day, second_date_year = second_date.split("/")
#     if first_date_year < second_date_year:
#         return first_date
#     elif first_date_year == second_date_year:
#         if first_date_month < second_date_month:
#             return first_date
#         elif first_date_month == second_date_month:
#             if first_date_day < second_date_day:
#                 return first_date
#             else:
#                 return second_date
#         else:
#             return second_date
#     return second_date


def get_earliest(*args: str):
    split_dates = []
    for date in args:
        split_dates.append(date.split("/"))
    current_year = split_dates[-1][2]
    current_month = split_dates[-1][0]
    current_day = split_dates[-1][1]
    for date in split_dates:
        # print(date)
        # print(f"current date {"/".join([current_month, current_day, current_year])}")
        if date[2] == current_year:
            if date[0] == current_month:
                if date[1] == current_day:
                    return "/".join([current_month, current_day, current_year])
                elif date[1] < current_day:
                    current_month = date[0]
                    current_day = date[1]
                    current_year = date[2]
                    continue
            elif date[0] < current_month:
                # print(f"current date {date}")
                # print("/".join([current_month, current_day, current_year]))
                current_month = date[0]
                current_day = date[1]
                current_year = date[2]
                # print("/".join([current_month, current_day, current_year]))
                continue
        elif date[2] < current_year:
            current_month = date[0]
            current_day = date[1]
            current_year = date[2]
            continue

    return "/".join([current_month, current_day, current_year])

        
    
        
        


newer = "27/01/1756"
older = "01/27/1756"
one_more = "02/24/2004"
# print(get_earliest(older, newer))
# print(get_earliest("01/24/1946", "01/29/1946", "03/29/1945"))
print(get_earliest(newer, older, one_more))
