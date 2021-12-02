{% macro compute_increases(table_name, column_name) %}
SELECT
    ROW_NUMBER() OVER () AS step,
    {{ column_name }},
    CASE
        WHEN {{ column_name }} - LAG({{ column_name }}) OVER () > 0
        THEN TRUE
        ELSE FALSE
    END AS increased
FROM {{ table_name }}
{% endmacro %}