import psutil

class Stats():

  @classmethod
  def get_cpu_percent(cls):
    cpu_percent = psutil.cpu_percent()
   # swap_memory=psutil.swap_memory()
   # disk_usage= psutil.disk_usage() 
    return cpu_percent
	
