pipeline {
    agent any
    stages {
   
	stage ('Build') {
	    agent {
	        dockerfile {
		    args '--rm -t blackjack:latest'
		}
	    }
	    steps {
	        echo $(pwd)
	    }
	}
    }
}