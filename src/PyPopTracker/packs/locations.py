import json
import os.path
from typing import Optional, Any

from .. import PopTrackerType
from ..json.encoder import PopTrackerJsonEncoder


class PopTrackerMapLocation(PopTrackerType):
    def __init__(self, _map: str, x: int, y: int, size=None, border_thickness=None, restrict_visibility_rules=None,
                 force_invisibility_rules=None):
        if restrict_visibility_rules is None:
            restrict_visibility_rules = []
        if force_invisibility_rules is None:
            force_invisibility_rules = []
        self.map: str = _map
        self.x: int = x
        self.y: int = y
        self.size: Optional[int] = size
        self.border_thickness: Optional[int] = border_thickness
        self.restrict_visibility_rules: list[list[str]] = restrict_visibility_rules
        self.force_invisibility_rules: list[list[str]] = force_invisibility_rules


class PopTrackerSection(PopTrackerType):
    def __init__(self, name, clear_as_group=False, item_count=1, chest_opened_img=None, chest_unopened_img=None,
                 hosted_item=None, access_rules=None, visibility_rules=None, ref=None):
        if access_rules is None:
            access_rules = []
        if visibility_rules is None:
            visibility_rules = []
        self.name: str = name
        self.clear_as_group: bool = clear_as_group
        self.chest_opened_img: Optional[str] = chest_opened_img
        self.chest_unopened_img: Optional[str] = chest_unopened_img
        self.item_count: int = item_count
        self.hosted_item: Optional[str] = hosted_item
        self.access_rules: list[list[str]] = access_rules
        self.visibility_rules: list[list[str]] = visibility_rules
        self.ref: Optional[str] = ref


class PopTrackerLocation(PopTrackerType):
    def __init__(self, name, short_name=None, access_rules=None, visibility_rules=None, chest_unopened_img=None,
                 chest_opened_img=None, overlay_background=None, color=None, parent=None, children=None,
                 map_locations=None, sections=None):
        if visibility_rules is None:
            visibility_rules = []
        if access_rules is None:
            access_rules = []
        if children is None:
            children = []
        if map_locations is None:
            map_locations = []
        if sections is None:
            sections = []
        self.name: str = name
        self.short_name: Optional[str] = short_name
        self.access_rules: list[list[str]] = access_rules
        self.visibility_rules: list[list[str]] = visibility_rules
        self.chest_unopened_img: Optional[str] = chest_unopened_img
        self.chest_opened_img: Optional[str] = chest_opened_img
        self.overlay_background: Optional[str] = overlay_background
        self.color: Optional[str] = color
        self.parent: Optional[str] = parent
        self.children: list[PopTrackerLocation] = children
        self.map_locations: list[PopTrackerMapLocation] = map_locations
        self.sections: list[PopTrackerSection] = sections


def export_locations(locations=list[PopTrackerLocation], out_path: Optional[str] = None, indent=2):
    if out_path is None:
        out_path = os.path.join('locations', 'locations.json')
    with open(out_path, mode='w') as f:
        json.dump(locations, f, indent=indent, cls=PopTrackerJsonEncoder)
