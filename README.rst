######
30-bot
######

Запуск
======

.. code-block:: shell

    git clone https://github.com/pml-30/30-bot.git && cd 30-bot
    poetry install

.. code-block:: shell

    export BOT_TOKEN=<your_bot_token>
    export DATABASE_DSN=<your_database_dsn>
    export CONVERTIO_KEY=<your_convertio_key
    export REDIS_DSN=<your_redis_dsn
    export BROKER_DSN=<your_broker_dsn>

Технологии
==========

* **Python 3.11** - язык программирования
* **PostgreSQL 15.4** - СУБД
* **RabbitMQ** - брокер сообщений & очередь
* **Redis** - вспомогательная СУБД
* **Docker** - контейнеризация
* **Kubernetes** - оркестровка Docker
