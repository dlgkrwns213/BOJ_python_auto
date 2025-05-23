WITH SKILL AS (
    SELECT SUM(CODE) AS CODE_SUM 
    FROM SKILLCODES 
    WHERE NAME IN ('Python', 'C#')
)

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM 
    DEVELOPERS
    JOIN
    SKILL
    ON  
    SKILL_CODE & SKILL.CODE_SUM <> 0
ORDER BY ID

