pipeline {
    agent any
    stages {
        stage('Test') {
	    steps {
	        sh 'chmod +x checkCoverage.sh'
		sh './checkCoverage.sh'
	    }
	}
    }
}