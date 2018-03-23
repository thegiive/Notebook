CREATE KEYSPACE inbound
   WITH REPLICATION = {
   'class' : 'SimpleStrategy',
   'replication_factor' : 2
};

CREATE TABLE inbound.gps_location 
    ( 
        id bigint PRIMARY KEY , 
        device_tag ascii , 
        device_name ascii, 
        acquired_time timestamp, 
        received_time timestamp , 
        lat float ,
        lng float ,
        location_address ascii, 
        sensor_detail text 
);

INSERT into  inbound.gps_location
( id  , device_tag  , device_name , acquired_time , received_time  , lat  , lng  , location_address , sensor_detail )
 VALUES 
 ( 1 , "aaa" , "·*8/10 ZS100-010100481-GPS" , "2018/01/01" , "2018/01/01" , 43.22626 , 51.572498 , "Karakiya area, Western Region, Kazakhstan" , "Yes:Standard report data,Power module on,Cell antenna available,GPS location mode,Temperature module valid,Humidity module valid,Acceleration module valid,Light module valid,Pressure module valid,Elevation calculated by pressure,Cell communication mode,Motion detected,Cell location mode;No:Buffer data,Power on,Charging,Battery out of range,Shipment assigned" ); 

 INSERT into  inbound.gps_location
( id    ,device_tag ,  device_name , acquired_time , received_time  , lat  , lng  , location_address , sensor_detail )
 VALUES 
 ( 1  , '12233' , 'ZS100-010100481-GPS' ,  '2017-05-05 00:00:00.000+0000' ,  '2017-05-05 00:00:00.000+0000' , 43.22626 , 51.572498 , 'Karakiya area, Western Region, ' ,'Yes:Standard report data,Static mode,Power module on,Cell antenna available,GPS location mode,Temperature module valid,Humidity module valid,Acceleration module valid,Light module valid,Pressure module valid,Elevation calculated by pressure,Cell communication mode,Cell location mode;No:Buffer data,Power on,Charging,Battery out of range,Motion detected,Shipment assigned'); 