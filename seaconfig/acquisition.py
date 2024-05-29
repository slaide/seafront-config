import json
import typing as tp
from dataclasses import dataclass
import dataclasses as dc

@dataclass
class AcquisitionWellSiteConfigurationDeltaTime:
    h:float
    m:float
    s:float

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
