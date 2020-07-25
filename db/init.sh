#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE ROLE bboi LOGIN PASSWORD 'passwd';
    CREATE DATABASE bboi WITH OWNER = bboi;
    \c bboi
    CREATE TABLE IF NOT EXISTS ascii_art (
    title varchar(32),
    art text
    );
    ALTER TABLE public.ascii_art OWNER TO bboi;
EOSQL