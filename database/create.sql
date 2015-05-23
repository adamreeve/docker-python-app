DROP SCHEMA IF EXISTS auth CASCADE;
CREATE SCHEMA auth;


CREATE TABLE auth.user (
      user_id uuid primary key
    , email varchar(250) NOT NULL
    , password varchar(100) NOT NULL
    , display_name varchar(100)
    , created timestamp with time zone NOT NULL
    , updated timestamp with time zone NOT NULL
);

CREATE UNIQUE INDEX user_email_idx ON auth.user (lower(trim(email)));
