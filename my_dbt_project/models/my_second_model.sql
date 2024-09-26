select *
from {{ ref("stg_my_first_model") }}
where id = 1