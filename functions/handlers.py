from functions.functions import (
    log_medication,
    get_last_taken,
    parse_time_slot
)

def handle_log_medication(slots, user_id):
    medication = slots.get("medication")
    person = slots.get("person")
    time_value = slots.get("time")

    parsed_time = parse_time_slot(time_value) if time_value else None

    return log_medication(
        medication=medication,
        person=person,
        time=parsed_time,
        user_id=user_id
    )

    return log_medication(medication, medicated, parsed_time)

def handle_get_medication(slots, user_id):
    medication = slots.get("medication")
    person = slots.get("person")

    return get_last_taken(
        medication=medication,
        person=person,
        user_id=user_id
    )