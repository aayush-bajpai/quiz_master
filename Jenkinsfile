pipeline {
    agent any
    environment {
        VENV_PATH = "/home/ubuntu/quiz_master/venv"
        PROJECT_DIR = "/home/ubuntu/quiz_master"
        PATH = "${VENV_PATH}/bin:$PATH"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aayush-bajpai/quiz_master.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                . ${VENV_PATH}/bin/activate
                pip install --upgrade pip
                pip install -r ${PROJECT_DIR}/requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                . ${VENV_PATH}/bin/activate
                cd ${PROJECT_DIR}
                python manage.py test
                """
            }
        }

        stage('Migrate & Collect Static') {
            steps {
                script {
                    try {
                        sh """
                        . ${VENV_PATH}/bin/activate
                        cd ${PROJECT_DIR}
                        python manage.py migrate
                        python manage.py collectstatic --noinput
                        """
                    } catch (err) {
                        // Rollback on failure
                        echo "Migration or static collection failed. Rolling back..."
                        sh """
                        cd ${PROJECT_DIR}
                        git reset --hard HEAD~1
                        sudo supervisorctl restart guni:*
                        sudo systemctl restart nginx
                        """
                        error("Pipeline failed and rollback executed!")
                    }
                }
            }
        }

        stage('Restart Services') {
            steps {
                sh """
                sudo supervisorctl restart guni:*
                sudo systemctl restart nginx
                """
            }
        }
    }

    post {
        failure {
            echo "Build failed! Check the logs."
            // Optional: send email or Slack notification
            // emailext to: 'you@example.com', subject: 'CI/CD Pipeline Failed', body: 'Check Jenkins logs'
        }
        success {
            echo "Pipeline completed successfully!"
            // Optional: send success notification
        }
    }
}
