
select id,origin,* from shipment ;
select * from shipment_location ;

select * from shipment_location; 
select * from shipment_event;


select origin,id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) ; 
update shipment set origin='Shanghai' where origin='taiwan'

Update shipment set (origin_lat , origin_lng) =  ( 42.367668 ,  71.017433 )

update shipment set origin='Shanghai', destination_lat=37.773972 ,  destination_lng=-122.431297 , origin_lat=31.267401 ,  origin_lng=121.522179 where id in ( select id from shipment order by random() limit 10 )  
update shipment set origin='London', destination_lat=37.773972 ,  destination_lng=-122.431297 , origin_lat=51.509865 ,  origin_lng=-0.118092 where id in ( select id from shipment order by random() limit 5 )  
update shipment set origin='Tokyo', destination_lat=37.773972 ,  destination_lng=-122.431297 , origin_lat=35.652832 ,  origin_lng=-139.839478 where id in ( select id from shipment order by random() limit 5 )  
Update shipment SET (origin , origin_lat , origin_lng) = ( 'BOS' , 42.367668 ,  71.017433 ) where id='d6c184af-6987-1a3b-d13a-61a003474bdc'

delete from shipment ; 
commit;

ALTER TABLE shipment rename column asn to asn_number; 

select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 

Update shipment set (origin , origin_lat , origin_lng) = ('BOS' , 42.367668 ,  71.017433) where id in (
                  select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('FRA'  , 50.04705,8.561494) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('NRT' ,  35.761719,140.386887) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('LHR' ,  51.469177,-0.477066) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('DXB' , 25.240961,55.374878) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('PVG' , 31.146822,121.798309) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('SYD' , -33.934055,151.167618) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('MEX' , 19.357122,-98.907997) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
                Update shipment set (origin , origin_lat , origin_lng) = ('SIN' , 1.358505,103.997559) where id in (select id from shipment where origin not in ('BOS' , 'FRA' , 'NRT' , 'LHR' , 'DXB' , 'PVG' , 'SYD' , 'MEX' , 'SIN' ) order by random() limit  10 ) ;
