from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from application import app

 
if __name__ == "__main__":
    app.run(debug=True)