# encoding:utf-8
from django.utils.translation import ugettext as _
import re
"""
All constants could be used in other modules
For reasons that models, views can't have unicode text in this project, all unicode text go here.
"""
CLOSE_REASONS = (
    (1, _('duplicate question')),
    (2, _('question is off-topic or not relevant')),
    (3, _('too subjective and argumentative')),
    (4, _('not a real question')),
    (5, _('the question is answered, right answer was accepted')),
    (6, _('question is not relevant or outdated')),
    (7, _('question contains offensive or malicious remarks')),
    (8, _('spam or advertising')),
    (9, _('too localized')),
)

TYPE_REPUTATION = (
    (1, 'gain_by_upvoted'),
    (2, 'gain_by_answer_accepted'),
    (3, 'gain_by_accepting_answer'),
    (4, 'gain_by_downvote_canceled'),
    (5, 'gain_by_canceling_downvote'),
    (-1, 'lose_by_canceling_accepted_answer'),
    (-2, 'lose_by_accepted_answer_cancled'),
    (-3, 'lose_by_downvoted'),
    (-4, 'lose_by_flagged'),
    (-5, 'lose_by_downvoting'),
    (-6, 'lose_by_flagged_lastrevision_3_times'),
    (-7, 'lose_by_flagged_lastrevision_5_times'),
    (-8, 'lose_by_upvote_canceled'),
)

#do not translate these!!!
POST_SORT_METHODS = (
                     ('latest', _('newest')),
                     ('oldest', _('oldest')),
                     ('active', _('active')),
                     ('inactive', _('inactive')),
                     ('hottest', _('hottest')),
                     ('coldest', _('coldest')),
                     ('mostvoted', _('most voted')),
                     ('leastvoted', _('least voted')),
                     ('relevant', _('relevance')),
                    )
#todo: add assertion here that all sort methods are unique
#because they are keys to the hash used in implementations of Q.run_advanced_search

DEFAULT_POST_SORT_METHOD = 'active'
POST_SCOPE_LIST = (
                    ('all', _('all')),
                    ('unanswered', _('unanswered')),
                    ('favorite', _('favorite')),
                   )
DEFAULT_POST_SCOPE = 'all'
PAGE_SIZE_CHOICES = (('10','10',),('30','30',),('50','50',),)

UNANSWERED_QUESTION_MEANING_CHOICES = (
    ('NO_ANSWERS', _('Question has no answers')),
    ('NO_ACCEPTED_ANSWERS', _('Question has no accepted answers')),
)
#todo: implement this
#    ('NO_UPVOTED_ANSWERS',),
#)

#todo:
#this probably needs to be language-specific
#and selectable/changeable from the admin interface
#however it will be hard to expect that people will type
#correct regexes - plus this must be an anchored regex
#to do full string match
TAG_REGEX = r'^[a-z0-9\+\.\-]+$'
TAG_SPLIT_REGEX = r'[ ,]+'

TYPE_ACTIVITY_ASK_QUESTION=1
TYPE_ACTIVITY_ANSWER=2
TYPE_ACTIVITY_COMMENT_QUESTION=3
TYPE_ACTIVITY_COMMENT_ANSWER=4
TYPE_ACTIVITY_UPDATE_QUESTION=5
TYPE_ACTIVITY_UPDATE_ANSWER=6
TYPE_ACTIVITY_PRIZE=7
TYPE_ACTIVITY_MARK_ANSWER=8
TYPE_ACTIVITY_VOTE_UP=9
TYPE_ACTIVITY_VOTE_DOWN=10
TYPE_ACTIVITY_CANCEL_VOTE=11
TYPE_ACTIVITY_DELETE_QUESTION=12
TYPE_ACTIVITY_DELETE_ANSWER=13
TYPE_ACTIVITY_MARK_OFFENSIVE=14
TYPE_ACTIVITY_UPDATE_TAGS=15
TYPE_ACTIVITY_FAVORITE=16
TYPE_ACTIVITY_USER_FULL_UPDATED = 17
TYPE_ACTIVITY_QUESTION_EMAIL_UPDATE_SENT = 18
TYPE_ACTIVITY_MENTION = 19
#TYPE_ACTIVITY_EDIT_QUESTION=17
#TYPE_ACTIVITY_EDIT_ANSWER=18

