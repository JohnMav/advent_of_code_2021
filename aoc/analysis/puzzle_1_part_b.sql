SELECT
    COUNT(
        CASE WHEN increased
             THEN group_number
             ELSE NULL
        END
    ) AS depth_increase_count
FROM {{ ref('puzzle_1_part_b') }}