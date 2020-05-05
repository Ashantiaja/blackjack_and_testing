pipeline {
    agent none
    stages {
        stage('Test') {
	    steps {
	        sh 'chmod +x checkCoverage.sh'
		sh './checkCoverage.sh'
	    }
	}
    }
}