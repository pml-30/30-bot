from pydantic import BaseModel, SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import ClassVar


class BotModel(BaseModel):
    token: SecretStr


class DatabaseModel(BaseModel):
    dsn: PostgresDsn


class ApplicationSettings(BaseSettings):
    bot: BotModel
    database: DatabaseModel

    project_dir: ClassVar[Path] = Path(__file__).parent.parent.parent.parent.resolve()

    model_config = SettingsConfigDict(env_file=project_dir / ".env", env_nested_delimiter="_")
