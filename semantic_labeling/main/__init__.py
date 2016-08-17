from pymongo import MongoClient

from pyspark import SparkContext
from semantic_labeling.utils.similarity_tests import ks_distribution_sim, mw_histogram_sim, jaccard_num_sim, jaccard_str_sim, \
    jaccard_name_sim

sc = SparkContext()
client = MongoClient()
db = client["main"]

DEBUG = False

data_collection = db["data"]
relation_collection = db["relation"]
coop_collection = db["coop"]

debug_writer = open('debug.txt', 'w')

KS_NUM = "ks_num"
MW_HIST = "mw_hist"
JC_NUM = "jc_num"
JC_TEXT = "jc_text"
JC_NAME = "jc_name"
TF_TEXT = "tf_text"
JC_FULL_TEXT = "jc_full_text"
KS_LENGTH = "ks_length"
KS_FRAC = "ks_frac"
EL_DIST = "el_dist"

GREATER = "greater"
LESS = "less"
EQUAL = "equal"
CONTAIN_IN = "contain_in"

similarity_test_map = {KS_NUM: ks_distribution_sim, MW_HIST: mw_histogram_sim, JC_NUM: jaccard_num_sim,
                       JC_TEXT: jaccard_str_sim, JC_NAME: jaccard_name_sim}

features = [JC_TEXT, JC_NUM, TF_TEXT, KS_NUM, MW_HIST, JC_NAME]
relations = [GREATER, LESS, EQUAL, CONTAIN_IN]
