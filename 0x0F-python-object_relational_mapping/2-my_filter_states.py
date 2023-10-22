#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import argparse

def main():
    parser = argparse.ArgumentParser(description="List states from the database hbtn_0e_0_usa")
    parser.add_argument("user", help="MySQL username")
    parser.add_argument("password", help="MySQL password")
    parser.add_argument("database", help="MySQL database name")
    parser.add_argument("state_name", help="State name to search for")
    
    args = parser.parse_args()

    db = MySQLdb.connect(host="localhost", user=args.user,
                         passwd=args.password, db=args.database, port=3306)
    cur = db.cursor()
    
    state_name = args.state_name
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (state_name,))
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
