from invoke import task


@task
def build(c, name):
    c.run("ls")
