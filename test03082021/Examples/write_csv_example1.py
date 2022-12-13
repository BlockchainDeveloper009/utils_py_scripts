import csv, re

orig = b'settlement-id\tsettlement-start-date\tsettlement-end-date\tdeposit-date\ttotal-amount\tcurrency\ttransaction-type\torder-id\tmerchant-order-id\tadjustment-id\tshipment-id\tmarketplace-name\tamount-type\tamount-description\tamount\tfulfillment-id\tposted-date\tposted-date-time\torder-item-code\tmerchant-order-item-id\tmerchant-adjustment-item-id\tsku\tquantity-purchased\n7293436482\t03.05.2018 09:10:07 UTC\t04.05.2018 20:30:23 UTC\t06.05.2018 20:30:23 UTC\t53,44\tEUR\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n7293436482\t\t\t\t\t\tOrder\t303-3746292-6119509\t\t\tDRGC8lFbB\tAmazon.de\tItemPrice\tPrincipal\t179,99\tMFN\t03.05.2018\t03.05.2018 17:12:22 UTC\t30407746733299\t\t\t3700546702556-180412-chp-18c10347-1\t1\n7293436482\t\t\t\t\t\tOrder\t303-3746292-6119509\t\t\tDRGC8lFbB\tAmazon.de\tItemFees\tCommission\t-32,40\tMFN\t03.05.2018\t03.05.2018 17:12:22 UTC\t30407746733299\t\t\t3700546702556-180412-chp-18c10347-1\t1\n7293436482\t\t\t\t\t\tRefund\t305-1251749-5602732\t305-1251749-5602732\tamzn1:crow:YZkTuxs4RhO8FpZez3cGCg\t\tAmazon.de\tItemPrice\tPrincipal\t-109,99\tAFN\t04.05.2018\t04.05.2018 18:24:39 UTC\t38048998219979\t\t142721169810\t3700546702082-180124-jpn-131N28-6\t\n7293436482\t\t\t\t\t\tRefund\t305-1251749-5602732\t305-1251749-5602732\tamzn1:crow:YZkTuxs4RhO8FpZez3cGCg\t\tAmazon.de\tItemFees\tCommission\t19,80\tAFN\t04.05.2018\t04.05.2018 18:24:39 UTC\t38048998219979\t\t142721169810\t3700546702082-180124-jpn-131N28-6\t\n7293436482\t\t\t\t\t\tRefund\t305-1251749-5602732\t305-1251749-5602732\tamzn1:crow:YZkTuxs4RhO8FpZez3cGCg\t\tAmazon.de\tItemFees\tRefundCommission\t-3,96\tAFN\t04.05.2018\t04.05.2018 18:24:39 UTC\t38048998219979\t\t142721169810\t3700546702082-180124-jpn-131N28-6\t\n'

# Split the long string into a list of lines
data = orig.decode('utf-8').splitlines()

# Open the file for writing
with open("tmp.csv", "w") as csv_file:
    # Create the writer object with tab delimiter
    writer = csv.writer(csv_file, delimiter='\t')
    for line in data:
        # Writerow() needs a list of data to be written, so split at all empty spaces in the line
        writer.writerow(re.split('\s+', line))
