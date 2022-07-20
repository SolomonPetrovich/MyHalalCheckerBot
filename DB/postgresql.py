import asyncpg
from asyncpg import Pool

from Config import db_config


class PostgreSQL:
    def __init__(self, pool):
        self.pool: Pool = pool

    @classmethod
    async def create(cls):
        pool = await asyncpg.create_pool(
            user=db_config.PGUSER,
            password=db_config.PGPASSWORD,
            database=db_config.PGDATABASE,
            host=db_config.PGHOST,
            port=db_config.PGPORT
        )
        return cls(pool)

    async def sql_get_result(self):
        sql = 'SELECT status FROM e_products'
        await self.pool.execute(sql)
