import wx

# Define the standard genetic code dictionary
standard_genetic_code = {
    "ttt": "Phe", "tct": "Ser", "tat": "Tyr", "tgt": "Cys",
    "tca": "Ser", "tcc": "Ser", "tac": "Tyr", "tgc": "Cys",
    "tta": "Leu", "tga": "TER", "ttg": "Leu", "tcg": "Ser",
    "tag": "TER", "tgg": "Trp", "ctt": "Leu", "cct": "Pro",
    "cat": "His", "cgt": "Arg", "ctc": "Leu", "ccc": "Pro",
    "cac": "His", "cgc": "Arg", "cta": "Leu", "cca": "Pro",
    "caa": "Gln", "cga": "Arg", "ctg": "Leu", "ccg": "Pro",
    "cag": "Gln", "cgg": "Arg", "att": "Ile", "act": "Thr",
    "aat": "Asn", "agt": "Ser", "atc": "Ile", "acc": "Thr",
    "aac": "Asn", "agc": "Ser", "ata": "Ile", "aca": "Thr",
    "aaa": "Lys", "aga": "Arg", "atg": "Met", "acg": "Thr",
    "aag": "Lys", "agg": "Arg", "gtt": "Val", "gct": "Ala",
    "gat": "Asp", "ggt": "Gly", "gtc": "Val", "gcc": "Ala",
    "gac": "Asp", "ggc": "Gly", "gta": "Val", "gca": "Ala",
    "gaa": "Glu", "gga": "Gly", "gtg": "Val", "gcg": "Ala",
    "gag": "Glu", "ggg": "Gly"
}

class DNAProteinTranslator(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='DNA to Protein Translator', size=(450, 300))
        
        # Panel and main sizer
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Label for DNA Sequence
        label = wx.StaticText(panel, label='Enter DNA Sequence:')
        label.SetForegroundColour(wx.WHITE)
        vbox.Add(label, 0, wx.ALL, 10)
        
        # TextCtrl for DNA sequence input
        self.dna_entry = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(self.dna_entry, 1, wx.EXPAND | wx.ALL, 10)
        
        # Button to translate DNA to Protein
        translate_button = wx.Button(panel, label='Translate')
        translate_button.Bind(wx.EVT_BUTTON, self.translate_to_protein)
        vbox.Add(translate_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        
        # Label for Translated Protein Sequence
        result_label = wx.StaticText(panel, label='Translated Protein Sequence:')
        result_label.SetForegroundColour(wx.WHITE)
        vbox.Add(result_label, 0, wx.ALL, 10)
        
        # TextCtrl to display translated protein sequence
        self.result_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.result_text, 1, wx.EXPAND | wx.ALL, 10)
        
        panel.SetSizer(vbox)
        self.Move(50,50)
    
        

    def translate_to_protein(self, event):
        sequence = self.dna_entry.GetValue().strip().lower()
        print(f"Input Sequence: {sequence}")
        
        # Validate input length
        if len(sequence) % 3 != 0:
            wx.MessageBox('Invalid sequence length!', 'Error', wx.OK | wx.ICON_ERROR)
            return
        
        # Translate sequence
        protein_sequence = []
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            if codon in standard_genetic_code:
                protein_sequence.append(standard_genetic_code[codon])
            else:
                protein_sequence.append("Unknown")
        
        translated_text = ' '.join(protein_sequence)
        self.result_text.SetValue(translated_text)
        print(f"Translated Protein Sequence: {translated_text}")

if __name__ == '__main__':
    app = wx.App(False)
    frame = DNAProteinTranslator()
    frame.SetBackgroundColour('black')
    frame.Show()
    app.MainLoop()
