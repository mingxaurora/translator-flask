from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)


bp = Blueprint('home', __name__, url_prefix="/auth")