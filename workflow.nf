#!/usr/bin/env nextflow

process PYSCRIPT {

    input:
    val STR

    output:
    path 'sample.json'

    script:
    """
    echo "Using path: \$WORKFLOW_PATH"
    python3 ${baseDir}/bin/script.py $STR
    """
}

process PYSCRIPT2 {

    input:
    path input_file

    output:
    path 'output2.txt'

    script:
    """
    python3 ${baseDir}/bin/script2.py $input_file
    """
}

workflow{
    Channel.of("Memes sind humorvolle Bilder, Videos oder Texte, die sich schnell im Internet verbreiten. Sie reflektieren oft aktuelle Ereignisse, kulturelle Phänomene oder alltägliche Situationen und werden häufig in sozialen Medien geteilt. Ursprünglich von Richard Dawkins als Konzept beschrieben, haben Memes sich zu einem wichtigen Bestandteil der Online-Kommunikation entwickelt. Sie ermöglichen es Nutzern, auf kreative Weise ihre Gedanken und Emotionen auszudrücken und fördern soziale Bindungen durch das Teilen gemeinsamer Erfahrungen. Memes sind nicht nur unterhaltsam, sondern auch ein effektives Werkzeug im Marketing, um das Publikum anzusprechen und Engagement zu erzeugen.") | PYSCRIPT
    PYSCRIPT2(PYSCRIPT.out)
}