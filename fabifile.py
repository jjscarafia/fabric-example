from fabric.api import local

def hello(name="world"):
    print("Hello world %s!" % name)
    print '__name__',__name__

def prepare_deploy():
    ''' llamar con fab prepare_deploy -f fabifile.py '''
    local("python print_example.py")
    local("git add -p && git commit")
    local("git push")