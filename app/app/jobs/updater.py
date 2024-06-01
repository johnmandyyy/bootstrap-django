from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs import jobs


def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(jobs.sample_job, 'interval', seconds=5)
	scheduler.start()