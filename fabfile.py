from fabric.api import settings, abort, env, run, sudo
from fabric.operations import prompt
from fabric.context_managers import cd
from fabric.contrib.files import exists
 

# cca webserver
env.hosts = ['209.40.90.63']

# prompt for username
env.user = prompt('Log in as user:', default=env.user)

# common base directory for all drupal sites
env['base_dir'] = '/opt/drupal/'


# -- SITES -- #

def ets_dev():
	env['dir'] = env['base_dir'] + 'ets14/'

# -- END SITES -- #
 

# -- TASKS -- #

# pull updates from github into selected site 
def pull():
	with cd(env['dir']):
	  run("git pull")

# == END TASKS == #