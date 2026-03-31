# Lab 10 - Create functions to automate our query execution and fetching

# Prepare and execute the query
def query_executor(cursor, query_name):
    print("---")
    print(f"Query: {query_name}")

    # The execute method runs the query
    cursor.execute(query_name)
    return cursor


# Fetch from a pre-executed query
def query_responder(cursor, fetch_type, fetch_amount=3):
    all_rows = []

    # Fetch all rows
    if fetch_type == "fetchall":
        all_rows = cursor.fetchall()
        for row in all_rows:
            print(row)

    # Fetch one row
    elif fetch_type == "fetchone":
        all_rows = cursor.fetchone()
        print(all_rows)

    # Fetch many rows
    elif fetch_type == "fetchmany":
        all_rows = cursor.fetchmany(fetch_amount)
        for row in all_rows:
            print(row)

    else:
        print("Invalid fetch type")

    return all_rows