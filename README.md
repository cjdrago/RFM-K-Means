# Online Retail
[Data Set Link](https://archive.ics.uci.edu/ml/datasets/online+retail)
### Context
Online retail is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

### Business Goal
We will be using the online retail trasnational dataset to build a RFM clustering and choose the best set of customers which the company should target.
> #### RFM
> RFM analysis objective is quite clear: *identify customers with recent purchase records (low recency), frequent purchase record(high frequency) and have spent good money (monetary is high). **Basically it is a marketing analysis tool used to identify a company's or an organization's best customers by using the measured mentioned before***. These customers likely to be more important than customers with low frequency and low monetary purchases. <br>
> There are also those customers in the middle, with moderately high frequency and monetary, but also very high recency. Perhaps these customers bought something in the past which is no longer offered or available.<br>
>RFM analysis allows a comparison between potential contributors or clients. It gives organizations a sense of how much revenue comes from repeat customers (versus new customers), and which levers they can pull to try to make customers happier so they become repeat purchasers.

### Attribute Information:

1. InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to **each transaction**. If this code starts with letter 'c', it indicates a cancellation.
2. StockCode: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.
3. Description: Product (item) name. Nominal.
4. Quantity: The quantities of each product (item) per transaction. Numeric.
5. InvoiceDate: Invice Date and time. Numeric, the day and time when each transaction was generated.
6. UnitPrice: Unit price. Numeric, Product price per unit in sterling.
7. CustomerID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.
8. Country: Country name. Nominal, the name of the country where each customer resides.

---

### Final clustering


<a href="https://cjdrago.github.io/RFM-K-Means/" target="_blank">Link to scaled-data plot (clustered)</a>

<a href="https://cjdrago.github.io/RFM-K-Means/nonScaled.html" target="_blank">Link to original-data plot (clustered)</a>
