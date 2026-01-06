from functions.functions import get_last_taken, time_since

# Same user ID we used when logging
USER_ID = "test-user-123"

print("=== Reading existing medications ===")

# Check last taken for "me"
last_taken_me = get_last_taken(
    medication="Ibuprofen",
    person=None,
    user_id=USER_ID
)
if last_taken_me:
    print(f"You last took Ibuprofen {time_since(last_taken_me)}")
else:
    print("No record found for Ibuprofen")

# Check last taken for Reggie
last_taken_reggie = get_last_taken(
    medication="Allergy medicine",
    person="Reggie",
    user_id=USER_ID
)
if last_taken_reggie:
    print(f"Reggie last took Allergy medicine {time_since(last_taken_reggie)}")
else:
    print("No record found for Reggie")
