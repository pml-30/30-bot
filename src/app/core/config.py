from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, PostgresDsn, SecretStr, RedisDsn, AmqpDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Bot(BaseModel):
    token: SecretStr


class PostgreSQL(BaseModel):
    dsn: PostgresDsn


class Redis(BaseModel):
    dsn: RedisDsn


class RabbitMQ(BaseModel):
    dsn: AmqpDsn


class Convertio(BaseModel):
    key: SecretStr


class ApplicationSettings(BaseSettings):
    bot: Bot
    postgres: PostgreSQL
    convertio: Convertio
    redis: Redis
    rabbitmq: RabbitMQ

    project_dir: ClassVar[Path] = Path(__file__).parent.parent.parent.parent.resolve()

    model_config = SettingsConfigDict(env_file=project_dir / ".env", env_nested_delimiter="_")
