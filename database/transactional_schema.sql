
CREATE TABLE clientes(
id SERIAL PRIMARY KEY,
nombre VARCHAR(100),
ciudad VARCHAR(50)
);

CREATE TABLE ventas(
id SERIAL PRIMARY KEY,
cliente VARCHAR(100),
ciudad VARCHAR(50),
producto VARCHAR(50),
ventas NUMERIC
);
