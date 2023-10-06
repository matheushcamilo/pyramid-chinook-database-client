import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from .models import (
    Customer,
    Base,
    DBSession,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    # Load and execute the SQL script
    try:
        sql_script_path = os.path.join(os.path.dirname(__file__), 'Chinook_Sqlite.sql')
        with open(sql_script_path, 'r') as sql_file:
            sql_script = sql_file.read()

        with engine.connect() as connection:
            connection.execute(sql_script)

        DBSession.commit()
    except Exception as e:
        print(f"Error loading SQL script: {e}")
