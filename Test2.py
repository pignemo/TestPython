import math
import cmath
import string

#Beginning Python from Novice to Professional

#page 32, chapter 2, list and tuple
#--------------------------------------------------------------
#name = raw_input("What is your name? ")
#print 'Hello. '+name+'!'


#sentence = raw_input('Sentence: ')
#
#screen_width = 80
#text_width = len(sentence)
#box_width = text_width+6
#left_margin = (screen_width-box_width)//2
#
#print
#print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
#print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
#print ' ' * left_margin + '| ' + sentence + ' |'
#print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
#print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
#print


#page 48, string
#--------------------------------------------------------------
#width = input('Please enter width: ')
#price_width = 10
#item_width = width - price_width
#
#header_format = '%-*s%*s'
#format = '%-*s%*.2f'
#
#print '=' * width
#
#print format % (item_width, 'Apples', price_width, 0.4)
#print format % (item_width, 'Pears', price_width, 0.5)
#print format % (item_width, 'Cantaloups', price_width, 1.92)
#print format % (item_width, 'Dried Apricots (16 0z.)', price_width, 8)
#print format % (item_width, 'Prunes (4 lbs.)', price_width, 12)
#
#print '=' * width


#page 58, chapter 4, dictionary
#--------------------------------------------------------------

#people = {
    #'Alice': {'phone': '2341',
              #'addr': 'Foo Drive 23'
              #},
    #'Beth': {'phone': '9102',
             #'addr': 'Bar Street 42'
             #},
    #'Cecil': {'phone': '3158',
              #'addr': 'Baz Avenue 90'
              #}
#}
#
#labels = {
    #'phone': 'phone number',
    #'addr': 'address'
#}
#
#name = raw_input('Name: ')
#
#request = raw_input('Phone number (p) or address (a)?')
#
#if request == 'p': key = 'phone'
#if request == 'a': key = 'addr'
#
#
#if name in people: print "%s's %s is %s. " % (name, labels[key], people[name][key])

#page 59, chapter 4, dictionary
#--------------------------------------------------------------
#template = '''<html><head><title>%(title)s</title></head><body><h1>%(text)s</h1><p>%(text)s</p></body>'''
#data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
#print template % data















