import sqlite3
con = sqlite3.connect("./instance/samp.sqlite3")

cur = con.cursor()
# res = cur.execute("SELECT * FROM user")
for row in cur.execute("SELECT * FROM user"):
    print(row)


# cur.execute("ALTER TABLE  user ADD Email")
cur.execute("ALTER TABLE  user ADD cat_name")
con.commit()
# ALTER TABLE Customers
# ADD Email varchar(255);

# class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(100), nullable=False)
    # catName = db.Column(db.String(100))  # Add catName column
    # email = db.Column(db.String(100))    # Add email column
    # password = db.Column(db.String(100), nullable=False)
    # role = db.Column(db.String(100), nullable=False)
