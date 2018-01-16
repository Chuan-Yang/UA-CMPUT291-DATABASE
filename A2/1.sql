select serial_no
from vehicle v, owner o, people p
where (v.serial_no = o.vehicle_id AND o.owner_id = p.sin
AND p.addr not like 'Edmonton');
