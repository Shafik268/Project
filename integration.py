from database.database import (
    insert_report,
    insert_resource,
    get_all_resources,
    get_total_reports,
    get_total_resources,
    get_total_shelters,
    get_recent_reports
)


# ======================================================
# REPORT FUNCTIONS
# ======================================================

def save_report(
    name,
    contact,
    disaster,
    location,
    urgency,
    description
):
    """
    Save an emergency report to the database.
    """

    insert_report(
        name,
        contact,
        disaster,
        location,
        urgency,
        description
    )


# ======================================================
# DASHBOARD FUNCTIONS
# ======================================================

def dashboard_data():
    """
    Return all dashboard statistics.
    """

    return {
        "total_reports": get_total_reports(),
        "resources": get_total_resources(),
        "shelters": get_total_shelters(),
        "reports": get_recent_reports()
    }


# ======================================================
# RESOURCE FUNCTIONS
# ======================================================

def save_resource(resource_name, quantity):
    """
    Save a resource into the database.
    """

    insert_resource(
        resource_name,
        quantity
    )


def resource_data():
    """
    Return all resources for the Resources page.
    """

    return {
        "resources": get_all_resources()
    }