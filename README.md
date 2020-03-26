#                              service_ans

Pacotes necessarios para que o serviço funcione:

      apt-get install python3  #Para dist baseadas em debian
      yum install python3 #Para dist baseadas em red hat 
      apt-get install python3-pip #Se não estiver usando o virtualenv
      
      
      pip3 install pandas
      pip3 install pymssql
      
#                              IMPORTANTE 
 O nome de todos os arquivos .xslx devem está no seguinte formato, exemplo:
 
      ARQ_CONF_ANS_2020_01
      No exexmplo acima, o arquivo é da competência de janeiro, ficando então: ARQ_CONF_ANS_2020_01
      
 Editar o arquivo "config.json" para atender as configurações de autênticação de banco de dados
