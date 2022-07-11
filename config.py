from distutils.debug import DEBUG


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "nghianguyen123"
    DM_NAME = "product-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "exanple"

    UPLOADS = "home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE =True 

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True 

    DM_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "exanple"

    UPLOADS = "home/username/projects/flask_test/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE =False
    # ?*(CHỈ TRAO ĐỔI DỮ LIỆU QUA LẠI NẾU CÓ HTTP AN TOÀN)

class TestingConfig(Config):
    TESTING = True

    DM_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "exanple"

    UPLOADS = "home/username/projects/flask_test/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE =False 
