# import os
# from pathlib import Path
# import logging
# from sqlmodel import create_engine, Session, SQLModel
# from dotenv import load_dotenv
# from sqlalchemy.exc import OperationalError

# # This finds the directory of database.py, goes up one level to 'indygx', and looks for .env
# env_path = Path(__file__).resolve().parent.parent / '.env'
# load_dotenv(dotenv_path=env_path, override=True)

# logger = logging.getLogger(__name__)

# DATABASE_URL = os.getenv("DATABASE_URL")
# default_db = Path(__file__).resolve().parent.parent / "dev.db"
# # sqlite_url = f"sqlite:///{default_db.as_posix()}

# # If DATABASE_URL is not set, use SQLite
# if not DATABASE_URL:
#     # DATABASE_URL = sqlite_url
#     logger.warning(
#         "DATABASE_URL not set; using SQLite database at %s",
#         default_db,
#     )
# else:
#     # Try to connect to the remote database, fall back to SQLite if it fails
#     try:
#         test_engine = create_engine(DATABASE_URL, pool_pre_ping=True)
#         with test_engine.connect() as conn:
#             pass  # Connection successful
#         logger.info("Connected to remote database: %s", DATABASE_URL.split('@')[-1] if '@' in DATABASE_URL else DATABASE_URL)
#     except (OperationalError, Exception) as e:
#         logger.warning(
#             "Failed to connect to remote database: %s. Falling back to SQLite database at %s",
#             str(e),
#             default_db,
#         )
#         # DATABASE_URL = sqlite_url

# engine = create_engine(
#     DATABASE_URL,
#     echo=True,
#     pool_pre_ping=True,
# )



# def get_session():
#     return Session(engine)




import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

def get_session():
    return Session(engine)


 
 