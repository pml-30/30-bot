from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotModel(BaseModel):
    token: SecretStr


class DatabaseModel(BaseModel):
    dsn: PostgresDsn


class ConvertioModel(BaseModel):
    key: SecretStr


class ApplicationSettings(BaseSettings):
    bot: BotModel
    database: DatabaseModel
    convertio: ConvertioModel

    project_dir: ClassVar[Path] = Path(__file__).parent.parent.parent.parent.resolve()

    model_config = SettingsConfigDict(env_file=project_dir / ".env", env_nested_delimiter="_")
