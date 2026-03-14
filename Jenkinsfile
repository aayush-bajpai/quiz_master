pipeline {
    agent any
    environment {
        VENV_PATH = "/home/ubuntu/venv"
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

        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                sh """
                # Create venv if not exists
                [ ! -d ${VENV_PATH} ] && python3 -m venv ${VENV_PATH}
                . ${VENV_PATH}/bin/activate
                pip install --upgrade pip
                pip install -r ${PROJECT_DIR}/requirements.txt
                """
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         sh """
        //         . ${VENV_PATH}/bin/activate
        //         cd ${PROJECT_DIR}
        //         python manage.py test
        //         """
        //     }
        // }

        stage('Migrate & Collect Static') {
            steps {
                sh """
                . ${VENV_PATH}/bin/activate
                cd ${PROJECT_DIR}
                // python manage.py migrate
                python manage.py collectstatic --noinput
                """
            }
        }

        stage('Restart Services') {
            steps {
                sh "sudo /usr/local/bin/restart_quiz_services.sh"
            }
        }

    }

    post {
        failure {
            echo "Build failed! Check the logs."
        }
        success {
            echo "Pipeline completed successfully!"
        }
    }
}
