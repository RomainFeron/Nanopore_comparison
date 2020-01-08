configfile: 'config.yaml'

include: 'rules/busco.smk'
include: 'rules/stats.smk'


rule summary:
    '''
    Aggregator rule triggering busco runs for all assemblies.
    Calls the python script 'busco_summary.py' that edits the assembly summary file to add
    BUSCO results for each lineage and each assembly.
    '''
    input:
        busco = expand('output/busco/{assembly}/.done', assembly=config['assemblies'].keys()),
        stats = expand('output/stats/{assembly}.csv', assembly=config['assemblies'].keys())
    output:
        'output/summary.tsv'
    benchmark:
        'benchmarks/summary.tsv'
    log:
        'logs/summary.txt'
    script:
        'scripts/summary.py'
