from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError

ldap_attr = {}
ldap_attr['cn'] = "test user"
ldap_attr['sn'] = "AD"
ldap_attr['mail'] = "laye.diop@adiop.fr"
ldap_attr['userPassword'] = 'userPassword'
ldap_attr['telephoneNumber'] = "0123444445542373"
ldap_attr['uid'] = 'rolland'
ldap_attr['uidNumber'] = 878
ldap_attr['accountActive'] = "True"
ldap_attr['amavisBannedFilesLover'] = "False"
ldap_attr['amavisBypassSpamChecks'] = "False"
ldap_attr['amavisBypassVirusChecks'] = 'FALSE'
ldap_attr['amavisSpamKillLevel'] = '2.0'
ldap_attr['amavisSpamLover'] = 'FALSE'
ldap_attr['amavisSpamModifiesSubj'] = 'FALSE'
ldap_attr['amavisSpamTag2Level'] = '2.0'
ldap_attr['amavisSpamTagLevel'] = '-999'
ldap_attr['amavisVirusLover'] = 'False'
ldap_attr['amavisWhiteListSender'] = "contact@adiop.fr"
ldap_attr['homeDirectory'] = "home"
ldap_attr['givenName'] = "Lilou"
ldap_attr['displayName'] = "Laurent"
ldap_attr['gidNumber'] = 5000
ldap_attr['facsimileTelephoneNumber'] = '0133444444444'
ldap_attr['vacationActive'] = False
    # ldap_attr['vacationActive'] = True
ldap_attr['vacationInfo'] = "TEST VACANCES"
ldap_attr['ou'] = 'Nom Service'
ldap_attr['postalAddress'] = 'Saisissez adresse'
ldap_attr['postalCode'] = "11111"
ldap_attr['postOfficeBox'] = 'Paris'
ldap_attr['l'] = "Paris"
ldap_attr['title'] = "usager"
ldap_attr['mailDrop'] = "toto@tata.fr"
ldap_attr['mailhost'] = 'localhost'  # "mailhost" "localhost";
ldap_attr['loginShell'] = "/bin/false"
ldap_attr['sambaSID'] = "S-1-5-21-1947415551-996157374-1848903544-2079"
ldap_attr_obj = ["person", "organizationalPerson", "inetOrgPerson", "posixAccount", "top", "shadowAccount"]

    # Bind connection to LDAP server
    #ldap_conn = connect_ldap_server()
server_uri = f"ldap://www.adiop.fr:389"
server = Server(server_uri, get_info=ALL)
#ldap_conn = Connection(server,
Connection(server,
           user='uid=admin,dc=adiop,dc=net',
           password='UtBX4PzS')

#bind_response = Connection.bind()

#print(bind_response)    # this will create testuser inside group1
user_dn = "ou=Public,dc=adiop,dc=net"
Connection.add(dn=user_dn,object_class=ldap_attr_obj,attributes=ldap_attr)

#try:
 # object class for a user is inetOrgPerson
#  response = ldap_conn.add(dn=user_dn,
                              #   object_class=ldap_attr_obj,
                              #   attributes=ldap_attr)
#except LDAPException as e:
#  response = e
#print(response)

