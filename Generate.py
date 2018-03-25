
# Update shipment (origin , origin_lat , origin_lng)
# SET ( 'BOS' , 42.367668 ,  71.017433 ) where id='d6c184af-6987-1a3b-d13a-61a003474bdc'

# 'BOS' , 42.367668 ,  71.017433
# 'FRA'  , 50.04705,8.561494
# 'NRT' ,  35.761719,140.386887
# 'LHR' ,  51.469177,-0.477066
# 'DXB' , 25.240961,55.374878
# 'PVG' , 31.146822,121.798309
# 'SYD' , -33.934055,151.167618
# 'MEX' ,  19.357122,-98.907997
airports = ['BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ]
airport_id_list = { 'BOS':  'd6c184af-6987-1a3b-d13a-61a003474bdc', 'DXB':	'fc645318-0252-d471-59b5-f73dee3965ed', 'PVG':	'c878bfdf-652c-49db-3613-85b10c542cfa', 'SIN':	'4c2d6f31-387a-223c-e48f-a6ecc1333ffd', 'LHR':	'2dd2283a-4fb6-8066-9cd2-1d830b817840', 'SYD': '0c199d9d-c9a8-55de-5a65-28db601d021e' , 'FRA':	'9b773e2b-7b49-47ac-becf-71cbbd727291',
        'NRT':	'2ada02c9-94b5-879d-e955-fd8255d138c9', 'BOS':	'd1c0c201-958b-effd-6f23-ed231c3d2c66', 'MEX':	'836036b9-5ccd-8034-45ea-72823d2a00c3' }
for airport in airports:
    print(airport_id_list[airport])
