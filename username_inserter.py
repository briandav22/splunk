import psycopg2


        
class Add_users:
    ## Handles the database connection
    def __init__(self,db_name,user,password,scrut_ip):
        try:
            self.conn = psycopg2.connect(f"dbname={db_name} user={user} password={password} host={scrut_ip}")
            print('Connected to Plixer DB')
        except psycopg2.Error as err:
            print(" Error: ", err)
        self.cur = self.conn.cursor()

    #method used to insert into DB
    def insert_users(self, ip, user_name, domain, data_source):

        query = (f"INSERT INTO plixer.summary_authentication_ip( ipaddress, username, domain, datasource, first_seen, last_login, last_logoff) VALUES (inet_a2b('{ip}'),'{user_name}','{domain}','{data_source}',UNIX_TIMESTAMP(NOW()),UNIX_TIMESTAMP(NOW()),UNIX_TIMESTAMP(NOW() + '86400 seconds')) ON CONFLICT (ipaddress,username,machine_name) DO UPDATE SET  last_login = UNIX_TIMESTAMP(NOW());")
        self.cur.execute(query)
        self.conn.commit()
        


    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print('disconnected from DB')
        





