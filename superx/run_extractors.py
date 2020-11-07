from information_extractors.item_info_extractor import InfoExtractor
from information_extractors.branch_info_extractor  import BranchExtractor

i_e = InfoExtractor()
b_e = BranchExtractor()

i_e.run_info_extractor()
b_e.run_branch_extractor()