#!/bin/bash

r1=(SRR10147881 SRR10147889 SRR10147888)
r2=(SRR10147883 SRR10147887 SRR10147886)
r3=(SRR10147880 SRR10147881 SRR10147883)
r4=(SRR10147882 SRR10147881 SRR10147883)
r5=(SRR10147884 SRR10147881 SRR10147883)
r6=(SRR10147885 SRR10147881 SRR10147883)
r7=(SRR10147890 SRR10147881 SRR10147883)
r8=(SRR10147891 SRR10147881 SRR10147883)
r9=(SRR10147892 SRR10147881 SRR10147883)
r10=(SRR10147970 SRR10147881 SRR10147883)

python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r1[0]} -c ${r1[0]} -f ${r1[1]} -m ${r1[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r2[0]} -c ${r2[0]} -f ${r2[1]} -m ${r2[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r3[0]} -c ${r3[0]} -f ${r3[1]} -m ${r3[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r4[0]} -c ${r4[0]} -f ${r4[1]} -m ${r4[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r5[0]} -c ${r5[0]} -f ${r5[1]} -m ${r5[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r6[0]} -c ${r6[0]} -f ${r6[1]} -m ${r6[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r7[0]} -c ${r7[0]} -f ${r7[1]} -m ${r7[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r8[0]} -c ${r8[0]} -f ${r8[1]} -m ${r8[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r9[0]} -c ${r9[0]} -f ${r9[1]} -m ${r9[2]}
python Variant_Het_Hom_and_Ti_Tv_ratio_INDEL_Cal.240313.py -i ${r10[0]} -c ${r10[0]} -f ${r10[1]} -m ${r10[2]}
