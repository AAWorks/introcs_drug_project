# -*- coding: utf-8 -*-
"""
@author: Alejandro
"""

import matplotlib.pyplot as plt
from tkinter import Tk, simpledialog

class drugdata:
    root = Tk()
    root.withdraw()
    drugs={'MARIJUANA':[29828, 3307, 944, 509],
           'COCAINE':[3828, 736, 221, 150],
           'HEROIN':[601, 201,80,52],
           'LSD':[1193,302,111,86],
           'OPIOID':[8436, 1595, 581, 321],
           'ECSTASY':[1717, 362, 128, 101],
           'INHALANTS':[824, 198, 50,34],
           'METH':[835,330,128,67]}        
    def analyze(self, drug, data):
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect='equal'))
        
        mylabels = ['Non-Suicidal', 'Thoughts', 'Planned', 'Attempted']

        for x in range(len(mylabels)):
            mylabels[x]=mylabels[x]+': '+str(data[x])

        slices, texts, autotexts = ax.pie(data, autopct='%1.1f%%',
                                  textprops=dict(color='w'), startangle=180,
                                  explode=[0,0.1,0.1,0.1], pctdistance=0.8,
                                  radius=1.05)

        ax.legend(slices, mylabels,
          loc='lower left',
          bbox_to_anchor=(-0.13,0.105),
          fontsize=7)

        plt.setp(autotexts, size=7, weight='bold')
        ax.set_title('SUICIDALNESS IN '+drug+' USERS, 18+\n '+'Total Users: '+str(sum(data)),
                     size=11, loc='center')

        plt.show()
    def summarize(self, data):
        affected = [4760,1107,333,499,2497,591,282,525]
        x_pos=[i for i, x in enumerate(data)]
        
        plt.style.use('ggplot')
        plt.figure(figsize=(10,3))
        plt.bar(data, affected, color='green')
        plt.xlabel("Drug Name")
        plt.ylabel("# of People (In Thousands)")
        plt.title("# of People With Suicidal Tendencies by Drug")

        plt.xticks(x_pos, data)

        plt.show()
    def GUI(self):
        query1=simpledialog.askstring('Analysis Type', 'ANALYZE a drug or SUMMARIZE the data: ').upper()
        if query1=='ANALYZE':
            try: 
                query2=simpledialog.askstring('Drug', 'Type the name of a drug:').upper()
                drugdata.analyze(query2, drugdata.drugs[query2])
            except:
                print('Not currently in this database.')
        elif query1=='SUMMARIZE':
            drugdata.summarize(drugdata.drugs.keys())
        else:
            pass

drugdata=drugdata()

while True:
    drugdata.GUI()

drugdata.root.mainloop()
