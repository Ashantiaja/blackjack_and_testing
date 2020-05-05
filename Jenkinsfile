pipeline {
    agent any
    stages {
    	stage('Build Dependencies?') {
	
	}

        stage('Test') {
	    steps {
	    	sh 'source virtual/bin/activate && chmod +x checkCoverage.sh && ./checkCoverage.sh'
	    }
	}
    }
}