from app.builder.template_builder import Builder

INDEX = (
    Builder()
    .addPage("app/index.html")
    .addTitle("index")
)

INDEX.build()

REPORTS = (
    Builder()
    .addPage("app/reports.html")
    .addTitle("reports")
)

REPORTS.build()

DATASETS = (
    Builder()
    .addPage("app/datasets.html")
    .addTitle("datasets")
)

DATASETS.build()

MAINTENANCE = (
    Builder()
    .addPage("app/maintenance.html")
    .addTitle("maintenance")
)

MAINTENANCE.build()

LOGIN = (
    Builder()
    .addPage("app/login.html")
    .addTitle("login")
)

LOGIN.build()
