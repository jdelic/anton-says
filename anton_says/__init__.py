# -* coding: utf-8 *-

import logging
import functools
from anton import events


_log = logging.getLogger(__name__)


@events.register("chanmsg")
@events.register("privmsg")
def filterinput(msgtype, irc, ircmsg):
    if msgtype == "chanmsg":
        replyfunc = functools.partial(irc.chanmsg, ircmsg["channel"])
    elif msgtype == "privmsg":
        replyfunc = functools.partial(irc.privnotice, ircmsg["source"]["nick"])

    if ircmsg["message"].startswith("!say "):
        say(irc, replyfunc, ircmsg["message"].split()[1:])
    elif ircmsg["message"].startswith("!msg "):
        whisper(irc, replyfunc, ircmsg["message"].split()[1:])


def say(irc, replyfunc, args):
    if len(args) < 2:
        replyfunc("(Not enough arguments) !say #channel something")
        return

    channel = args[0]
    message = args[1:]

    if not channel.startswith('#'):
        replyfunc("(Channel must start with #) !say #channel something")
        return

    irc.chanmsg(channel, " ".join(message))


def whisper(irc, replyfunc, args):
    if len(args) < 2:
        replyfunc("(Not enough arguments) !msg nick message")

    nick = args[0]
    message = args[1:]

    irc.privnotice(nick, " ".join(message))

