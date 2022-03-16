import joblib
from model import modeling_sim
import bz2file as bz2
import pickle

if __name__ == "__main__":
    model = modeling_sim()
    joblib.dump(model, 'similarity.pkl')