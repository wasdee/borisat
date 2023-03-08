# borisat
Python Library #borisat ดึงข้อมูลชื่อและที่อยู่บริษัทจากเลขที่ประจำตัวผู้เสียภาษี 😎

a python library for retrieving company public data in thailand. ~~It has its own public database for caching, so, it is really fast, smart, and save lot of time and energy.~~

## Get Started
```shell
pip install borisat
```

```python
import borisat

a_valid_tax_id = tax_id = '0105558096348'

if borisat.is_exist(tax_id):
    company = borisat.get_info(tax_id=tax_id) 
    print(company)
# NID='0105558096348' title_name='บริษัท' name='โฟลว์แอคเคาท์ จำกัด' surname='-' branch_name='โฟลว์แอคเคาท์ จำกัด' branch_number=0 branch_title_name='บริษัท' business_first_date='2016/04/07' building_name='ชุดสกุลไทย สุรวงศ์ ทาวเวอร์' floor_number='11' room_number='12B' village_name='-' house_number='141/12' moo_number='-' soi_name='-' street_name='สุรวงศ์' thambol='สุริยวงศ์' amphur='บางรัก' province='กรุงเทพมหานคร' post_code='10500'

another_valid_tax_id = tax_id = "0994000160097"
company = borisat.get_info(tax_id=tax_id) 
print(company)
# NID='0994000160097' title_name='มหาวิทยาลัย' name='เทคโนโลยีพระจอมเกล้าธนบุรี' surname='-' branch_name='กลุ่มงานส่งเสริมและบริการวิจัย' branch_number=0 branch_title_name='-' business_first_date='2013/09/17' building_name='สำนักงานอธิการบดี' floor_number='-' room_number='-' village_name='-' house_number='126' moo_number='-' soi_name='-' street_name='ประชาอุทิศ' thambol='บางมด' amphur='ทุ่งครุ' province='กรุงเทพมหานคร' post_code='10140'
```

## Why it is the way it is?
0. [the government public api is obsolete, doc is unclear and this is 2020, and it is SOAP api. OMG](https://github.com/CircleOnCircles/rd_soap). thus, we need some kinds of modern interface. took me a day to figure many things out.
1. [retriving data from the government public api is F\*\*king slow in the business hours](https://github.com/CircleOnCircles/rd_soap). thus, we need some kinds of cache. a public one where who use this lib could enjoy.


## Roadmap 

See project board
