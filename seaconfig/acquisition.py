import typing as tp
from .config_item import ConfigItem
from .wellplates import Wellplate
from pydantic import BaseModel, Field

class AcquisitionWellSiteConfigurationDeltaTime(BaseModel):
    "delta time struct with hour,minute and second components. used for delta t spec in "
    h:float=Field(...,title="Hours")
    "hour component of the delta time"
    m:float=Field(...)
    s:float=Field(...)

class AcquisitionWellSiteConfigurationSiteSelectionItem(BaseModel):
    """
    indicate if this item in the AcquisitionWellSiteConfiguration site grid should be imaged or not
    """
    row:int
    col:int
    selected:bool

class AcquisitionWellSiteConfiguration(BaseModel):
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

        num_t:int - number of time points
        delta_t:AcquisitionWellSiteConfigurationDeltaTime - time between time points

        mask:tp.List[AcquisitionWellSiteConfigurationSiteSelectionItem] - mask of sites to acquire. If cell.selected is True, then site (cell.row,cell.col) will be acquired.

    """

    num_x:int
    delta_x_mm:float
    num_y:int
    delta_y_mm:float
    num_t:int
    delta_t:AcquisitionWellSiteConfigurationDeltaTime

    mask:tp.List[AcquisitionWellSiteConfigurationSiteSelectionItem]
    
class AcquisitionChannelConfig(BaseModel):
    name:str
    handle:str

    illum_perc:float
    exposure_time_ms:float
    analog_gain:float

    z_offset_um:float

    num_z_planes:int
    delta_z_um:float
    
    enabled:bool=True

class PlateWellConfig(BaseModel):
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

class Version(BaseModel):
    "semantic version number (see https://semver.org/ for details)"
    major:int
    minor:int
    patch:int

    def smaller_than(self,other:"Version")->bool:
        if self.major<other.major: return True
        if self.major>other.major: return False

        if self.minor<other.minor: return True
        if self.minor>other.minor: return False

        if self.patch<other.patch: return True
        if self.patch>other.patch: return False

        return False

LATEST_SPEC_VERSION=Version(major=5,minor=0,patch=3)

class AcquisitionConfig(BaseModel):
    project_name:str
    plate_name:str
    cell_line:str
    
    grid:AcquisitionWellSiteConfiguration

    wellplate_type:Wellplate
    plate_wells:tp.List[PlateWellConfig]

    channels:tp.List[AcquisitionChannelConfig]

    autofocus_enabled:bool

    machine_config:tp.Optional[tp.List[ConfigItem]]=None

    comment:tp.Optional[str]=None
    " arbitrary text comment embedded in the config file. may be used to communicate of intented context of use of the protocol (or any other purpose). "

    spec_version:Version=Field(default_factory=lambda:LATEST_SPEC_VERSION)
    " version of the sdatetimepecification that was used to create the protocol file. "

    timestamp:tp.Optional[str]=None
    " creation timestamp of this protocol in utc "
