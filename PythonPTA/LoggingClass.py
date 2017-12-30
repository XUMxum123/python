#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging;

#-------------------------------------------------------------------------------
def loggingDemo():
    """Just demo basic usage of logging module
    """
    logging.info("You should see this info both in log file and cmd window");
    logging.warning("You should see this warning both in log file and cmd window");
    logging.error("You should see this error both in log file and cmd window");

    logging.debug("You should ONLY see this debug in log file");
    return;

#-------------------------------------------------------------------------------    
def initLogging(logFilename):

    logging.basicConfig(
                    level    = logging.DEBUG,
                    format   = 'LINE %(lineno)-4d  %(levelname)-8s %(message)s',
                    datefmt  = '%m-%d %H:%M',
                    filename = logFilename,
                    filemode = 'w');
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler();
    console.setLevel(logging.INFO);
    # set a format which is simpler for console use
    formatter = logging.Formatter('LINE %(lineno)-4d : %(levelname)-8s %(message)s');
    # tell the handler to use this format
    console.setFormatter(formatter);
    logging.getLogger('').addHandler(console);

def logging_stdout():
    
    import sys
    origin = sys.stdout
    f = open('my_logging.log', 'w')
    sys.stdout = f
    # ===================================
    print 'Start of program'

    # 你的程序放到这里，过程中所有print到屏幕的内容都同时保存在my_logging.log里面了。
    print 'Being processed...'

    print 'End of program'
    # ===================================
    sys.stdout = origin
    f.close()

if __name__=="__main__":
    logFilename = "crifan_logging_demo.log"
    print '###############################################################################'
    print 'Example 1: using logging'
    initLogging(logFilename)
    loggingDemo()

    print '###############################################################################'
    print 'Example 2: using sys.stdout'
    logging_stdout()