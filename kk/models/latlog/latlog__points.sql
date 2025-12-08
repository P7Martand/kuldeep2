{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_orchestration"
  })
}}

WITH create_point AS (

  SELECT *
  
  FROM {{ ref('latlog__create_point')}}

),

points AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    from_wkt AS from_wkt,
    Alteryx_Distance_KM AS Alteryx_Distance_KM,
    Formula_Distance_KM AS Formula_Distance_KM,
    Difference_Alteryx_KM_2 AS Difference_Alteryx_KM_2,
    h3_approx_distance AS h3_approx_distance,
    Difference_Alteryx_KM AS Difference_Alteryx_KM
  
  FROM create_point AS in0

)

SELECT *

FROM points
