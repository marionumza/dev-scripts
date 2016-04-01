#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #############################################################################
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
# #############################################################################
import os
import sys
import logging

logger = logging.getLogger(__name__)
logger.info('this does not work :(')

"""
Help dict
    'name':'clientname','port':'portnumber','odoover':'odoo-version'
    'repos': [
    # install repository of standard modules
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
    # install multiple single repos in a installdir
         {'usr': 'jobiols', 'instdir':'ml', 'repo': 'meli_oerp', 'branch': '8.0'},
         {'usr': 'jobiols', 'instdir':'ml', 'repo': 'payment_mercadopago', 'branch': '8.0'},
    # install repo with inner path
         {'usr': 'jobiols', 'innerdir':'addons/fpoc', 'repo': 'odoo_fpoc', 'branch': 'master'},
    ]
    'images':[
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
    ]
    'install'[
        'module-to-install',
        'another-module'
    ]
"""

clients__ = [
    #######################################################################
    {'name': 'makeover', 'port': '8068', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         #         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},

         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'str', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'knowledge', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'bank-statement-import', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'jeo', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'nixel', 'port': '8090', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'tablero_nixel', 'instdir': 'nixel', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'valente', 'port': '8091', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},

     ],
     'install': ['disable_openerp_online',  # Remove odoo.com bindings
                 'l10n_ar_base',  # argentinian localization

                 'express_checkout'  # ventas express
                 'hide_product_variants',  # no trabajamos con variantes.
                 'l10n_ar_bank_cbu',  # añade cbu a la información del banco
                 'l10n_ar_aeroo_stock',  # impresion de remitos
                 'l10n_ar_chart_generic_withholding',  # Generic withholding management
                 #                 'account_accountant',      # Manage financial and analitical accounting
                 ]
     },
    #######################################################################
    {'name': 'atly', 'port': '8069', 'odoover': '7.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'atly-work', 'branch': '7.0'},
         {'usr': 'jobiols', 'repo': 'atly-orig', 'branch': '7.0'},
     ],
     'images': [
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-adhoc', 'ver': '7.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'sooftart', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},

         #    magento
         {'usr': 'jobiols', 'repo': 'connector-magento', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'connector-ecommerce', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'connector', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'e-commerce', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'product-attribute', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
     ]
     },
    #######################################################################
    {'name': 'textil', 'port': '8071', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'product-attribute', 'branch': '7.0'},
         {'usr': 'oca', 'repo': 'e-commerce', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '8.0'}
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },

    #######################################################################
    {'name': 'pos', 'port': '8091', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'innerdir': 'addons', 'repo': 'odoo_fpoc',
          'branch': 'master'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ],
     'install': ['l10n_ar_base', 'sale']
     }
]

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
YELLOW_LIGHT = "\033[33m"
CLEAR = "\033[0;m"


class Environment:
    def __init__(self, args, clients):
        self._clients = []
        for cli in clients:
            self._clients.append(Client(self, cli))

        self._home_dir = '/odoo/'
        self._home_template = self._home_dir + 'odoo-'
        self._psql = self._home_dir + 'postgresql/'
        self._args = args

    def get_base_dir(self):
        return self._home_dir

    def debug_mode(self):
        return self._args.debug

    def test_mode(self):
        return self._args.test

    def no_dbfilter(self):
        return self._args.no_dbfilter

    def get_modules_from_params(self):
        if self._args.module is None:
            self.msgerr('need -m option (module name or all for all modules)')
        return self._args.module

    def get_database_from_params(self):
        if self._args.database is None:
            self.msgerr('need -d option (database name)')
        if len(self._args.database) > 1:
            self.msgerr('only one database expected')
        return self._args.database[0]

    def get_new_database_from_params(self):
        if self._args.new_database is None:
            self.msgerr('need -w option (new database name)')
        if len(self._args.new_database) > 1:
            self.msgerr('only one new database name expected')
        return self._args.new_database[0]


    def get_timestamp_from_params(self):
        if self._args.timestamp is None:
            self.msgerr(
                'need -t option (timestamp, see --backup-list for available timestamps)')
        if len(self._args.database) > 1:
            self.msgerr('only one timestamp expected')
        return self._args.timestamp[0]

    def get_clients_from_params(self, cant='multi'):
        if self._args.client is None:
            self.msgerr('need -c option (client name)')

        for cli in self._args.client:
            if self.get_client(cli) is None:
                self.msgerr('there is no ' + cli + ' client in this environment')

        if cant == 'multi':
            return self._args.client
        else:
            if len(self._args.client) > 1:
                self.msgerr('only one client expected')
            return self._args.client[0]

    def get_args(self):
        return self._args

    def get_client(self, clientName):
        cli = None
        for client in self._clients:
            if client.get_name() == clientName:
                cli = client
        return cli

    def get_clients_form_dict(self):
        return self._clients

    def get_template_dir(self):
        return self._home_template

    def get_psql_dir(self):
        return self._psql

    def green(self, string):
        return GREEN + string + CLEAR

    def yellow(self, string):
        return YELLOW + string + CLEAR

    def red(self, string):
        return RED + string + CLEAR

    def yellow_light(self, string):
        return YELLOW_LIGHT + string + CLEAR

    def msgrun(self, msg):
        if not self._args.quiet:
            print self.yellow(msg)

    def msgdone(self, msg):
        if not self._args.quiet:
            print self.green(msg)

    def msgerr(self, msg):
        if not self._args.quiet:
            print self.red(msg)
            sys.exit()

    def msginf(self, msg):
        if not self._args.quiet:
            print self.yellow_light(msg)


