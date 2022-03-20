from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import url as sa_url
import pandas as pd
import logging 

# Script to import sheet for table 'historico' in Postgresql database.

log = logging.getLogger(__name__)

# Create the params for URL.
url = sa_url.URL(drivername='postgresql+psycopg2',
                username='postgres',
                password='postgres',
                host='localhost',
                port=5432,
                database='servicemetric')

# Create a connection using URL.
engine = create_engine(url)
log.info('Conect into the database.')
file_name = r'C:\Users\Camila\ServiceMetric\Reports\export_table_helpdesk.xlsx'
file_name = Path(file_name)

with open(file_name, 'rb') as handle:
    df = pd.read_excel(handle)
    print(df)

# Create a table historico using excel sheet.
df.to_sql('historico', con=engine, schema="servicemetric")





