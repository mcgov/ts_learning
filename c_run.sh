#!/bin/sh

START_TIME=`date "+%m_%d_%Y_%H%M%S"`;
OUTPUT_FILENAME="CRUN_${START_TIME}";

TOP_DIR=`pwd`;
LOG_DIR="${TOP_DIR}/LOG";


OUTPUT_DIR="${TOP_DIR}/choice_outputs";

TEMP_OUTPUT_FILE="${LOG_DIR}/tempfile.rbl";

#make a temporary file;
if [ -e ${TEMP_OUTPUT_FILE} ]
then
	echo "Deleting old temporary files...";
	rm ${TEMP_OUTPUT_FILE};
fi

touch ${TEMP_OUTPUT_FILE};
#echo ${OUTPUT_FILE};

OUTPUT_DIR="${TOP_DIR}/choice_outputs";
OUTPUT_FILE="${OUTPUT_DIR}/${OUTPUT_FILENAME}.rbl";

python Choice.py  >> ${TEMP_OUTPUT_FILE};

if [ `wc -l ${TEMP_OUTPUT_FILE} | head -c1` != "4" ]; then
	echo "Something didn't come out right with this run!";
	cat ${TEMP_OUTPUT_FILE};
else
	echo "Sending temp output to ${OUTPUT_FILE}";
	mv ${TEMP_OUTPUT_FILE} ${OUTPUT_FILE};
fi

##This file should be a specific number of lines long...


  

 