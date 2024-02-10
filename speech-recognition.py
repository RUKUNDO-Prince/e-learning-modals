import torch
import torchaudio
import torch.nn as nn
import pandas as pd
import numpy as np

class LogMelSpec(nn.Module):
    def __init__(self, sample_rate=8000, n_mels=128, win_length=160, hop_length=80):
        super(LogMelSpec, self).__init__()
        self.transform = torchaudio.transforms.MelSpectrogram(
            sample_rate=sample_rate, n_mels=n_mels,
            win_length=win_length, hop_length=hop_length
        )

        def forward(self, x):
            x = self.transform(x)
            x = np.log(x + 1e-14)
            return x

class TextProces:
    def __init__(self):
        """
            ' 0
            <SPACE> 1
            a 2
            b 3
            c 4
            d 5
            e 6
            f 7
            g 8
            h 9
            i 10
            j 11
            k 12
            l 13
            m 14
            n 15
            o 16
            p 17
            q 18
            r 19
            s 20
            t 21
            u 22
            v 23
            w 24
            x 25
            y 26
            z 27
        """
        self.char_map = {}
        self.index_map = {}
        for line in char_map_str.strip().split("\n"):
            ch, index = line.split()
            self.char_map