#!/usr/bin/python
import sys
import tax_collector
# Taxes script w/ standard deductions 

if __name__ == '__main__':

#  test_cases = [1000, 9000, 10000, 50000, 100000, 400000, 500000]
#  for x in range(len(test_cases)):
#    print "Test Case " + str(test_cases[x]) + ": " + str(calculateSingle(test_cases[x]))
  #print calculateSingle(int(sys.argv[1]))
  
  #basic = 4741*9 + 5389*3
  basic  = 5398.20*12
  #bah = 2166*12
  bah = 2352*12
  bas = 253.63*12
  bonus = 0 
  deductions = 0 #(573*4)+(51+50+72.29+116.85+47.91+573)*8 + (1070*7)+3400 + 4000
  rental_property = 0#1330*8
  roth = .30
  
  taxable = rental_property + basic + bonus - tax_collector.standardDeduction(deductions) - tax_collector.personalExemptions(1)
  print "#####ANNUAL#####"
  print "Deductions: " + str(tax_collector.standardDeduction(deductions))
  print "Pay before taxes: " + str(basic+bah+bas+bonus)
  print "Taxable Income: " + str(taxable)
  print "Federal Taxes: " + str(tax_collector.calculateFederal(taxable, True))
  print "Social Security Tax: " + str(tax_collector.socialSecurityTax(taxable))
  print "Medicare Tax: " + str(tax_collector.medicareTax(taxable))
  #print "Health Insurance Benefit: " + str(47.82*12) #based of tricare reserve select
  
  p_tax_pay = basic + bah + bas + bonus - tax_collector.calculateFederal(taxable, True) - tax_collector.socialSecurityTax(taxable) - tax_collector.medicareTax(taxable)
  
#calculating monthly
  print "Pay after taxes: " + str(p_tax_pay)
  print "Roth Contribution: " + str(basic*roth)
  print "\n\n#####MONTHLY#####"
  print "Pay before taxes: " + str((basic+bah+bas+bonus)/12)
  print "Taxable Income: " + str(taxable/12)
  print "Federal Taxes: " + str(tax_collector.calculateFederal(taxable, True)/12)
  print "Social Security Tax: " + str(tax_collector.socialSecurityTax(taxable)/12)
  print "Medicare Tax: " + str(tax_collector.medicareTax(taxable)/12)
  #print "Health Insurance Benefit: " + str(47.82*12) #based of tricare reserve select
  print "Pay after taxes: " + str(p_tax_pay/12)
  print "Roth Contribution: " + str(basic*roth/12)
  print "Take home: " + str((p_tax_pay - (basic*roth))/12)
  
  print "\n\n#####BI-MONTHLY#####"
  print "Take home: " + str((p_tax_pay - (basic*.20))/12/2)
  feels_like = taxable

  while p_tax_pay > (feels_like - tax_collector.calculateFederal(feels_like,True) - tax_collector.calculateState(feels_like, "NJ", True) - tax_collector.socialSecurityTax(feels_like) - tax_collector.medicareTax(feels_like)):
    feels_like += 10
  print "\n\n#####CIVILIAN#####"
  print "Feels Like a Civilian: " + str(feels_like)
  print "Federal Taxes: " + str(tax_collector.calculateFederal(feels_like, True))
  print "State Taxes: " + str(tax_collector.calculateState(feels_like, "NJ", True))
  print "Social Security Tax: " + str(tax_collector.socialSecurityTax(feels_like))
  print "Medicare Tax: " + str(tax_collector.medicareTax(feels_like))
  print "Pay after taxes: " + str(feels_like - tax_collector.calculateFederal(feels_like, True) - tax_collector.calculateState(feels_like, "NJ", True) - tax_collector.socialSecurityTax(feels_like) - tax_collector.medicareTax(feels_like))
