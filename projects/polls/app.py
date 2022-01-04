############------------ IMPORTS ------------############
import psycopg2
from psycopg2.errors import DivisionByZero
import database
import settings


############------------ GLOBAL VARIABLE(S) ------------############
MENU_PROMPT = """
-- MENU --
(1) create a poll
(2) list open polls
(3) vote on a poll
(4) show poll votes
(5) select a random winner from a poll option
(6) exit

Enter your choice:
"""

############------------ FUNCTION(S) ------------############


############------------ DRIVER CODE ------------############
