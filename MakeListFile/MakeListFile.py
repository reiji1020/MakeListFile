import sys
import glob

# �f�[�^�̓����Ă���t�@�C�����w��
positive_dir = glob.glob('F:\\IMAGE\\CellDeep\\ImageData_cutting_Positive\\*.*')
negative_dir = glob.glob('F:\\IMAGE\\CellDeep\\ImageData_cutting_Negative\\*.*')

# �t�@�C���I�[�v��
listfile = open('F:\\IMAGE\\CellDeep\\train.txt','w')

for pis_file in positive_dir:
    listfile.write(pis_file+'\n')

for nega_file in negative_dir:
    listfile.write(nega_file+'\n')

listfile.close()