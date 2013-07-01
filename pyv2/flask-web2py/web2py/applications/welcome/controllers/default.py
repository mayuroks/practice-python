# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


from sim import similar_search
from requests import get 
def index():
    form = FORM(INPUT(_name='artist', requires=IS_NOT_EMPTY()),INPUT(_name='song', requires=IS_NOT_EMPTY()),INPUT(_type='submit'))
    if form.process().accepted:
        session.artist = form.vars.artist
        session.song = form.vars.song
        redirect(URL('sim'))
    return dict(form=form)

def sim():
    list = [1,2,3]
    return dict(list=similar_search(session.artist,session.song))
