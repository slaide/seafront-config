import json
import typing as tp
from dataclasses import dataclass
import dataclasses as dc

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
class AcquisitionWellSiteConfiguration:
    num_x:int
    delta_x:float
    num_y:int
    delta_y:float
    num_z:int
    delta_z:float
    num_t:int
    delta_t:AcquisitionWellSiteConfigurationDeltaTime

    def __post_init__(self):
        self.num_x=int(self.num_x)
        self.delta_x=float(self.delta_x)
        self.num_y=int(self.num_y)
        self.delta_y=float(self.delta_y)
        self.num_z=int(self.num_z)
        self.delta_z=float(self.delta_z)
        self.num_t=int(self.num_t)

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

    def __post_init__(self):
        self.illum_perc=float(self.illum_perc)
        self.exposure_time_ms=float(self.exposure_time_ms)
        self.analog_gain=float(self.analog_gain)
        self.z_offset_um=float(self.z_offset_um)

    def to_dict(self)->dict:
        return dc.asdict(self)

@dataclass
class AcquisitionConfig:
    project_name:str
    plate_name:str
    cell_line:str
    
    grid:AcquisitionWellSiteConfiguration

    wellplate_type:str

    channels:tp.List[AcquisitionChannelConfig]

    def to_dict(self)->dict:
        return dc.asdict(self)

    @staticmethod
    def from_json(s:tp.Union[str,dict])->"AcquisitionConfig":
        if isinstance(s,dict):
            d = s
        else:
            d = json.loads(s)
        return AcquisitionConfig(**d)
