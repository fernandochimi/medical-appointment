# coding: utf-8
from resources.appointments import AppointmentResource
from resources.patients import PatientResource
from resources.procedures import ProcedureResource

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

PROCEDURES = ProcedureResource().get_list
PROCEDURE_DETAIL = ProcedureResource().get_detail
CREATE_PROCEDURE = ProcedureResource().register
ALTER_PROCEDURE = ProcedureResource().alter
DELETE_PROCEDURE = ProcedureResource().delete


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

    app.router.add_get(r"/procedures", PROCEDURES, name="procedures")
    app.router.add_get(r"/procedures/{procedure_id}",
                       PROCEDURE_DETAIL, name="procedure_detail")
    app.router.add_post(r"/procedures",
                        CREATE_PROCEDURE, name="create_procedures")
    app.router.add_put(r"/procedures/{procedure_id}",
                       ALTER_PROCEDURE, name="alter_procedure")
    app.router.add_delete(r"/procedures/{procedure_id}",
                          DELETE_PROCEDURE, name="delete_procedure")
