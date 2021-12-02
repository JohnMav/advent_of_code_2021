SELECT
	step,
	direction,
	distance,
	horizontal_position,
	depth_position AS aim_position,
	SUM(
        CASE WHEN direction = 'forward'
             THEN (distance * depth_position)
         ELSE 0
        END
    ) OVER (ROWS UNBOUNDED PRECEDING) AS depth_position
FROM {{ ref('puzzle_2_part_a') }}