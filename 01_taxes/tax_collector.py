#!/usr/bin/python
import sys
import argparse
# Taxes script w/ deductions 

def calculateFederal(s, status):
  tax_rate = [.1, .15, .25, .28, .33, .35, .396]
  if status == True: #single
    tax_bracket = [0, 9276, 37651, 91151, 190151, 413351, 415051]
    capital = 121505.25 
  else: #joint
    tax_bracket = [0, 18651, 75901, 153101, 233351, 416701, 470701]
    capital = 131628

  return calculateTax(s, tax_bracket, tax_rate, capital)

def calculateState(s, state, status):
  #right now this is limited to NJ single, in the future i'd like to pass two additional variables of State(XX) & Filing Status(S/J) probably will make this into a switch case statement

  #NJ Taxes#
  tax_bracket = [0, 20001, 35001, 40001, 75001, 500001]
  tax_rate = [.014, .0175, .035, .05525, .0637, .0897]
  capital = 12052 #need to update this value
  #married
  tax_bracket = [0, 20000, 50000, 70000, 80000, 150000, 500000]
  tax_rate = [.014, .0175, .0245, .035, .0553, .0637, .0897]
  capital = 12000 

  #including maryland
  #tax_bracket = [0, 2000, 3000, 100000, 125000, 150000, 250000]
  #tax_rate = [.02, .04, .0475, .05, .0525, .055, .0575]
  #capital = 12760

  #Income tax free states are AK, FL, NV, SD, TX, NH, TN (seven)
  #tax_bracket = [0]
  #tax_rate = [0]
  #capital = 0
  
  return calculateTax(s, tax_bracket, tax_rate, capital)

def calculateTax(s, tax_bracket, tax_rate, capital):
  bracket = 0
  remainder = 0
  taxes = 0
  if s >= tax_bracket[-1]:
    return (s-tax_bracket[-1])*tax_rate[-1]+capital #hardcoded taxes
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

def standardDeduction(s):
  if int(s) > 6350:
    return int(s)
  else: 
    return int(6350)

def personalExemptions(s):
  return s*4050
 
def compileTax(s,b,status,p_Ex):
  print "Annual Salary: " + str(s)
  a = s
  s -= standardDeduction(b)+personalExemptions(p_Ex)
  print "Deductions: " + str(standardDeduction(b))
  print "Personal Exemption: " + str(personalExemptions(p_Ex))
  print "Federal Tax: " + str(calculateFederal(s, status))
  print "State Tax: " + str(calculateState(s, "NJ", status))
  print "Social Security Tax: " + str(socialSecurityTax(s))
  print "Medicare Tax: " + str(medicareTax(s))
  total = calculateFederal(s, status) + calculateState(s, "NJ", status) + socialSecurityTax(s) + medicareTax(s)
  print "Total Taxes: " + str(total)
  print "Post Tax: " + str(a-total)
  return total

if __name__ == '__main__':
#  test_cases = [1000, 9000, 10000, 50000, 100000, 400000, 500000]
#  for x in range(len(test_cases)):
#    print "Test Case " + str(test_cases[x]) + ": " + str(calculateSingle(test_cases[x]))
  #print calculateSingle(int(sys.argv[1]))
  if len(sys.argv) <= 2:
    deduction = 0
  else:
    deduction = sys.argv[2]
  status = True #married
  compileTax(int(sys.argv[1]),deduction, status, 1)
  
