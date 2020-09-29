from username_inserter import Add_users

db_name = 'plixer'
scrutinizer_user = 'scrutremote'
scrutinizer_password = 'admin'
scrutinizer_host = '10.30.16.26'

test_db = Add_users(db_name,scrutinizer_user,scrutinizer_password,scrutinizer_host)

test_db.close_connection()