WITH deconstructed_bits AS (
    SELECT 
        ROW_NUMBER() OVER () AS reading_number,
        {% for i in range(1,11) %}
        GET_BIT(reading::BIT(12), {{ i }}) AS bit_{{ i }}
        {% endfor %}
    FROM public_seed_data.puzzle_3
), sum_table AS (
	SELECT
		  bit_order,
		  COUNT(elem) AS total_elements,
		  SUM(elem::INT) AS bit_sum
	FROM public_seed_data.puzzle_3 AS p, 
		 UNNEST(STRING_TO_ARRAY(p.reading, NULL)) WITH ORDINALITY a(elem, bit_order)
	GROUP BY bit_order
	ORDER BY bit_order ASC
), most_common_binary AS (
	SELECT
		STRING_AGG(result_bit, '')::BIT(12) AS most_common_binary
	FROM (
		SELECT 
			bit_order,
			CASE
				WHEN bit_sum >= (total_elements / 2.0)
				THEN '1'
				ELSE '0'
			END AS result_bit
		FROM sum_table
		ORDER BY bit_order
	) AS result_binary
)

SELECT 
    *
FROM deconstructed_bits AS d
INNER JOIN most_common_binary AS m
    ON {% for i in range(0,11) %}
        d.bit_{{ i }} = GET_BIT(m.most_common_binary, {{ i }})
    {% endfor %}