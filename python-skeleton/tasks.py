from invoke import task


@task
def clean(c):
    pass


@task
def build(c, install_pipenv=False):
    if install_pipenv:
        c.run('pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pipenv')

    c.run('pipenv sync')


@task
def run_dev(c):
    c.run('pipenv run manage.py runserver')


@task
def test(c):
    c.run('coverage erase')
    c.run('coverage run manage.py test')
    c.run('coverage xml -i')


@task
def quality_gate(c, runner_home='$SONAR_RUNNER_HOME', name='${name}'):
    c.run('%s/bin/sonar-scanner '
          '-Dsonar.sources=./ '
          '-Dsonar.projectKey=%s '
          '-Dsonar.projectName=%s '
          '-Dsonar.projectDescription="" '
          '-Dsonar.projectVersion=${baseVersion} '
          '-Dsonar.exclusions="static/**,manage.py,tasks.py,venv/**,venv-pypy/**" '
          '-Dsonar.inclusions="**/*.py" '
          '-Dsonar.scm.exclusions.disabled=true '
          '-Dsonar.host.url=http://sonar.riachuelo.net:8080/ '
          '-Dsonar.python.coverage.reportPaths=coverage.xml '
          '-Dsonar.coverage.exclusions="rchlo_base/*,app/*,**/tests.py,manage.py,tasks.py"' % (runner_home, name, name))
