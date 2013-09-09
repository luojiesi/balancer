from models import *

import webapp2

class Transaction(webapp2.RequestHandler):

    # get all transactions for one user
    def get(self):
        uid = self.request.get('uid', '')
        if not uid:
            # render error page
            return
        user = User.get_by_id(uid)
        transactions = [Transaction.get_by_id(x) for x in user.transactions]

        # render result page with transactions
        return

    def post(self):
        # get participated users
        uids = self.request.get('uids', [])
        # {uid: amount_paid}
        paid_uids = self.request.get('paid_uids', {})
        note = self.request.get('note', '')

        #validate data

        # allocate an id
        tid = 1

        data = dict(zip(uids, [0] * len(uids)))
        data.update(paid_uids)

        tran = Transaction(date='today',
                           note=note,
                           data=data,
                           id=tid)
        @ndb.transactional
        def add_tran():
            tran.put()
            for uid in uids:
                user = User.get_from_id(uid)
                user.transactions.append(tid)
                user.put()
        add_tran()
