	CREATE TABLE us_coins (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		numista_id INTEGER,
		name TEXT NOT NULL,
		years TEXT NOT NULL,
		composition TEXT NOT NULL,
		description TEXT
	);

	CREATE TABLE us_coin_years (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		coin_id INTEGER NOT NULL,
		numista_id INTEGER,
		year INTEGER,
		mintage INTEGER,
		mint_letter TEXT,
		description TEXT,
		FOREIGN KEY (coin_id) REFERENCES us_coins(id)
	);

	CREATE TABLE us_coin_prices (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		coin_year_id INTEGER NOT NULL,
		g INTEGER,
		vg INTEGER,
		f INTEGER,
		vf INTEGER,
		xf INTEGER,
		au INTEGER,
		unc INTEGER,
		FOREIGN KEY (coin_year_id) REFERENCES us_coin_years(id)
	);

	CREATE TABLE collection (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		coin_id INTEGER NOT NULL,
		condition TEXT,
		tag TEXT,
		image BLOB,
		buy_price INTEGER,
		note TEXT
	);
