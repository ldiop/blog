from ldap3 import Server, Connection, ALL
server=Server('www.adiop.fr')
conn = Connection(server, user='cn=admin,dc=adiop,dc=net', password='UtBX4PzS')
conn.bind()

dn='uid=fredegonde,ou=Public,dc=adiop,dc=net'
object_class=['person', 'organizationalperson', 'inetorgperson',  "posixAccount", "top", "shadowAccount"]
ldap_values={'sn': 'neustrie', 'cn': 'neustrie fredegonde','homeDirectory': "Burgondie", 'gidNumber': 100, 'uid': 'fredegonde' ,'uidNumber': 904, 'mail': ['fredegonde@example.com', 'neustrie.example@example.com']}
conn.add(dn, object_class, ldap_values)