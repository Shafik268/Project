from database.database import get_total_reports, insert_report


def save_report(
    name,
    contact,
   disaster,
   location,
   urgency,
   description
):

    insert_report(
        name,
        contact,
        disaster,
        location,
        urgency,
        description
    )
    from database.database import get_total_reports

from database.database import get_total_resources

from database.database import get_total_shelters

from database.database import get_recent_reports
def dashboard_data():

    return {

        "total_reports": get_total_reports(),

        "resources": get_total_resources(),

        "shelters": get_total_shelters(),

        "reports": get_recent_reports()

    }