"""Reproduce the illustrative limiting-phase figure from certified coefficients."""
from pathlib import Path
import json
import math
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir())/"saw-lab-matplotlib"))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def endpoints(record):
    scale=2**record['denominator_power_of_two']
    return np.array([int(record['lower_numerator'])/scale,int(record['upper_numerator'])/scale])


def generate(certificate):
    target=Path(__file__).resolve().parent
    J=[[endpoints(v) for v in row] for row in certificate['integrals']]
    t=math.sqrt(2)-1;eta=1/math.sqrt(2);A=1/t**2
    theta=np.linspace(.22,.43,500)
    B=A*np.sin(np.pi*theta)/np.sin(np.pi*(eta-theta))
    Plo=1-(1-t)-A*J[0][0][1]+B*J[1][0][0]
    Phi=1-(1-t)-A*J[0][0][0]+B*J[1][0][1]
    Hlo=1+t*t*(-3-A*J[0][1][1]+B*J[1][1][0])
    Hhi=1+t*t*(-3-A*J[0][1][0]+B*J[1][1][1])
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'saw-lab-m4-v1'})
    fig,ax=plt.subplots(figsize=(7.0,4.2),layout='constrained')
    ax.axvspan(.30,.35,color='#eaf1f7',label='Proof interval')
    ax.axhline(0,color='#56606b',linewidth=.9)
    for lo,hi,color,label in [(Plo,Phi,'#1d5fa2',r'$1+P_0(\theta)$'),(Hlo,Hhi,'#a54a20',r'$1+H_0(\theta)$')]:
        ax.fill_between(theta,lo,hi,color=color,alpha=.20)
        ax.plot(theta,(lo+hi)/2,color=color,lw=2,label=label)
    ax.axvline(.30,color='#64798c',ls=':',lw=1)
    ax.axvline(.35,color='#64798c',ls=':',lw=1)
    ax.set(xlabel=r'Phase $\theta$',ylabel='Limiting function value',xlim=(.22,.43))
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=.2);ax.legend(frameon=False,loc='upper left')
    fig.savefig(target/'critical_phase.pdf',metadata={'Creator':'Self-Avoiding Walk Lab','CreationDate':None,'ModDate':None})
    fig.savefig(target/'critical_phase.svg',metadata={'Date':None})
    fig.savefig(target/'critical_phase.png',dpi=160,metadata={'Software':'Self-Avoiding Walk Lab'})
    plt.close(fig)
    return ['figures/critical_phase.pdf','figures/critical_phase.svg','figures/critical_phase.png']


if __name__=='__main__':
    source=Path(__file__).resolve().parents[1]/'proof-checkers/expected-integrals.json'
    generate(json.loads(source.read_text()))
