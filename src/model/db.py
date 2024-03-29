import json as js

from .__parser__ import Parse

PATH = "./src/data/data.json"


class Model:  
    """It's dialog with Json Database
    """       

    def get_channels() -> dict:
        """Returns all channels saved
        """

        db = open(PATH, "r")
        f = db.read()
        chans = js.loads(f)
        db.close

        return chans


    def add_channel(chan_name: str, url: str):
        """Add a new channel to database
        params:
        - chan_name: str
        - url: str (ready to save)
        """

        new_url = Parse.rts(url)

        try:
            to_add = {chan_name: new_url}

            f = open(PATH, "r")
            data = js.load(f)
            f.close()

            data.update(to_add)
            f = open(PATH, "w")
            js.dump(data, f, indent=4)
            f.close()
        except:
            raise ValueError()


    def del_channel(chan_name: str):
        """Delete a channel from database
        param:
        - chan_name: str
        """

        try:

            f = open(PATH, "r")
            data = js.load(f)
            f.close()

            data.pop(chan_name, None)
            f = open(PATH, "w")
            js.dump(data, f, indent=4)
            f.close()
        except:
            raise ValueError()


    def update_channel(old_chan_name: str, new_chan_name: str, url: str):
        """Updates name and url from a channel saved on database
        params:
        - old_chan_name: str
        - nem_chan_name: str
        - url: str (ready to save)
        """

        try:
            Parse.rts(url)
        except:
            raise ValueError("Wrong url")
        
        try:

            f = open(PATH, "rw")
            data = js.load(f)

            data.pop(old_chan_name, None)
            data.update({new_chan_name: url})

            js.dump(data, f)
            f.close()
        except:
            raise ValueError()