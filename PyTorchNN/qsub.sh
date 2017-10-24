lr=(0.001 0.01 0.1)
dr=(0 0.001 0.01)
dp=(0 0.2 0.4 0.6)
hln=(64 128 256 512 1024)
nhl=(1 2 3 4 5)

for lr_i in ${lr[@]}
do
    for dr_i in ${dr[@]}
    do
        for dp_i in ${dp[@]}
        do
            for hln_i in ${hln[@]}
            do
                for nhl_i in ${nhl[@]}
                do
                    sed 's/LR/'$lr_i'/g' <qsub_template.in >qsub.in
                    sed 's/DR/'$dr_i'/g' -i qsub.in
                    sed 's/DP/'$dp_i'/g' -i qsub.in
                    sed 's/HLN/'$hln_i'/g' -i qsub.in
                    sed 's/NHL/'$nhl_i'/g' -i qsub.in
                    qsub -A bakx qsub.in
                done
            done
        done
    done
done
