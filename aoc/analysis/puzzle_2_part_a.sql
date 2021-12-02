SELECT
    step,
    horizontal_position * depth_position
FROM {{ ref('puzzle_2_part_a') }}
ORDER BY step DESC
LIMIT 1