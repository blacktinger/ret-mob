# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from retmobapp.app import create_app
from retmobapp.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag(default=True) else ProdConfig

app = create_app(CONFIG)

if __name__ == '__main__':
	app.run()

