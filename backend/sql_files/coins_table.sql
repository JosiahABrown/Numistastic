	CREATE TABLE coins (
		ID INT PRIMARY KEY AUTOINCREMENT,
		numista_id INT,
		name TEXT NOT NULL,
		issuer TEXT NOT NULL,
		years TEXT,
		composition TEXT,
		description TEXT
	);

	CREATE TABLE coin_years (
		ID INT PRIMARY KEY AUTOINCREMENT,
		numista_id INT,
		year INT,
		mintage INT,
		mint_letter TEXT,
		description TEXT,
		coin_id INT NOT NULL
	);

	CREATE TABLE coin_prices (
		ID INT PRIMARY KEY AUTOINCREMENT,
		g INT,
		vg INT,
		f INT,
		vf INT,
		xf INT,
		au INT,
		unc INT,
		coin_year_id INT NOT NULL
	);

	CREATE TABLE collection (
		ID INT PRIMARY KEY AUTOINCREMENT,
		coin_id INT NOT NULL,
		condition TEXT,
		tag TEXT,
		image BLOB,
		buy_price INT,
		note TEXT
	);
