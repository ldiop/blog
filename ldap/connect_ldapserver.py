from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError


def connect_ldap_server():
    try:

        # Provide the hostname and port number of the openLDAP
        server_uri = f"ldap://www.adiop.fr:389"
        server = Server(server_uri, get_info=ALL)
        # username and password can be configured during openldap setup
        connection = Connection(server,
                                user='uid=adiop,dc=adiop,dc=net',
                                password=UtBX4PzS)
        bind_response = connection.bind()  # Returns True or False
    except LDAPBindError as e:
        connection = e