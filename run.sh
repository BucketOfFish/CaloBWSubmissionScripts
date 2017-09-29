rm -rf TrainedModels
#qsub qsub.in
source qsub.sh
mkdir Output
cp qsub.in Output/
cp CaloDNN/Classification* Output/
