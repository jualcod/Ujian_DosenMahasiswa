import pymongo; import pandas as pd;    import matplotlib.pyplot as plt
from pymongo import MongoClient

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]

def read_mongo_dos(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    # Make a query to the specific DB and Collection
    cursor = db['Dosen'].find(query)
    # Expand the cursor and construct the DataFrame
    df_dos =  pd.DataFrame(list(cursor))
    return df_dos
def read_mongo_mah(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    # Make a query to the specific DB and Collection
    cursor = db['Mahasiswa'].find(query)
    # Expand the cursor and construct the DataFrame
    df_mah =  pd.DataFrame(list(cursor))
    return df_mah
# read_mongo_dos('Kampus', 'Dosen')
# read_mongo_mah('Kampus', 'Mahasiswa')
df1_dos = read_mongo_dos('Kampus', 'Dosen')
df2_mah = read_mongo_mah('Kampus', 'Mahasiswa')
# print(df1_dos);   print(df2_mah)

status_dos = ['dosen', 'dosen', 'dosen']
status_mah = ['mahasiswa', 'mahasiswa', 'mahasiswa']
df1_dos_new = df1_dos[['asal', 'nama', 'usia']]
df2_mah_new = df2_mah[['asal', 'nama', 'usia']]
df1_dos_new.insert(loc=2, column='status', value=status_dos)
df2_mah_new.insert(loc=2, column='status', value=status_mah)
print(df1_dos_new); print(df2_mah_new)      # Print answer

# Create Usia Graph

plt.bar(df1_dos.nama.tolist(), df1_dos.usia.tolist())
plt.bar(df2_mah.nama.tolist(), df2_mah.usia.tolist())
plt.title('Usia Warga Kampus')
plt.legend(['Dosen', 'Mahasiswa'])
plt.grid()
plt.show()