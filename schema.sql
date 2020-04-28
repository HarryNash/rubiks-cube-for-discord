CREATE TABLE public.cubes
(
  channel_id bigint NOT NULL,
  progress text,
  CONSTRAINT cubes_pkey PRIMARY KEY (channel_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.cubes
  OWNER TO postgres;
