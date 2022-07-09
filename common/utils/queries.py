import re

def pretty_sql(queryset):
    query = str(queryset.query)
    query = query.replace('"', '')
    table_name = re.search('SELECT (\w+)\.', query).group(1) 
    query = query.replace(f'{table_name}.', '')
    sql_clauses = ['FROM', 'WHERE', 'ORDER BY', 'LIMIT', 'GROUP BY']
    for clause in sql_clauses:
        query = query.replace(clause, '\n' + clause)
    print(query)