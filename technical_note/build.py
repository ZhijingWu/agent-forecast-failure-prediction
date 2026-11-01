"""Render frozen aggregates and compile the note; no inference or estimation."""
from pathlib import Path
import subprocess,os,sys,hashlib,json
ROOT=Path(__file__).resolve().parent
def main():
    env=dict(os.environ,SOURCE_DATE_EPOCH='1793548800',FORCE_SOURCE_DATE='1',TZ='UTC',CUDA_VISIBLE_DEVICES='',PYTHONDONTWRITEBYTECODE='1',MPLCONFIGDIR=str(ROOT/'build/matplotlib_cache'),TEXMFVAR=str(ROOT/'build/texmfvar'),TEXMFCONFIG=str(ROOT/'build/texmfconfig'),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    build=ROOT/'build';build.mkdir(exist_ok=True)
    subprocess.run([sys.executable,'-B',str(ROOT/'plot_existing_results.py')],cwd=ROOT,env=env,check=True)
    for i in range(2):
        p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','main.tex'],cwd=ROOT,env=env,capture_output=True,text=True)
        (build/('compile_pass_%d.txt'%(i+1))).write_text(p.stdout+'\n'+p.stderr,encoding='utf8')
        if p.returncode:print(p.stdout[-5000:]);raise SystemExit(p.returncode)
    # Standalone vector exports of all editable conceptual figures.
    for name in ['graphical_abstract','architecture','roadmap']:
        tex=r"\documentclass[border=2pt]{standalone}\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15\usepackage[T1]{fontenc}\usepackage{lmodern,xcolor,tikz}\usetikzlibrary{arrows.meta,positioning}\definecolor{navy}{HTML}{163A53}\definecolor{blue}{HTML}{2B658C}\definecolor{slate}{HTML}{526775}\definecolor{ice}{HTML}{EDF4F8}\definecolor{mist}{HTML}{F2F4F5}\begin{document}\input{figures/"+name+r".tex}\end{document}"
        (build/(name+'.tex')).write_text(tex,encoding='utf8')
        p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','build/'+name+'.tex'],cwd=ROOT,env=env,capture_output=True,text=True)
        if p.returncode:print(p.stdout[-4000:]);raise SystemExit(p.returncode)
    print(subprocess.run(['pdfinfo',str(build/'main.pdf')],capture_output=True,text=True,check=True).stdout)
    print('PDF_SHA256',hashlib.sha256((build/'main.pdf').read_bytes()).hexdigest())
if __name__=='__main__':main()
