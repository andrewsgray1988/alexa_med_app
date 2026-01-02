from functions.handlers import (
    handle_log_medication,
    handle_get_medication
)

def run_intent(intent, slots):
    if intent == "LogMedicationIntent":
        return handle_log_medication(slots)

    if intent == "GetLastTaken":
        return handle_get_medication(slots)

    raise ValueError(f"Unknown intent: {intent}")