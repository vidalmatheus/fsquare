import inspect
from functools import wraps

from invoke import task


def projtask(func):
    """
    Task to be executed on project root.
    """
    @wraps(func)
    def wrapper(c, *args, **kwargs):
        with c.cd(c.config._project_prefix):
            return func(c, *args, **kwargs)

    wrapper.__signature__ = inspect.signature(func)
    return task(wrapper)


@projtask
def dkdb(c):
    c.run("docker run --name postgres-db --rm \
        -e POSTGRES_USER={{name}} -e POSTGRES_PASSWORD={{name}} \
        -p 5432:5432 \w
        -v $PROJ_BASE/docker/dkdata/postgres:/var/lib/postgresql/data \
        postgres")


@projtask
def dknginx(c):
    c.run("docker-compose -f docker/compose/nginx.yaml build")
    c.run("docker-compose -f docker/compose/nginx.yaml up")


@projtask
def dkdev(c):
    c.run("docker-compose -f docker/compose/dev.yaml up")


@projtask
def dkfulldev(c):
    c.run("docker-compose -f docker/compose/fulldev.yaml up")


@projtask
def dkbuild(c):
    c.run("docker build -t {{name}} .")


@projtask
def pycoverage(c):
    c.run("pytest --flake8 --durations=10 --cov --cov-report=term --cov-report=html:./htmlcov")
