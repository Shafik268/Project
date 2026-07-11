from database.database import insert_report


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