# coding: utf-8
from resources.appointments import AppointmentResource
from resources.patients import PatientResource

APPOINTMENTS = AppointmentResource().get_list
APPOINTMENT_DETAIL = AppointmentResource().get_detail
CREATE_APPOINTMENT = AppointmentResource().register
ALTER_APPOINTMENT = AppointmentResource().alter
DELETE_APPOINTMENT = AppointmentResource().delete

PATIENTS = PatientResource().get_list
PATIENT_DETAIL = PatientResource().get_detail
CREATE_PATIENT = PatientResource().register
ALTER_PATIENT = PatientResource().alter
DELETE_PATIENT = PatientResource().delete


def setup_routes(app):
    app.router.add_get(r"/appointments", APPOINTMENTS, name="appointments")
    app.router.add_get(r"/appointments/{appointment_id}",
                       APPOINTMENT_DETAIL, name="appointment_detail")
    app.router.add_post(r"/appointments",
                        CREATE_APPOINTMENT, name="create_appointment")
    app.router.add_put(r"/appointments/{appointment_id}",
                       ALTER_APPOINTMENT, name="alter_appointment")
    app.router.add_delete(r"/appointments/{appointment_id}",
                          DELETE_APPOINTMENT, name="delete_appointment")

    app.router.add_get(r"/patients", PATIENTS, name="patients")
    app.router.add_get(r"/patients/{patient_id}",
                       PATIENT_DETAIL, name="patient_detail")
    app.router.add_post(r"/patients",
                        CREATE_PATIENT, name="create_patients")
    app.router.add_put(r"/patients/{patient_id}",
                       ALTER_PATIENT, name="alter_patient")
    app.router.add_delete(r"/patients/{patient_id}",
                          DELETE_PATIENT, name="delete_patient")