class Client:
    def __init__(self, env, dic):
        self._env = env
        self._name = dic['name']
        self._port = dic['port']
        self._ver = dic['odoover']
        self._repos = []
        for rep in dic['repos']:
            self._repos.append(Repo(self, rep))
        self._images = []
        for img in dic['images']:
            self._images.append(Image(self, img))

        try:
            self._install = dic['install']
        except:
            self._install = None

    def get_init_modules(self):
        return ','.join(self._install)

    def get_base_dir(self):
        return self._env.get_base_dir()

    def get_ver(self):
        return self._ver

    def get_backup_dir(self):
        return self.get_home_dir() + self._name + '/backup/'

    def get_log_backup_file(self):
        return '/var/log/odoo/odoo.log'

    def get_repos(self):
        return self._repos

    def get_images(self):
        return self._images

    def get_image(self, ImageName):
        ret = None
        for img in self._images:
            if img.get_name() == ImageName:
                ret = img
        if ret is None:
            raise Exception('no image ' + ImageName + ' found')
        return ret

    def get_name(self, pad=0):
        return self._name.ljust(pad)

    def get_port(self):
        return self._port

    def get_home_dir(self):
        return self._env.get_template_dir() + self._ver + '/'

    def get_addons_path(self):
        # path to addons inside image
        path = '/mnt/extra-addons/'
        paths = []
        for repo in self.get_repos():
            paths.append(path + repo.getPathDir())
        return ','.join(paths)


class Repo:
    def __init__(self, cli, dict):
        self._dict = dict
        self._cli = cli

    def _getRepo(self):
        return self._dict['usr'] + '/' + self._dict['repo']

    def get_formatted_repo(self):
        ret = 'b ' + self._dict['branch'].ljust(7) + ' ' + self._getRepo().ljust(30)
        return ret

    def getPathDir(self):
        try:
            ret = self._dict['instdir']
        except:
            try:
                ret = self._dict['repo'] + '/' + self._dict['innerdir']
            except:
                ret = self._dict['repo']

        return ret

    def getInstDir(self):
        try:
            ret = self._dict['instdir'] + '/' + self._dict['repo']
        except:
            ret = self._dict['repo']
        return self._cli.get_home_dir() + 'sources/' + ret

    def getPullRepo(self):
        return 'git -C ' + self.getInstDir() + ' pull'

    def getCloneRepo(self):
        return 'git clone --depth 1 -b ' + \
               self._dict['branch'] + \
               ' http://github.com/' + \
               self._getRepo() + ' ' + \
               self.getInstDir()

class Image:
    def __init__(self, cli, dict):
        self._cli = cli
        self._dict = dict

    def getVer(self):
        try:
            ver = self._dict['ver']
        except:
            ver = 'latest'
        return ver

    def getFormattedImage(self):
        ret = self._dict['usr']
        try:
            ret += '/' + self._dict['img']
        except:
            a = 1

        try:
            ret += ':' + self._dict['ver']
        except:
            a = 1

        return ret

    def get_image(self):
        try:
            usr = self._dict['usr']
        except:
            usr = ''

        try:
            image = self._dict['img']
        except:
            image = ''

        try:
            ver = self._dict['ver']
        except:
            ver = ''

        ret = usr
        if image != '':
            ret += '/' + image
        if ver != '':
            ret += ':' + ver

        return ret

    def get_name(self):
        return self._dict['name']

    def getPullImage(self):
        return 'sudo docker pull ' + self.get_image()
