#! /usr/bin/env python

import tkFileDialog

import ConfigParser
import datetime
import logging
import ast

config = ConfigParser.RawConfigParser()
file_read = config.read('config.cfg')
if not file_read:
    print 'unable to read config.'
    exit()

LOG_FOLDER = config.get('misc', 'log_folder')
log_file = config.get('misc', 'log_file') + datetime.date.today() 
logger = logging.getLogger('application_log')
hdlr = logging.FileHandler(LOG_FOLDER + log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(getattr(logging, config.get('misc', 'level').upper(), logging.INFO))

logger.info('Started application')
read_files = config.get('misc', 'read_files')
read_files = ast.literal_eval(read_files)
open_file_input = True
if read_files:
    ui = input('Open files to read?("n" or "N"/press enter to continue)')
    if ui[0].upper() == 'N':
        open_file_input = False
if open_file_input:
    read_files = tkFileDialog.askopenfilenames()
    config.set('misc', value=str(read_files))

#appending comment in test branch
