"""Render only previously verified summary statistics; no new experiments/fits."""
from pathlib import Path
import json,datetime,os
os.environ.setdefault('MPLCONFIGDIR',str(Path(__file__).parent/'build/matplotlib_cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).parent
DATA=json.loads((BASE/'data/aggregate_results.json').read_text(encoding='utf8'))
EPOCH=datetime.datetime(2026,11,1,16,0,tzinfo=datetime.timezone.utc)
def export(fig,name):
    fig.savefig(BASE/'figures'/(name+'.pdf'),bbox_inches='tight',metadata={'CreationDate':EPOCH,'ModDate':EPOCH,'Title':name,'Creator':'Verified Manling note plot source'})
    fig.savefig(BASE/'figures'/(name+'.svg'),bbox_inches='tight',metadata={'Date':EPOCH.isoformat()})
    fig.savefig(BASE/'figures'/(name+'.png'),dpi=300,bbox_inches='tight')
def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9.5,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.fonttype':'none','svg.hashsalt':'manling-note-redesign-20261102-v001','axes.labelcolor':'#163A53','text.color':'#163A53','xtick.color':'#526775','ytick.color':'#163A53'})
    navy='#163A53';blue='#2B658C';slate='#657887'
    fig,ax=plt.subplots(figsize=(2.85,1.18));counts=[DATA['counts'][k] for k in ['current_available','forecast_available','forecast_exact']];labels=['Current state','Forecast available','Forecast exact']
    ax.barh(range(3),[100*x/224 for x in counts],height=.47,color=[blue,navy,slate])
    for i,v in enumerate(counts):ax.text(100*v/224+2,i,f'{v}/224',va='center',fontsize=9.5)
    ax.set(yticks=range(3),yticklabels=labels,xlim=(0,105),xticks=[0,50,100]);ax.invert_yaxis();ax.tick_params(axis='both',labelsize=9);ax.set_xlabel('Initial packets (%)',fontsize=9.5,labelpad=3);ax.grid(axis='x',alpha=.13);ax.set_axisbelow(True);fig.subplots_adjust(left=.34,bottom=.33,right=.98,top=.98);export(fig,'availability');plt.close(fig)
    fig,ax=plt.subplots(figsize=(7.0,1.43));points=DATA['gain_points'];short=[]
    for i,p in enumerate(points):
        color=blue if p['scope']=='registered' else slate
        ax.plot([p['lo'],p['hi']],[i,i],color=color,lw=1.6);ax.scatter([p['mean']],[i],color=color,s=22,zorder=3)
        ax.text(1.035,i,f"{p['mean']:.5f} [{p['lo']:.5f}, {p['hi']:.5f}]",transform=ax.get_yaxis_transform(),va='center',fontsize=8.9,color=color)
        short.append(('Registered' if p['scope']=='registered' else 'Full tail')+' / '+('replay + task' if p['baseline']=='ordinary_replay_task_progress_deadlock' else 'matched interactions'))
    ax.set_yticks(range(4),short,fontsize=9.5);ax.invert_yaxis();ax.set_xlim(-.0045,.013);ax.set_xticks([-.004,0,.004,.008,.012],['-0.004','0','0.004','0.008','0.012']);ax.tick_params(axis='x',labelsize=9);ax.axvline(0,color='#9BAAB5',ls='--',lw=.9);ax.set_xlabel('Baseline log loss - candidate log loss (nats)',fontsize=9.5,labelpad=3);ax.grid(axis='x',alpha=.13);ax.set_axisbelow(True);fig.subplots_adjust(left=.30,right=.67,top=.94,bottom=.30);export(fig,'paired_gain');plt.close(fig)
    print('Rendered existing counts and paired intervals; no fits, model calls or new episode data.')
if __name__=='__main__':main()
