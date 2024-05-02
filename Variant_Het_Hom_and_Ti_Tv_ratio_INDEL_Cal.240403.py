#####################
# Written by mhchoi #
# Date: 2024-04-03  #
#####################

def target_variants_parser(input_file, child_name, father_name, mother_name):
	Hom_count = 0;  Het_count = 0
	Ti_Tv_Dic = {'Ti':{'A-G':0,'G-A':0,'C-T':0,'T-C':0}, \
				 'Tv':{'A-C':0,'A-T':0,'C-A':0,'T-A':0,'G-C':0,'G-T':0,'C-G':0,'T-G':0}}

	chr_Dic = dict()
	for x in range(1, 23):
		chr_Dic.setdefault('chr{0}'.format(x), 0)

	with open(input_file, 'r') as f:
		for lines in f:
			if not lines.startswith('#'):
				items = lines.strip().split('\t')

				if items[0] in chr_Dic:
					c_gt = items[c_index].split(':')[0]
					f_gt = items[f_index].split(':')[0]
					m_gt = items[m_index].split(':')[0]

					# Hom/Het count
					if (c_gt == '1/1') or (c_gt == '1|1'): Hom_count += 1
					elif c_gt != '1/1' and c_gt != '1|1': Het_count += 1
					else: pass

					# Ti/Tv count
					if 'A-G' in '{0}-{1}'.format(items[3], items[4]) or \
					   'G-A' in '{0}-{1}'.format(items[3], items[4]) or \
					   'C-T' in '{0}-{1}'.format(items[3], items[4]) or \
					   'T-C' in '{0}-{1}'.format(items[3], items[4]):
						Ti_Tv_Dic['Ti']['{0}-{1}'.format(items[3], items[4])] += 1
					else:
						Ti_Tv_Dic['Tv']['{0}-{1}'.format(items[3], items[4])] += 1

					# Each chromosome count
					chr_Dic[items[0]] += 1

				# Pass the variants in sex chromosome
				else: pass

			# Pass the header line,
			# but I want to take the value of the index of the child sample
			else:
				if '#CHROM' in lines:
					c_index = int([n for n, a in enumerate(lines.strip().split('\t')) \
								   if child_name in a][0])
					f_index = int([n for n, a in enumerate(lines.strip().split('\t')) \
								   if father_name in a][0])
					m_index = int([n for n, a in enumerate(lines.strip().split('\t')) \
								   if mother_name in a][0])
				else: pass

	Ti_total_count = Ti_Tv_Dic['Ti']['A-G']+Ti_Tv_Dic['Ti']['G-A']+\
					 Ti_Tv_Dic['Ti']['C-T']+Ti_Tv_Dic['Ti']['T-C']
	Tv_total_count = Ti_Tv_Dic['Tv']['A-C']+Ti_Tv_Dic['Tv']['A-T']+\
					 Ti_Tv_Dic['Tv']['C-A']+Ti_Tv_Dic['Tv']['T-A']+\
					 Ti_Tv_Dic['Tv']['G-C']+Ti_Tv_Dic['Tv']['G-T']+\
					 Ti_Tv_Dic['Tv']['C-G']+Ti_Tv_Dic['Tv']['T-G']

	#return Het_count/float(Hom_count), Ti_Tv_Dic, Ti_total_count, Tv_total_count
	return Ti_Tv_Dic, Ti_total_count, Tv_total_count, chr_Dic

