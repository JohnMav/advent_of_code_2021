WITH depth_groups AS (
	SELECT 
		SUM(depth) OVER (ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) AS depth_sum
	FROM {{ ref('puzzle_1') }}
)

{{ compute_increases('depth_groups', 'depth_sum') }}