# -*- coding: utf-8 -*-
'''
Copyright (c) 2015 Heidelberg University Library
Distributed under the GNU GPL v3. For full terms see the file
LICENSE.md
'''
from gluon.storage import Storage
from gluon.custom_import import track_changes
settings = Storage()

settings.migrate = True
settings.title = 'CrossAsia eBooks'
settings.subtitle = ''
settings.author_email = 'heiup@ub.uni-heidelberg.de'
settings.keywords = 'CrossAsia E-Books, Universitätsbibliothek Heidelberg, Universität Heidelberg, digitales Publizieren, Open Access, omp, python, mysql, knv, onix, arthistoricum'
settings.description = 'CrossAsia E-Books'
settings.layout_theme = 'Default'
# settings.database_uri = 'sqlite://storage.sqlite'
# settings.database_uri = 'mysql://omp-user:omp-password@localhost:3306/omptest'
settings.security_key = '1228409b-a1fc-4868-92b1-a973a607d3f1'
settings.email_server = 'login'
settings.email_sender = 'login'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []

track_changes(True)
