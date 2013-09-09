from models import *

import webapp2

class User(webapp2.RequestHandler):

    # get all transactions, balances for one user
    def get(self):
        uid = self.request.get('uid', '')
        if not uid:
            # render error page
            return
        user = User.get_by_id(uid)
        transactions = [Transaction.get_by_id(x) for x in user.transactions]

        from_balances = Balance.query(from_user=user.key)
        to_balances = Balance.query(to_user=user.key)

        # render result page with all the info
        return
