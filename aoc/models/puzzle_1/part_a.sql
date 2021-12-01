SELECT
    ROW_NUMBER() OVER (),
    depth,
    CASE
        WHEN depth - LAG(depth) OVER () > 0
        THEN TRUE
        ELSE FALSE
    END AS increased
FROM public_seed_data.puzzle_1