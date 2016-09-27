#!/usr/bin/env python
import click
import os
import json
import sys
from subprocess import call

configuration_file = os.path.expanduser("~/.servant-cli.json")

# Try to load configuration file
if os.path.isfile(configuration_file):
  with open(configuration_file, 'r') as f:
    config = json.load(f)
else:
  print "Couldn't find configuration file \"" + configuration_file + "\""
  sys.exit(1)

# Inherit shell environment
env = {}
env.update(os.environ)
env['VAGRANT_CWD'] = os.path.expanduser(config["servant_root"])

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def servant():
    """Command line interface for Servant - the Vagrant based web-development virtual machine."""
    pass

@servant.command()
def up():
    """Start/boot servant machine"""
    call(["vagrant", "up"], env=env)
    return

@servant.command()
def down(**kwargs):
    """Shutdown and power off servant machine"""
    call(["vagrant", "suspend"], env=env)
    return

@servant.command()
def reboot(**kwargs):
    """Reboot servant machine"""
    call(["vagrant", "reload"], env=env)
    return

@servant.command()
def reload(**kwargs):
    """Run provisioning formulae"""
    call(["vagrant", "provision"], env=env)
    return

@servant.group()
def services(**kwargs):
    """Control Apache, PHP-FPM and MySQL server"""
    pass

@services.command()
@click.argument('action', type=click.Choice(['restart', 'start', 'status', 'stop']))
def apache(action):
    """Control Apache2 web server"""
    click.echo(action)
    return

@services.command()
@click.argument('action', type=click.Choice(['restart', 'start', 'status', 'stop']))
def php(**kwargs):
    """Control PHP-FPM"""
    click.echo(action)
    return

@services.command()
@click.argument('action', type=click.Choice(['restart', 'start', 'status', 'stop']))
def mysql(**kwargs):
    """Control MySQL database server"""
    click.echo(action)
    return

@servant.command()
def projects(**kwargs):
    pass

@servant.command()
def ssh(**kwargs):
    """SSH into servant"""
    call(["vagrant", "ssh"], env=env)
    return

if __name__ == '__main__':
    servant()
