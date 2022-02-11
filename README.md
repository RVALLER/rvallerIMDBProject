NAME: RYAN VALLER


INSTALL INSTR: This iteration of read me for sprint 2 requires you pull my updated project and have the following files:
all files therein the tests folder. Test_sprint2.py especially integral for tests. Furthermore, make sure all dependancies are
installed. (see requirements.txt). Also, output.csv may be required (might not be) for first half of db. nothing to be manipulated,
just needs to be pulled along with project directory. From there: open database_stuff.py -> run. It *should* exit code 0 and write the tables
and all necessary api data to the database. IF IT DOES NOT: open the db and wipe data to assure a smooth repopulation :)


DESCRIPTION: This program builds upon the first sprint that scrapes the data from imDB's API website. The
data included is: top 250 shows, ratings data for the wheel of time, and top 1,50,150,200.
from that initial data scrape, implements various methods including sqlite3, output.csv, test modules, pandas, and requests
to neatly output the api data into the database as instructed. It also uses a dictionary flattener to more easily output the
ratings data into their own unique table in movie_api.db.


MISSING FEATURES: Hopefully no features were skipped for sprint 2 and everything (at least on my machine!) builds a-ok.

