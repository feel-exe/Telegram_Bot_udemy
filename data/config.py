from environs import Env

env = Env()

env.read_env()

# admins = env.str("ADMINS")
# айдишник разработчиков по умолчанию. добавление новых админов выполняется отдельно
admins = [307136400]


BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str("ip")

DB_USER = env.str("PG_USER")
DB_PASS = env.str("PG_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")


DT_BASE = env.str("DATABASE")

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{IP}/{DT_BASE}"

banned_users = [26516516516, 1651, 651651]

allowed_users = [
    307136400
]