TYPE_ACTIVITY = (
    (TYPE_ACTIVITY_ASK_QUESTION, _('question')),
    (TYPE_ACTIVITY_ANSWER, _('answer')),
    (TYPE_ACTIVITY_COMMENT_QUESTION, _('commented question')),
    (TYPE_ACTIVITY_COMMENT_ANSWER, _('commented answer')),
    (TYPE_ACTIVITY_UPDATE_QUESTION, _('edited question')),
    (TYPE_ACTIVITY_UPDATE_ANSWER, _('edited answer')),
    (TYPE_ACTIVITY_PRIZE, _('received award')),
    (TYPE_ACTIVITY_MARK_ANSWER, _('marked best answer')),
    (TYPE_ACTIVITY_VOTE_UP, _('upvoted')),
    (TYPE_ACTIVITY_VOTE_DOWN, _('downvoted')),
    (TYPE_ACTIVITY_CANCEL_VOTE, _('canceled vote')),
    (TYPE_ACTIVITY_DELETE_QUESTION, _('deleted question')),
    (TYPE_ACTIVITY_DELETE_ANSWER, _('deleted answer')),
    (TYPE_ACTIVITY_MARK_OFFENSIVE, _('marked offensive')),
    (TYPE_ACTIVITY_UPDATE_TAGS, _('updated tags')),
    (TYPE_ACTIVITY_FAVORITE, _('selected favorite')),
    (TYPE_ACTIVITY_USER_FULL_UPDATED, _('completed user profile')),
    (TYPE_ACTIVITY_QUESTION_EMAIL_UPDATE_SENT, _('email update sent to user')),
    (TYPE_ACTIVITY_MENTION, _('mentioned in the post')),
)

#response activity has receiving user not empty
RESPONSE_ACTIVITY_TYPES_FOR_DISPLAY = (
    TYPE_ACTIVITY_ANSWER,
    TYPE_ACTIVITY_COMMENT_QUESTION,
    TYPE_ACTIVITY_COMMENT_ANSWER,
    TYPE_ACTIVITY_UPDATE_ANSWER,
    TYPE_ACTIVITY_UPDATE_QUESTION,
    TYPE_ACTIVITY_UPDATE_ANSWER,
    TYPE_ACTIVITY_PRIZE,
    TYPE_ACTIVITY_MARK_ANSWER,
    TYPE_ACTIVITY_VOTE_UP,
    TYPE_ACTIVITY_VOTE_DOWN,
    TYPE_ACTIVITY_CANCEL_VOTE,
    TYPE_ACTIVITY_DELETE_QUESTION,
    TYPE_ACTIVITY_DELETE_ANSWER,
    TYPE_ACTIVITY_MARK_OFFENSIVE,
    TYPE_ACTIVITY_FAVORITE,
)

RESPONSE_ACTIVITY_TYPES_FOR_EMAIL = (
    TYPE_ACTIVITY_COMMENT_QUESTION,
    TYPE_ACTIVITY_COMMENT_ANSWER,
    TYPE_ACTIVITY_UPDATE_ANSWER,
    TYPE_ACTIVITY_UPDATE_QUESTION,
)

TYPE_RESPONSE = {
    'QUESTION_ANSWERED' : _('question_answered'),
    'QUESTION_COMMENTED': _('question_commented'),
    'ANSWER_COMMENTED'  : _('answer_commented'),
    'ANSWER_ACCEPTED'   : _('answer_accepted'),
}

CONST = {
    'closed'            : _('[closed]'),
    'deleted'           : _('[deleted]'),
    'default_version'   : _('initial version'),
    'retagged'          : _('retagged'),
}

#how to filter questions by tags in email digests?
TAG_EMAIL_FILTER_CHOICES = (
    ('ignored', _('exclude ignored tags')),
    ('interesting',_('allow only selected tags'))
)

NOTIFICATION_DELIVERY_SCHEDULE_CHOICES= (
                            ('i',_('instantly')),
                            ('d',_('daily')),
                            ('w',_('weekly')),
                            ('n',_('no email')),
                        )

USERS_PAGE_SIZE = 28#todo: move it to settings?
USERNAME_REGEX_STRING = r'^[\w ]+$'

TWITTER_STYLE_MENTION_TERMINATION_CHARS = ' ;,.!?'#chars that can go after @mention

COMMENT_HARD_MAX_LENGTH = 2048

#an exception import * because that file has only strings
from forum.const.message_keys import *