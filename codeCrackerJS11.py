#-------------------------------------------------------------------------------
# Name:        codeCracker
# Purpose:
#
# Author:      Jeff Nuss
#
# Created:     16/11/2011
# Copyright:   (c) Jeff Nuss 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

## Recursive funtion to reverse the algorithm
def codeCracker(n):
    i = 0.0
    charList = "abcdefghijklmnopqrstuvwxyz"
    while i < 27:
        i += 1
        if (n - i) == 0:
            password.append(charList[int(i - 1)])
            return 0
        test = (n - i) % 17
        if test == 0:
            newNumber = (n - i) / 17.0
            password.append(charList[int(i - 1)])
            if codeCracker(newNumber) == 0:
                return 0
    password.pop()

password = []
##codeCracker(53) ## cb
##codeCracker(907) ## cbf
##codeCracker(15421) ## cbfb
codeCracker(248410397744610)

password.reverse()
print (''.join(password))
