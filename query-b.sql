(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5` FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'AURN St Pauls' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Bath Road' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Brislington Depot' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'CREATE Centre Roof' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Cheltenham Road \ Station Road' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Colston Avenue' AND YEAR(r.datetime) = 2019 )
UNION 
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Fishponds Road' AND YEAR(r.datetime) = 2019 )
UNION 
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Newfoundland Road Police Station' AND YEAR(r.datetime) = 2019 )
UNION 
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Old Market' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Parson Street School' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Rupert Street' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = "Shiner's Garage" AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Temple Way' AND YEAR(r.datetime) = 2019 )
UNION
(SELECT datetime, location, AVG(r.`pm 2.5`) AS `Mean of PM 2.5`, AVG(r.`vpm 2.5`) AS `Mean of VPM 2.5`  FROM readings r, stations s WHERE r.`stationid-fk` = s.stationId AND s.location = 'Wells Road' AND YEAR(r.datetime) = 2019 )
