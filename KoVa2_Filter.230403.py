#####################
# Written by mhchoi #
# Date: 2023-04-03  #
#####################

def KoVa2_info_Dic_Maker():
	KoVa2_info_Dic = dict()

	for x in range(1, 23):
		with open("/home/mhchoi/2.Reference/5.Korean/KoVa2/1_KOVA.v7.chr{0}.tsv".format(x), "r") as f:
			for lines in f:
				if 'chrom' not in lines:
					items = lines.strip().split('\t')

					# Target: AF >= 1% in KoVa2
					if float(items[8]) >= 0.01:
						# Type: indel
						if (len(items[2]) > 1) or (len(items[3]) > 1):
							## Save format: {INDEL, {chr_name, {position, set(Ref-Alt)}}}
							if 'INDEL' not in KoVa2_info_Dic:
								KoVa2_info_Dic.setdefault('INDEL', dict())\
											  .setdefault(items[0], dict())\
											  .setdefault(int(items[1]), set())\
											  .add('{0}-{1}'.format(items[2], items[3]))
							else:
								if items[0] not in KoVa2_info_Dic['INDEL']:
									KoVa2_info_Dic['INDEL'].setdefault(items[0], dict())\
												  .setdefault(int(items[1]), set())\
												  .add('{0}-{1}'.format(items[2], items[3]))
								else:
									if int(items[1]) not in KoVa2_info_Dic['INDEL'][items[0]]:
										KoVa2_info_Dic['INDEL'][items[0]]\
													  .setdefault(int(items[1]), set())\
													  .add('{0}-{1}'.format(items[2], items[3]))
									else:
										KoVa2_info_Dic['INDEL'][items[0]][int(items[1])]\
													  .add('{0}-{1}'.format(items[2], items[3]))
						# Type: Snp
						else:
							## Save format: {SNP, {chr_name, {position, set(Ref-Alt)}}}
							if 'SNP' not in KoVa2_info_Dic:
								KoVa2_info_Dic.setdefault('SNP', dict())\
											  .setdefault(items[0], dict())\
											  .setdefault(int(items[1]), set())\
											  .add('{0}-{1}'.format(items[2], items[3]))
							else:
								if items[0] not in KoVa2_info_Dic['SNP']:
									KoVa2_info_Dic['SNP'].setdefault(items[0], dict())\
												  .setdefault(int(items[1]), set())\
												  .add('{0}-{1}'.format(items[2], items[3]))
								else:
									if int(items[1]) not in KoVa2_info_Dic['SNP'][items[0]]:
										KoVa2_info_Dic['SNP'][items[0]]\
													  .setdefault(int(items[1]), set())\
													  .add('{0}-{1}'.format(items[2], items[3]))
									else:
										KoVa2_info_Dic['SNP'][items[0]][int(items[1])]\
													  .add('{0}-{1}'.format(items[2], items[3]))
					else: pass
				else:
					print (lines.strip().split('\t')[8])

	return KoVa2_info_Dic

def table_filter_by_KoVa2(KoVa2_info_Dic, input_table, type_info):
	outfile = open('{0}.non_KoVa2.table'.format(input_table.split('/')[-1].split('.table')[0]), 'w')

	with open(input_table, 'r') as f:
		for lines in f:
			if not lines.startswith('TYPE'):
				items = lines.strip().split('\t')

				if items[1] in KoVa2_info_Dic[type_info]:
					if int(items[2]) in KoVa2_info_Dic[type_info][items[1]]:
						if '{0}-{1}'.format(items[3], items[4]) in KoVa2_info_Dic[type_info][items[1]][int(items[2])]:
							pass
						else: outfile.write(lines)
					else: outfile.write(lines)
				else: outfile.write(lines)

				'''
				# Pass HC-BAM filter of the target
				if items[-6] == 'True':
					if items[1] in KoVa2_info_Dic[type_info]:
						if int(items[2]) in KoVa2_info_Dic[type_info][items[1]]:
							if '{0}-{1}'.format(items[3], items[4]) in KoVa2_info_Dic[type_info][items[1]][int(items[2])]:
								pass
							else: outfile.write(lines)
						else: outfile.write(lines)
					else: outfile.write(lines)
				else: pass
				'''
			else: outfile.write(lines)

	outfile.close()

