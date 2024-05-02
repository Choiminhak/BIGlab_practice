#####################
# Written by mhchoi #
# Date: 2024-03-13  #
#####################

def target_variants_parser(input_file):
	ins_count = 0; del_count = 0

	chr_Dic = dict()
	for a in range(1, 23):
		chr_Dic.setdefault('chr{0}'.format(a), 0)

	chr_Dic.setdefault('chrX', 0)
	chr_Dic.setdefault('chrY', 0)

	with open(input_file, 'r') as f:
		for lines in f:
			if not lines.startswith('#'):
				items = lines.strip().split('\t')

				if len(items[3]) < len(items[4]):
					del_count += 1
				else:
					ins_count += 1

				chr_Dic[items[0]] += 1

			# Pass the header line,
			else: pass

	#print ('INS/DEL ratio: {0}'.format(ins_count/float(del_count)))

	return ins_count, del_count, chr_Dic,

def main(args):
	v_count_1 = subprocess.check_output(\
				'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.2_0.8.non_LCR.non_KnownVariant.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.2_0.8.non_LCR.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.2_0.8.vcf |'\
				' awk {1}{2}print $1,$2,$4,$5{3}{1} | sort | uniq | wc -l'\
				.format(args.input_name, "'", "{", "}"), shell = True)
	v_count_2 = subprocess.check_output(\
				'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.3_0.7.non_LCR.non_KnownVariant.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.3_0.7.non_LCR.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.3_0.7.vcf |'\
				' awk {1}{2}print $1,$2,$4,$5{3}{1} | sort | uniq | wc -l'\
				.format(args.input_name, "'", "{", "}"), shell = True)
	v_count_3 = subprocess.check_output(\
				'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.4_0.6.non_LCR.non_KnownVariant.vcf '\
				#'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.4_0.6.non_LCR.vcf '\
				#'grep -v {1}#{1} {0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.4_0.6.vcf '\
				'| awk {1}{2}print $1,$2,$4,$5{3}{1} | sort | uniq | wc -l'\
				.format(args.input_name, "'", "{", "}"), shell = True)

	ins_count_1, del_count_1, chr_Dic_1 = target_variants_parser('{0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.AB_Filter.0.3_0.7.vcf'\
												.format(args.input_name))

	ins_count_2, del_count_2, chr_Dic_2 = target_variants_parser('{0}.true_DNM.dINDEL.Local_HC.true_DNM.INDEL.'\
															     'AB_Filter.0.3_0.7.non_LCR.non_KnownVariant.vcf'\
												.format(args.input_name))

	if ins_count_1 > 0 and del_count_1 > 0:
		if ins_count_2 > 0 and del_count_2 > 0:
			print ('{0}\t{1}\t{2}\t{3}\t{4}\t'\
				   '{5}\t{6}\t{7}\t{8}\t{9}\t'\
				   '{10}\t{11}\t{12}\t{13}\t{14}\t'\
				   '{15}\t{16}\t{17}\t{18}\t{19}\t'\
				   '{20}\t{21}\t{22}\t{23}\t{24}\t'\
				   '{25}\t{26}\t{27}\t{28}\t'\
				   .format(\
				   v_count_1.decode().strip(), v_count_2.decode().strip(), v_count_3.decode().strip(),\
				   ins_count_1/float(del_count_1), ins_count_2/float(del_count_2),\
				   chr_Dic_2['chr1'], chr_Dic_2['chr2'], chr_Dic_2['chr3'], chr_Dic_2['chr4'], chr_Dic_2['chr5'],\
				   chr_Dic_2['chr6'], chr_Dic_2['chr7'], chr_Dic_2['chr8'], chr_Dic_2['chr9'], chr_Dic_2['chr10'],\
				   chr_Dic_2['chr11'], chr_Dic_2['chr12'], chr_Dic_2['chr13'], chr_Dic_2['chr14'], chr_Dic_2['chr15'],\
				   chr_Dic_2['chr16'], chr_Dic_2['chr17'], chr_Dic_2['chr18'], chr_Dic_2['chr19'], chr_Dic_2['chr20'],\
				   chr_Dic_2['chr21'], chr_Dic_2['chr22'], chr_Dic_2['chrX'], chr_Dic_2['chrY']))
		else:
			print ('{0}\t{1}\t{2}\t{3}\t{4}\t'\
				   '{5}\t{6}\t{7}\t{8}\t{9}\t'\
				   '{10}\t{11}\t{12}\t{13}\t{14}\t'\
				   '{15}\t{16}\t{17}\t{18}\t{19}\t'\
				   '{20}\t{21}\t{22}\t{23}\t{24}\t'\
				   '{25}\t{26}\t{27}\t{28}\t'\
				   .format(\
				   v_count_1.decode().strip(), v_count_2.decode().strip(), v_count_3.decode().strip(),\
				   ins_count_1/float(del_count_1), 0,\
				   chr_Dic_2['chr1'], chr_Dic_2['chr2'], chr_Dic_2['chr3'], chr_Dic_2['chr4'], chr_Dic_2['chr5'],\
				   chr_Dic_2['chr6'], chr_Dic_2['chr7'], chr_Dic_2['chr8'], chr_Dic_2['chr9'], chr_Dic_2['chr10'],\
				   chr_Dic_2['chr11'], chr_Dic_2['chr12'], chr_Dic_2['chr13'], chr_Dic_2['chr14'], chr_Dic_2['chr15'],\
				   chr_Dic_2['chr16'], chr_Dic_2['chr17'], chr_Dic_2['chr18'], chr_Dic_2['chr19'], chr_Dic_2['chr20'],\
				   chr_Dic_2['chr21'], chr_Dic_2['chr22'], chr_Dic_2['chrX'], chr_Dic_2['chrY']))
	else:
		print ('{0}\t{1}\t{2}\t{3}\t{4}\t'\
			   '{5}\t{6}\t{7}\t{8}\t{9}\t'\
			   '{10}\t{11}\t{12}\t{13}\t{14}\t'\
			   '{15}\t{16}\t{17}\t{18}\t{19}\t'\
			   '{20}\t{21}\t{22}\t{23}\t{24}\t'\
			   '{25}\t{26}\t{27}\t{28}\t'\
			   .format(\
			   v_count_1.decode().strip(), v_count_2.decode().strip(), v_count_3.decode().strip(),\
			   0, 0,\
			   chr_Dic_2['chr1'], chr_Dic_2['chr2'], chr_Dic_2['chr3'], chr_Dic_2['chr4'], chr_Dic_2['chr5'],\
			   chr_Dic_2['chr6'], chr_Dic_2['chr7'], chr_Dic_2['chr8'], chr_Dic_2['chr9'], chr_Dic_2['chr10'],\
			   chr_Dic_2['chr11'], chr_Dic_2['chr12'], chr_Dic_2['chr13'], chr_Dic_2['chr14'], chr_Dic_2['chr15'],\
			   chr_Dic_2['chr16'], chr_Dic_2['chr17'], chr_Dic_2['chr18'], chr_Dic_2['chr19'], chr_Dic_2['chr20'],\
			   chr_Dic_2['chr21'], chr_Dic_2['chr22'], chr_Dic_2['chrX'], chr_Dic_2['chrY']))

if __name__ == '__main__':
	import sys, argparse, subprocess
	parser = argparse.ArgumentParser(description = '')
	parser.add_argument('-i', '--input_name', type = str, help = '')
	args = parser.parse_args()
	main(args)
