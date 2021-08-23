from vacloud.api.job_input import IJobInput


def run(job_input: IJobInput):

   job_input.execute_query("""
   create view if not exists super_collider.vw_dim_example as 
   SELECT "id" as id, "1.2" as version 
   """)

   job_input.execute_query("""
   create table if not exists super_collider.dim_example (id string, version string)
   """)

   template_name = "load/dimension/scd1"
   template_args = {"target_schema": "super_collider",
                    "target_table": "dim_{}".format("example"),
                    "source_schema": "super_collider",
                    "source_view": "vw_dim_{}".format("example"),
                    "staging_schema": "super_collider" }
   job_input.execute_template(template_name, template_args)
