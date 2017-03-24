rm -rf submission/
mkdir submission
mkdir submission/code

cp *.py submission/code/
cp blind_results.txt submission/
cp report/report.pdf submission/andrew_clarke_bioinformatics_150391471.pdf

zip -r andrew_clarke_bioinformatics_150391471.zip submission
