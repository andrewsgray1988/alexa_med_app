from datetime import datetime, timedelta
from functions.general import (
    load_last_taken,
    save_medication
)

DEFAULT_PERSON = "me"

def log_medication(medication, person=None, time=None, user_id=None):
    if not user_id:
        raise ValueError("user_id is required")

    person_key = (person or DEFAULT_PERSON).lower()
    med_key = medication.lower()

    if isinstance(time, datetime):
        recorded_time = time.isoformat()
    elif isinstance(time, str):
        recorded_time = time
    else:
        recorded_time = datetime.now().isoformat()

    save_medication(
        user_id=user_id,
        person=person_key,
        medication=med_key,
        timestamp=recorded_time
    )

    return person_key, med_key, recorded_time

def get_last_taken(medication, person=None, user_id=None):
    if not user_id:
        raise ValueError("user_id is required")

    person_key = (person or DEFAULT_PERSON).lower()
    med_key = medication.lower()

    timestamp = load_last_taken(
        user_id=user_id,
        person=person_key,
        medication=med_key
    )

    if not timestamp:
        return None

    return timestamp

def time_since(timestamp):
    if not timestamp:
        return None

    past_time = datetime.fromisoformat(timestamp)
    now = datetime.now()

    delta = now - past_time
    total_seconds = int(delta.total_seconds())

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    parts = []

    if days:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes or not parts:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

    return " ".join(parts) + " ago"

def parse_time_slot(time_value):
    now = datetime.now()

    if not time_value:
        return None

    if time_value.startswith("PT"):
        hours = 0
        minutes = 0

        if "H" in time_value:
            hours = int(time_value.split("T")[1].split("H")[0])
        if "M" in time_value:
            minutes = int(time_value.split("M")[0].split("T")[-1])

        return now - timedelta(hours=hours, minutes=minutes)

    if ":" in time_value:
        hour, minute = map(int, time_value.split(":"))
        return now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if "-" in time_value:
        year, month, day = map(int, time_value.split("-"))
        return datetime(year, month, day)

    return now

