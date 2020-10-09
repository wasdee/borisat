# borisat
a python library for retrieving company public data in thailand. It has its own public database for caching, so, it is really fast, smart, and save lot of time and energy.

## Get Started
```
pip install borisat
```

```
import borisat

borisat.get_info(tax_id='0105558096348')

```

## Why it is the way it is?
0. [the government public api is obsolete, doc is unclear and this is 2020, and it is SOAP api. OMG](https://github.com/CircleOnCircles/rd_soap). thus, we need some kinds of modern interface.
1. [retriving data from the government public api is F\*\*king slow in the business hours](https://github.com/CircleOnCircles/rd_soap). thus, we need some kinds of cache. a public one where who use this lib could enjoy.

### A public cache?
There is no such thing as a public cache/database. There is a close thing.
1. Public Google BigQuery
2. Smart contact. Blockchain 

being a cache key value access is so critical. if you use BigQuery to query for a single row, since it is a column-based db in will cost a lot when your database get bigger, very costly. and to let other have your write-only key to the database is nut.

on surface Blockchain seems legit. there is a mapping data type on solidity. Wow, this might be a way to go. I took my word back when I saw a blog, [No, you don’t store data on the blockchain – here’s why](https://jaxenter.com/blockchain-data-164727.html) 1MB for 700 Dollars, holy cow! I knows that there is [a hashgraph blockchain](https://www.hedera.com/). the price is great, but there is no official python support + the unofficial is 2 years old of unmaintain.

ok then, my last combo would be create a cache serverless api + store on a serverless database which I pay myself and let the lib call my fast api first, if there is no data, call the gov server, then lib call my api to store the cache. open source everything that is my experiment.
