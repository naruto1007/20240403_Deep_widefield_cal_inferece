import os
import sys

os.system('python main_RSM.py \
--RMBG_model_folder arr_202110011541 \
--RMBG_model_name E_30_Iter_4009 \
--SEG_model_folder TS3DUnetFFD_20211129-1355 \
--SEG_model_name seg_30 \
--test_datasize 20000 \
--datasets_path /zjbs-data/share/calcium_data_code/20240403_deepwonder/datasets/ \
--datasets_folder exp_013_miniscope \
--GPU 0')