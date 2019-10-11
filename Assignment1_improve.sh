
#!/bin/bash

echo 'Please make sure you copied all your fq.gz file in ./fastq/'
echo 'You genome sequence should be in the dir ./genome/ in fasta.gz'
echo 'Please put your bedfile in ./bed/'

echo 'Please enter the file name of your slender sequence data'
read -a slender
echo 'Please enter the file name of your stumpy sequence data'
read -a stumpy
all =("${slender[*]}""${stumpy[*]}")

# Step 1: quality check on the paried-end raw sequence data

echo "Step 1: quality check on the paried-end raw sequence data"
cd ./fastq

for file in ./${all[*]}_1.fq.gz
do
	fastqc -q ${file}.fq.gz
done
for file in ./${all[*]}_2.fq.gz
do
	fastqc -q ${file}.fq.gz
done

echo "Step1 done."

# Step 2: assess the numbers and quality of the raw sequence data

echo "Step 2: assess the numbers and quality of the raw sequence data"
for zip in ./${all[*]}.zip
do
	unzip $zip
done
rm ./${all[*]}.zip

for dir in ./*
do
	if test -d $dir
	then
		more $dir/summary.txt >> quality_of_raw_data.txt
		grep "Total Sequences" $dir/fastqc_data.txt >> quality_of_raw_data.txt
		grep "Sequences flagged as poor quality" $dir/fastqc_data.txt >> quality_of_raw_data.txt
		grep "Sequence length" $dir/fastqc_data.txt >> quality_of_raw_data.txt
		echo $'\n' >> quality_of_raw_data.txt
	fi
done

echo "Your quality assess of raw sequence data have been saved in quality_of_raw_data.txt"
echo "Step2 done."

# Step 3: align the read pairs and transfer to bam format

echo "Step3 started..."
gzip ../genome/*.fasta.gz -d
bowtie2-build ../genome/*.fasta genome

for file in ./${all[*]}_1.fq.gz
do
	bowtie2 -p 8 -x genome -1 $file -2 ${file:0:0-8}_2.fq.gz -S ${file:0:0-8}.sam
	samtools sort ${file:0:0-8}.sam > ${file:0:0-8}.bam
done
echo "Step3 done."

#Step 4: Generate counts data in bed format

echo "Step4 started..."
for file in ./*.bam
do
	samtools index ${file:0:0-4}.bam
	bedtools multicov -bams ${file:0:0-4}.bam -bed ../bed/*.bed > ${file:0:0-4}.txt
done
echo "Step4 done."

#Step 5: Generate output data

echo "Step5 started..."

awk '{print NR,$4}' ${all[0]}.txt > initial.tmp
for file in ./${all[*]}.txt
do
	awk '{print NR,$7}' ${file}.txt > ${file}.tmp
	join initial.tmp ${file}.tmp > initial1.tmp
	rm initial.tmp
	mv initial1.tmp initial.tmp
done
mv initial.tmp initial.txt

awk 'BEGIN{OFS = "\t"};{print $0}}' tmp.txt >> output.txt
echo "Step5 done."

echo "PLease check your output at ./fastq/output.txt"
