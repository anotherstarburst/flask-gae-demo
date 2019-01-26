#!/usr/bin/python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


class CourseRatings(ndb.Model):
    email = ndb.StringProperty(default="")
    rating = ndb.IntegerProperty(default=0)
    comments = ndb.TextProperty(default="")

    updated = ndb.DateTimeProperty(auto_now=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

