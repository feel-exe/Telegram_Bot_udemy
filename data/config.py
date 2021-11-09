from environs import Env

env = Env()

env.read_env()

admins = env.str("ADMINS")
BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str("ip")

DB_USER = env.str("PG_USER")
DB_PASS = env.str("PG_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")


DT_BASE = env.str("DATABASE")

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{IP}/{DT_BASE}"

# ____________________
# import os
#
# from dotenv import load_dotenv
#
# load_dotenv()
#
# BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
#
# admins = [
#     307136400
# ]
#
# PG_USER = str(os.getenv("PGU_SER"))
# PG_PASS = str(os.getenv("PG_PASS"))
# DB_NAME = str(os.getenv("DB_NAME"))
# DB_HOST = str(os.getenv("DB_HOST"))

# ____________________
#
# ip = os.getenv("ip")
#
# db_host = ip  # Если вы запускаете базу не через докер!
# # db_host = "db"  # Если вы запускаете базу через докер и у вас в services стоит название базы db
#
# aiogram_redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }
#
#
# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"
banned_users = [26516516516, 1651, 651651]
