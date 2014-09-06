echo "Moving used choice outputs back into circulation!";
if [ `ls -1 old_choice_outputs` ]; then
	mv old_choice_outputs/* choice_outputs/;
else
	echo "Couldn't find any old outputs to move!";
fi