from fabric.api import local, cd
import os
import time

HERE = os.path.abspath(os.path.dirname(__file__))
manage = os.path.join('manage.py')


def publish(test='yes'):
    '''
    Easy publishing of my nice open source project
    '''
    if test == 'yes':
        validate()

    local('git push')

    from django_facebook import __version__
    tag_name = 'v%s' % __version__

    local('python setup.py sdist upload')
    local('git tag %s' % tag_name)
    local('git push origin --tags')


def validate():
    with cd(HERE):
        local('pep8 --exclude=migrations --ignore=E501,E225 apps')
        local('python %s test apps' % manage)


def full_validate():
    with cd(HERE):
        local('pep8 --exclude=migrations --ignore=E501,E225 apps')
        local('CUSTOM_USER_MODEL=0 python %s test apps' % manage)
        local('CUSTOM_USER_MODEL=1 python %s test apps' % manage)
        local('CUSTOM_USER_MODEL=0 MODE=userena python %s test apps' % manage)


def clean():
    local('del *.pyc /s/q')
    local('del *.zip')
    local('rm -rf runtime')
#    local('bash -c "autopep8 -i *.py"')
#    local('bash -c "autopep8 -i apps/*.py"')
#    local('bash -c "autopep8 -i apps/*.py"')

def pack(name='photo'):
    ver = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    local('mkdir E:\\Documents\\backups\\codes\\%s' % (name))
    local('zip -r -q E:/Documents/backups/codes/%s/%s.zip .' % (name, ver))

def docs():
    local('sphinx-build -Eav docs html')

def run():
    local('python %s runserver' % manage)

def init():
    local('python %s schemamigration apps --initial' % manage)
    local('python %s migrate' % manage)

def mig():
    local('python %s schemamigration apps --auto' % manage)
    local('python %s migrate' % manage)
