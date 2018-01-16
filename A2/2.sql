select name,addr
from people p
where p.sin IN
((select p.sin
from owner o1, owner o2, owner o3
where o1.owner_id = p.sin
AND o2.owner_id = p.sin
AND o3.owner_id = p.sin
AND o1.vehicle_id <> o2.vehicle_id
AND o1.vehicle_id <> o3.vehicle_id
AND o2.vehicle_id <> o3.vehicle_id)
intersect
(select p.sin
from owner o, vehicle v, vehicle_type vt
where o.owner_id = p.sin
AND o.vehicle_id = v.serial_no
AND v.type_id = vt.type_id
AND vt.type = 'SUV'));