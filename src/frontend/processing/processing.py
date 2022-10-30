from read_user_input import *
from check_for_update import *
from serve_analysis_data import *
from serve_near_real_data import *
# Each of these functions comes from their respective scripts above^



item_name = read_input()
check_files()
analysis_data(item_name)
near_real_data(item_name)