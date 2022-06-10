# Phylum
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: NOA
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that, for every taxon, outputs its phylum
in an NOA file importable into Cytoscape (Shannon et al, 2003).

The plugin accepts as input a TXT file of tab-delimited keyword-value
pairs:

csvfile: CSV file of taxa abundances (samples are rows, taxa are columns)
taxfile: PhyloSeq (McMurdie et al, 2013) formatted taxonomy file


