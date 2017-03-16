# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
# def valid_month(month):
#     month = month.title()
#     for i in months:
#         if i == month:
#             return month
    
#     return None

# refactored
# def valid_month(month):
#     if month:
#         cap_month = month.capitalize()
#         if cap_month in months:
#             return cap_month

# refactored with dictionary to map first three letters of each month
# user only has to input first three letters correctly
# list comprehensions used to create the dictionary of month abbreviations. 
# If we were to translate this code: month_abbvs = dict((m[:3].lower(),m) for m in months) 
# it would be: month_abbvs = {} for m in months: month_abbvs[m[:3].lower()] = m
month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)


print valid_month("january") 
# => "January"    
print valid_month("Janruary") 
# => "January"
print valid_month("feb")
# => February
print valid_month("octuber")
# => October
print valid_month("foo")
# => None
print valid_month("")
# => None
