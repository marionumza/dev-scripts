#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ##############################################################################
#
# Jorge Obiols Software,
# Copyright (C) 2015-Today JEO <jorge.obiols@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##############################################################################

import argparse
import sys
from datetime import datetime
import json
import subprocess

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
YELLOW_LIGHT = "\033[33m"
CLEAR = "\033[0;m"
REPOS_DIR = '/home/jorge/git-repos/'


def sc__(params):
    if args.verbose:
        print '>', params
    p = subprocess.Popen(params.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()


def sc_(params):
    if args.verbose:
        print '>', params
    return subprocess.call(params, shell=True)


def green(string):
    return GREEN + string + CLEAR


def yellow(string):
    return YELLOW + string + CLEAR


def red(string):
    return RED + string + CLEAR


def yellow_light(string):
    return YELLOW_LIGHT + string + CLEAR


def msgrun(msg):
    print yellow(msg)


def msgdone(msg):
    print green(msg)


def msgerr(msg):
    print red(msg)
    sys.exit()


def msginf(msg):
    print yellow_light(msg)

# levantar datos de archivo de configuracion, tiene
# que estar en el mismo directorio que este archivo
with open('update-forks-data.json') as f:
    json = json.load(f)
repos = json['repos']


class repo:
    """ Repositorio
    """

    def __init__(self, dict):
        self._usr = dict['usr']
        self._repo = dict['repo']
        self._branch = dict['branch']
        try:
            self._upstream = dict['upstream']
        except:
            self._upstream = dict['repo']

    def delete(self):
        msgrun('deleting {}'.format(self.dir()))
        sc_('sudo rm -r {}'.format(self.dir()))

    def upstream(self):
        return 'https://github.com/{}/{}'.format(self._usr, self._upstream)

    def origin(self):
        return 'https://github.com/jobiols/{}'.format(self._repo)

    def usr(self):
        return self._usr

    def repo(self):
        return self._repo

    def branch(self):
        return self._branch

    def format_branches(self, branches):
        if type(branches) == type([]):
            ret = ','.join(branches)
        else:
            ret = branches
        return ret

    def name(self):
        return '{:14} {:10} {}'.format(
            self._usr,
            self.format_branches(self._branch),
            self._repo)

    def dir(self):
        return REPOS_DIR + self._repo

    def create_local_repo(self):
        msgrun('Local repo does not exist! Cloning origin...')
        sc_('git clone {} {}'.format(self.origin(), self.dir()))

        msgrun('adding remote upstream')
        sc_('git -C {} remote add upstream {}'.format(self.dir(), self.upstream()))

    def _shortver(self):
        return datetime.now().strftime('%Y%m%d%H%M')

    def _longver(self):
        return datetime.now().strftime(':%B %d, %Y')

    def update(self):
        msgrun('{} {}/{}:({})'.format(
            20 * '-', self.usr(), self.repo(), ', '.join(self.branch())))

        # chequear local repo y crearlo si no existe
        if sc_('git -C {} status'.format(self.dir())):
            self.create_local_repo()

        # extraer con checkout todos los branches, si no existe crearlo
        msgrun('checkin out branches ({})'.format(', '.join(self.branch())))
        for branch in self.branch():
            if sc_('git -C {} checkout {}'.format(self.dir(), branch)):
                msgrun('Branch {} does not exist, creating it'.format(branch))
                sc_('git -C {} checkout -b {}'.format(self.dir(), branch))

        # traer los remotes
        msgrun('Fetching all branches from upstream')
        sc_('git -C {} fetch upstream'.format(self.dir()))

        # mergear cada branch con el local
        msgrun('Merging each remote branch with local ones')
        for branch in self.branch():
            sc_('git -C {} checkout {}'.format(self.dir(), branch))
            sc_('git -C {} merge upstream/{}'.format(self.dir(), branch))

        """
        # le pongo el tag a la nueva versión creada
        msgrun('tagging repo')
        out, err = sc_('git -C {} tag -a v{} -m "update fork on {}"'.format(
                self.dir(), self._shortver(), self._longver()))
        print 'aaa',out,err
        msgerr('tagging fail')
        exit()
        """
        # subo la version nueva a mi repo, todos los branches
        msgrun('pushing all branches to origin')
        sc_('git -C {} push origin --all'.format(self.dir()))

        """
        # subo el tag
        msgrun('push --tags')
        if sc_('git -C {} push origin --tags {}'.format(
                self.dir(), branch)):
            msgerr('push fail')
        """


class repos:
    """ Conjunto de repositorios definido en el archivo de configuracion
    """

    def __init__(self, json):
        self._repos = []
        for dict in json['repos']:
            if not self.alredy_exists(dict):
                self._repos.append(repo(dict))

    def find_repo(self, repo_name):
        for repo in self._repos:
            if repo.repo() == repo_name:
                return repo
        return False

    def delete_local_repos(self):
        if args.repo:
            repo_name = args.repo[0]
            repo = self.find_repo(repo_name)
            if repo:
                repo.delete()
            else:
                msgerr('no hay repo ' + repo_name)
        else:
            for repo in self._repos:
                repo.delete()

    def alredy_exists(self, dict):
        for rp in self._repos:
            if rp._repo == dict['repo']:
                msgerr('duplicate repo {}'.format(rp.name()))

    def list_repos(self):
        for rp in self._repos:
            msginf(rp.name())

    def update(self, repo_name):
        for r in self._repos:
            if r.repo() == repo_name:
                r.update()
                return True
        msgerr('repo "{}" not found'.format(repo_name))

    def update_all(self):
        for r in self._repos:
            r.update()


rp = repos(json)

# argparse options
#########################################################################################
def list():
    msgrun('Currently maintained repositories')
    rp.list_repos()


def update():
    if args.repo is None:
        msgerr('need -r')
    rp.update(args.repo[0])


def delete():
    if args.repo is None:
        msgerr('need -r')
    rp.delete_local_repos()


def delete_all():
    rp.delete_local_repos()


def update_all():
    rp.update_all()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    Update forks v 1.1.0 ------------------------------------------------------
    This script manages a set of repositories, each one having three locations: The
    original one, the fork of the original in my github and a clone of this fork in my
    workstation.
    The program's goal is to update the fork in github to the latest version of the
    original repo. To do that it makes a fetch to the original repo downloading the
    last version to the workstation, does a merge and then performs a push to the fork.
    """)
    parser.add_argument('-U',
                        '--update-all',
                        action='store_true',
                        help="Updates all branches of all forks")

    parser.add_argument('-u',
                        '--update',
                        action='store_true',
                        help="Update specifics fork, requires -r use -b to specify branch")

    parser.add_argument('-r',
                        '--repo',
                        action='append',
                        dest='repo',
                        help="Repo to update")

    parser.add_argument('-d',
                        '--delete',
                        action='store_true',
                        help="Delete specific repo, This is usefull to start fresh. Requires -r")

    parser.add_argument('-D',
                        '--delete-all',
                        action='store_true',
                        help="Delete all repos, This is usefull to start fresh.")

    parser.add_argument('-b',
                        '--branch',
                        action='append',
                        dest='branch',
                        help="Branch to update")

    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help="List al currently maintained repos")

    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help="Show commands")

    args = parser.parse_args()

    if args.update_all:
        update_all()

    if args.list:
        list()

    if args.update:
        update()

    if args.delete:
        delete()

    if args.delete_all:
        delete_all()
