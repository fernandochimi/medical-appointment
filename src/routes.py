# coding: utf-8
from resources.appointments import AppointmentResource

GET_APPOINTMENTS = AppointmentResource().get_appointments


def setup_routes(app):
    # app.router.add_get(r"/", index)
    app.router.add_get(r"/appointments", GET_APPOINTMENTS, name="appointments")
    # app.router.add_get(r"/appointments/{appointment_id:^[-+]?[0-9]+$}")
