pipeline {
    agent any
    stages {

        stage('Test') {
	    steps {
	    	sh 'python3 -m venv virtual'
	        sh 'source virtual/bin/activate'
		sh 'pip install coverage'
		sh 'coverage run --source=source_files/ -m pytest'
		sh 'coverage report'
	    }
	}
    
	stage ('Build') {
	    steps {
	        sh 'source virtual/bin/activate'
	    	sh 'pip install pyinstaller'
	    	sh 'pyinstaller source_files/ui.py'
	    }
	}
    }
}