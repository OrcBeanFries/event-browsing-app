import sqlite3

sqliteConnection = sqlite3.connect("EventPlannerDB.db")
cursor = sqliteConnection.cursor()

sql_command = """CREATE TABLE accounts (
accountID INTEGER PRIMARY KEY, 
accountType TEXT CHECK(creatorType IN ('Student','Faculty')),
username TEXT UNIQUE,
password TEXT NOT NULL, 
recoveryEmail TEXT NOT NULL
);

CREATE TABLE RSVPed_Events (
rsvpID INTEGER UNIQUE,
EventID INTEGER,
creatorID INTEGER,
userWhoRSVPID INTEGER,

FOREIGN KEY (eventID) REFERENCES events(eventID),
FOREIGN KEY (creatorID) REFERENCES events(accountID),
FOREIGN KEY (userWhoRSVPID) REFERENCES accounts(accountID)
);


CREATE TABLE events (
eventID INTEGER PRIMARY KEY,     
creatorID INTEGER,
creatorType TEXT CHECK(creatorType IN ('Student','Faculty')),
eventName TEXT NOT NULL, 
eventDescription TEXT NOT NULL,         
images BLOB,
eventType TEXT CHECK(eventType IN ("Art", "Math", "Science", "Computer Science", "History", "Education", "Political Science", "Software Engineering", "Business", "Sports", "Honors", "Workshops", "Study Session", "Dissertation", "Performance", "Competition")),    
eventAccess TEXT CHECK(eventAccess IN ('Public','Private', 'Inactive')), 
startDateTime TEXT NOT NULL, 
endDateTime TEXT NOT NULL, 
numberOfLikes INTEGER,

FOREIGN KEY (creatorID) REFERENCES accounts(accountID),
FOREIGN KEY (creatorType) REFERENCES accounts(accountType)
);
)"""
cursor.execute(sql_command)

sqliteConnection.commit()
sqliteConnection.close()
