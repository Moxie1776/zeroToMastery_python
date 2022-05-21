from flask import Flask


# Create app
def create_app():
  app = Flask(__name__)
  app.debug = False

  from app.data import dp
  app.register_blueprint(dp)

  import logging
  import os
  from logging.handlers import RotatingFileHandler

  if not app.debug:
    if not os.path.exists("logs"):
      os.mkdir("logs")
    file_handler = RotatingFileHandler(
      "logs/log.txt", maxBytes=10240, backupCount=20
        )
    file_handler.setFormatter(
      logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
          )
        )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info("Flask Startup")

  return app
