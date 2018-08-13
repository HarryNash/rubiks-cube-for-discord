# Rubik's Cube for Discord

### Commands
  - `!rubik` lists the available commands.
  - `!hands` performs the moves affixed to it, e.g. `!hands R F2 x R'` will rotate the right face 90° clockwise, rotate the front face 180° clockwise, revolve the cube on it's x axis 90° then rotate the right face 90° counterclockwise.
  - `!solve` solves the cube.
  - `!text` displays the current cube configuration in text format.
  - `!jumble` jumbles the cube.
  - `!custom` configures the cube with a valid string of 54 colour characters.

### Preview
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Imgur Image](https://i.imgur.com/xoSvkb7.gif)

### Setup
- Run this PostgreSQL code to create the `cubes` table:
    ```sh
    CREATE TABLE public.cubes
    (
      channel_id text NOT NULL,
      progress text,
      CONSTRAINT cubes_pkey PRIMARY KEY (channel_id)
    )
    WITH (
      OIDS=FALSE
    );
    ALTER TABLE public.cubes
      OWNER TO postgres;
    ```
- Create a file called `secret.py` and fill it with the your own discord token and database credentials.
![Imgur Image](http://i.imgur.com/Q7ZSeTZ.png)
- Run this code in the `rubiks-cube-for-discord` directory:
    ```sh
    $ sudo -H pip3 install -r requirements.txt
    $ python3 bot.py
    ```
