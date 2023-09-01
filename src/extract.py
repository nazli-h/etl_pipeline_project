

import psycopg2
import pandas as pd

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


# new
def extract_transactional_data(dbname, host, port, user, password):
    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)
    # query
    query = """
            select ot.customer_id,
                   ot.invoice,
                   ot.stock_code,
                   /* this is code to replace the missing value in description with unknown*/
                   case when sd.description is null then 'Unknown'
                        else sd.description end as description,
                   /* this code to fix the invoice_date's data type*/
                   ot.price,
                   ot.quantity,
                   cast(ot.invoice_date as datetime) as invoice_date,
                   ot.country,
                   ot.price * ot.quantity as total_order_value
            from bootcamp.online_transactions ot
            left join ( select *
                        from bootcamp.stock_description
                        where description <> '?') sd on ot.stock_code = sd.stock_code
            where ot.customer_id <> ''
              and ot.stock_code not in ('BANK CHARGES', 'POST', 'D','M','CRUK')
            """
    online_trans_cleaned = pd.read_sql(query, connect)
    print("The shape of my data is:", online_trans_cleaned.shape)
    return online_trans_cleaned
