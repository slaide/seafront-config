import typing as tp
from datetime import datetime, timezone

from pydantic import BaseModel


def datetime2str(dt: datetime) -> str:
    """
    return datetime, formatted as str

    also converts the timezone to utc
    """

    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


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
            f"{self.value = } ; {type(self.value) = }!=str"
        )
        return self.value

    @property
    def intvalue(self) -> int:
        assert isinstance(self.value, int), (
            f"{self.value = } ; {type(self.value) = }!=int"
        )
        return self.value

    @property
    def floatvalue(self) -> float:
        assert isinstance(self.value, float), (
            f"{self.value = } ; {type(self.value) = }!=float"
        )
        return self.value

    @property
    def boolvalue(self) -> bool:
        # from ConfigItemOption.get_bool_options()
        assert isinstance(self.value, str), (
            f"{self.value = } ; {type(self.value) = }!=bool"
        )
        return self.value == "yes"

    def override(self, other: "ConfigItem"):
        """
        update value from other item
        """
        assert self.handle == other.handle, f"{self.handle = } != {other.handle = }"
        assert self.value_kind == other.value_kind, f"{self.value_kind = } != {other.value_kind = }"
        self.value = other.value
