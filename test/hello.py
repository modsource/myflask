#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   baocheng
#   E-mail  :   baocheng@botpy.com
#   Date    :   2015/11/20 23:58:30
#   Desc    :
#
from __future__ import absolute_import, print_function, division, with_statement

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
