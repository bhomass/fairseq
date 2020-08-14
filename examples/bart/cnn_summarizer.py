import torch
from fairseq.models.bart import BARTModel


class CNN_Summarizer():
    
    def __init__(self, path):
        self.bart = BARTModel.from_pretrained(
            '/content/drive/My Drive/' + path,
            checkpoint_file='model.pt'
        )
        self.bart.cuda()
        self.bart.eval()
        self.bart.half()
        
    def summary(self, source):
        slines = [source]
        with torch.no_grad():
            hypotheses_batch = self.bart.sample(slines, beam=4, lenpen=2.0, max_len_b=140, min_len=55, no_repeat_ngram_size=3)
            return hypotheses_batch[0]       
        
    