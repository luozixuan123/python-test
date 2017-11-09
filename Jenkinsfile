podTemplate(label: 'python_pod',containers: [
    containerTemplate(name: 'python', image: 'registry-vpc.cn-hangzhou.aliyuncs.com/luozixuan/python:latest', ttyEnabled: true, command: 'cat'),
    containerTemplate(
            name: 'jnlp',
            image: 'registry-vpc.cn-hangzhou.aliyuncs.com/nanhangfei/jnlp-slave:3.7-1-alpine',
            args: '${computer.jnlpmac} ${computer.name}',
            command: ''
    )
  ])
{
node ('python_pod') {
    
    def configFile = readFile("config.json")
    def slurper = new groovy.json.JsonSlurper()
    def configStates = slurper.parseText(configFile)

    echo 'ready go'

    stage("clone code"){
        git credentialsId: '434aa890-ec99-4dd4-93ea-686fb6c3a3d2', url: 'https://github.com/luozixuan123/python-test.gt'
        echo 'clone code complete'
    }

    stage("python test"){
        container('python'){
            stage("unit test"){
                sh 'pytest --junitxml=./python_test/test/pytest_report.xml'
                echo 'unit test complete'
            }

            stage("run py"){
                if (configStates.mainDir != ""){
                    sh 'python ' + configStates.mainDir
                }
                echo 'run py complete'
            }
        }
    }

    stage("start check code"){
        def sonarhome = tool name: 'sonarqube scanner 2.5', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        def status = sh sonarhome + '/bin/sonar-runner -Dsonar.host.url='+sonarHostUrl+' -Dsonar.username=admin -Dsonar.password=admin -Dsonar.projectName='+projectName+' -Dsonar.projectVersion='+configStates.projectVersion+' -Dsonar.projectKey='+projectName+' -Dsonar.sources=. -X'
        echo 'start check code complete'
    }

    stage("get check report"){
        sh 'curl -o sonar_report.txt'+ ' ' +projectName+'/api/qualitygates/project_status?projectKey='+projectName
        def jsonPayload = readFile 'sonar_report.txt'
        def states = slurper.parseText(jsonPayload)
        if (states.projectStatus.status == 'OK'){
            echo 'pass sonarqube code check'
        }else {
            echo 'fail sonarqube code check'
            error 'sonarqube check fail'
        }
        echo 'get check report complete'
    }

    stage("depoly"){
        // ssh
        echo 'deploy complete'
    }

    stage('park code'){
        sh 'tar -zcvf code.tar.gz' + configStates.projectName
        echo 'park code complete'
    }

    stage('push test report'){
        junit allowEmptyResults: true, testResults: 'unittest_report.xml'
        echo 'push test report complete'
    }

    stage('archive artifacts'){
        archiveArtifacts 'code.tar.gz'
        echo 'archive artifacts complete'
    }
}