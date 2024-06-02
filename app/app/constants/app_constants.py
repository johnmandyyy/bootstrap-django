from app.logs.logging import Levels, LogTypes

#App Related
APP_NAME = "app"
SOFTWARE_NAME = "App Name"
SOFTWARE_DESCRIPTION = "App Description"

#Database Related
EXCEPT_MODELS = [
    "LogEntry",
    "Permission",
    "Group",
    "User",
    "ContentType",
    "Session",
]

# Logging Related
LOG_LEVEL = Levels()
LOG_TYPE = LogTypes()



