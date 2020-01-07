import logging
import os
import re
from collections import defaultdict


def setup_logging(snakemake):
    '''
    Utility function to setup a logger for snakemake python scripts.
    First setup an stdout logger to output errors if logger setup fails,
    then setup the real logger directed to the caller rule's log file.
    '''
    # Setup logging
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s]::%(levelname)s  %(message)s',
                        datefmt='%Y.%m.%d - %H:%M:%S')
    # Check if script was called by snakemake, exit with exception otherwise
    try:
        snakemake
    except NameError:
        logging.error('This script is meant to be called by snakemake.')
        raise
    # Reset logging handler
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # Setup logging again with output file
    logging.basicConfig(filename=snakemake.log[0],
                        level=logging.INFO,
                        format='[%(asctime)s]::%(levelname)s  %(message)s',
                        datefmt='%Y.%m.%d - %H:%M:%S')


# Main script execution
if __name__ == '__main__':

    setup_logging(snakemake)

    busco_results = snakemake.input.busco
    stats_results = snakemake.input.stats
    output_file_path = snakemake.output

    output_file = open(output_file_path, 'w')
    header_fields = ['Assembly', 'File', 'Scaffolds', 'Total scaffold size', 'Longest scaffold', 'Shortest scaffold', 'Scaffolds > 1Kb', 'Scaffolds > 10Kb',
                     'Scaffolds > 100Kb', 'Scaffolds > 1Mb', 'Scaffolds > 10Mb', 'Mean scaffold size', 'Median scaffold size', 'Scaffold N50', 'Scaffold L50',
                     'Scaffold \%A', 'Scaffold \%C', 'Scaffold \%G', 'Scaffold \%T', 'Scaffold \%N',
                     '% Assembly in scaffolds', 'Contigs', 'Contigs in scaffolds', 'Total contig size', 'Longest contig', 'Shortest contig', 'Contigs > 1Kb', 'Contigs > 10Kb',
                     'Contigs > 100Kb', 'Contigs > 1Mb', 'Contigs > 10Mb', 'Mean contig size', 'Median contig size', 'Contig N50', 'Contig L50',
                     'Contig \%A', 'Contig \%C', 'Contig \%G', 'Contig \%T', 'Contig \%N',
                     'Complete BUSCOs', 'Single-copy BUSCOs', 'Duplicated BUSCOs', 'Fragmented BUSCOs', 'Missing BUSCOs', 'Total BUSCOs']
    header = '\t'.join(header_fields)
    output_file.write(f'{header}\n')

    correspondence = {'File': ('Assembly'),
                      'Scaffolds': ('Number of scaffolds'),
                      'Total scaffold size': ('Total size of scaffolds'),
                      'Longest scaffold': ('Longest scaffold'),
                      'Shortest scaffold': ('Shortest scaffold'),
                      'Mean scaffold size': ('Mean scaffold size'),
                      'Median scaffold size': ('Median scaffold size'),
                      'Scaffold N50': ('N50 scaffold length'),
                      'Scaffold L50': ('L50 scaffold count'),
                      'Scaffold \%A': ('scaffold %A'),
                      'Scaffold \%C': ('scaffold %C'),
                      'Scaffold \%G': ('scaffold %G'),
                      'Scaffold \%T': ('scaffold %T'),
                      'Scaffold \%N': ('scaffold %N'),
                      '% Assembly in scaffolds': ('Percentage of assembly in scaffolded contigs'),
                      'Contigs': ('Number of contigs'),
                      'Contigs in scaffolds': ('Number of contigs in scaffolds'),
                      'Total contig size': ('Total size of contigs'),
                      'Longest contig': ('Longest contig'),
                      'Shortest contig': ('Shortest contig'),
                      'Mean contig size': ('Mean contig size'),
                      'Median contig size': ('Median contig size'),
                      'Contig N50': ('N50 contig length'),
                      'Contig L50': ('L50 contig count'),
                      'Contig \%A': ('contig %A'),
                      'Contig \%C': ('contig %C'),
                      'Contig \%G': ('contig %G'),
                      'Contig \%T': ('contig %T'),
                      'Contig \%N': ('contig %N'),
                      'Scaffolds > 1Kb': ('Number of scaffolds > 1K nt', 'Percentage of scaffolds > 1K nt'),
                      'Scaffolds > 10Kb': ('Number of scaffolds > 10K nt', 'Percentage of scaffolds > 10K nt'),
                      'Scaffolds > 100Kb': ('Number of scaffolds > 100K nt', 'Percentage of scaffolds > 100K nt'),
                      'Scaffolds > 1Mb': ('Number of scaffolds > 1M nt', 'Percentage of scaffolds > 1M nt'),
                      'Scaffolds > 10Mb': ('Number of scaffolds > 10M nt', 'Percentage of scaffolds > 10M nt'),
                      'Contigs > 1Kb': ('Number of contigs > 1K nt', 'Percentage of contigs > 1K nt'),
                      'Contigs > 10Kb': ('Number of contigs > 10K nt', 'Percentage of contigs > 10K nt'),
                      'Contigs > 100Kb': ('Number of contigs > 100K nt', 'Percentage of contigs > 100K nt'),
                      'Contigs > 1Mb': ('Number of contigs > 1M nt', 'Percentage of contigs > 1M nt'),
                      'Contigs > 10Mb': ('Number of contigs > 10M nt', 'Percentage of contigs > 10M nt')}

    size_correspondence = {}

    data = defaultdict(dict)

    for stats_file_path in stats_results:
        assembly = os.path.splitext(os.path.split(stats_file_path)[-1])[0]
        data[assembly][header_fields[0]] = assembly
        with open(stats_file_path) as stats_file:
            header = stats_file.readline()[:-1].split(',')
            fields = stats_file.readline()[:-1].split(',')
        tmp = dict(zip(header, fields))
        for new_header, old_headers in correspondence.items():
            if len(old_headers) == 1:
                data[assembly][new_header] = tmp[old_headers[0]]
            else:
                data[assembly][new_header] = f'{tmp[old_headers[0]]} ({tmp[old_headers[1]]}%)'

    # Define regex used to parse BUSCO summary files
    summary_regex = r'C:-?(\d+.\d)%\[S:-?(\d+.\d)%,D:-?(\d+.\d)%\],F:-?(\d+.\d)%,M:-?(\d+.\d)%,n:\d+'

    # BUSCO summary results are stored in 'short_summary_<run>.txt'
    for busco_result in busco_results:
        busco_dir = os.path.split(busco_result)[0]
        assembly = os.path.split(busco_dir)[-1]
        busco_file_path = os.path.join(busco_dir, f'short_summary_{assembly}_actinopterygii.txt')
        with open(busco_file_path) as busco_file:
            for line in busco_file:
                matches = re.search(summary_regex, line)
                if matches:
                    data[assembly]['complete'] = matches.group(1)
                    data[assembly]['single'] = matches.group(2)
                    data[assembly]['duplicated'] = matches.group(3)
                    data[assembly]['fragmented'] = matches.group(4)
                    data[assembly]['missing'] = matches.group(5)

    for assembly, results in data.items():
        summary_file.write('\t'.join([results[header_field] for header_field in header_fields]))
        summary_file.write('\n')

    summary_file.close()
