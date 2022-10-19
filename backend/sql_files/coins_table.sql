	CREATE TABLE coins (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		issuer TEXT NOT NULL,
		year INT,
		mintage TEXT,
		composition TEXT,
		mint_letter TEXT,
		description TEXT
	);

	CREATE TABLE collection (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		coin_id INT NOT NULL,
		condition TEXT,
		note TEXT
	);
