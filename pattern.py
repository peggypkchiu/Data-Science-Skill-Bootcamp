"""
output the star pattern shown below:
*
**
***
****
*****
****
***
**
*
Starting from 1* in the first row, increase by 1* in the next row until 5*,
then decrease by 1* in the next row until remain 1* in the last row.
"""
for i in range (1,10):
    if i >= 5:
        print("*"*(10-i))
    else:
        print("*"*i)
