class DataBaseConfig:
    url: str = "postgresql+psycopg2://postgres:Vovka_2018@localhost:5432/olx"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


database_config = DataBaseConfig()
