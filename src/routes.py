# coding: utf-8
from resources.appointments import AppointmentResource

APPOINTMENTS = AppointmentResource().get_list
APPOINTMENT_DETAIL = AppointmentResource().get_detail


def setup_routes(app):
    app.router.add_get(r"/appointments", APPOINTMENTS, name="appointments")
    app.router.add_get(r"/appointments/{appointment_id}",
                       APPOINTMENT_DETAIL, name="appointment_detail")
