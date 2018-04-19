def fine(r_day, r_month, r_year, e_day, e_month, e_year):
    if r_year < e_year:
        return 0
    elif r_year > e_year:
        return 10000

    if r_month < e_month:
        return 0
    elif r_month > e_month:
        return 500 * (r_month - e_month)

    if r_day > e_day:
        return 15 * (r_day - e_day)
    else:
        return 0

r_day, r_month, r_year = map(int, input().split(" "))
e_day, e_month, e_year = map(int, input().split(" "))
print(fine(r_day, r_month, r_year, e_day, e_month, e_year))
