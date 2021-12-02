SELECT 
	ROW_NUMBER() OVER () AS step,
	direction,
	distance,
	SUM(
		CASE
			WHEN direction = 'forward'
			THEN distance
			ELSE 0
		END 
	) OVER (ROWS UNBOUNDED PRECEDING) AS horizontal_position,
	SUM(CASE
			WHEN direction = 'up'
			THEN -distance
			WHEN direction = 'down'
			THEN distance
			ELSE 0
		END
	) OVER (ROWS UNBOUNDED PRECEDING) AS depth_position
FROM {{ ref('puzzle_2') }}