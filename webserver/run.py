from app import create_app

app = create_app()

if __name__ == "__main__":
  # app.run(debug=True, host='localhost', port=5001)
  app.run(debug=True)
