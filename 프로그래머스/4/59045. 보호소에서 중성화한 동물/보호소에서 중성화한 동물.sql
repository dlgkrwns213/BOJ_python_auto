SELECT ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME
FROM 
    ANIMAL_INS ins
    JOIN
    ANIMAL_OUTS outs
    ON ins.animal_id = outs.animal_id
where  
    SUBSTRING(ins.SEX_UPON_INTAKE, 1, 6) = 'Intact'
    AND
    SUBSTRING(outs.SEX_UPON_OUTCOME, 1, 6) <> 'Intact';