def vcf_filter_by_KoVa2(KoVa2_info_Dic, input_VCF, type_info):
	if not os.path.isfile('./{0}.non_KoVa2.sort.vcf.gz'.format(input_VCF.split('/')[-1].split('.vcf')[0])):
		# 1. Filtering the variants in KoVa2
		outfile = open('{0}.non_KoVa2.vcf'.format(input_VCF.split('/')[-1].split('.vcf')[0]), 'w')

		#with gzip.open(input_VCF, 'r') as f:
		with open(input_VCF, 'r') as f:
			for lines in f:
				#lines = lines.decode("ascii")

				if not lines.startswith('#'):
					items = lines.strip().split('\t')

					## Save format: {INDEL, {chr_name, {position, set(Ref-Alt)}}}
					if items[0] in KoVa2_info_Dic[type_info]:
						if int(items[1]) in KoVa2_info_Dic[type_info][items[0]]:
							if '{0}-{1}'.format(items[3], items[4]) in KoVa2_info_Dic[type_info][items[0]][int(items[1])]:
								pass
							else: outfile.write(lines)
						else: outfile.write(lines)
					else: outfile.write(lines)

				# Write the header to output file
				else: outfile.write(lines)

		outfile.close()
		
		# 2. Compression the VCF file
		for e_cmd in ["source ~/.bash_profile", \
					  "time bcftools sort -m 30G -o {0}.non_KoVa2.sort.vcf.gz "\
					  "-O z -T denovo_candidate_sort_TMP {0}.non_KoVa2.vcf".format(input_VCF.split('.vcf')[0]), \
					  "mkdir IndexFeatureFile_TMP_KoVa2_{0}".format(type_info), \
					  "time gatk.4.2.6.1 --java-options {0}-Xms16g -Xmx16g -XX:+UseParallelGC -XX:ParallelGCThreads=15{0} "\
					  "IndexFeatureFile --input {1}.non_KoVa2.sort.vcf.gz --tmp-dir IndexFeatureFile_TMP_KoVa2_{2} "\
					  ">& gatk.IndexFeatureFile.KoVa2.running.log".format('"', input_VCF.split('.vcf')[0], type_info), \
					  "/bin/rm -rf {0}.non_KoVa2.vcf IndexFeatureFile_TMP_KoVa2_{1}".format(input_VCF.split('.vcf')[0], type_info)]:

			#print (e_cmd)
			subprocess.run(e_cmd, shell=True)
	else:
		pass

def main(args):
	if not os.path.isfile('./{0}.non_KoVa2.sort.vcf.gz'.format(args.input_VCF.split('/')[-1].split('.vcf')[0])):
		# Make KoVa2 files to Python dictionary form
		if not os.path.isfile("/home/mhchoi/2.Reference/5.Korean/KoVa2.dic"):
			KoVa2_info_Dic = KoVa2_info_Dic_Maker()
			
			with open("/home/mhchoi/2.Reference/5.Korean/KoVa2.dic", 'wb') as f:
				pickle.dump(KoVa2_info_Dic, f)
		else:
			with open("/home/mhchoi/2.Reference/5.Korean/KoVa2.dic", 'rb') as f:
				KoVa2_info_Dic = pickle.load(f)

		##################
		# Input table file
		if len(args.input_VCF) == 0:
			table_filter_by_KoVa2(KoVa2_info_Dic, args.input_table, args.type_info)

		# Input VCF file
		else:
			vcf_filter_by_KoVa2(KoVa2_info_Dic, args.input_VCF, args.type_info)
	else: pass

if __name__ == '__main__':
	import sys, argparse, pickle, os, gzip, subprocess
	parser = argparse.ArgumentParser(description = '')
	parser.add_argument('-iv', '--input_VCF', type = str, default = '', help = '')
	parser.add_argument('-it', '--input_table', type = str, default = '', help = '')
	parser.add_argument('-t', '--type_info', type = str, help = '')
	args = parser.parse_args()
	main(args)
