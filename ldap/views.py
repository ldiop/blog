from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render
import ldap3
from ldap3 import Server, Connection, ALL, SUBTREE, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException, LDAPBindError
from . import getuidnumber

from .forms import EmailForm
# Create your views here.


def connect_ldap_server():
    try:

        # Provide the hostname and port number of the openLDAP
        server_uri = f"ldap://www.adiop.fr:389"
        server = Server(server_uri, get_info=ALL)
        # username and password can be configured during openldap setup
        connection = Connection(server,
                     user='uid=adiop,dc=adiop,dc=net',
                     password='UtBX4PzS')
        bind_response = connection.bind()  # Returns True or False
    except LDAPBindError as e:
        connection = e

@login_required(login_url='acceslogin')
def index(request):
    server_uri = f"ldap://www.adiop.fr:389"
    server = Server(server_uri, get_info=ALL)
    connection = Connection(server,
                            user='uid=adiop,dc=adiop,dc=net',
                            password='UtBX4PzS')
    bind_response = connection.bind()
    # Provide a search base to search for.
    search_base = 'ou=Public,dc=adiop,dc=net'
    # provide a uidNumber to search for. '*" to fetch all users/groups
    search_filter = '(uid=*)'

    # Establish connection to the server
    ldap_conn = connection
    try:
        # only the attributes specified will be returned


        ldap_conn.search('ou=Public,dc=adiop,dc=net', '(&(objectclass=*))',
        #ldap_conn.search('ou=Public,dc=adiop,dc=net', '(& (objectclass= *)(uidNumber=510))',

                    attributes=['uid', 'mail', 'displayName', 'uidNumber'])
        # search will not return any values.
        # the entries method in connection object returns the results
        emailis = connection.entries
        emailist = [i for i in emailis if i is not None]
        #print(emailist)
    except LDAPException as e:
        results = e



    paginator = Paginator(emailist, 12)
    page = request.GET.get('page')
    emailist = paginator.get_page(page)

    context = {'emailist': emailist}
    return render(request, 'emailusers.html', context)

@login_required(login_url='acceslogin')
def indexb(request):
    total_entries = 0
    server_uri = f"ldap://www.adiop.fr:389"
    server = Server(server_uri, get_info=ALL)
    c = Connection(server, user='uid=adiop,dc=adiop,dc=net', password='UtBX4PzS')
    bind_response = c.bind()

    c.search(search_base='ou=Public,dc=adiop,dc=net',
             search_filter='(objectClass=*)',
             search_scope=SUBTREE,
             attributes=['uid', 'mail', 'displayName', 'uidNumber'],
             paged_size=5)
    total_entries += len(c.response)
    #for entry in c.entries:
        # print(entry['dn'], entry['attributes'])
        #print(entry.uid.value, entry.displayName.value, entry.mail.value)

    cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
    while cookie:
        c.search(search_base='ou=Public,dc=adiop,dc=net',
                 search_filter='(objectClass=*)',
                 search_scope=SUBTREE,
                 attributes=['uid', 'mail', 'displayName', 'uidNumber'],
                 paged_size=5,
                 paged_cookie=cookie)
        total_entries += len(c.response)
        cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
        for entry in c.entries:
             print(entry['dn'], entry['attributes'])
             print(entry.uid.value, entry.displayName.value, entry.mail.value)

    print('Total entries retrieved:', total_entries)
    emailistb = c.entries
    context = {'emailist': emailistb}
    return render(request, 'emailusers.html', context)


@login_required(login_url='acceslogin')
def email_detail(request, mpk):
    server_uri = f"ldap://www.adiop.fr:389"
    server = Server(server_uri, get_info=ALL)
    connection = Connection(server,
                            user='cn=admin,dc=adiop,dc=net',
                            password='UtBX4PzS')
    bind_response = connection.bind()
    search_base = 'ou=Public,dc=adiop,dc=net'
    mpkey = mpk

    search = "(uidNumber={})".format(mpkey)
    search_filter = search
    ldap_conn = connection
    try:
        ldap_conn.search(search_base=search_base,
                         search_filter=search_filter,
                         search_scope=SUBTREE,
                         attributes=['uidNumber', 'uid', 'mail', 'userPassword', 'displayName', 'vacationInfo', 'vacationActive', 'telephoneNumber'])
        results = connection.response
    except LDAPException as e:
        results = e
    maildetailb = ldap_conn.entries
    uid = maildetailb[0]['uid']
    uidNumber = maildetailb[0]['uidNumber']
    userPassword = maildetailb[0]['userPassword']
    mail = maildetailb[0]['mail']
    displayName = maildetailb[0]['displayname']
    vacationActive = maildetailb[0]['vacationActive']
    vacationInfo = maildetailb[0]['vacationInfo']
    telephoneNumber = maildetailb[0]['telephoneNumber']

    #print("BTOTALITE", maildetailb[0])
    #print( "MPKEY", mpkey, "MPK" ,mpk)
    context = {'mpkey': mpkey, 'uid': uid, 'uidNumber':uidNumber, 'mail': mail, 'displayName':displayName, 'vacationActive': vacationActive, 'vacationInfo':vacationInfo, 'telephoneNumber':telephoneNumber}
    return render(request, 'emailusers_detail.html', context)

