"""
Fichier dédié à l'initialisation des variables de configuration de l'application.

Référence: http://flask.pocoo.org/docs/1.0/config/#development-production
"""


TEMPLATES_AUTO_RELOAD = True
DEBUG = False
# TOP_LEVEL_DIR =

# cf. https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b
#################
## 1ere option ##
#################
"""
# config.py
DATABASE_CONFIG = {
    'host': 'localhost',
    'dbname': 'company',
    'user': 'user',
    'password': 'password',
    'port': 3306
}

# main.py
import pymysql
import config

def connect_db(dbname):
    if dbname != config.DATABASE_CONFIG['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    conn = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                           user=config.DATABASE_CONFIG['user'],
                           password=config.DATABASE_CONFIG['password'],
                           db=config.DATABASE_CONFIG['dbname'])
    return conn

connect_db('company')
"""



#################
##  2e option  ##
#################

"""
# config.py
class Config:
    APP_NAME = 'myapp'
    SECRET_KEY = 'secret-key-of-myapp'
    ADMIN_NAME = 'administrator'

    AWS_DEFAULT_REGION = 'ap-northeast-2'
    
    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880 # 5MB

    
class DevelopmentConfig(Config):
    DEBUG = True
    
    AWS_ACCESS_KEY_ID = 'aws-access-key-for-dev'
    AWS_SECERT_ACCESS_KEY = 'aws-secret-access-key-for-dev'
    AWS_S3_BUCKET_NAME = 'aws-s3-bucket-name-for-dev'
    
    DATABASE_URI = 'database-uri-for-dev'
    
class TestConfig(Config):
    DEBUG = True
    TESTING = True
    
    AWS_ACCESS_KEY_ID = 'aws-access-key-for-test'
    AWS_SECERT_ACCESS_KEY = 'aws-secret-access-key-for-test'
    AWS_S3_BUCKET_NAME = 'aws-s3-bucket-name-for-test'
    
    DATABASE_URI = 'database-uri-for-dev'
  

class ProductionConfig(Config):
    DEBUG = False

    AWS_ACCESS_KEY_ID = 'aws-access-key-for-prod'
    AWS_SECERT_ACCESS_KEY = 'aws-secret-access-key-for-prod'
    AWS_S3_BUCKET_NAME = 'aws-s3-bucket-name-for-prod'

    DATABASE_URI = 'database-uri-for-dev'


class CIConfig:
    SERVICE = 'travis-ci'
    HOOK_URL = 'web-hooking-url-from-ci-service'
   
# main.py
import sys
import config

...

if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    
    if env == 'dev':
        app.config = config.DevelopmentConfig
    elif env == 'test':
        app.config = config.TestConfig
    elif env == 'prod':
        app.config = config.ProductionConfig
    else:
        raise ValueError('Invalid environment name')
   
app.ci = config.CIConfig

"""