from models import *

import webapp2

class User(webapp2.RequestHandler):

    # calculate amount needs to pay
    def get(self):
        uids = self.request.get('uids', [])
        #validate data

        amount = {}
        for uid in uids:
            from_balances = Balance.query(from_user=uid,
                                         to_user in uids)
            to_balances = Balance.query(to_user=uid,
                                         from_user in uids)
            from_amount = reduce(lambda x,y: x.value+y.value, from_balances)
            to_amount = reduce(lambda x,y: x.value+y.value, to_balances)
            amount[uid] = from_amount - to_amount

        # render results
        return

    # make the payment
    def post(self):
        uids = self.request.get('uids', [])
        #validate data

        balances = Balance.query(from_user in uid,
                                 to_user in uid)
        @ndb.transactional
        def pay():
            for b in balances:
                b.value = 0
            b.put()
        pay()
