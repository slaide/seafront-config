import typing as tp
import dataclasses as dc
from dataclasses import dataclass

@dataclass
class ConfigItemOption:
    name:str
    handle:str
    info:tp.Optional[tp.Any]=None

    def to_dict(self)->dict:
        return dc.asdict(self)
    
    @staticmethod
    def get_bool_options()->tp.List["ConfigItemOption"]:
        return [
            ConfigItemOption(
                name="Yes",
                handle="yes",
            ),
            ConfigItemOption(
                name="No",
                handle="no",
            ),
        ]

@dataclass
class ConfigItem:
    name:str
    handle:str
    value_kind:tp.Literal["number","text","option","action"]
    value:tp.Union[int,float,str]
    frozen:bool=False
    options:tp.Optional[tp.List[ConfigItemOption]]=None

    def __post_init__(self):
        if self.options is not None:
            self.options=[o if type(o) == ConfigItemOption else ConfigItemOption(**o) for o in self.options] # type: ignore

    @property
    def intvalue(self)->int:
        assert isinstance(self.value,int), f"{self.value = } ; {type(self.value) = }!=int"
        return self.value

    @property
    def floatvalue(self)->float:
        if isinstance(self.value,int):
            self.value=float(self.value)
        assert isinstance(self.value,float), f"{self.value = } ; {type(self.value) = }!=float"
        return self.value
    
    @property
    def boolvalue(self)->bool:
        # from ConfigItemOption.get_bool_options()
        assert isinstance(self.value,str), f"{self.value = } ; {type(self.value) = }!=bool"
        return self.value=="yes"

    def override(self,other:"ConfigItem"):
        """
            update value from other item
        """
        assert self.handle==other.handle, f"{self.handle = } != {other.handle = }"
        match self.value_kind:
            case "number":
                if isinstance(self.value,int):
                    self.value=int(other.value)
                else:
                    self.value=float(other.value)
            case _:
                self.value=other.value

    def to_dict(self)->dict:
        ret=dc.asdict(self)
        if self.options is not None:
            ret['options']=[o.to_dict() for o in self.options]
        return ret