def main(args):
	v_count_1 = subprocess.check_output(\
				'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.2_0.8.non_LCR.non_KnownVariant.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.2_0.8.non_LCR.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.2_0.8.vcf |'\
				' awk {1}{2}print $1,$2,$4,$5{3}{1} | sort | uniq | grep -v "chrX" | grep -v "chrY" | wc -l'\
				.format(args.input_name, "'", "{", "}"), shell = True)
	v_count_2 = subprocess.check_output(\
				'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.3_0.7.non_LCR.non_KnownVariant.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.3_0.7.non_LCR.vcf |'\
				#'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.3_0.7.vcf |'\
				' awk {1}{2}print $1,$2,$4,$5{3}{1} | sort | uniq | grep -v "chrX" | grep -v "chrY" | wc -l'\
				.format(args.input_name, "'", "{", "}"), shell = True)
	v_count_3 = subprocess.check_output(\
				'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.4_0.6.non_LCR.non_KnownVariant.vcf '\
				#'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.4_0.6.non_LCR.vcf '\
				#'grep -v {1}#{1} {0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.4_0.6.vcf '\
				'| awk {1}{2}print $1,$2,$4,$5{3}{1} | sort | uniq | grep -v "chrX" | grep -v "chrY" | wc -l'\
				.format(args.input_name, "'", "{", "}"), shell = True)
	'''
	Het_Hom_ratio_1, Ti_Tv_Dic_1, Ti_total_count_1, Tv_total_count_1 = target_variants_parser(\
						   '{0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.2_0.8.vcf'.format(args.input_name), \
						   args.child_name, args.father_name, args.mother_name)

	Het_Hom_ratio_2, Ti_Tv_Dic_2, Ti_total_count_2, Tv_total_count_2 = target_variants_parser(\
						   '{0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.3_0.7.vcf'.format(args.input_name), \
						   args.child_name, args.father_name, args.mother_name)

	Het_Hom_ratio_3, Ti_Tv_Dic_3, Ti_total_count_3, Tv_total_count_3 = target_variants_parser(\
						   '{0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.4_0.6.vcf'.format(args.input_name), \
						   args.child_name, args.father_name, args.mother_name)
	'''

	Ti_Tv_Dic_1, Ti_total_count_1, Tv_total_count_1, chr_Dic_1 = target_variants_parser(\
						   '{0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.2_0.8.non_LCR.non_KnownVariant.vcf'.format(args.input_name), \
						   args.child_name, args.father_name, args.mother_name)

	Ti_Tv_Dic_2, Ti_total_count_2, Tv_total_count_2, chr_Dic_2 = target_variants_parser(\
						   '{0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.3_0.7.non_LCR.non_KnownVariant.vcf'.format(args.input_name), \
						   args.child_name, args.father_name, args.mother_name)

	Ti_Tv_Dic_3, Ti_total_count_3, Tv_total_count_3, chr_Dic_3 = target_variants_parser(\
						   '{0}.true_DNM.dSNV.Local_HC.true_DNM.SNV.AB_Filter.0.4_0.6.non_LCR.non_KnownVariant.vcf'.format(args.input_name), \
						   args.child_name, args.father_name, args.mother_name)

	'''
	print ('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}'\
		   '\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t'\
		   '{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}\t{30}'\
		   '{31}\t{32}\t{33}\t{34}\t{35}\t{36}\t{37}\t{38}\t{39}\t{40}'\
		   '{41}\t{42}\t{43}\t{44}'\
			.format(v_count_1.decode().strip(), v_count_2.decode().strip(), v_count_3.decode().strip(), \
					Het_Hom_ratio_1, Ti_total_count_1/float(Tv_total_count_1), \
					Het_Hom_ratio_2, Ti_total_count_2/float(Tv_total_count_2), \
					Het_Hom_ratio_3, Ti_total_count_3/float(Tv_total_count_3), \
					Ti_Tv_Dic_1['Ti']['A-G'], Ti_Tv_Dic_1['Ti']['G-A'], \
					Ti_Tv_Dic_1['Ti']['C-T'], Ti_Tv_Dic_1['Ti']['T-C'], \
					Ti_Tv_Dic_1['Tv']['A-C'], Ti_Tv_Dic_1['Tv']['A-T'], \
					Ti_Tv_Dic_1['Tv']['C-A'], Ti_Tv_Dic_1['Tv']['T-A'], \
					Ti_Tv_Dic_1['Tv']['G-C'], Ti_Tv_Dic_1['Tv']['G-T'], \
					Ti_Tv_Dic_1['Tv']['C-G'], Ti_Tv_Dic_1['Tv']['T-G'], \
					Ti_Tv_Dic_2['Ti']['A-G'], Ti_Tv_Dic_2['Ti']['G-A'], \
					Ti_Tv_Dic_2['Ti']['C-T'], Ti_Tv_Dic_2['Ti']['T-C'], \
					Ti_Tv_Dic_2['Tv']['A-C'], Ti_Tv_Dic_2['Tv']['A-T'], \
					Ti_Tv_Dic_2['Tv']['C-A'], Ti_Tv_Dic_2['Tv']['T-A'], \
					Ti_Tv_Dic_2['Tv']['G-C'], Ti_Tv_Dic_2['Tv']['G-T'], \
					Ti_Tv_Dic_2['Tv']['C-G' ], Ti_Tv_Dic_2['Tv']['T-G'], \
					Ti_Tv_Dic_3['Ti']['A-G'], Ti_Tv_Dic_3['Ti']['G-A'], \
					Ti_Tv_Dic_3['Ti']['C-T'], Ti_Tv_Dic_3['Ti']['T-C'], \
					Ti_Tv_Dic_3['Tv']['A-C'], Ti_Tv_Dic_3['Tv']['A-T'], \
					Ti_Tv_Dic_3['Tv']['C-A'], Ti_Tv_Dic_3['Tv']['T-A'], \
					Ti_Tv_Dic_3['Tv']['G-C'], Ti_Tv_Dic_3['Tv']['G-T'], \
					Ti_Tv_Dic_3['Tv']['C-G' ], Ti_Tv_Dic_3['Tv']['T-G']))
	'''

	print ('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}'\
		   '\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t'\
		   '{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}\t'\
		   '{30}\t{31}\t{32}\t{33}\t{34}\t{35}\t{36}\t{37}\t{38}\t{39}'\
			.format(v_count_1.decode().strip(), v_count_2.decode().strip(), v_count_3.decode().strip(), \
					Ti_total_count_1/float(Tv_total_count_1), \
					Ti_total_count_2/float(Tv_total_count_2), \
					Ti_total_count_3/float(Tv_total_count_3), \
					Ti_Tv_Dic_2['Ti']['A-G'], Ti_Tv_Dic_2['Ti']['G-A'], \
					Ti_Tv_Dic_2['Ti']['C-T'], Ti_Tv_Dic_2['Ti']['T-C'], \
					Ti_Tv_Dic_2['Tv']['A-C'], Ti_Tv_Dic_2['Tv']['A-T'], \
					Ti_Tv_Dic_2['Tv']['C-A'], Ti_Tv_Dic_2['Tv']['T-A'], \
					Ti_Tv_Dic_2['Tv']['G-C'], Ti_Tv_Dic_2['Tv']['G-T'], \
					Ti_Tv_Dic_2['Tv']['C-G' ], Ti_Tv_Dic_2['Tv']['T-G'], \
					chr_Dic_2['chr1'], chr_Dic_2['chr2'], chr_Dic_2['chr3'], \
					chr_Dic_2['chr4'], chr_Dic_2['chr5'], chr_Dic_2['chr6'], \
					chr_Dic_2['chr7'], chr_Dic_2['chr8'], chr_Dic_2['chr9'], \
					chr_Dic_2['chr10'], chr_Dic_2['chr11'], chr_Dic_2['chr12'], \
					chr_Dic_2['chr13'], chr_Dic_2['chr14'], chr_Dic_2['chr15'], \
					chr_Dic_2['chr16'], chr_Dic_2['chr17'], chr_Dic_2['chr18'], \
					chr_Dic_2['chr19'], chr_Dic_2['chr20'], chr_Dic_2['chr21'], \
				 	chr_Dic_2['chr22']))

if __name__ == '__main__':
	import sys, argparse, subprocess
	parser = argparse.ArgumentParser(description = '')
	parser.add_argument('-i', '--input_name', type = str, help = '')
	parser.add_argument('-c', '--child_name', type = str, help = '')
	parser.add_argument('-f', '--father_name', type = str, help = '')
	parser.add_argument('-m', '--mother_name', type = str, help = '')
	args = parser.parse_args()
	main(args)
