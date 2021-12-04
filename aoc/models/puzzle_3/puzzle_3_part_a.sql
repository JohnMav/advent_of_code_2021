WITH sum_table AS (
	SELECT
		  bit_order,
		  COUNT(elem) AS total_elements,
		  SUM(elem::INT) AS bit_sum
	FROM public_seed_data.puzzle_3 AS p, 
		 UNNEST(STRING_TO_ARRAY(p.reading, NULL)) WITH ORDINALITY a(elem, bit_order)
	GROUP BY bit_order
	ORDER BY bit_order ASC
), gamma_result AS (
	SELECT
		STRING_AGG(result_bit, '')::BIT(12) AS gamma_binary
	FROM (
		SELECT 
			bit_order,
			CASE
				WHEN bit_sum > (total_elements / 2.0)
				THEN '1'
				ELSE '0'
			END AS result_bit
		FROM sum_table
		ORDER BY bit_order
	) AS result_binary
), epsilon_result AS (
	SELECT
		STRING_AGG(result_bit, '')::BIT(12) AS epsilon_binary
	FROM (
		SELECT 
			bit_order,
			CASE
				WHEN bit_sum > (total_elements / 2.0)
				THEN '0'
				ELSE '1'
			END AS result_bit
		FROM sum_table
		ORDER BY bit_order
	) AS result_binary
)

SELECT 
	gamma_binary,
	epsilon_binary,
	gamma_binary::INT AS gamma_result,
	epsilon_binary::INT AS epsilon_result,
	gamma_binary::INT * epsilon_binary::INT AS power
FROM gamma_result
CROSS JOIN epsilon_result;