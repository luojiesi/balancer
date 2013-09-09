from google.appengine.ext import ndb

# key will be fbid
class User(ndb.Model):
    name = ndb.StringProperty()
    transactions = ndb.KeyProperty(kind='Transaction', repeated=True)

# use id as identifier
class Transaction(ndb.Model):
    date = ndb.DateTimeProperty()
    note = ndb.StringProperty()
    # a json object, format:
    # {uid1:amount1, uid2:amount2, ...}
    data = ndb.JsonProperty()

# use id
class Balance(ndb.Model):
    from_uer = ndb.KeyProperty(User)
    to_user = ndb.KeyProperty(User)
    value = ndb.FloatProperty()
