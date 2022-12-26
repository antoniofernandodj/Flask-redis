import os.path
from typing import Optional

from flask import Blueprint, render_template, make_response, request
from random import randint
from pathlib import Path
from ..ext.cache import cache_expire
from .. import utils


bp = Blueprint('user', __name__)
static_folder = os.path.join(str(Path(__file__).parent.parent), 'static')


@bp.route('/')
@cache_expire(time=5)
def index():
    return render_template('index.html', randint=randint)


@bp.route('/static/image')
def image():
    return utils.get_content(
        url='http://cdn.eso.org/images/screen/eso1907a.jpg',
        content_type='image/jpg'
    )
