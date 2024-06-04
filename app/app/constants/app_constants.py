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

# Permission Related
TOKEN_HAS_EXPIRY = False
TOKEN_VALIDITY = 60 * 60

# Logging Related
LOG_LEVEL = Levels()
LOG_TYPE = LogTypes()



