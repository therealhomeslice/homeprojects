#!/usr/bin/python
import datetime
def currentSystem(tafcs, years_left):
  col = [10054, 10318.80, 10587.00, 11106] #caps at thsi rate over 26 
  ltcol = [8798.10, 9062.70] #caps at this rate after 22
  maj = 7648 #caps at this rate after 18

  rate = tafcs*.025
  inflation = pow(1.021, years_left)
  print "#####Legacy Retirement System#####"
  print "Major Retirement: " + str(rate*inflation*maj)
  
  if tafcs > 21 and tafcs < 24:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[1])
  elif tafcs >= 24 and tafcs < 26:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[2])
  elif tafcs >= 26:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[3])
  else:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[0])

def newSystem(tafcs, years_left):
  col = [10054, 10318.80, 10587.00, 11106] #caps at thsi rate over 26 
  ltcol = [8798.10, 9062.70] #caps at this rate after 22
  maj = 7648 #caps at this rate after 18

  rate = tafcs*.02
  inflation = pow(1.021, years_left)
  print "\n#####Blended Retirement System#####"
  print "Major Retirement: " + str(rate*inflation*maj)
  
  if tafcs > 21 and tafcs < 24:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[1])
  elif tafcs >= 24 and tafcs < 26:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[2])
  elif tafcs >= 26:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[3])
  else:
    print "Lt Col Retirement: " + str(rate*inflation*ltcol[1])
    print "Col Retirement: " + str(rate*inflation*col[0])

#def tspMatching():
  

if __name__ == "__main__":
  now = datetime.datetime.now()
  print now.year
  tafcsd = 2013
  proj_service = 20
  retire_date = tafcsd + proj_service
  years_left = retire_date - now.year

  print years_left
  print retire_date

  currentSystem(proj_service, years_left)
  newSystem(proj_service, years_left)
  print "\n"




