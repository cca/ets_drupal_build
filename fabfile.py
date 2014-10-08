from fabric.api import settings, abort, env, run, sudo
from fabric.operations import prompt
from fabric.context_managers import cd
from fabric.contrib.files import exists
 

# cca webserver
env.hosts = ['209.40.90.63']

# prompt for username
env.user = prompt('Log in as user:', default=env.user)


# -- SITES -- #

def ets_dev():
	env['dir'] = '/opt/drupal/ets14/'

# -- END SITES -- #
 

# -- ACTIONS -- #

# pull updates from github into selected site 
def pull():
	with cd(env['dir']):
	  run("git pull")

# == END ACTIONS == #