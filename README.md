# amazon_cogs_fees_by_merchantID

### 

### **Summary**

This is a step by step process to gather amazon reports, then run a python script to understand the COG, FBA fees, seller fees, of amazon FBM & FBA sales.  This will also map the amazon order ID to the merchant ID.

### Dependencies:

1. Python &  Python pandas library
[https://www.python.org/downloads/](https://www.python.org/downloads/)
[https://pandas.pydata.org/docs/getting_started/install.html](https://pandas.pydata.org/docs/getting_started/install.html)
2. Amazon Seller Access to pull the reports.

Note* The recommended file names are no longer needed.  The script will ask you for the input as seen below.

```bash
python amazon_cogs_fees_by_merchantID.py
Enter Unified Transaction CSV File Name :2022Jan1-2022Oct31CustomUnifiedTransaction.csv
Enter sku COG CSV File Name :sku_cost.csv
Enter order date report CSV File Name :orderdatereport.csv
Info:  Starting
2022Jan1-2022Oct31CustomUnifiedTransaction.csv
sku_cost.csv
orderdatereport.csv
```

### **Step 1. Get Amazon Fulfillment Report**

[https://sellercentral.amazon.com/reportcentral/FlatFileAllOrdersReport/1](https://sellercentral.amazon.com/reportcentral/FlatFileAllOrdersReport/1)

Pull the date range. you’re looking for, then download the report.

Name the Amazon Fulfillment Reports **orderdatereport.csv**.  Make sure it is saved with utf-8 encoding. 


Notes*  In the report it has one sku per line, if an order has multiple products, it will have the order number duplicated, on two separate lines, see image.
**Sales Channel,** This is going to show both Non-Amazon and Amazon, and you need to filter it in order to get the Shopify & Konnective orders, vs the normal orders.
You can see on **merchant-order-id** column the IDs that are from konnective & shopify.


### Step 2. Go to the Date Range Reports of Payment Reports

https://sellercentral.amazon.com/payments/reports/custom/request?ref_=xx_report_ttab_trans&tbla_daterangereportstable=sort:{"sortOrder"%3A"DESCENDING"};search:undefined;pagination:1;

Make sure it is a Transaction Report type, NOT summary type, select the Date range, hit Update, and Download the report.

Name the Amazon Date Range Report **unifiedtransaction.csv.**  Make sure it is saved with utf-8 encoding. 


Notes* One sku per line, if an order has multiple products, it will have the order number duplicated, on two separate lines, with the same order ID See picture.


### Step 3. Create the sku_cost.csv

In order for this automation to run, you need a csv with the sku’s and costs mapped.
You can find the sku mapped to the cost here on the “Amazon Skus” tab.

Save this to a separate csv as **sku_cost.csv.**
The headers should be sku & cost.  Do not include multiple COGs.  If you need too, run this twice, it can only handle one cost column.
An example file is below, but this should be done using COGs google sheet, incase of change in COG pricing.


### Step 4: Save amazon_cogs_fees_by_merchantID.py to your desktop/VM/workstation


### Step 5. Save all files in the same directory

To run correctly, all files should be saved in the same directory.

### Step 6 Final Step. Run your python script to get amazon_cogs_fees_by_merchantID.csv ouput.

```bash
python amazon_cogs_fees_by_merchantID.py
```

If your running windows open a command line window.  You may need to download python & panda library.  Same with if you are on linux.
This will create the amazon_cogs_fees_by_merchantID.csv file.  
This file will contain the following headings…

```bash

 order id, quantity, COG, selling fees, fba fees, marketplace, MerchantID

```

You now have your completed report as amazon_cogs_fees_by_merchantID.csv.
