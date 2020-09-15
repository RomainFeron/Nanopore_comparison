# Nanopore assembly method comparison

This repository contains the results of assembly quality assessment for several assembly and polishing methods for Nanopore and Illumina reads. The data and final genome assembly are included in [*Pan, Q.et al., (2020). The rise and fall of the ancient northern pike master sex determining gene. bioRxiv.*](https://www.biorxiv.org/content/10.1101/2020.05.31.125336v1.abstract).

**Information in this repository is not complete and will be updated soon.**

## Results

The full summary table including all assembly metrics and BUSCO metrics is available [here](output/summary.tsv). A short table with only the most important metrics is provided below:

| Assembler | Reads | Racon rounds | Polca rounds | Pilon rounds | Scaffolds | Total scaffold size | Longest scaffold | Median scaffold size | Scaffold N50 | Scaffold L50 | Complete BUSCOs (%) | Single-copy BUSCOs (%) | Duplicated BUSCOs (%) | Fragmented BUSCOs (%) |
| :------- | --------: | --------: | --------: | --------: | --------: | ------------------: | ---------------: | -------------------: | -----------: | -----------: | ------------------: | ---------------------: | --------------------: | --------------------: |
| canu | raw | 0 | 0 | 0 | 3227 | 951948846 | 10942431 | 47627 | 1534791 | 149 | 43.7 | 42.9 | 0.8 | 7.4 |
| canu | raw | 1 | 0 | 0 | 3071 | 965393679 | 11078614 | 52248 | 1538696 | 150 | 56.7 | 55.5 | 1.2 | 7.9 |
| canu | raw | 2 | 0 | 0 | 3037 | 965700424 | 11087656 | 52831 | 1555114 | 149 | 57.6 | 56.6 | 1 | 8 |
| canu | raw | 2 | 0 | 1 | 3037 | 967423163 | 11110507 | 52883 | 1559591 | 149 | 94.5 | 90.6 | 3.9 | 2.8 |
| canu | raw | 2 | 1 | 0 | 3037 | 966320640 | 11094938 | 52855 | 1556531 | 149 | 74.1 | 71.7 | 2.4 | 9.1 |
| flye | corrected | 0 | 0 | 0 | 1329 | 916399443 | 29664458 | 100741 | 3800379 | 51 | 60 | 58.8 | 1.2 | 7.8 |
| flye | corrected | 1 | 0 | 0 | 1244 | 918414721 | 29727285 | 123939 | 3807314 | 51 | 59.2 | 57.7 | 1.5 | 8.1 |
| flye | corrected | 2 | 0 | 0 | 1231 | 918733717 | 29733036 | 127128 | 3807983 | 51 | 58.9 | 57.6 | 1.3 | 7.9 |
| flye | corrected | 2 | 0 | 1 | 1231 | 919922954 | 29788268 | 127613 | 3816572 | 51 | 94.4 | 90.9 | 3.5 | 2.8 |
| flye | corrected | 2 | 1 | 0 | 1231 | 918585399 | 29732637 | 127163 | 3808094 | 51 | 71.3 | 69.3 | 2 | 9.1 |
| flye | raw | 0 | 0 | 0 | 1757 | 947335101 | 35593798 | 10348 | 10807385 | 25 | 60 | 58.7 | 1.3 | 8.3 |
| flye | raw | 1 | 0 | 0 | 1401 | 942065221 | 35433054 | 21075 | 10751775 | 25 | 59.9 | 58.6 | 1.3 | 8.2 |
| flye | raw | 2 | 0 | 0 | 1352 | 941676606 | 35430667 | 23319 | 10747330 | 25 | 59.8 | 58.3 | 1.5 | 8.6 |
| flye | raw | 2 | 0 | 1 | 1352 | 942304953 | 35434112 | 23311 | 10752412 | 25 | 94.5 | 90.9 | 3.6 | 2.9 |
| flye | raw | 2 | 1 | 0 | 1352 | 941422740 | 35421523 | 23322 | 10749561 | 25 | 72.1 | 70 | 2.1 | 8.9 |
| flye | trimmed | 0 | 0 | 0 | 1699 | 908968079 | 17279927 | 133056 | 1983562 | 100 | 59.9 | 58.7 | 1.2 | 7.8 |
| flye | trimmed | 1 | 0 | 0 | 1648 | 911198514 | 17324657 | 142987 | 1991917 | 100 | 59.7 | 58.2 | 1.5 | 7.4 |
| flye | trimmed | 2 | 0 | 0 | 1634 | 911564900 | 17331222 | 145624 | 1993190 | 100 | 59.2 | 57.7 | 1.5 | 7.4 |
| flye | trimmed | 2 | 0 | 1 | 1634 | 913040417 | 17363090 | 145919 | 1990260 | 100 | 93.9 | 90.4 | 3.5 | 3 |
| flye | trimmed | 2 | 1 | 0 | 1634 | 911410720 | 17326448 | 145629 | 1989349 | 100 | 71.6 | 69.5 | 2.1 | 8.5 |
| wtdbg2 | corrected | 0 | 0 | 0 | 2810 | 885831968 | 23252592 | 23709 | 3525371 | 60 | 43 | 42.7 | 0.3 | 6.3 |
| wtdbg2 | corrected | 1 | 0 | 0 | 2597 | 895437456 | 23513364 | 26764 | 3559418 | 60 | 56.5 | 55.3 | 1.2 | 8.1 |
| wtdbg2 | corrected | 2 | 0 | 0 | 2535 | 895312360 | 23529299 | 27517 | 3560626 | 60 | 56.9 | 55.7 | 1.2 | 7.9 |
| wtdbg2 | corrected | 2 | 0 | 1 | 2535 | 896816104 | 23571653 | 27471 | 3562908 | 60 | 93 | 89.5 | 3.5 | 2.7 |
| wtdbg2 | corrected | 2 | 1 | 0 | 2535 | 895293217 | 23530634 | 27476 | 3560501 | 60 | 70.4 | 68.5 | 1.9 | 8.5 |
| wtdbg2 | raw | 0 | 0 | 0 | 1227 | 867381815 | 27191330 | 22375 | 7356404 | 32 | 33.4 | 33 | 0.4 | 5.7 |
| wtdbg2 | raw | 1 | 0 | 0 | 1132 | 879206707 | 27550322 | 26886 | 7458027 | 32 | 56.2 | 54.8 | 1.4 | 8.1 |
| wtdbg2 | raw | 2 | 0 | 0 | 1120 | 879589208 | 27562967 | 27355 | 7460231 | 32 | 57.2 | 56.2 | 1 | 7.9 |
| wtdbg2 | raw | 2 | 0 | 1 | 1120 | 880869069 | 27593451 | 27398 | 7473325 | 32 | 93.2 | 89.8 | 3.4 | 2.5 |
| wtdbg2 | raw | 2 | 1 | 0 | 1120 | 879576357 | 27563414 | 27350 | 7462154 | 32 | 69.6 | 67.9 | 1.7 | 8.3 |
| wtdbg2 | trimmed | 0 | 0 | 0 | 2792 | 877426181 | 17149271 | 29942 | 2183325 | 94 | 43.4 | 42.8 | 0.6 | 6.9 |
| wtdbg2 | trimmed | 1 | 0 | 0 | 2661 | 886838528 | 17322380 | 34351 | 2209111 | 94 | 56.9 | 55.8 | 1.1 | 7.7 |
| wtdbg2 | trimmed | 2 | 0 | 0 | 2613 | 887016948 | 17333162 | 35749 | 2211406 | 94 | 57.8 | 56.8 | 1 | 7.8 |
| wtdbg2 | trimmed | 2 | 0 | 1 | 2613 | 888765491 | 17357701 | 35797 | 2219808 | 94 | 93.7 | 90.2 | 3.5 | 2.7 |
| wtdbg2 | trimmed | 2 | 1 | 0 | 2613 | 886978594 | 17330674 | 35728 | 2211370 | 94 | 70.4 | 68.3 | 2.1 | 8.8 |

*Reads: raw means original Nanopore reads, corrected means Nanopore reads corrected by Canu, trimmed means Nanopore reads corrected and trimmed by Canu*

## Data

### Nanopore reads

Nanopore reads were obtained from two individuals (two rounds of sequencing). Methods for the first round are described in [Pan *et al.*, 2019](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1008013), in the Methods section **Genome sequencing and assembly**. Methods for the second round are described in [Pan *et al.*, 2020](https://www.biorxiv.org/content/10.1101/2020.05.31.125336v1.full), in the Methods section **Genome and population genomics sequencing**.

TODO: stats for all reads

### Illumina reads

## Methods

This should have been a snakemake workflow but it was not. Next time... Instead examples of the commands used for each software are provided below.

### Assembly

#### Canu

#### Flye

#### wtdbg2

### Polishing

#### Racon

#### Pilon

```bash
ASSEMBLY=<assembly_file>

bwa index $ASSEMBLY

bwa mem -t 24 $ASSEMBLY \
<reads_file_1> \
<reads_file_2> | \
samtools view -bh > $ASSEMBLY.bam

samtools sort -@ 24 -o $ASSEMBLY.sorted.bam $ASSEMBLY.bam

samtools index $ASSEMBLY.sorted.bam

pilon -Xmx230G \
--genome $ASSEMBLY \
--frags $ASSEMBLY.sorted.bam \
--output <output_file> \
--changes \
--fix all \
--threads 24
```

#### Polca

```bash
polca.sh \
-a <assembly_file> \
-r '<reads_file_1> <reads_file_2>' \
-t 32
```
