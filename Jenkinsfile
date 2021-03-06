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
		stash(name: 'compiled-results', includes: 'source_files/*.py')
	    }
	}

	stage ('Test') {
	    environment {
	        COVPATH = './.local/lib/python3.5/site-packages'
	    }
	    agent {
	        docker {
		    image 'python:3.5.9-buster'
		}
	    }
	    steps {
	    	withEnv(["HOME=${env.WORKSPACE}"]) {
		    sh 'pip install coverage'
		    sh 'PATH=$PATH:/var/jenkins_home/workspace/blackjack_pipeline@2/.local/bin:/var/jenkins_home/workspace/blackjack_pipeline@2/.local/lib/python3.5/site-packages'
		    sh 'pip install pytest'
		    sh 'python3 -m coverage run --source=source_files/ --omit=source_files/ui.py -m pytest'
		    sh 'python3 -m coverage report'
		    sh 'python3 -m coverage html'
		}
	    }
	    post {
	        success {
		    archiveArtifacts "htmlcov/index.html"
		}
	    }
	}

	stage ('Deploy') {
    	    environment {
                VOLUME = '$(pwd)/source_files'
                IMAGE = 'cdrx/pyinstaller-linux:latest'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh 'docker run --rm -v "$(pwd)/source_files:/src/" cdrx/pyinstaller-linux:latest "pyinstaller -F ui.py"'
                }
            }
	    post {
	        success {
		    sh 'ls'
		    archiveArtifacts "${env.BUILD_ID}/source_files/dist/ui"
		}
	    }
	}
    }
}