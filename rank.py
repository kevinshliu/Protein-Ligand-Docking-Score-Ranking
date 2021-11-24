##############################################################################################
#	Author: Sally R. Ellingson
#	Date: June 16, 2011
#	Use: Call script in directory of *.pdbqt files created by Autodock Vina
#	Results: Sorted list (by energy)
#	Output: Rank	Energy	Ligand(from pdbqt file name)
#       Revised by Shih-Hsien Liu
##############################################################################################

import glob

#get a list of result pdbqt files in directory
file_list=glob.glob('out/*.pdbqt')

#space for storing results
results={}

for file_name in file_list:
  result_file=open(file_name, 'r')
  lines=result_file.readlines()
  score_line=lines[1].split()
  vina_score=float(score_line[3])
 
  #store in dictionary
  if vina_score not in results:
    results[vina_score]=[]
  results[vina_score].append(file_name)
  result_file.close()

#sort by vina_score
sorted_scores=sorted(results, reverse=False)

#print sorted output
output_file=open('results.csv', 'w')
output_file.write('Vina_score,Cluster_Ligand')
for vina_score in sorted_scores:
  number=len(results[vina_score])
  for x in range(number):
    output_file.write('\n' + str(vina_score) + ',' + results[vina_score][x])
output_file.close()

#sort by file names as well
import pandas as pd

data = pd.read_csv('results.csv')
data.sort_values(by=['Vina_score', 'Cluster_Ligand'], inplace=True, ascending=[True, True])
data.to_csv('results.csv', index=False)

