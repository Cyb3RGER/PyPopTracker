import json
from typing import Any

from .. import PopTrackerType


class PopTrackerJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, PopTrackerType):
            return {k: v for k, v in o.__dict__.items() if
                    v is not None and not ((isinstance(v, list) or isinstance(v, dict)) and len(v) == 0)}
        return json.JSONEncoder.default(self, o)
