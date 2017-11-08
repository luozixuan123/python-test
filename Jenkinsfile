podTemplate(label: 'python_pod',containers: [
    containerTemplate(name: 'python', image: 'registry-vpc.cn-hangzhou.aliyuncs.com/luozixuan/python:latest', ttyEnabled: true, command: 'cat'),
    // containerTemplate(
    //     name: 'sonar-scanner',
    //     image: 'registry-vpc.cn-hangzhou.aliyuncs.com/luozixuan/sonar-scanner:latest',
    //     ttyEnabled: true,
    //     command: '',
    //     envVars: [
    //         envVar(key: 'SONAR_HOST_URL', value: 'http://sonarqube.platform:9000'),
    //         envVar(key: 'SONAR_PROJECT_KEY', value: 'python-pipeline-docker'),
    //         envVar(key: 'SONAR_PROJECT_NAME', value: 'python-pipeline-docker'),
    //         envVar(key: 'SONAR_PROJECT_VERSION', value: '1.1'),
    //     ]),
    containerTemplate(
            name: 'jnlp',
            image: 'registry-vpc.cn-hangzhou.aliyuncs.com/nanhangfei/jnlp-slave:3.7-1-alpine',
            args: '${computer.jnlpmac} ${computer.name}',
            command: ''
    )
  ])
{
node ('python_pod') {
    
    def projectName='python-pipeline-test'
    def sonarReportFile = 'sonar_report.txt'
    def sonarHostUrl = 'http://120.55.61.61:9000'
    //def sonarHostUrl = 'http://116.62.235.239:30622'

    stage('Check a project') {
            git credentialsId: '0361a995-132b-44de-84a9-eb214698c3a1', url: 'https://github.com/luozixuan123/python-test'
            // container('sonar-scanner'){
            //     sh 'ls'
            // }
            container('python') {
                stage('Unit Test'){
                    sh 'pytest --junitxml=./python_test/test/pytest_report.xml'
                    sh 'python python_test/run.py'
                }
                stage('Sonar Check') {
                        def sonarhome = tool name: 'sonarqube scanner 2.5', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                       echo sonarhome + '\\bin'
                        def status = sh sonarhome + '/bin/sonar-runner -Dsonar.host.url='+sonarHostUrl+' -Dsonar.username=admin -Dsonar.password=admin -Dsonar.projectName='+projectName+' -Dsonar.projectVersion=1.8.6 -Dsonar.projectKey='+projectName+' -Dsonar.sources=. -X'
                }
                stage('Get Sonar Report'){
                        sh 'curl -o sonar_report.txt'+ ' ' +projectName+'/api/qualitygates/project_status?projectKey='+projectName
                        def jsonPayload = readFile 'sonar_report.txt'
                        def slurper = new groovy.json.JsonSlurper()
                        def states = slurper.parseText(jsonPayload)
                        if (states.projectStatus.status == 'OK'){
                            echo 'success'
                        }else {
                            //error 'sonarqube check fail'
                            echo 'fail'
                        }
                }
                stage('Deploy') {
                    // sh 'python python_test/run.py'
                    //sh 'echo "Wyun4test"|sudo -S scp -r . root@120.55.61.61:/opt/code'
                    echo 'deploy'
                }
                stage('Park Code'){
                    sh 'tar -zcvf python_test.tar.gz python_test'
                }

                stage('Push test report'){
                    junit allowEmptyResults: true, testResults: 'python_test/test/pytest_report.xml'
                }
                stage('ArchiveArtifacts'){
                    archiveArtifacts 'python_test.tar.gz'
                }

            }
        }

    }
}