

rule stats:
    '''
    '''
    input:
        lambda wildcards: config['assemblies'][wildcards.assembly]
    output:
        stats = 'output/stats/{assembly}.stats',
        csv = 'output/stats/{assembly}.csv'
    log:
        'logs/stats/{assembly}.log'
    benchmark:
        'benchmarks/stats/{assembly}.tsv'
    resources:
        memory = lambda wildcards, attempt: config['stats']['memory'] * attempt
    params:
        runtime = config['stats']['runtime'],
        csv_file = lambda wildcards, input: os.path.splitext(input[0])[0] + '.csv'
    shell:
        'scripts/assemblathon_stats.pl {input} -csv > {output.stats} 2> {log}; '
        'mv {params.csv_file} {output.csv} 2>> {log}'
