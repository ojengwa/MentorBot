from fabric.api import run, local


def host_name():
    run('uname s')


def deploy(msg=""):
    local("git add .")
    if not msg:
        local("git commit")
    else:
        local("git commit %s" % msg)

    local("git push")
