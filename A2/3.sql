select licence_no, name
from drive_licence d, people p
where p.sin = d.sin
AND d.class <> 'nondriving'
AND p.sin not IN 
(select p.sin
from owner o, vehicle v
where o.owner_id = p.sin
AND v.serial_no = o.vehicle_id
AND v.color = 'red'
);