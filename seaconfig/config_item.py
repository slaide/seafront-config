import typing as tp
from datetime import datetime, timezone

from pydantic import BaseModel


def datetime2str(dt: datetime) -> str:
    """
    return datetime, formatted as str

    also converts the timezone to utc
    """

    # Convert to UTC and format as YYYY-MM-DD_HH.MM.SS
    utc_dt = dt.astimezone(timezone.utc)
    return utc_dt.strftime("%Y-%m-%d_%H.%M.%S")


class ConfigItemOption(BaseModel):
    name: str
    handle: str
    info: tp.Optional[tp.Any] = None

    @staticmethod
    def get_bool_options() -> tp.List["ConfigItemOption"]:
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


class ConfigItem(BaseModel):
    name: str
    handle: str
    value_kind: tp.Literal["int", "float", "text", "option", "action"]
    value: tp.Union[int, float, str]
    frozen: bool = False
    options: tp.Optional[tp.List[ConfigItemOption]] = None

    @property
    def strvalue(self) -> str:
        assert isinstance(self.value, str), (
            f"{self.value = } ; on ${self.handle} {type(self.value) = }!=str"
        )
        return self.value

    @property
    def intvalue(self) -> int:
        assert self.value_kind=="int" and isinstance(self.value, int), (
            f"{self.value = } ; on ${self.handle} {self.value_kind}!='int' or {type(self.value) = }!=int"
        )
        return self.value

    @property
    def floatvalue(self) -> float:
        if isinstance(self.value, int) and self.value_kind=="float":
            self.value=float(self.value)

        assert self.value_kind=="float" and isinstance(self.value, float), (
            f"{self.value = } ; on ${self.handle} {self.value_kind}!='float' or {type(self.value) = }!=float"
        )
        return self.value

    @property
    def boolvalue(self) -> bool:
        # from ConfigItemOption.get_bool_options()
        assert isinstance(self.value, str), (
            f"{self.value = } ; on ${self.handle} {type(self.value) = }!=bool"
        )
        return self.value == "yes"

    def override(self, other: "ConfigItem"):
        """
        update value from other item
        """
        assert self.handle == other.handle, f"on ${self.handle} {self.handle = } != {other.handle = }"
        assert self.value_kind == other.value_kind, f"on ${self.handle} {self.value_kind = } != {other.value_kind = }"
        self.value = other.value
