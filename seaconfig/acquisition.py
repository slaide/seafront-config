import json
import typing as tp
from dataclasses import dataclass
import dataclasses as dc
from .config_item import ConfigItem
from datetime import datetime

@dataclass
class AcquisitionWellSiteConfigurationDeltaTime:
    h:float
    m:float
    s:float

    def __post_init__(self):
        self.h=int(self.h)
        self.m=int(self.m)
        self.s=int(self.s)

    def to_dict(self)->dict:
        return dc.asdict(self)

@dataclass
class AcquisitionWellSiteConfigurationSiteSelectionItem:
    row:int
    col:int
    plane:int
    selected:bool

    def __post_init__(self):
        self.row=int(self.row)
        self.col=int(self.col)
        self.plane=int(self.plane)

@dataclass
class AcquisitionWellSiteConfiguration:
    """
    all config related to well site acquisition

    Note:
        - What is a well site?
            Each well can be imaged at different positions within it. Each position where we take a set of images
            (set here means one image per channel), is a [well] site. A regular configuration is to take 9 images
            per well, i.e. 9 sites. These sites are configured in a grid, with 3 x coordinates, and 3 y coordinates,
            for a total of 3x3=9 pairs of x and y coordinates, hence 9 sites.
    
    Fields:
        num_x:int - number of x coordinates
        delta_x_mm:float - distance between x coordinates
        num_y:int - number of y coordinates
        delta_y_mm:float - distance between y coordinates
        num_z:int - number of z coordinates
        delta_z_um:float - distance between z coordinates

        num_t:int - number of time points
        delta_t:AcquisitionWellSiteConfigurationDeltaTime - time between time points

        mask:tp.List[AcquisitionWellSiteConfigurationSiteSelectionItem] - mask of sites to acquire. If cell.selected is True, then site (cell.row,cell.col) will be acquired.

    """

    num_x:int
    delta_x_mm:float
    num_y:int
    delta_y_mm:float
    num_z:int
    delta_z_um:float
    num_t:int
    delta_t:AcquisitionWellSiteConfigurationDeltaTime

    mask:tp.List[AcquisitionWellSiteConfigurationSiteSelectionItem]

    def __post_init__(self):
        self.num_x=int(self.num_x)
        self.delta_x_mm=float(self.delta_x_mm)
        self.num_y=int(self.num_y)
        self.delta_y_mm=float(self.delta_y_mm)
        self.num_z=int(self.num_z)
        self.delta_z_um=float(self.delta_z_um)
        self.num_t=int(self.num_t)

        self.delta_t = AcquisitionWellSiteConfigurationDeltaTime(**self.delta_t) # type: ignore
        self.mask = [AcquisitionWellSiteConfigurationSiteSelectionItem(**d) for d in self.mask] # type: ignore

    def to_dict(self)->dict:
        return dc.asdict(self)
    
@dataclass
class AcquisitionChannelConfig:
    name:str
    handle:str
    illum_perc:float
    exposure_time_ms:float
    analog_gain:float
    z_offset_um:float
    
    enabled:bool=True

    def __post_init__(self):
        self.illum_perc=float(self.illum_perc)
        self.exposure_time_ms=float(self.exposure_time_ms)
        self.analog_gain=float(self.analog_gain)
        self.z_offset_um=float(self.z_offset_um)

    def to_dict(self)->dict:
        return dc.asdict(self)

@dataclass
class PlateWellConfig:
    """
    acquisition configuration for a well on a plate

    Fields:
        row:int - row index on plate, starting at 0
        col:int - column index on plate, starting at 0
        selected:bool - indicates if this well should be imaged
    """

    row:int
    col:int
    selected:bool

    @property
    def well_name(self)->str:
        return f"{chr(ord('A')+self.row)}{self.col+1}"
    
    def to_dict(self)->dict:
        return dc.asdict(self)

@dataclass
class Version:
    "semantic version number (see https://semver.org/ for details)"
    major:int
    minor:int
    patch:int
    
    def to_dict(self)->dict:
        return dc.asdict(self)

LATEST_SPEC_VERSION=Version(1,0,0)

def _ensure_type(v,T,convert_v_to_T:tp.Callable|None=None):
    """
    if v is of type T, returns v.
    otherwise [assume v is a dict] returns T(**v)
    """
    if isinstance(v,T):
        return v

    if convert_v_to_T is not None:
        return convert_v_to_T(v)

    return T(**v)

@dataclass
class AcquisitionConfig:
    project_name:str
    plate_name:str
    cell_line:str
    
    grid:AcquisitionWellSiteConfiguration

    wellplate_type:str
    plate_wells:tp.List[PlateWellConfig]

    channels:tp.List[AcquisitionChannelConfig]

    autofocus_enabled:bool

    machine_config:tp.Optional[tp.List[ConfigItem]]=None

    comment:tp.Optional[str]=None
    " arbitrary text comment embedded in the config file. may be used to communicate of intented context of use of the protocol (or any other purpose). "

    spec_version:Version=LATEST_SPEC_VERSION
    " version of the sdatetimepecification that was used to create the protocol file. "

    timestamp:tp.Optional[datetime]=None
    " creation timestamp of this protocol in utc "

    def to_dict(self)->dict:
        ret=dc.asdict(self)
        if self.timestamp is not None:
            ret["timestamp"]=self.timestamp.isoformat(timespec="seconds")
        return ret
    
    def __post_init__(self):
        self.grid = _ensure_type(self.grid,AcquisitionWellSiteConfiguration)
        self.plate_wells = [_ensure_type(d,PlateWellConfig) for d in self.plate_wells]
        self.channels = [_ensure_type(d,AcquisitionChannelConfig) for d in self.channels]
        if self.machine_config is not None:
            self.machine_config=[_ensure_type(c,ConfigItem) for c in self.machine_config]

        self.spec_version=_ensure_type(self.spec_version, Version)
        if self.timestamp is not None:
            self.timestamp=_ensure_type(self.timestamp, datetime, datetime.fromisoformat)

    @staticmethod
    def from_json(s:tp.Union[str,dict])->"AcquisitionConfig":
        if isinstance(s,dict):
            d = s
        else:
            d = json.loads(s)
        return AcquisitionConfig(**d)
