SELECT ID, FISH_NAME, LENGTH
FROM
    (
        SELECT *
        FROM FISH_INFO
        WHERE 
            (FISH_TYPE, LENGTH)
            IN (
                select FISH_TYPE, MAX(LENGTH)
                from FISH_INFO
                GROUP BY FISH_TYPE
            )
    ) as fi
    join
    FISH_NAME_INFO as fni
    on fi.fish_type = fni.fish_type
    


