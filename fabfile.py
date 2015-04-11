from fabric.api import run, local


def host_name():
    run('uname s')


def deploy():
    local("git add .")
    local("git commit")
    local("git push")
