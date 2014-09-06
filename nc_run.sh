#!/bin/sh

START_TIME=`date "+%m_%d_%Y_%H%M%S"`;
OUTPUT_FILENAME="NC_RUN_${START_TIME}";

TOP_DIR=`pwd`;
LOG_DIR="${TOP_DIR}/LOG";
OUTPUT_DIR="${TOP_DIR}/no_choice_outputs";
INPUT_DIR="${TOP_DIR}/choice_outputs"; 
#this takes input from the output of the other one
ARCHIVE_DIR="${TOP_DIR}/old_choice_outputs";
OUTPUT_FILE="${OUTPUT_DIR}/${OUTPUT_FILENAME}";
#echo ${OUTPUT_FILE};
touch ${OUTPUT_FILE};

if [ `ls -1 choice_outputs/ | head -1` ]; then 
	INPUT_FILENAME=`ls -1 ${INPUT_DIR} | head -1`;
	echo "Found input  file ${INPUT_FILENAME}";

	USE_INPUT_FILE=${INPUT_DIR}/${INPUT_FILENAME};

	python No-Choice.py  ${USE_INPUT_FILE} >> ${OUTPUT_FILE};

	if [ `stat -c%s ${OUTPUT_FILE}` > 0 ];
	then
		echo "Moving ${USE_INPUT_FILE} to ${ARCHIVE_DIR}/${INPUT_FILENAME}"
		mv ${USE_INPUT_FILE} ${ARCHIVE_DIR}/${INPUT_FILENAME};
		#gzip -6 ${ARCHIVE_DIR}/${INPUT_FILENAME};
	else
		echo -e "\033[31mERROR:\033[0m There was no output printed to the output file!";
		echo "Input will be left in place and reused!";
	fi
else
	echo -e "\033[31mERROR:\033[0m Found no input files to use!";
fi


 