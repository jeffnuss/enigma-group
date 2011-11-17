#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jeff Nuss
#
# Created:     16/11/2011
# Copyright:   (c) Jeff Nuss 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def codeCracker(n):
    i = 0.0

    while i < 27:
        i += 1
        test = (n - i) % 17
        if (n - i) == 0:
            print("done")
            return 0;
        if test == 0:
            print(i)
            codeCracker((n - i) / 17.0)
    return -1




codeCracker(248410397744610)