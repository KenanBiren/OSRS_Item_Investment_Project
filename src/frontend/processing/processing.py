from check_for_update import *
from read_user_input import *
from serve_analysis_data import *
from serve_near_real_data import *




item_name = read_input()
check_files()
analysis_data(item_name)
near_real_data(item_name)