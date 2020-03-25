import json 

class Config:

    
    with open(r'/home/suporte/service_ans/config.json', 'r') as read_json:
        config_db = json.load(read_json)

    # Database config
    db_host = config_db['host']
    db_domain = config_db['domain']
    db_user = config_db['user']
    db_password = config_db['password']
    db_name = config_db['database']
    
    
    path = '/home/share_ans'

