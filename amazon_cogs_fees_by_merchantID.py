import csv
import numbers
# Import pandas library
import pandas as pd



# Get Input 
num1 = input ("Enter Unified Transaction CSV File Name :")
num2 = input ("Enter sku COG CSV File Name :")
num3 = input ("Enter order date report CSV File Name :")
#num4 = input ("Name your own Output File CSV File Name :")

print("Info:  Starting")

print(num1)
print(num2)
print(num3)

# If not taking user input, 
#UnifiedTransaction_Raw = pd.read_csv('unifiedtransaction.csv')
#sku_cost =  pd.read_csv('sku_cost.csv')
#orderdatereport = pd.read_csv('orderdatereport.csv')

UnifiedTransaction_Raw = pd.read_csv(num1)
#Make sure the cost is a number, and does not have a $ format
sku_cost =  pd.read_csv(num2)
orderdatereport = pd.read_csv(num3)

#Cut the first 8 rows.
UnifiedTransaction = UnifiedTransaction_Raw.iloc[8:]


print(sku_cost.columns)


sku_cost_dictionary = dict (zip(sku_cost['sku'], sku_cost['cost']))

UnifiedTransaction['COG'] = UnifiedTransaction['sku'].map(sku_cost_dictionary)



# take the sku, and add a numeric column for the sku 
UnifiedTransactionAltered = UnifiedTransaction.groupby(['order id']).agg({'date/time': 'first', 'quantity': 'sum', 'COG': 'sum', 'selling fees': 'sum', 'fba fees': 'sum', 'marketplace': 'first'})
print(UnifiedTransactionAltered)
print(UnifiedTransactionAltered.columns)


UnifiedTransactionAltered.to_csv('helper.csv')

amazon_cogs_fees_by_merchantID = pd.read_csv('helper.csv')


#Take the orderID and change it to regular shopify/kk order ID 
df_new = orderdatereport[['amazon-order-id', 'merchant-order-id']]

dictionary = dict (zip(orderdatereport['amazon-order-id'], orderdatereport['merchant-order-id']))
#print(dictionary)



#Dictionary
amazon_cogs_fees_by_merchantID['MerchantID'] = amazon_cogs_fees_by_merchantID['order id'].map(dictionary)

amazon_cogs_fees_by_merchantID.to_csv('amazon_cogs_fees_by_merchantID.csv')

print("Example Data here")

print(amazon_cogs_fees_by_merchantID)
print("Info: completed please look at amazon_cogs_fees_by_merchantID.csv file")
