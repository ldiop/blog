from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPException


server_uri = f"ldap://www.adiop.fr:389"
server = Server(server_uri, get_info=ALL)
connection = Connection(server,
                            user='uid=adiop,dc=adiop,dc=net',
                            password='UtBX4PzS')
bind_response = connection.bind()
    # Provide a search base to search for.
search_base = 'ou=Public,dc=adiop,dc=net'
    # provide a uidNumber to search for. '*" to fetch all users
search_filter = '(uidNumber=*)'
ldap_conn = connection
try:
# only the attributes specified will be returne
    ldap_conn.search('ou=Public,dc=adiop,dc=net', '(&(objectclass=*))',
                    attributes=['uidNumber'])
    uidlis = ldap_conn.entries
    uidlist = [i for i in uidlis if i is not None]
except LDAPException as e:
    results = e
#print(uidlist)

def valuid():
    uidNumtemp = 0
    return uidNumtemp
    results = e
uidlist = uidlist = [i for i in ldap_conn.entries if i is not None]
uidNumtemp = valuid()
uidlistall = []
uidNum = 0
#print("TYPEDE", uidlist)

for i in uidlist:
    if i.uidNumber.value:
        uidlistall.append(i.uidNumber.value)
        uidNum = i.uidNumber.value
        #print(type(uidNum), uidNum)
        #print("UIDLISTALL", uidlistall)
        # print(max(uidlistall))
newUid = int(max(uidlistall)) + 1
def valuidnewuid():
    newuidNum = newUid
    return newuidNum
valuidnewuid()