CREATE TABLE mestre (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    experiencia INTEGER
);

CREATE TABLE sistema (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    versao VARCHAR(50)
);

CREATE TABLE jogador (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE mesa (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    codigo_mestre INTEGER REFERENCES mestre(codigo),
    codigo_sistema INTEGER REFERENCES sistema(codigo)
);

CREATE TABLE personagem (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    codigo_jogador INTEGER REFERENCES jogador(codigo),
    codigo_mesa INTEGER REFERENCES mesa(codigo)
);
```
