from flask import Flask


def get_config(dev_env):
    if dev_env == 'prod':
        config_name = 'config.ProdConfig'
    elif dev_env == 'dev':
        config_name = 'config.DevConfig'
    elif dev_env == 'test':
        config_name = 'config.TestConfig'
    else:
        raise EnvironmentError
    return config_name


def init_app(app_name, dev_env):
    config_name = get_config(dev_env)

    app = Flask(app_name,
                static_path=None,
                static_url_path=None,
                static_folder='static',
                template_folder='templates',
                instance_path=None,
                instance_relative_config=False
                )

    app.config.from_object(config_name)

    return app
