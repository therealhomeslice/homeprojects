#!/usr/bin/python

# Taxes script w/o deductions 

def calculateSingle(s):
  tax_bracket = [0, 9276, 37651, 91151, 190151, 413351, 415051]
  tax_rate = [.1, .15, .25, .28, .33, .35, .396]
  bracket = 0
  remainder = 0
  taxes = 0
  if s >= 415051:
    return (s-415051)*.396+120528.5 #hardcoded taxes
  for x in range(len(tax_bracket)-1):
    if s > tax_bracket[x] and s < tax_bracket[x+1]:
      bracket = x
      remainder = s - tax_bracket[x] 
      taxes += remainder*tax_rate[x]
  for x in range(0, bracket+1):
    if x > 1:
      taxes += (tax_bracket[x] - tax_bracket[x-1])*tax_rate[x-1]
    else:
      taxes += tax_bracket[x] * tax_rate[x-1]
  return taxes

def calculateNJState(s):
  tax_bracket = [0, 20001, 35001, 40001, 75001, 500001]
  tax_rate = [.014, .0175, .035, .05525, .0637, .0897]

  bracket = 0
  remainder = 0
  taxes = 0
  if s >= 415051:
    return (s-415051)*.396+120528.5 #hardcoded taxes
  for x in range(len(tax_bracket)-1):
    if s > tax_bracket[x] and s < tax_bracket[x+1]:
      bracket = x
      remainder = s - tax_bracket[x] 
      taxes += remainder*tax_rate[x]
  for x in range(0, bracket+1):
    if x > 1:
      taxes += (tax_bracket[x] - tax_bracket[x-1])*tax_rate[x-1]
    else:
      taxes += tax_bracket[x] * tax_rate[x-1]
  return taxes

def socialSecurityTax(s):
  return s*.062

def medicareTax(s):
  return s*.0145

#if __name__ == '__main__':
  
