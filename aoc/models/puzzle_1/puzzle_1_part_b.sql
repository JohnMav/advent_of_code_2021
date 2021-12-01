WITH depth_groups AS (
	SELECT 
		ROW_NUMBER() OVER () AS group_number,
		depth,
		lead(depth,1) OVER () AS depth_2,
		lead(depth,2) OVER () AS depth_3
	FROM {{ ref('puzzle_1') }}
)

SELECT
	group_number,
	depth + depth_2 + depth_3 AS depth_sum,
	CASE
		WHEN 
			depth + depth_2 + depth_3 > LAG(depth + depth_2 + depth_3) OVER (ORDER BY group_number ASC)
		THEN TRUE
		ELSE FALSE
	END AS increased
FROM depth_groups