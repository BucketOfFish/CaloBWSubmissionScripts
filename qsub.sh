nhyperparamcombos=20

((nhyperparamcombos--))
for hyperparamset in $(seq 0 $nhyperparamcombos)
do
    sed 's/HYPERPARAMSET/'$hyperparamset'/g' <qsub_template.in >qsub.in
    qsub qsub.in
done
