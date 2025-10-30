pipeline{
    agent any
    stages{
        stage("Running testcases using selenium"){
            steps{
                bat 'pip install -r requirements.txt'
                bat 'start /B python app.py'
                bat 'ping 127.0.0.1 -n 5 > nul'
                bat 'pytest -v'
            }
        }
        stage('Docker Login'){
            steps{
                bat 'docker login -u komsujani23 -p Sujani@23'
                bat 'docker build -t testapp:v1 .'
            }
        }
        stage('Pushing image to Docker'){
            steps{
                bat 'docker tag testapp:v1 komsujani23/sample:exam'
                bat 'docker push komsujani23/sample:exam'
            }
        }
        stage('Deploying to Kubernetes'){
            steps{
                bat 'kubectl apply -f deployment.yaml --validate=False'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'Pipeline finished successfully'
        }
        failure{
            echo 'Pipeline failed.'
        }
    }
}