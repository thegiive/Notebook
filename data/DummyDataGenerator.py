import psycopg2
conn = psycopg2.connect( host="localhost", user="postgres", password="mysecretpassword", dbname="postgres" )
cur = conn.cursor()

import csv

file_name = "flight_data/Flight_B6833_(10a2028c).csv"
 with open(file_name, newline='') as File:
     reader = csv.reader(File)
     for row in reader:
         dit  = row[3].split(",")
         if(len(dit) > 1):
             sql  = "Insert into public.shipment_location (id , lat , lng , shipment_id  , located_at )  "
             sql += "VALUES (uuid_in(md5(random()::text || now()::text)::cstring) ,"
             sql += f"{dit[0]} , {dit[1]} , '3d93cb79-9b39-70be-bb20-b45fd4d95138' , now() "
             cur.execute(sql)
conn.commit()


#INSERT INTO public.shipment_location  (id , lat , lng , shipment_id  , located_at )
# VALUES (uuid_in(md5(random()::text || now()::text)::cstring) ,
# 37.611099 , -122.389915  , '3d93cb79-9b39-70be-bb20-b45fd4d95138' , now() ) ;

stage_list  = ['[MYKULA, MY]DEPARTED FROM LOCAL DISTRIBUTION CENTER', '[IPZ Frankfurt, DE]PROCESSED AT TRANSIT FACILITY', '[MT Los Angeles, DE]PROCESSED AT EXPORT           FACILITY', '[Compton, CA, US]PROCESSING COMPLETED AT ORIGIN', '[Deutsche Post Los Angeles, DE]PROCESSED AT EXPORT FACILITY', '[Compton, CA,                   US]PROCESSED', '[Compton, CA, US]ARRIVAL AT DHL ECOMMERCE DISTRIBUTION CENTER', '[UNITED STATES]EN ROUTE TO DHL ECOMMERCE DISTRIBUTION CENTER', '[UNITED      STATES]ELECTRONIC NOTIFICATION RECEIVED: YOUR ORDER HAS BEEN PROCESSED AND TRACKING WILL BE UPDATED SOON']
location_id_list = ['c9953557-f6ca-8ed2-36f5-8c2c21219c50', 'ae8ca673-18e1-f56b-0f14-1e6bfa14a2a9', '57d3dc43-27db-0861-7f06-c59ebc3fa7a2', '7e0fb42c-7f7c-1d0c-f827-c67cb50004ba', '026570dd-11fc-0f99-6447-037cd31f064d', 'e3ee8879-d34d-57d0-598d-88d511c6338e', '6525e2b6-f19a-c23d-8288-196d474d0e12', '255102c1-3f32-11e1-1ed5-8911899c629e', '00870bf7-9ab6-3710-6d0e-327b1e9751e2']
i = 0
for stage_text in stage_list:
    sql  = " INSERT INTO public.shipment_event (id , shipment_location_id , "
    sql += "shipment_id , event_discription , event_source_url , operated_at) "
    sql += "VALUES ( uuid_in(md5(random()::text || now()::text)::cstring) , "
    sql += "'"+location_id_list[i]+"',"
    sql += f"'3d93cb79-9b39-70be-bb20-b45fd4d95138'  , {stage_text} , "
    sql += "'https://china.tracking.my/dhl/RX581393374DE' , now() ; "
    cur.execute(sql)
    i += 1

conn.commit()


# INSERT INTO public.shipment_event (id , shipment_location_id ,
#             shipment_id , event_discription , event_source_url , operated_at)
# VALUES (
#     uuid_in(md5(random()::text || now()::text)::cstring) , 'c9953557-f6ca-8ed2-36f5-8c2c21219c50' ,
#     '3d93cb79-9b39-70be-bb20-b45fd4d95138' , '[UNITED STATES]ELECTRONIC NOTIFICATION RECEIVED: YOUR ORDER HAS BEEN PROCESSED AND TRACKING WILL BE UPDATED SOON' ,
#     'https://china.tracking.my/dhl/RX581393374DE' , now()
# )
conn.close()
