md=(3 4 5 6 7)
ne=(400 600 800 1000 1200)
lr=(0.01 0.1 0.5)

for md_i in ${md[@]}
do
    for ne_i in ${ne[@]}
    do
        for lr_i in ${lr[@]}
        do
            sed 's/MD/'$md_i'/g' <qsub_template.in >qsub.in
            sed 's/NE/'$ne_i'/g' -i qsub.in
            sed 's/LR/'$lr_i'/g' -i qsub.in
            qsub -A bakx qsub.in
        done
    done
done
