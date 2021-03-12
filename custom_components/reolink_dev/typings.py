""" Typing declarations for strongly typed dictionaries """

from typing import Any, List, TypedDict
from datetime import datetime, date

VodEvent = TypedDict(
    "VodEvent",
    {
        "start": datetime,
        "end": datetime,
        "file": str,
        "thumbnail": Any,
    },
)

MediaSourceCacheEntry = TypedDict(
    "MediaSourceCacheEntry",
    {
        "entry_id": str,
        "unique_id": str,
        "event_id": str,
        "name": str,
        "playback_months": int,
        "playback_thumbs": bool,
        "playback_day_entries": List[date],
        "playback_events": dict[str, VodEvent],
    },
    total=False,
)
