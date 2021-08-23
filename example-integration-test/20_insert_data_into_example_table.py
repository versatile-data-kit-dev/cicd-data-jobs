"""
Detailed documentation of VDK provided functionalities in job_input object can be found here:
https://gitlab.eng.vmware.com/core-build/productanalytics/blob/master/analytics/vdk/src/vacloud/api/job_input.py
"""
def run(job_input):
   """
   This method is called automatically during execution. Only scripts containing this method are executed by VDK.
      Arguments:
         job_input: object automatically passed to run() method by VDK on execution.
   """
   job_input.execute_query("""
   INSERT OVERWRITE super_collider.example_table VALUES
   ('vc1', 'esx1', 1),
   ('vc1', 'esx2', 2),
   ('vc2', 'esx3', 10),
   ('vc2', 'esx4', 5),
   ('vc3', 'esx5', 0);
   """)
