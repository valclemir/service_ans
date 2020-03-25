LOGDIRECTORY='/var/log'
FILELOGNAME='service-ans.log'
DIR='/home/suporte/service_ans'
DIRECTORYTOEXEC=$DIR

TIMESLEEP=7200
FLGSILENT=1

FILELOG=$LOGDIRECTORY/$FILELOGNAME

print () {
    if [[ $FLGSILENT -gt 0 ]]; then
	echo $1 >> $FILELOG &
    fi
}

execTo () {
    python3 $1 1>> $2 2>> $2  #Executa em paralelo
}

if [[ -e $DIRECTORYTOEXEC ]]; then
    print "Run Files"
    while [[ true ]]; do
	    FILESPY=$DIR/controlers.py
            print "Monitor $FILESPY"
	    execTo $FILESPY $FILELOG & #@ Roda em paralelo
            sleep $TIMESLEEP;
    done;
else
    print "not exist directory"
fi

