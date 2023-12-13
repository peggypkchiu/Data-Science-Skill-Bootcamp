"""
Ask user to input time used for all three events of a triathlon, which are swimming, cycling and running
Calculate total sum of time taken to complete the triathlon
Print total time taken
If total time is equal or less than 100, award will be "Provincial Colours"
If total time is 101-105 minutes, award will be "Provincial Half Colours
If total time is 106-110 minutes, award will be "Provincial Scroll"
If total time is equal to or more than 111, no award will be granted
Print award granted
"""
swimming_time = int(input("Please enter time taken to complete swimming of triathlon (in minutes): \n"))
cycling_time = int(input("Please enter time taken to complete cycling of triathlon (in minutes): \n"))
running_time = int(input("Please enter time taken to complete running of triathlon (in minutes): \n"))
total_time = swimming_time + cycling_time + running_time
if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"
print(f"Thank you for your participation! {award} is received based on total time taken for all three events of triathlon.")
