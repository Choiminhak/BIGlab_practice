#!/bin/bash

# Written by mhchoi
# Date: 23-04-03

input_vcf=$1
type_info=$2
outname=$3

# 1.Filter out Korean KoVa2 SNP & INDEL with more than 1% AF
#echo "python /EXTDATA/mhchoi/0.Denovo_mutation_project/0.The_Scripts_and_pipelines_for_calling_the_DNMs/0.GATK_GenomicsDBImport_to_PossibleDenovo/0.Total_pipelines_for_dSNV_dINDEL/Pipeline_test_20220818/0.GATK_4.2.6.1/KoVa2_Filter.230403.py -iv $input_vcf -t $type_info"
python /EXTDATA/mhchoi/0.Denovo_mutation_project/0.The_Scripts_and_pipelines_for_calling_the_DNMs/0.GATK_GenomicsDBImport_to_PossibleDenovo/0.Total_pipelines_for_dSNV_dINDEL/Pipeline_test_20220818/0.GATK_4.2.6.1/KoVa2_Filter.230403.py -iv $input_vcf -t $type_info

source ~/.bash_profile
echo "echtvar anno -e /home/mhchoi/2.Reference/4.Gnomad/gnomad.v3.1.2.echtvar.v2.zip -i 'gnomad_af < 0.01' ${outname}.non_KoVa2.sort.vcf.gz ${outname}.non_KnownVariant.vcf.gz"
echtvar anno -e /home/mhchoi/2.Reference/4.Gnomad/gnomad.v3.1.2.echtvar.v2.zip -i 'gnomad_af < 0.01' ${outname}.non_KoVa2.sort.vcf.gz ${outname}.non_KnownVariant.vcf.gz
gzip -d ${outname}.non_KnownVariant.vcf.gz
