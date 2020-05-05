pipeline {
    agent any
    
    stages {
   
	stage ('Build') {
	    agent {
	        docker {
		    image 'python:3.5.9-buster'
		}
	    }
	    steps {
	        sh 'python -m py_compile source_files/ui.py'
		sh 'echo "Bash commands run even with container agent running"'
		stash(name: 'compiled-results', includes: 'source_files/*.py')
	    }
	}

	stage ('Test') {
	    agent {
	        label 'master'
	    }
	    steps {
	    	sh 'echo hi'
	    }
	}
    }
}