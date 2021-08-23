def run(job_input):
   results = job_input.execute_query("""
   SELECT vc_id, COUNT(DISTINCT esx_id), SUM(vm_count)
   FROM super_collider.example_table
   GROUP BY vc_id
   """)
   job_input.load(results, "super_collider.example_aggregated_table")
