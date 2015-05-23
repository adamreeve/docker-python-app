from hello import app, config


wsgi_app = app.create_app(config)


if __name__ == '__main__':
    wsgi_app.run(host="0.0.0.0", port=8080, debug=config.DEBUG)
