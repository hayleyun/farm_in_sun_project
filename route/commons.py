from flask import Flask,render_template,request,jsonify,redirect,url_for,Blueprint
from ml import predict_lang,trans_lang
from flask import session
import db
from datetime import timedelta
bp = Blueprint('commons', __name__, url_prefix='/commons')




