from django.db import models
import pickle
import numpy as np 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence  import pad_sequences
from tensorflow.keras.models import load_model


# Create your models here.
from django.utils import timezone

SEQUENCE_LENGTH=100



class Message(models.Model):
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    when_sent = models.DateTimeField(null=False, blank=False, default=timezone.now)
    read = models.BooleanField(default=False)
    spam_detected = models.BooleanField(default=False)

    def do_analysis(self, text):
        tokenizer=Tokenizer()
        int_label={0:'ham',1:'spam'}
        model=load_model('model.h5')
        sequence = tokenizer.texts_to_sequences([text]) 
        # pad the sequence
        sequence = pad_sequences(sequence, maxlen=SEQUENCE_LENGTH)
        # get the prediction
        prediction = model.predict(sequence)[0]
        # one-hot encoded vector, revert using np.argmax
        return int_label[np.argmax(prediction)]

    def get_predictions(self,  ):
        res = self.do_analysis(self.content)
        if res == 'spam':
            self.spam_detected = True
        self.save( )
