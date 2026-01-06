from functions.functions import (
    log_medication,
    get_last_taken,
    parse_time_slot
)

def handle_log_medication(slots, user_id):
    medication = slots.get("medication")
    person = slots.get("person")

    duration = slots.get("duration")
    time = slots.get("time")

    time_value = duration or time
    parsed_time = parse_time_slot(time_value) if time_value else None

    if not person or person.lower() in ["i", "me"]:
        person = "me"

    return log_medication(
        medication=medication,
        person=person,
        time=parsed_time,
        user_id=user_id
    )

def handle_get_medication(slots, user_id):
    medication = slots.get("medication")
    person = slots.get("person")

    if not person or person.lower() in ["i", "me"]:
        person = "me"

    return get_last_taken(
        medication=medication,
        person=person,
        user_id=user_id
    )

def run_intent(intent, slots):
    if intent == "LogMedicationIntent":
        return handle_log_medication(slots)

    if intent == "GetLastTaken":
        return handle_get_medication(slots)

    raise ValueError(f"Unknown intent: {intent}")