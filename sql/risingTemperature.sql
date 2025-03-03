-- Rising Temperature

/*Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).*/

SELECT w1.id FROM Weather WHERE temperature > (
    SELECT w2.Temperature FROM Weather WHERE 
    recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
);