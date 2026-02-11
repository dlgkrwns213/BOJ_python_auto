SELECT ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME
FROM ANIMAL_INS AS ins
JOIN ANIMAL_OUTS AS outs
WHERE
    ins.ANIMAL_ID = outs.ANIMAL_ID
    AND
    ins.SEX_UPON_INTAKE NOT IN ('Spayed Female', 'Spayed Male', 'Neutered Female', 'Neutered Male')
    AND
    outs.SEX_UPON_OUTCOME IN ('Spayed Female', 'Spayed Male', 'Neutered Female', 'Neutered Male')