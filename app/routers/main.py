from flask import Blueprint, render_template, request, redirect, url_for

#Create Blueprint
main = Blueprint('main', __name__)

#Index Page
@main.route('/')
def index():
    return 'Index'