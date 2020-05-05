pipeline {
    agent any
    stages {
   
	stage ('Build') {
	    agent {
	        dockerfile {
		    args '-t blackjack:latest'
		}
	    }
	    steps {
	        echo $(pwd)
	    }
	}
    }
}