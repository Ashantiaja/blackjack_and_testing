pipeline {
    agent none
    stages {
        stage('Build') {
	    agent {
	        docker {
		    image 'python:3'
		}
	    }
	    steps {
	        sh 'python3 source_files/ui.py'
	    }
	}
    }
}