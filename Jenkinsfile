pipeline {
    agent any
    environment {
    
    }
    stages {
   
	stage ('Build') {
	    agent {
	        docker {
		    image 'python:3.5.9-buster'
		}
	    }
	    steps {
	        sh 'python -m py_compile source_files/ui.py'
		stash(name: 'compiled-results', includes: 'source_files/*.py')
	    }
	}
    }
}