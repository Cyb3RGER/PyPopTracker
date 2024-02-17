import json
import os
from typing import Optional, Any

from .. import PopTrackerType
from ..json.encoder import PopTrackerJsonEncoder


class PopTrackerItem(PopTrackerType):
    def __init__(self, name, type, codes=None, capturable=None):
        self.name: str = name
        self.type: str = type
        self.codes: Optional[str] = codes
        self.capturable: Optional[bool] = capturable


class PopTrackerStaticItem(PopTrackerItem):
    def __init__(self, name, codes, capturable=None, img=None, img_mods=None):
        super().__init__(name, "static", codes, capturable)
        self.img: Optional[str] = img
        self.img_mods: Optional[str] = img_mods


class PopTrackerToggleItem(PopTrackerItem):
    def __init__(self, name, codes, capturable=None, img=None, img_mods=None, disabled_img=None,
                 disabled_img_mods=None, initial_active_state=None):
        super().__init__(name, "toggle", codes, capturable)
        self.img: Optional[str] = img
        self.img_mods: Optional[str] = img_mods
        self.disabled_img: Optional[str] = disabled_img
        self.disabled_img_mods: Optional[str] = disabled_img_mods
        self.initial_active_state: Optional[bool] = initial_active_state


class PopTrackerConsumableItem(PopTrackerItem):
    def __init__(self, name, codes, capturable=None, img=None, img_mods=None, disabled_img=None,
                 disabled_img_mods=None, min_quantity=None, max_quantity=None, increment=None, decrement=None,
                 initial_quantity=None, overlay_background=None, overlay_font_size=None):
        super().__init__(name, "consumable", codes, capturable)
        self.img: Optional[str] = img
        self.img_mods: Optional[str] = img_mods
        self.disabled_img: Optional[str] = disabled_img
        self.disabled_img_mods: Optional[str] = disabled_img_mods
        self.min_quantity: Optional[int] = min_quantity
        self.max_quantity: Optional[int] = max_quantity
        self.increment: Optional[int] = increment
        self.decrement: Optional[int] = decrement
        self.initial_quantity: Optional[int] = initial_quantity
        self.overlay_background: Optional[str] = overlay_background
        self.overlay_font_size: Optional[str] = overlay_font_size


class PopTrackerToggleBadgedItem(PopTrackerItem):
    def __init__(self, name, codes, base_item, capturable=None, img=None, img_mods=None, disabled_img=None,
                 disabled_img_mods=None, initial_active_state=None):
        super().__init__(name, "toggle_badged", codes, capturable)
        self.img: Optional[str] = img
        self.img_mods: Optional[str] = img_mods
        self.disabled_img: Optional[str] = disabled_img
        self.disabled_img_mods: Optional[str] = disabled_img_mods
        self.base_item: str = base_item
        self.initial_active_state: Optional[bool] = initial_active_state


class PopTrackerCompositeImage:
    def __init__(self, left, right, codes, img=None, img_mods=None, disabled_img=None, disabled_img_mods=None):
        self.left: bool = left
        self.right: bool = right
        self.img: Optional[str] = img
        self.img_mods: Optional[str] = img_mods
        self.disabled_img: Optional[str] = disabled_img
        self.disabled_img_mods: Optional[str] = disabled_img_mods
        self.codes: list[str] = codes


class PopTrackerCompositeToggleItem(PopTrackerItem):
    def __init__(self, name, codes, capturable=None, images=None, item_left=None, item_right=None, img_mods=None,
                 disabled_img=None, disabled_img_mods=None, initial_active_state=None):
        super().__init__(name, "composite_toggle", codes, capturable)
        assert images is not None or (item_left is not None and item_right is not None), \
            "A composite_toggle item needs either images or item_left and item_right set"
        self.images: Optional[list[PopTrackerCompositeImage]] = images
        self.item_left: Optional[str] = item_left
        self.item_right: Optional[str] = item_right
        self.img_mods: Optional[str] = img_mods
        self.disabled_img: Optional[str] = disabled_img
        self.disabled_img_mods: Optional[str] = disabled_img_mods


class PopTrackerItemStage:
    def __init__(self, name, codes, secondary_codes=None, inherit_codes=None, img=None, img_mods=None,
                 disabled_img=None, disabled_img_mods=None):
        self.name: str = name
        self.codes: str = codes
        self.secondary_codes: Optional[str] = secondary_codes
        self.inherit_codes: Optional[bool] = inherit_codes
        self.img: Optional[str] = img
        self.img_mods: Optional[str] = img_mods
        self.disabled_img: Optional[str] = disabled_img
        self.disabled_img_mods: Optional[str] = disabled_img_mods


class PopTrackerProgressiveItem(PopTrackerItem):
    def __init__(self, name, codes, stages, capturable=None, allow_disabled=None, initial_stage_idx=None, loop=None):
        super().__init__(name, "progressive", codes, capturable)
        self.stages: list[PopTrackerItemStage] = stages
        self.allow_disabled: Optional[bool] = allow_disabled
        self.initial_stage_idx: Optional[int] = initial_stage_idx
        self.loop: Optional[bool] = loop


class PopTrackerProgressiveToggleItem(PopTrackerItem):
    def __init__(self, name, codes, stages, capturable=None, initial_stage_idx=None, loop=None):
        super().__init__(name, "progressive_toggle", codes, capturable)
        self.stages: list[PopTrackerItemStage] = stages
        self.initial_stage_idx: Optional[int] = initial_stage_idx
        self.loop: Optional[bool] = loop


def export_items(locations=list[PopTrackerItem], out_path: Optional[str] = None, indent=2):
    if out_path is None:
        out_path = os.path.join('locations', 'locations.json')
    with open(out_path, mode='w') as f:
        json.dump(locations, f, indent=indent, cls=PopTrackerJsonEncoder)
