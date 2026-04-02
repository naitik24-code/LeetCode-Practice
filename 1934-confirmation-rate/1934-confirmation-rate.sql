SELECT 
    u.user_id,
    ROUND(
        IFNULL(SUM(c.action = 'confirmed') / COUNT(c.action), 0),
        2
    ) AS confirmation_rate
FROM Signups u
LEFT JOIN Confirmations c
ON u.user_id = c.user_id
GROUP BY u.user_id;