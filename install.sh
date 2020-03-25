#!/bin/bash

echo "INICIANDO A CONFIGURACAO DO SERVICO..."

lib="/lib/systemd/system/ans.service"
etc="/etc/systemd/system/ans.service"


DIRSERVICE="/usr/bin/ans.sh"


cp -r /home/suporte/service_ans/ans.sh $DIRSERVICE #copia o arquivo do servico para o caminho /usr/bin/
chmod +x $DIRSERVICE
echo $DIRSERVICE

#@ ARQUIVO DE CONFIGURACAO DO SERVICO 
echo  "
[Unit]
Description=Rotina de coleta ANS
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/bin/bash $DIRSERVICE
StandardInput=tty-force

[Install]
WantedBy=multi-user.target


" > $lib
#echo $lib $etc
cp -r $lib $etc
chmod 644 $etc



#systemctl start ans
systemctl enable ans #@ Habilita o servico para iniciar com o SO 

echo "SERVICO CONFIGURADO COM SUCESSO!"

