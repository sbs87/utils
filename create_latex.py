## parse manifest, store as dictionary 
import csv
## print formatted tex file
plot_man=dict()
with open('plot_manifest.txt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        plot_man[row[0]]=row[2]
        


# Tex template

open_bracket="{"
close_bracket="}"
bs='\\'

line1='{}begin{}figure{}'.format(bs,open_bracket,close_bracket)
line4='{}end{}figure{}'.format(bs,open_bracket,close_bracket)


for plot_n, plot in enumerate(plot_man):
    #print(plot)
    #print(plot_n)
    if plot_n==0:
        continue
    fig_num=plot_n
    fig_captopn=plot_man[plot]
    plot_filename=plot+".pdf"
    line2='{}caption{}Figure {} {}{} '.format(bs,open_bracket,fig_num,fig_captopn,close_bracket)
    line3='{}includegraphics[width=\columnwidth]{}{}{}'.format(bs,open_bracket,plot_filename,close_bracket)
    tex_out="{}\n  {}\n  {}\n{}".format(line1,line2,line3,line4)
    print(tex_out)

