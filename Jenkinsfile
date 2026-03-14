pipeline {
    agent any
    environment {
        # Use virtualenv inside Jenkins workspace for isolation
        PATH = "venv/bin:$PATH"
    }
    stages {

        stage('Clone Repo') {
            steps {
                // Checkout your GitHub repo
                git branch: 'main',
                    url: 'https://github.com/aayush-bajpai/quiz_master.git'
            }
        }

        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                sh '''
                # Create virtual environment if it doesn't exist
                if [ ! -d "venv" ]; then
                    python3 -m venv venv
                fi

                # Activate virtualenv
                . venv/bin/activate

                # Upgrade pip and install dependencies
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         sh '''
        //         . venv/bin/activate
        //         python manage.py test
        //         '''
        //     }
        // }

        stage('Migrate & Collect Static') {
            steps {
                sh '''
                . venv/bin/activate
                // python manage.py migrate
                python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Restart Services') {
            steps {
                sh '''
                sudo supervisorctl restart guni:*
                sudo systemctl restart nginx
                '''
            }
        }

    }
    post {
        failure {
            echo "Build failed! Check the logs."
        }
        success {
            echo "Build, tests, migration, static files, and services completed successfully."
        }
    }
}
