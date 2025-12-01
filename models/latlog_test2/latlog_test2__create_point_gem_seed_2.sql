{{
  config({    
    "materialized": "table",
    "alias": "create_point_gem_seed",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH create_point_gem_seed_1 AS (

  SELECT * 
  
  FROM {{ source('sony.orch_test', 'create_point_gem_seed') }}

)

SELECT *

FROM create_point_gem_seed_1
