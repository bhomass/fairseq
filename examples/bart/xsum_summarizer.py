import torch
from fairseq.models.bart import BARTModel


class XSum_Summarizer():
    
    def __init__(self, path):
        self.bart = BARTModel.from_pretrained(
            '/content/drive/My Drive/' + path,
            checkpoint_file='model.pt'
        )
        self.bart.cuda()
        self.bart.eval()
        self.bart.half()
        
    def summarize(self, source):
        slines = [source]
        with torch.no_grad():
            hypotheses_batch = self.bart.sample(slines, beam=6, lenpen=1.0, max_len_b=60, min_len=10, no_repeat_ngram_size=3)
            return hypotheses_batch[0]       
        
    