@login_required(login_url='acceslogin')
def t_email_add(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            ldap_attr = {}
            #ldap_attr['objectclass'] = ["person", "organizationalPerson", "inetOrgPerson", "posixAccount", "top","shadowAccount"]
            ldap_attr_obj = ["inetOrgPerson", "posixAccount","sambaSamAccount","amavisAccount","shadowAccount","mailAccount", "vacation"]
            ldap_attr['cn'] = form.cleaned_data[ 'cn' ]
            ldap_attr['sn'] = form.cleaned_data[ 'sn' ]
            ldap_attr['mail'] = form.cleaned_data[ 'mail']
            ldap_attr['userPassword'] = form.cleaned_data[ 'userPassword']
            ldap_attr['telephoneNumber'] = form.cleaned_data[ 'telephoneNumber']
            ldap_attr['uid'] = form.cleaned_data[ 'sn' ]+"."+form.cleaned_data['cn']
            useruid = form.cleaned_data[ 'sn' ]+"."+form.cleaned_data['cn']
            ldap_attr['uidNumber'] = uidkey = getuidnumber.getuidnumber()
            ldap_attr['gidNumber'] = 100
            ldap_attr['accountActive'] = 'TRUE'
            ldap_attr['amavisBannedFilesLover'] = 'FALSE'
            ldap_attr['amavisBypassSpamChecks'] = 'FALSE'
            ldap_attr['amavisBypassVirusChecks'] = 'FALSE'
            ldap_attr['amavisSpamKillLevel'] = '2.0'
            ldap_attr['amavisSpamLover'] =  'FALSE'
            ldap_attr['amavisSpamModifiesSubj'] = 'FALSE'
            ldap_attr['amavisSpamTag2Level'] = '2.0'
            ldap_attr['amavisSpamTagLevel'] = '-999'
            ldap_attr['amavisVirusLover'] = 'FALSE'
            ldap_attr['amavisWhiteListSender'] = "contact@adiop.fr"
            ldap_attr['homeDirectory'] = form.cleaned_data['cn']
            ldap_attr['givenName'] = form.cleaned_data['cn']
            ldap_attr['displayName'] = form.cleaned_data['sn']+form.cleaned_data['cn']
            ldap_attr['facsimileTelephoneNumber'] = form.cleaned_data['telephoneNumber']
            ldap_attr['vacationActive'] = str(form.cleaned_data['vacationActive']).upper()
            #ldap_attr['vacationActive'] = True
            ldap_attr['vacationInfo'] = form.cleaned_data['vacationInfo']
            ldap_attr['ou'] = 'Nom Service'
            ldap_attr['postalAddress'] = 'Saisissez adresse'
            ldap_attr['postalCode'] = "11111"
            ldap_attr['postOfficeBox'] = 'Paris'
            ldap_attr['l'] = "Paris"
            ldap_attr['title'] = "usager"
            ldap_attr['mailDrop'] = form.cleaned_data['mail']
            ldap_attr['mailhost'] = 'localhost'# "mailhost" "localhost";
            ldap_attr['loginShell'] = "/bin/false"
            ldap_attr['sambaSID'] = "S-1-5-21-1947415551-996157374-1848903544-2079"
            server = Server('www.adiop.fr')
            conn = Connection(server, user='cn=admin,dc=adiop,dc=net', password='UtBX4PzS')
            #conn.bind()
            # Provide a search base to search for.
            # Bind connection to LDAP server
            ldap_conn = conn
            ldap_conn.bind()
            # this will create testuser inside group1
            #user_dn = "'uid= %s' %(uid), ou=Public,dc=adiop,dc=net"
            user_dn = "uid="+form.cleaned_data[ 'sn' ]+"."+form.cleaned_data['cn']+", ou=Public,dc=adiop,dc=net"
            user_uid = [form.cleaned_data[ 'sn' ]+"."+form.cleaned_data['cn']]
            print(user_dn)
            print(ldap_attr)
            #ldap_conn.search('ou=Public,dc=adiop,dc=net', uid=user_uid,
             #           attributes='uid')

            #ldap_conn.add(dn=user_dn, object_class=ldap_attr_obj, attributes=ldap_attr)
            try:
                ldap_conn.add(dn=user_dn, object_class=ldap_attr_obj, attributes = ldap_attr)
                #response = ldap_conn.add(user_dn, ldap_attr_obj, ldap_attr)
            #except LDAPException as e:
            except:
                response = "Erreur"
                context = {response: response}
                return render(request, 'emailusers_add.html', context)
            return redirect('t_email_detail',uidkey)
            #return render(request, 'emailusers_add.html')
    else:
        form = EmailForm()
    context = {'form': form}
    return render(request, 'emailusers_add.html', context)

@login_required(login_url='acceslogin')
def t_email_edit(request, mpk):
    form = EmailForm(request.POST)
    server_uri = f"ldap://www.adiop.fr:389"
    server = Server(server_uri, get_info=ALL)
    connection = Connection(server,
                            user='cn=admin,dc=adiop,dc=net',
                            password='UtBX4PzS')
    bind_response = connection.bind()

    search_base = 'ou=Public,dc=adiop,dc=net'
    mpkey = mpk

    search = "(uidNumber={})".format(mpkey)
    search_filter = search
    ldap_conn = connection
    #try:
    ldap_conn.search(search_base=search_base,
                         search_filter=search_filter,
                         search_scope=SUBTREE,
                         attributes=['cn', 'sn', 'mail', 'userPassword', 'telephoneNumber', 'vacationInfo',
                                     'vacationActive'])


    #except LDAPException as e:
    #    results = e
    #    print(results)
    results = ldap_conn.entries
    print("Resultats", results)
    userdetailb = results
    request.method = 'POST'
    data = {'cn': userdetailb[0]['cn'], 'sn':userdetailb[0]['sn'], 'userPassword':userdetailb[0]['userPassword'],
            'mail':userdetailb[0]['mail'], 'telephoneNumber':userdetailb[0]['telephoneNumber'],
            'vacationActive':userdetailb[0]['vacationActive'], 'vacationInfo':userdetailb[0]['vacationInfo']}

    if request.method == 'POST':

        form = EmailForm(request.POST, initial=data)
        print( "Voici", userdetailb)
        if form.is_valid():
            user_dn =  "uid=" + form.cleaned_data['sn'] + "." + form.cleaned_data['cn'] + ", ou=Public,dc=adiop,dc=net"
            ldap_conn.modify(user_dn,
                     {'cn': [(MODIFY_REPLACE, [form.cleaned_data['cn']])],
                      'sn': [(MODIFY_REPLACE, [form.cleaned_data['sn']])],
                      'mail': [(MODIFY_REPLACE, [form.cleaned_data['mail']])],
                      'userPassword': [(MODIFY_REPLACE, [form.cleaned_data['userPassword']])],
                      'telephoneNumber': [(MODIFY_REPLACE, [form.cleaned_data['telephoneNumber']])],
                      'vacationActive': [(MODIFY_REPLACE, [str(form.cleaned_data['vacationActive']).upper()])],
                      'vacationInfo': [(MODIFY_REPLACE, [form.cleaned_data['vacationInfo']])]})
            return redirect('t_email_detail', mpk)

        else:
            form = EmailForm(initial=data)
        context = {'form': form}
        return render(request, 'emailusers_add.html', context)

def t_email_delete(request, mpk):
    server_uri = f"ldap://www.adiop.fr:389"
    server = Server(server_uri, get_info=ALL)
    connection = Connection(server,
                            user='cn=admin,dc=adiop,dc=net',
                            password='UtBX4PzS')
    bind_response = connection.bind()

    search_base = 'ou=Public,dc=adiop,dc=net'
    mpkey = mpk

    search = "(uidNumber={})".format(mpkey)
    search_filter = search
    ldap_conn = connection
    # try:
    ldap_conn.search(search_base=search_base,
                     search_filter=search_filter,
                     search_scope=SUBTREE,
                     attributes=['uid', 'sn', 'mail', 'displayName'])


    # except LDAPException as e:
    #    results = e
    #    print(results)
    results = ldap_conn.entries
    print("Resultats", results)

    emaildetailb = ldap_conn.entries
    uid = emaildetailb[0]['uid']
    mail = emaildetailb[0]['mail']
    displayName = emaildetailb[0]['displayname']


    if request.method == 'POST':
        user_dn = "uid="+str(uid)+", ou=Public,dc=adiop,dc=net"
        ldap_conn.delete(user_dn)

        return redirect('/')
    context = {'mail': mail, 'displayName': displayName,'uid': uid}
    return render(request, 'emailusers_delete.html', context)


