from username_inserter import Add_users

db_name = 'plixer'
scrutinizer_user = 'scrutremote'
scrutinizer_password = 'scrutinizerAdminPassword'
scrutinizer_host = 'scrutinizerIPAddress'

test_db = Add_users(db_name,scrutinizer_user,scrutinizer_password,scrutinizer_host)

test_db.close_connection()