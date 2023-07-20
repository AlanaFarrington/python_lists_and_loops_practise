# Carly's Clippers
# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. 
#Your job is to go through the lists of data that have been collected in the past couple of weeks. 
#You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

#hairstyles provided
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#prices matching each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#number of times each hairstyle was completed last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
total_price = 0
for value in prices:
  total_price += value

#That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
average_price = total_price / len(prices)
print("""Average Haircut Price: 
£""" + str(average_price))
new_prices = [value - 5 for value in prices]
#print(new_prices)

#Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. 
#She first wants to know how much revenue was brought in last week and what her average daily revenue is.
total_revenue = 0
for i in range (len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: £" + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: £" + str(average_daily_revenue))

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts Under £30 are:")
for cut in cuts_under_30:
  print(cut)