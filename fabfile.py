from fabric.api import settings, abort, env, run, sudo
from fabric.operations import prompt
from fabric.context_managers import cd
from fabric.contrib.files import exists
 

# cca webserver
env.hosts = ['209.40.90.63']

# prompt for drupal site name
env['site_dir'] = prompt('Enter drupal site name:')

# prompt for username
env.user = prompt('Log in as user:', default=env.user)

# common base directory for all drupal sites
env['base_dir'] = '/opt/drupal/'
 
# working directory
env['dir'] = env['base_dir'] + env['site_dir'] + '/'


# == TASKS == #

# pull updates from github into selected site 
def pull():

	print "running `git pull` on " + env['dir']

	with cd(env['dir']):

	  run("git pull")

	  print "clearing all caches..."

	  run("drush cc all")

# == END TASKS == #