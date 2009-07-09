#!/usr/bin/env python
from threadedcomments.moderation import *
from threadedcomments.models import PLAINTEXT

class ArticleModerator(CommentModerator):
	akismet 			= True
	enable_field 		= 'enable_comments'
	email_notification 	= True
	auto_close_field	= 'pub_date'
	close_after			= 30
	allowed_markup		= [PLAINTEXT]

moderator.register(Article, ArticleModerator)

