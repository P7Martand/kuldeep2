{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_orchestration"
  })
}}

WITH points AS (

  SELECT *
  
  FROM {{ ref('latlog__points')}}

),

single_point AS (

  SELECT * 
  
  FROM points AS in0
  
  LIMIT 1

)

SELECT *

FROM single_point
