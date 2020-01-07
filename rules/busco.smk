import os
from snakemake.remote.HTTP import RemoteProvider

# Initialize RemoteProvider object for remote input file (busco gene model)
HTTP = RemoteProvider()

rule download_busco_lineage:
    '''
    Download a lineage gene model required by a BUSCO run directly from BUSCO's website.
    Lineages are stored in a hidden 'lineages' directory.
    '''
    input:
        HTTP.remote('http://busco.ezlab.org/v2/datasets/{lineage}_odb9.tar.gz', allow_redirects=True)

    output:
        directory('output/.busco_lineages/{lineage}_odb9')
    log:
        'logs/download_busco_lineage/{lineage}.log'
    benchmark:
        'benchmarks/download_busco_lineage/{lineage}.tsv'
    shell:
        'tar -xf {input} -C output/.busco_lineages 2>&1 > {log}'


rule busco_run:
    '''
    Run BUSCO on a single assembly with a single lineage using the official wrapper.
    '''
    input:
        assembly = lambda wildcards: config['assemblies'][wildcards.assembly],
        lineage = 'output/.busco_lineages/actinopterygii_odb9'
    output:
        touch('output/busco/{assembly}/.done')
    conda:
        '../envs/busco.yaml'
    log:
        'logs/busco/{assembly}.log'
    benchmark:
        'benchmarks/busco/{assembly}.tsv'
    threads: config['busco']['threads']
    shadow: 'shallow'
    params:
        mode = config['busco']['mode'],
        extra = config['busco']['extra'],
        runtime = config['busco']['runtime'],
        tmp_output_dir = '{assembly}',
        output_dir = 'output/busco/{assembly}'
    resources:
        memory = lambda wildcards, attempt: config['busco']['memory'] * attempt
    shell:
        'run_busco --in {input.assembly} --out {params.tmp_output_dir} --force'
        ' --cpu {threads} --mode {params.mode} --lineage {input.lineage}'
        ' {params.extra} 2>&1 > {log};'
        ' rm -rf {params.output_dir}/*;'
        ' mv -f run_{params.tmp_output_dir}/* {params.output_dir}'
