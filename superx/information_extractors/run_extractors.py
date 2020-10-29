from branch_info_extractor import BranchExtractor
from item_info_extractor import InfoExtractor

run_extractors()

def run_extractors():
    item_info_extractor = InfoExtractor()
    branch_info_extractor = BranchExtractor()

    item_info_extractor.run_info_extractor()
    branch_info_extractor.run_branch_extractor()

