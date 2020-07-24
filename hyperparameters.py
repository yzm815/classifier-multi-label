# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:23:12 2018

@author: cm
"""



import os
import sys
pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(pwd)
from classifier_multi_label_textcnn.utils import load_vocabulary



class Hyperparamters:
    # Train Parameters    
    print_step = 100
    summary_step = 10
    batch_size = 64          
    num_saved_per_epoch = 3
    logdir = 'logdir/model_02'
    
    # Load dict
    dict_id2label,dict_label2id = load_vocabulary(os.path.join(pwd,'data','vocabulary_label.txt') )
    label_vocabulary = list(dict_id2label.values())

    # Optimization parameters
    use_tpu = None
    num_train_epochs = 20
    warmup_proportion = 0.1   
    do_lower_case = True
    learning_rate = 5e-5 
    
    # TextCNN parameters
    num_filters = 128
    filter_sizes = [2,3,4,5,6,7]
    embedding_size = 384
    keep_prob = 0.5
    
    # Sequence and Label
    sequence_length = 60
    num_labels = len(list(dict_id2label))    
    
    # BERT model
    model = 'albert_small_zh_google'
    bert_path = os.path.join(pwd,model)
    data_dir = os.path.join(pwd,'data')
    vocab_file = os.path.join(pwd,model,'vocab_chinese.txt')
    init_checkpoint = os.path.join(pwd,model,'albert_model.ckpt')
    saved_model_path = os.path.join(pwd,'model')    
    
    
    
    
    
    
    
    


    
    
