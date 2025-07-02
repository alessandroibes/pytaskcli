
from datetime import datetime


def format_datetime(dt_str: str) -> str:
    return datetime.fromisoformat(dt_str).strftime("%d/%m/%Y %H:%M:%S")
