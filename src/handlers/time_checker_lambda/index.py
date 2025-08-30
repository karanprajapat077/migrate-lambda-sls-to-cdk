from datetime import datetime
from .utils.logger import SimpleLogger

logger = SimpleLogger("TimeChecker")

def lambda_handler(event, context):
    method = "lambda_handler"
    logger.start(method)

    # Get target time from event
    target_time_str = event.get("target_time", "18:30")  # default 18:30
    logger.message(method, f"Target time received: {target_time_str}")

    # Current time
    now = datetime.now()
    current_time_str = now.strftime("%H:%M")
    logger.message(method, f"Current time: {current_time_str}")

    # Parse target time
    try:
        target_time = datetime.strptime(target_time_str, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
    except ValueError:
        logger.message(method, "Invalid time format. Use HH:MM (24hr).")
        logger.end(method)
        return {"statusCode": 400, "body": "Invalid time format. Use HH:MM."}

    # Compare times
    if now >= target_time:
        logger.message(method, "Target time has already been reached ✅")
        response = {
            "statusCode": 200,
            "body": f"Target time {target_time_str} has already been reached."
        }
    else:
        time_diff = target_time - now
        minutes_left = divmod(time_diff.seconds, 60)[0]
        logger.message(method, f"Time remaining: {minutes_left} minutes ⏳")
        response = {
            "statusCode": 200,
            "body": f"Time remaining to reach {target_time_str}: {minutes_left} minutes."
        }

    logger.end(method)
    return response
