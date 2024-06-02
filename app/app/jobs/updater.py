from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs import jobs

class Scheduler:

	def __init__(self):
		pass


	def start(self):

		scheduler = BackgroundScheduler()
		tasks = jobs.Tasks()

		scheduler.add_job(tasks.sample_job, 'interval', seconds=5)
		scheduler.start()