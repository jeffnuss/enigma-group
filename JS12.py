#-------------------------------------------------------------------------------
# Name:        Enigma_Group_JS12_cracker
# Purpose:
#
# Author:      Jeff Nuss
#
# Created:     09/12/2011
# Copyright:   (c) Jeff Nuss 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Yeah, this is messy, but it gets the job done. I could've made it automatic
# but didn't care to take the time; it was quick enough to just do guess and
# check manually anyways

run1 = False

if run1:
    for year in range (158845, 158850):
        checkSum = 0
        passCheck = 318338237039211050000

        for x in range(1,year):
            checkSum += x
        checkResult = (passCheck - 1337) / (year ** 2)
        if (float(checkSum) == checkResult):
            print(year)

else:

    year = 158847
    passCheck = 1337
    checkSum = 0
    for x in range (1, year + 1):
        passCheck += year * x * year
    if passCheck < 318338237039211050000:
        print('increase')

##    year = 158848
##    checkSum = 0
##    passCheck = 318338237039211050000
##    for x in range(1,year):
##        checkSum += x
##    checkResult = (passCheck - 1337) / (year ** 2)
##    if (float(checkSum) > checkResult):
##        print ('reduce')
